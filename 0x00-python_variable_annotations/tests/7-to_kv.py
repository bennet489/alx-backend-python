#!/usr/bin/env python3
"""
Contains function to_kv that takes a string k and an int OR float v
as arguments and retunrs a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns tuple"""
    return k, v ** 2
