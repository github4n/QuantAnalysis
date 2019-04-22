import numpy as np

PEAK, VALLEY = 1, -1


def percent_identify_initial_pivot(X, up_thresh, down_thresh):
    """Quickly identify the X[0] as a peak or valley."""
    x_0 = X[0]
    max_x = x_0
    max_t = 0
    min_x = x_0
    min_t = 0
    up_thresh += 1
    down_thresh += 1

    for t in range(1, len(X)):
        x_t = X[t]

        if x_t / min_x >= up_thresh:
            return VALLEY if min_t == 0 else PEAK

        if x_t / max_x <= down_thresh:
            return PEAK if max_t == 0 else VALLEY

        if x_t > max_x:
            max_x = x_t
            max_t = t

        if x_t < min_x:
            min_x = x_t
            min_t = t

    t_n = len(X) - 1
    return VALLEY if x_0 < X[t_n] else PEAK


def percent_peak_valley_pivots(X, up_thresh, down_thresh):
    """
    Finds the peaks and valleys of a series.
    """
    if down_thresh > 0:
        raise ValueError('The down_thresh must be negative.')

    initial_pivot = percent_identify_initial_pivot(X, up_thresh, down_thresh)

    t_n = len(X)
    pivots = np.zeros(t_n, dtype='i1')
    pivots[0] = initial_pivot

    up_thresh += 1
    down_thresh += 1

    trend = -initial_pivot
    last_pivot_t = 0
    last_pivot_x = X[0]
    for t in range(1, len(X)):
        x = X[t]
        r = x / last_pivot_x

        if trend == -1:
            if r >= up_thresh:
                pivots[last_pivot_t] = trend
                trend = 1
                last_pivot_x = x
                last_pivot_t = t
            elif x < last_pivot_x:
                last_pivot_x = x
                last_pivot_t = t
        else:
            if r <= down_thresh:
                pivots[last_pivot_t] = trend
                trend = -1
                last_pivot_x = x
                last_pivot_t = t
            elif x > last_pivot_x:
                last_pivot_x = x
                last_pivot_t = t

    if last_pivot_t == t_n - 1:
        pivots[last_pivot_t] = trend
    elif pivots[t_n - 1] == 0:
        pivots[t_n - 1] = -trend

    return pivots


def num_identify_initial_pivot(X, up_thresh, down_thresh):
    """Quickly identify the X[0] as a peak or valley."""
    x_0 = X[0]
    max_x = x_0
    max_t = 0
    min_x = x_0
    min_t = 0
    for t in range(1, len(X)):
        x_t = X[t]

        if x_t - min_x >= up_thresh:
            return VALLEY if min_t == 0 else PEAK

        if x_t - max_x >= down_thresh:
            return PEAK if max_t == 0 else VALLEY

        if x_t > max_x:
            max_x = x_t
            max_t = t

        if x_t < min_x:
            min_x = x_t
            min_t = t

    t_n = len(X) - 1
    return VALLEY if x_0 < X[t_n] else PEAK


def num_peak_valley_pivots(X, up_thresh, down_thresh):
    """
    Finds the peaks and valleys of a series.
    """
    if down_thresh > 0:
        raise ValueError('The down_thresh must be negative.')

    initial_pivot = num_identify_initial_pivot(X, up_thresh, down_thresh)

    t_n = len(X)
    pivots = np.zeros(t_n, dtype='i1')
    pivots[0] = initial_pivot

    trend = -initial_pivot
    last_pivot_t = 0
    last_pivot_x = X[0]
    for t in range(1, len(X)):
        x = X[t]
        r = x - last_pivot_x

        if trend == -1:
            if r >= up_thresh:
                pivots[last_pivot_t] = trend
                trend = 1
                last_pivot_x = x
                last_pivot_t = t
            elif x < last_pivot_x:
                last_pivot_x = x
                last_pivot_t = t
        else:
            if r <= down_thresh:
                pivots[last_pivot_t] = trend
                trend = -1
                last_pivot_x = x
                last_pivot_t = t
            elif x > last_pivot_x:
                last_pivot_x = x
                last_pivot_t = t

    if last_pivot_t == t_n - 1:
        pivots[last_pivot_t] = trend
    elif pivots[t_n - 1] == 0:
        pivots[t_n - 1] = -trend

    return pivots