##!/home/kenno/.pyenv/shims/python3
# tpyecode.py
"""型判定モジュール."""


def judgement(
    code: str | int | float | bytes | object | list | tuple | dict | set,
) -> type:
    """型を判定する関数です."""
    return type(code)

