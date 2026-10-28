import numpy as np

def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    arr = np.array(values)
    return arr.reshape(-1, width).tolist()

def block(matrix: list[list[float]], rows: list[int], columns: list[int]) -> list[list[float]]:
    arr = np.asarray(matrix)
    return arr[np.ix_(rows, columns)].tolist()

def column_means(matrix: list[list[float]]) -> list[float]:
    arr = np.asarray(matrix)
    return np.mean(arr, axis=0).tolist()

def column_range(matrix: list[list[float]], column: int) -> float:
    arr = np.asarray(matrix)
    return np.ptp(arr, axis=0).tolist()[column]

print(reshape_rows([1, 2, 3], 1))