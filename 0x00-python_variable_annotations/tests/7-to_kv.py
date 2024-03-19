#!/usr/bin/env python3
"""Containes function that takes a string and init OR float
as arguments and returns tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return the tuple"""
    return k, v ** 2
