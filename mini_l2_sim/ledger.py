from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Account:
    address: str
    balance: int = 0


@dataclass
class Ledger:
    accounts: Dict[str, Account] = field(default_factory=dict)

    def get_balance(self, address: str) -> int:
        account = self.accounts.get(address)
        return account.balance if account else 0

    def credit(self, address: str, amount: int) -> None:
        if amount < 0:
            raise ValueError("amount must be non-negative")
        account = self.accounts.setdefault(address, Account(address=address))
        account.balance += amount

    def debit(self, address: str, amount: int) -> None:
        if amount < 0:
            raise ValueError("amount must be non-negative")
        current = self.get_balance(address)
        if amount > current:
            raise ValueError("insufficient balance")
        account = self.accounts.setdefault(address, Account(address=address))
        account.balance -= amount

