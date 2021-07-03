Mini L2 Simulator
==================

Mini L2 Simulator is a tiny, educational project that models a very
simple optimistic-rollup style system on top of an L1-like chain.

The goal is not to be production-ready, but to provide a small codebase
to play with concepts such as:

- batched L2 transactions
- posting rollup blocks to L1
- a naive fraud proof style re-execution

Everything is implemented as plain Python data structures with no
external dependencies beyond the standard library.

## Status

This project is a personal side experiment and is not intended for any
real-world usage.

## Quick overview

- `mini_l2_sim/ledger.py` – in-memory L1 and L2 account ledgers
- `mini_l2_sim/rollup.py` – batching, block creation and posting to L1
- `mini_l2_sim/cli.py` – small command-line interface for submitting
  L2 transfers and applying batches

No packaging or publishing is planned; the project is meant to be read
and hacked on locally.
