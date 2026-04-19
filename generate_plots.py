"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

import numpy as np


def generate_data(seed):
    """Generate synthetic sensor temperature data and timestamps.

    Parameters
    ----------
    seed : int
        Seed for NumPy's random number generator to ensure reproducible data.

    Returns
    -------
    sensor_a : numpy.ndarray
        Array of shape (200,) with Sensor A temperatures in degrees Celsius,
        sampled from a normal distribution with mean 25 and standard deviation 3.
    sensor_b : numpy.ndarray
        Array of shape (200,) with Sensor B temperatures in degrees Celsius,
        sampled from a normal distribution with mean 27 and standard deviation 4.5.
    timestamps : numpy.ndarray
        Array of shape (200,) containing timestamps in seconds, sampled uniformly
        from 0 to 10.
    """
    rng = np.random.default_rng(seed=seed)
    n = 200
    timestamps = rng.uniform(0, 10, n)
    sensor_a = rng.normal(loc=25, scale=3, size=n)
    sensor_b = rng.normal(loc=27, scale=4.5, size=n)
    return sensor_a, sensor_b, timestamps
