import matplotlib.pyplot as plt
import numpy as np
import smplotlib  # noqa

initial_mass = 0.35
trial_9 = np.array(
    [
        [0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35],
        [0.42, 0.39, 0.40, 0.38, 0.35, 0.35, 0.40, 0.36],
        [0.35, 0.39, 0.37, 0.39, 0.36, 0.37, 0.38, 0.36],
        [0.39, 0.35, 0.35, 0.38, 0.39, 0.36, 0.36, 0.38],
        [0.38, 0.35, 0.37, 0.34, 0.34, 0.36, 0.36, 0.37],
        [0.34, 0.38, 0.36, 0.36, 0.37, 0.35, 0.38, 0.32],
    ]
)

trial_21 = np.array(
    [
        [0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35],
        [0.38, 0.35, 0.33, 0.37, 0.36, 0.35, 0.37, 0.38],
        [0.37, 0.32, 0.38, 0.34, 0.36, 0.36, 0.37, 0.37],
        [0.38, 0.38, 0.38, 0.38, 0.37, 0.38, 0.32, 0.33],
        [0.36, 0.3, 0.38, 0.38, 0.36, 0.37, 0.34, 0.37],
        [0.34, 0.34, 0.33, 0.35, 0.33, 0.35, 0.3, 0.35],
    ]
)

trial_34 = np.array(
    [
        [0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35],
        [0.36, 0.37, 0.36, 0.37, 0.37, 0.35, 0.36, 0.35],
        [0.35, 0.35, 0.36, 0.36, 0.35, 0.36, 0.37, 0.35],
        [0.36, 0.36, 0.34, 0.35, 0.35, 0.35, 0.35, 0.34],
        [0.33, 0.34, 0.35, 0.34, 0.33, 0.32, 0.31, 0.3],
        [0.33, 0.29, 0.3, 0.32, 0.29, 0.31, 0.31, 0.29],
    ]
)

trial_40 = np.array(
    [
        [0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35, 0.35],
        [0.36, 0.35, 0.36, 0.32, 0.35, 0.32, 0.36, 0.32],
        [0.35, 0.33, 0.33, 0.38, 0.35, 0.34, 0.36, 0.34],
        [0.31, 0.32, 0.37, 0.35, 0.35, 0.31, 0.32, 0.32],
        [0.3, 0.3, 0.37, 0.33, 0.32, 0.29, 0.32, 0.28],
        [0.35, 0.29, 0.32, 0.26, 0.29, 0.28, 0.28, 0.27],
    ]
)

# Times in minutes
times = np.array(
    [
        0,
        90,
        160,
        235,
        290,
        360,
    ]
)
trial_9 /= 0.01 * initial_mass
trial_21 /= 0.01 * initial_mass
trial_34 /= 0.01 * initial_mass
trial_40 /= 0.01 * initial_mass
trial_9 -= 100
trial_21 -= 100
trial_34 -= 100
trial_40 -= 100

t9_av = np.average(trial_9, axis=1)
t21_av = np.average(trial_21, axis=1)
t34_av = np.average(trial_34, axis=1)
t40_av = np.average(trial_40, axis=1)

t9_stdev = np.std(trial_9, axis=1)
t21_stdev = np.std(trial_21, axis=1)
t34_stdev = np.std(trial_34, axis=1)
t40_stdev = np.std(trial_40, axis=1)

fig, ax = plt.subplots()
ax.errorbar(
    times, t9_av, yerr=t9_stdev, capsize=2, alpha=0.5, fmt="o-", label="$9^oC$ Water"
)
ax.errorbar(
    times + 2.5,
    t21_av,
    yerr=t21_stdev,
    capsize=2,
    alpha=0.5,
    fmt="o-",
    label="$21^oC$ Water",
)
ax.errorbar(
    times + 5,
    t34_av,
    yerr=t34_stdev,
    capsize=2,
    alpha=0.5,
    fmt="o-",
    label="$34^oC$ Water",
)
ax.errorbar(
    times + 7.5,
    t40_av,
    yerr=t40_stdev,
    capsize=2,
    alpha=0.5,
    fmt="o-",
    label="$40^oC$ Water",
)
ax.set_ylabel("Change in Mass (%)")
ax.set_xlabel("Time ($min$)")
ax.grid(alpha=0.2)
ax.set_title("Change in Apple Mass vs. Time")
ax.legend()
plt.show()
