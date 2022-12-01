"""this is a doc string"""
from __future__ import annotations

import typing as t

MyType = t.Union[str, int]


def foo() -> tuple[dict[str, int], str | None]:
    pass


def bar() -> int | str:
    v: str | None = "hahah"

    return v or 12134


def baz() -> None | (
    int
):
    return 42


def taf() -> (
    int | str | tuple
):
    return 44
