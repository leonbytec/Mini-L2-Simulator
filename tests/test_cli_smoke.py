from mini_l2_sim.cli import build_parser


def test_build_parser_has_expected_commands():
    parser = build_parser()
    subparsers_action = next(
        a for a in parser._actions if getattr(a, "dest", None) == "command"
    )
    choices = set(subparsers_action.choices.keys())
    assert {"tx", "batch", "state"}.issubset(choices)

