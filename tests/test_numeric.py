import pytest
from shared.src.shared.utils import numeric
import math

# -------------------------
# Arithmetic Tests
# -------------------------
def test_add_subtract_multiply_divide():
    assert numeric.add(1,2) == 3
    assert numeric.subtract(5,3) == 2
    assert numeric.multiply(2,3) == 6
    assert numeric.divide(6,3) == 2
    assert numeric.divide(5,0) == float('inf')

# -------------------------
# Statistics Tests
# -------------------------
def test_mean_median_stddev_zscore():
    vals = [1,2,3,4,5]
    assert numeric.mean(vals) == 3
    assert numeric.median(vals) == 3
    assert math.isclose(numeric.standard_deviation(vals), math.sqrt(2)), "Std dev mismatch"
    assert math.isclose(numeric.z_score(3, vals), 0.0), "Z-score mismatch"
    assert numeric.z_score(3, []) == 0.0

# -------------------------
# Normalization & Scaling
# -------------------------
def test_normalize_list():
    vals = [10,20,30]
    normalized = numeric.normalize_list(vals)
    assert normalized[0] == 0.0
    assert normalized[-1] == 1.0
    # edge case: all values same
    assert numeric.normalize_list([5,5,5]) == [0.0,0.0,0.0]

def test_moving_average():
    vals = [1,2,3,4,5]
    assert numeric.moving_average(vals, 2) == [1.5, 2.5, 3.5, 4.5, 2.5]
    assert numeric.moving_average([],2) == []

# -------------------------
# Distance Metrics
# -------------------------
def test_distances():
    p1, p2 = (1,2), (4,6)
    assert math.isclose(numeric.euclidean_distance(p1,p2), 5.0)
    assert numeric.manhattan_distance(p1,p2) == 7

# -------------------------
# Correlation & Covariance
# -------------------------
def test_cov_corr():
    x = [1,2,3]
    y = [2,4,6]
    assert math.isclose(numeric.covariance(x,y), 2.0)
    assert math.isclose(numeric.correlation(x,y), 1.0)

# -------------------------
# Percentiles
# -------------------------
def test_percentile():
    vals = [10,20,30,40,50]
    assert numeric.percentile(vals, 50) == 30
    assert numeric.percentile(vals, 0) == 10
    assert numeric.percentile(vals, 100) == 50
    assert numeric.percentile([], 50) == 0.0
