import numpy as np

def make_hours() -> list[int]:
    return np.arange(0, 21+1, 3).tolist()

def vector_report(values: list[float]) -> dict:
    dictionary = {
        "third": values[2],
        "last": values[-1],
        "middle": values[2:6],
        "evert_second": values[::2],
        "reversed": values[::-1]
    }

    return dictionary

def change_vector(values:list[float]) -> list[float]:
    arr = np.asarray(values.copy())
    arr[1:4] = 99.0
    arr[::2] = -1.0
    return arr.tolist()

def cap_above(values:list[float], limit:float) -> list[float]:
    arr = np.array(values.copy())
    arr[arr > limit] = limit
    return arr.tolist

def celsius_to_fahrenheit(values:list[float]) -> list[float]:
    arr = np.array(values.copy())
    return (arr * (9 / 5) + 32).tolist()