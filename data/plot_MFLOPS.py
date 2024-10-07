"""

E. Wes Bethel, Copyright (C) 2022

October 2022

Description: This code loads a .csv file and creates a 3-variable plot

Inputs: the named file "data_MFLOPS.csv"

Outputs: displays a chart with matplotlib

Dependencies: matplotlib, pandas modules

Assumptions: developed and tested using Python version 3.8.8 on macOS 11.6

"""

import pandas as pd
import matplotlib.pyplot as plt


def compute_MFLOPs(data, coef, exp):
    
    for i, n in enumerate(problem_sizes):
        total_ops = coef * (n ** exp)
        mflops = (total_ops / 1000000) / (data[i] / 1000)
        print("mflops = ", mflops)
        data[i] = mflops

    return data


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

#plt.title("Comparison of MFLOPS/s Between Basic, Vectorized, and CBLAS")
plt.title("Comparison of MFLOPS/s Between OpenMP and CBLAS")

xlocs = [i for i in range(len(problem_sizes))]

plt.xticks(xlocs, problem_sizes)

code1_MFLOPS = compute_MFLOPs(code1_time, 2, 2)
code2_MFLOPS = compute_MFLOPs(code2_time, 2, 2)
code3_MFLOPS = compute_MFLOPs(code3_time, 2, 2)
code4_MFLOPS = compute_MFLOPs(code4_time, 2, 2)
code5_MFLOPS = compute_MFLOPs(code5_time, 2, 2)
code6_MFLOPS = compute_MFLOPs(code6_time, 2, 2)
code7_MFLOPS = compute_MFLOPs(code7_time, 2, 2)

#plt.plot(code1_MFLOPS, "r-o")
#plt.plot(code2_MFLOPS, "g-x")
#plt.plot(code3_MFLOPS, "b-^")
#plt.plot(code4_MFLOPS, "c-.")
plt.plot(code5_MFLOPS, "m-v")
#plt.plot(code6_MFLOPS, "y-d")
plt.plot(code7_MFLOPS, "k-h")

#plt.xscale("log")
#plt.yscale("log")

plt.xlabel("Problem Sizes")
plt.ylabel("MFLOPS/s")

#varNames = [var_names[1], var_names[2], var_names[3], var_names[4], var_names[5], var_names[6], var_names[7]]
#varNames = [var_names[1], var_names[2], var_names[7]]
varNames = [var_names[5], var_names[7]]

plt.legend(varNames, loc="best")

plt.grid(axis='both')

plt.show()

# EOF
