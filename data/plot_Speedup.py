"""

E. Wes Bethel, Copyright (C) 2022

October 2022

Description: This code loads a .csv file and creates a 3-variable plot

Inputs: the named file "data_speedup.csv"

Outputs: displays a chart with matplotlib

Dependencies: matplotlib, pandas modules

Assumptions: developed and tested using Python version 3.8.8 on macOS 11.6

"""

import pandas as pd
import matplotlib.pyplot as plt


def compute_speedup(data, ref_data):
    # ref_data is the baseline time (time_basic)
    speedups = []
    
    for ref, time in zip(ref_data, data):
        if time > 0:  # Avoid division by zero
            speedup = ref / time
            print("speedup = ", speedup)
        else:
            speedup = float('inf')  # If time is zero, speedup is infinite
        speedups.append(speedup)
    
    print()
    return speedups
    


fname = "data_runtime.csv"
df = pd.read_csv(fname, comment="#")
print(df)

var_names = list(df.columns)

# split the df into individual vars
# assumption: column order - 0=problem size, 1=1-thread time, 2=4-thread time, 3=16-thread time, 4=64-thread time

problem_sizes = df[var_names[0]].values.tolist()
time_basic = df[var_names[1]].values.tolist()
time_1_thread = df[var_names[3]].values.tolist()
time_4_threads = df[var_names[4]].values.tolist()
time_16_threads = df[var_names[5]].values.tolist()
time_64_threads = df[var_names[6]].values.tolist()

plt.title("Speedup VMM OpenMP vs Basic")

xlocs = [i for i in range(len(problem_sizes))]
plt.xticks(xlocs, problem_sizes)

# Compute speedups
speedup_1_threads = compute_speedup(time_1_thread, time_basic)
speedup_4_threads = compute_speedup(time_4_threads, time_basic)
speedup_16_threads = compute_speedup(time_16_threads, time_basic)
speedup_64_threads = compute_speedup(time_64_threads, time_basic)

# Plot speedups
plt.plot(xlocs, speedup_1_threads, "r-o", label="omp-1")
plt.plot(xlocs, speedup_4_threads, "g-x", label="omp-4")
plt.plot(xlocs, speedup_16_threads, "b-^", label="omp-16")
plt.plot(xlocs, speedup_64_threads, "c-d", label="omp-64")

# Add expected speedup lines based on the number of threads
expected_speedup_1 = [1] * len(problem_sizes)
expected_speedup_4 = [4] * len(problem_sizes)
expected_speedup_16 = [16] * len(problem_sizes)
expected_speedup_64 = [64] * len(problem_sizes)

plt.plot(xlocs, expected_speedup_1, "r--", label="Expected Speedup omp-1")
plt.plot(xlocs, expected_speedup_4, "g--", label="Expected Speedup omp-4")
plt.plot(xlocs, expected_speedup_16, "b--", label="Expected Speedup omp-16")
plt.plot(xlocs, expected_speedup_64, "c--", label="Expected Speedup omp-64")

plt.xlabel("Problem Size")
plt.ylabel("Speedup")
plt.legend(loc="best")
plt.grid(axis='both')
plt.show()

# EOF
