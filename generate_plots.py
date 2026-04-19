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

# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.
def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """Plot sensor temperatures versus time on an existing Axes.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Array of Sensor A temperature readings in degrees Celsius.
    sensor_b : numpy.ndarray
        Array of Sensor B temperature readings in degrees Celsius.
    timestamps : numpy.ndarray
        Array of timestamps in seconds corresponding to sensor readings.
    ax : matplotlib.axes.Axes
        Existing Matplotlib Axes object to modify in place.

    Returns
    -------
    None
        This function modifies ``ax`` directly and does not return a value.
    """
    ax.scatter(timestamps, sensor_a, color="tab:blue", alpha=0.7, label="Sensor A")
    ax.scatter(timestamps, sensor_b, color="tab:orange", alpha=0.7, label="Sensor B")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Temperature (°C)")
    ax.set_title("Sensor Temperature vs Time")
    ax.legend()

# Create plot_histogram(sensor_a, sensor_b, ax) that draws
# the histogram from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.
def plot_histogram(sensor_a, sensor_b, ax):
    """Plot overlaid temperature histograms for two sensors on an Axes.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Array of Sensor A temperature readings in degrees Celsius.
    sensor_b : numpy.ndarray
        Array of Sensor B temperature readings in degrees Celsius.
    ax : matplotlib.axes.Axes
        Existing Matplotlib Axes object to modify in place.

    Returns
    -------
    None
        This function modifies ``ax`` directly and does not return a value.
    """
    ax.hist(sensor_a, bins=30, alpha=0.5, color="tab:blue", label="Sensor A")
    ax.hist(sensor_b, bins=30, alpha=0.5, color="tab:orange", label="Sensor B")
    ax.axvline(
        sensor_a.mean(),
        color="tab:blue",
        linestyle="--",
        linewidth=2,
        label="Sensor A mean",
    )
    ax.axvline(
        sensor_b.mean(),
        color="tab:orange",
        linestyle="--",
        linewidth=2,
        label="Sensor B mean",
    )
    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Count")
    ax.set_title("Temperature Distributions: Sensor A vs Sensor B")
    ax.legend()


# Create plot_boxplot(sensor_a, sensor_b, ax) that draws
# the box plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.
def plot_boxplot(sensor_a, sensor_b, ax):
    """Plot side-by-side sensor temperature box plots on an existing Axes.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Array of Sensor A temperature readings in degrees Celsius.
    sensor_b : numpy.ndarray
        Array of Sensor B temperature readings in degrees Celsius.
    ax : matplotlib.axes.Axes
        Existing Matplotlib Axes object to modify in place.

    Returns
    -------
    None
        This function modifies ``ax`` directly and does not return a value.
    """
    ax.boxplot([sensor_a, sensor_b], labels=["Sensor A", "Sensor B"])
    overall_mean = np.concatenate([sensor_a, sensor_b]).mean()
    ax.axhline(
        overall_mean,
        color="gray",
        linestyle="--",
        linewidth=2,
        label="Overall mean",
    )
    ax.set_xlabel("Sensor")
    ax.set_ylabel("Temperature (deg C)")
    ax.set_title("Sensor Temperature Distribution Comparison")
    ax.legend()
