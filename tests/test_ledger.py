from mini_l2_sim.ledger import Ledger


def test_transfer_moves_balance_between_accounts():
    ledger = Ledger()
    ledger.credit("alice", 50)

    ledger.transfer("alice", "bob", 10)

    assert ledger.get_balance("alice") == 40
    assert ledger.get_balance("bob") == 10

