import pytest

EXPECTED_OUTPUT = """
milkomeda
├── c1
│   └── milkomeda  (default)
├── c1-testnet
│   └── milkomeda  (default)
├── a1
│   └── milkomeda  (default)
├── a1-testnet
│   └── milkomeda  (default)
└── local  (default)
    └── test  (default)
""".strip()


def assert_rich_text(actual: str, expected: str):
    """
    The output from `rich` causes a bunch of extra spaces to
    appear at the end of each line. For easier testing, we remove those here.
    """
    actual = f"milkomeda{actual.split('milkomeda')[-1]}"

    expected = expected.strip()
    lines = actual.split("\n")
    new_lines = []
    for line in lines:
        if line:
            new_lines.append(line.rstrip())

    actual = "\n".join(new_lines)
    print(actual)
    assert actual == expected


def test_networks(runner, cli):
    result = runner.invoke(cli, ["networks", "list"])
    assert_rich_text(result.output, EXPECTED_OUTPUT)
