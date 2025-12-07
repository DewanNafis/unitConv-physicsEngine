"""Basic unit conversion functions."""


def m_to_cm(meters: float) -> float:
    return meters * 100


def cm_to_m(centimeters: float) -> float:
    return centimeters / 100


def kg_to_g(kilograms: float) -> float:
    return kilograms * 1000


def g_to_kg(grams: float) -> float:
    return grams / 1000


def c_to_f(celsius: float) -> float:
    return (celsius * 9/5) + 32


def f_to_c(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5/9


def s_to_min(seconds: float) -> float:
    return seconds / 60


def min_to_s(minutes: float) -> float:
    return minutes * 60
