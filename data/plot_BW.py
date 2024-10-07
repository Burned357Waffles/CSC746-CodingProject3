"""

E. Wes Bethel, Copyright (C) 2022

October 2022

Description: This code loads a .csv file and creates a 3-variable plot

Inputs: the named file "data_BW.csv"

Outputs: displays a chart with matplotlib

Dependencies: matplotlib, pandas modules

Assumptions: developed and tested using Python version 3.8.8 on macOS 11.6

"""

import pandas as pd
import matplotlib.pyplot as plt


def compute_BW(data, n_bytes, max_BW=204.8):
    # max bandwidth is 204.8 GB/s
    # runtime is stored in data in ms

    # Calculate bandwidth and then percent utilization
    percent_bandwidth = []
    for t, d in zip(data, problem_sizes):
        bw = (d * n_bytes) / (t / 1000) # BW = Total Data Transferred / Time in seconds
        bw_GB = bw / 1000000000 # Convert to GB 
        percent_utilization = (bw_GB / max_BW) * 100
        print("percent_utilization = ", percent_utilization)
        
        percent_bandwidth.append(percent_utilization)
    
    print()
    return percent_bandwidth


fname = "data_runtime.csv"
df = pd.read_csv(fname, comment="#")
print(df)

var_names = list(df.columns)

#print("var names =", var_names)

# split the df into individual vars
# assumption: column order - 0=problem size, 1=blas time, 2=basic time

problem_sizes = df[var_names[0]].values.tolist()
code1_time = df[var_names[1]].values.tolist()
code2_time = df[var_names[2]].values.tolist()
code3_time = df[var_names[3]].values.tolist()
code4_time = df[var_names[4]].values.tolist()
code5_time = df[var_names[5]].values.tolist()
code6_time = df[var_names[6]].values.tolist()
code7_time = df[var_names[7]].values.tolist()

plt.title("Comparison of Percent Bandwidth Utilization Between Basic, OpenMP, and CBLAS")

xlocs = [i for i in range(len(problem_sizes))]

plt.xticks(xlocs, problem_sizes)

code1_BW = compute_BW(code1_time, 8)
#code2_BW = compute_BW(code2_time, 8)
code3_BW = compute_BW(code3_time, 8)
code4_BW = compute_BW(code4_time, 8)
code5_BW = compute_BW(code5_time, 8)
code6_BW = compute_BW(code6_time, 8)
code7_BW = compute_BW(code7_time, 8)

plt.plot(code1_BW, "r-o")
#plt.plot(code2_BW, "g-x")
plt.plot(code3_BW, "b-^")
plt.plot(code4_BW, "c-.")
plt.plot(code5_BW, "m-v")
plt.plot(code6_BW, "y-d")
plt.plot(code7_BW, "k-h")

#plt.xscale("log")
#plt.yscale("log")

plt.xlabel("Problem Sizes")
plt.ylabel("Percent Bandwidth Utilization")

#varNames = [var_names[1], var_names[2], var_names[3], var_names[4], var_names[5], var_names[6], var_names[7]]
#varNames = [var_names[1], var_names[2], var_names[7]]
#varNames = [var_names[3], var_names[4], var_names[5], var_names[6], var_names[7]]
varNames = [var_names[1], var_names[3], var_names[4], var_names[5], var_names[6], var_names[7]]

plt.legend(varNames, loc="best")

plt.grid(axis='both')

plt.show()

# EOF
