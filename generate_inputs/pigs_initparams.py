import pigs_initialconds as pigs
import numpy as np

#Define the vertical grid
z = np.arange(0,-300,-3)

#Set the experiment parameters. Note that the model grid is 2D in y-z.
dx = 4 #Grid spacing in the x-direction
dy = 4 #Grid spacing in the x-direction
nx = 1 #Number of grid points in x
ny = 1440 #Number of grid points in y
f = -1.4e-4 #Coriolis frequency
rhs_restore_width = 4 #Width of right-hand side (convective side) restoring region
lhs_restore_width = 200 #Width of left-hand side (stabilising side) restoring region
max_temp = 3 #Surface temperature
min_temp = 1 #Bottom temperature
temp_diff_from_surf = 1 #Temperature anomaly in convective region

#Create the binary input files.
pigs.create_pigs_binary(z,dx, dy, nx, ny, f, rhs_restore_width,
    lhs_restore_width, max_temp, min_temp, temp_diff_from_surf)
