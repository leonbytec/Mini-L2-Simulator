import argparse
from dataclasses import asdict
from typing import List

from .rollup import RollupNode


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Mini L2 rollup simulator")
    sub = parser.add_subparsers(dest="command", required=True)

    tx = sub.add_parser("tx", help="queue a transfer on L2")
    tx.add_argument("sender")
    tx.add_argument("recipient")
    tx.add_argument("amount", type=int)

    sub.add_parser("batch", help="apply all pending L2 transactions")
    sub.add_parser("state", help="print the latest state root")

    return parser


def handle_tx(node: RollupNode, args: argparse.Namespace) -> None:
    node.submit_tx(args.sender, args.recipient, args.amount)
    print(f"queued tx {args.sender} -> {args.recipient} ({args.amount})")


def handle_batch(node: RollupNode) -> None:
    block = node.apply_mempool()
    print(f"applied block #{block.index} with {len(block.transactions)} txs")


def handle_state(node: RollupNode) -> None:
    print(node.latest_state_root())


def main(argv: List[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    # For now we keep the node in-memory only; this keeps the example
    # small and avoids storage decisions.
    node = RollupNode()

    if args.command == "tx":
        handle_tx(node, args)
    elif args.command == "batch":
        handle_batch(node)
    elif args.command == "state":
        handle_state(node)
    else:
        parser.error(f"unknown command {args.command!r}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
