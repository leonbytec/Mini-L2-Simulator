import argparse

from .ledger import Ledger
from .rollup import RollupNode


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Mini L2 rollup simulator")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("init-ledger", help="create an empty ledger")

    tx = sub.add_parser("tx", help="submit a simple transfer on L2")
    tx.add_argument("sender")
    tx.add_argument("recipient")
    tx.add_argument("amount", type=int)

    sub.add_parser("batch", help="apply all pending L2 transactions")

    return parser


def main(argv: list[str] | None = None) -> int:
    _ = Ledger()  # placeholder usage to keep things simple for now
    _ = RollupNode()
    parser = build_parser()
    parser.parse_args(argv)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

