import timer_plus as tp
import numpy as np
import pandas as pd

# example
pd_stmt_list = []
np_stmt_list = []
glob_list = []
repeat_list = []
name_list = []

for i, N in enumerate(N_list):
    pd_stmt_list.append("d.sum()")
    np_stmt_list.append("np.sum(d)")
    glob_list.append(dict(d=data[:N:], pd=pd, np=np,))
    repeat_list.append(7)
    name_list.append("N=%.1E" % N)

pd_time = tp.TimerCollection(pd_stmt_list, glob_list, repeat_list, name_list).get_statistics
np_time = tp.TimerCollection(np_stmt_list, glob_list, repeat_list, name_list).get_statistics
