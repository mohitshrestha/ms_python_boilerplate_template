"""Numeric utilities: arithmetic, descriptive stats, normalization, distances."""

from typing import List, Tuple
import math

# -------------------------
# Arithmetic
# -------------------------
def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    return a / b if b != 0 else float('inf')

# -------------------------
# Descriptive Statistics
# -------------------------
def mean(values: List[float]) -> float:
    return sum(values) / len(values) if values else 0.0

def median(values: List[float]) -> float:
    n = len(values)
    if n == 0:
        return 0.0
    sorted_vals = sorted(values)
    mid = n // 2
    return (sorted_vals[mid-1] + sorted_vals[mid]) / 2 if n % 2 == 0 else sorted_vals[mid]

def standard_deviation(values: List[float]) -> float:
    mu = mean(values)
    return math.sqrt(sum((x - mu) ** 2 for x in values) / len(values)) if values else 0.0

def z_score(value: float, values: List[float]) -> float:
    sd = standard_deviation(values)
    return (value - mean(values)) / sd if sd != 0 else 0.0

# -------------------------
# Normalization & Scaling
# -------------------------
def normalize_list(values: List[float]) -> List[float]:
    min_val, max_val = min(values), max(values)
    if max_val == min_val:
        return [0.0 for _ in values]
    return [(v - min_val) / (max_val - min_val) for v in values]

def moving_average(values: List[float], window: int = 3) -> List[float]:
    if not values or window <= 0:
        return []
    return [
        sum(values[i:i+window]) / min(window, len(values[i:i+window]))
        for i in range(len(values))
    ]

# -------------------------
# Distance Metrics
# -------------------------
def euclidean_distance(p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def manhattan_distance(p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

# -------------------------
# Correlation & Covariance
# -------------------------
def covariance(x: List[float], y: List[float]) -> float:
    if len(x) != len(y) or not x:
        return 0.0
    mean_x, mean_y = mean(x), mean(y)
    return sum((xi-mean_x)*(yi-mean_y) for xi, yi in zip(x, y)) / len(x)

def correlation(x: List[float], y: List[float]) -> float:
    cov = covariance(x, y)
    std_x, std_y = standard_deviation(x), standard_deviation(y)
    return cov / (std_x * std_y) if std_x != 0 and std_y != 0 else 0.0

# -------------------------
# Percentiles
# -------------------------
def percentile(values: List[float], p: float) -> float:
    if not values:
        return 0.0
    sorted_vals = sorted(values)
    k = (len(values)-1) * (p / 100)
    f, c = math.floor(k), math.ceil(k)
    return sorted_vals[f] if f == c else sorted_vals[f] + (sorted_vals[c]-sorted_vals[f])*(k-f)

# -------------------------
# Example Usage
# -------------------------
if __name__ == "__main__":
    values = [10, 20, 30, 40, 50]
    print("Values:", values)
    print("Mean:", mean(values))
    print("Median:", median(values))
    print("Std Dev:", standard_deviation(values))
    print("Z-score of 20:", z_score(20, values))
    print("Normalized:", normalize_list(values))
    print("Moving Avg (window=2):", moving_average(values, 2))
    print("Euclidean Distance:", euclidean_distance((1,2),(4,6)))
    print("Manhattan Distance:", manhattan_distance((1,2),(4,6)))
    print("Correlation:", correlation([1,2,3],[2,4,6]))
    print("90th Percentile:", percentile(values, 90))
