import os
import time

print(os.getcwd())
des_dir = os.getcwd()+"\\MCS_Matrix\\"
print(des_dir)
matrixfiles = os.listdir(des_dir)

mhs_res_file = des_dir+"mhs_clock_res.txt"
if os.path.exists(des_dir+"mhs_clock_res.txt"):
    with open(mhs_res_file, 'r+') as file:
        file.truncate(0)
for fname in matrixfiles:
    if "_res" in fname:
        continue
    abs_fname = des_dir+fname
    print(abs_fname)

    # begin_time = nowTime()
    '''
    the first os invoke is only to write |M_matrix.txt|2.3700|    | to "mhs_clock_res.txt"
    '''
    os.system("mhs2.exe -i "+des_dir+fname) #write to "mhs_clock_res.txt"



