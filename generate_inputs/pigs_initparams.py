from initial_conditions import pigs_initialconds as pigs
import numpy as np

#Define the vertical grid
z1=np.concatenate([-0.5*np.ones((50)) ,np.array([-0.6, -0.7, -0.8, -0.9]),
                   -1*np.ones((14)),-1.5*np.ones((32))] )
z=np.cumsum(z1)
z = np.arange(0,-300,-3)

dx = 4
dy = 4
nx = 1
ny = 1440
f = -1e-4
rhs_restore_width = 288
lhs_restore_width = 200
max_temp = 3
min_temp = 1
temp_diff_from_surf = 1


pigs.create_pigs_binary(z,dx, dy, nx, ny, f, rhs_restore_width, 
    lhs_restore_width, max_temp, min_temp, temp_diff_from_surf)
#Timestampt the generation file
import datetime
date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
time_stamp = date[0:4] + '_' + date[5:7] + '_'+ date[8:10] + '_'+ date[11:13] + '_'+ date[14:16]

import shutil
shutil.copy2('/work/n01/n01/liamb/pig/pigs/initial_conditions/pigs_initialconds.py', 'pigs_initialconds_' + time_stamp + '.py')
