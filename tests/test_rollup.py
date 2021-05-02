from mini_l2_sim.ledger import Ledger
from mini_l2_sim.rollup import RollupNode


def test_apply_mempool_creates_l1_record_and_updates_balances():
    node = RollupNode()
    node.l2_ledger.credit("alice", 100)

    node.submit_tx("alice", "bob", 30)
    block = node.apply_mempool()

    assert block.index == 0
    assert len(node.l1_records) == 1
    assert node.l2_ledger.get_balance("alice") == 70
    assert node.l2_ledger.get_balance("bob") == 30
    assert node.latest_state_root()

