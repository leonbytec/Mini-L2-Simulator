from dataclasses import dataclass, field
from typing import List, Dict

from .ledger import Ledger


@dataclass
class Transaction:
    sender: str
    recipient: str
    amount: int


@dataclass
class L2Block:
    index: int
    transactions: List[Transaction]


@dataclass
class L1Record:
    block_index: int
    state_root: str


def simple_state_root(ledger: Ledger) -> str:
    """
    Very naive "state root" that just concatenates sorted balances.
    This is only for demonstration and not collision resistant.
    """
    parts = []
    for address in sorted(ledger.accounts.keys()):
        parts.append(f"{address}:{ledger.accounts[address].balance}")
    return "|".join(parts)


@dataclass
class RollupNode:
    l2_ledger: Ledger = field(default_factory=Ledger)
    l1_records: List[L1Record] = field(default_factory=list)
    mempool: List[Transaction] = field(default_factory=list)

    def submit_tx(self, sender: str, recipient: str, amount: int) -> None:
        tx = Transaction(sender=sender, recipient=recipient, amount=amount)
        self.mempool.append(tx)

    def _apply_tx(self, tx: Transaction, ledger: Ledger) -> None:
        ledger.debit(tx.sender, tx.amount)
        ledger.credit(tx.recipient, tx.amount)

    def apply_mempool(self) -> L2Block:
        if not self.mempool:
            raise ValueError("no pending transactions")
        block_index = len(self.l1_records)
        txs = list(self.mempool)
        self.mempool.clear()
        for tx in txs:
            self._apply_tx(tx, self.l2_ledger)
        record = L1Record(block_index=block_index, state_root=simple_state_root(self.l2_ledger))
        self.l1_records.append(record)
        return L2Block(index=block_index, transactions=txs)

    def post_block_to_l1(self, block: L2Block) -> L1Record:
        # In this simplified version, posting is the same as applying
        # the mempool and recording the state root.
        del block  # kept for now to show the intended API shape
        raise NotImplementedError("explicit posting is not wired yet")

