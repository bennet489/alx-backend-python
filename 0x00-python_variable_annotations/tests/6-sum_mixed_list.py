#!/usr/bin/env python3
"""
Function sum_mixed_list which takes a list
mxd_lst of integers and floats and returns
their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns float"""
    return sum(mxd_lst)
