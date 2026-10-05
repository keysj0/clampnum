"""Clamp a number into an inclusive range."""
from __future__ import annotations


def clamp(value: float, low: float, high: float) -> float:
    if low > high:
        raise ValueError("下界不能大于上界")
    if value < low:
        return low
    if value > high:
        return high
    return value


def overflow(value: float, low: float, high: float) -> float:
    if low > high:
        raise ValueError("下界不能大于上界")
    if value < low:
        return low - value
    if value > high:
        return value - high
    return 0.0


def within(value: float, low: float, high: float) -> bool:
    if low > high:
        raise ValueError("下界不能大于上界")
    return low <= value <= high


def clamp_all(values: list[float], low: float, high: float) -> list[float]:
    return [clamp(value, low, high) for value in values]
