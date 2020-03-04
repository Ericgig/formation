import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
from glob import glob
from scipy import stats


def integral(t, R):
    """Find the total responce"""
    return integrate.simps(R, t)

def find_exp(t, A, dist=20, N=100):
    """Find the exponencial decay"""
    slope = np.zeros(N-dist)
    error = np.zeros(N-dist)
    logA = np.log(A)
    for i in range(N-dist):
        (slope_,_), fit, _, _, _ = np.polyfit(t[i:i+dist], logA[i:i+dist], 1, full=1)
        slope[i] = slope_
        error[i] = fit

    error_min = np.min(error)
    error_max = np.max(error)
    err_good = np.where(error < 0.9*error_min+0.1*error_max)
    return np.min(slope[err_good])

    #plt.plot(slope)
    #plt.plot(error)
    #plt.plot(np.arange(N-dist)[err_good],b[err_good],"o")

def time_high(t, B):
    """Find the exponencial decay"""
    high_range = np.where(B>0.5)[0]
    return t[high_range[-1]]-t[high_range[1]]


def find_jump(t, C):
    """Find the reading jump in C and return their times"""
    diffs = np.abs(np.diff(C))
    return t[np.where(diffs>0.5)]

def analyse(file):
    dt = 0.1
    n_data = 100
    t = numpy.arange(n_data) * dt -1
    data = numpy.loadtxt(fname=file, delimiter=',')
    R = data[:,0]
    A = data[:,1]
    B = data[:,2]
    C = data[:,3]
    return [integral(t,R), A[0]-A[-1], find_exp(t,A), time_high(t, B), len(find_jump(t, C))]

if __name__ == "__main__":
    file_list = glob("*.csv")
    file_list_corr = []
    for file in file_list:
        if not file == "result.csv":
        file_list_corr += [file]
    result = np.array([analyse(file) for file in file_list_corr])
    np.savetxt("result.csv", result, delimiter=",")