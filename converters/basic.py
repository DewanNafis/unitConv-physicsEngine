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


def inch_to_cm(inches: float) -> float:
    return inches * 2.54


def cm_to_inch(centimeters: float) -> float:
    return centimeters / 2.54


def feet_to_m(feet: float) -> float:
    return feet * 0.3048


def m_to_feet(meters: float) -> float:
    return meters / 0.3048


def inch_to_m(inches: float) -> float:
    return inches * 0.0254


def m_to_inch(meters: float) -> float:
    return meters / 0.0254


def yard_to_m(yards: float) -> float:
    return yards * 0.9144


def m_to_yard(meters: float) -> float:
    return meters / 0.9144


def mile_to_km(miles: float) -> float:
    return miles * 1.60934


def km_to_mile(kilometers: float) -> float:
    return kilometers / 1.60934
