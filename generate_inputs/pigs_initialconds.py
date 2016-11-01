import numpy as np
import genpigs as gm #Associated module in this repo
import matplotlib.pyplot as plt #If you want to view inputs

def create_pigs_binary(z,dx, dy, nx, ny, f, rhs_restore_width,lhs_restore_width,
    max_temp, min_temp, temp_diff_from_surf):
    #Make sure the input parameters are of the right type
    nx = int(nx)
    ny = int(ny)
    dx = int(dx)
    dy = int(dy)
    f = float(f)
    rhsw = float(rhs_restore_width)
    lhsw = float(lhs_restore_width)
    max_temp = float(max_temp)
    min_temp = float(min_temp)
    tdiff = float(temp_diff_from_surf)
    nz = len(z)

    #Generate the grid
    y = np.arange(0,dy*ny,ny)
    x,y, bottom_depth = gm.gen_grid(dx,dy,nx,ny,z)
    #Set the wall to be on the left-hand side
    bottom_depth[:,0] = 0
    #Write the bathymetry file
    gm.write_topography(dx,dy,nx,ny,np.transpose(bottom_depth))

    #Create the temperature initial condition
    #Set the initial profile to be uniform stratification
    temp = np.tile(np.linspace(max_temp,min_temp,nz),(ny,1))
    #Add the initial temperature anomaly on the right-hand side
    temp[-rhsw/dy:,-3:] = np.transpose(np.tile(np.linspace(min_temp,max_temp-tdiff,rhsw/dy),(3,1)))
    #Set the restoring temperature field now before adding the iniital
    #perturbation
    restore_temp = temp
    #Add the initial perturbation
    temp = temp + 1e-3*np.random.rand(ny,nz)

    #Create the initial salt field for the passive tracer
    salt = np.zeros((ny,nz))
    #Add the passive tracer into the convective region
    salt[-rhsw/dy:,-3:] = np.transpose(np.tile(np.linspace(0,1,rhsw/dy),(3,1)))

    #Create the mask for the RBCS restoring on the left and right-hand sides
    mask = np.zeros( (ny, nz) )
    #Only restore at the bottom right-hand corner
    mask[-rhsw/dy:,-3:] = np.ones(np.shape(mask[-rhsw/dy:,-3:]))
    #Restore along the full height of the left-hand side.
    mask[0:lhsw/dy,:] = np.transpose(np.tile(np.linspace(1,0,lhsw/dy),(nz,1)))

    #Plot a field if wanted
    #plt.figure()
    #ax = plt.subplot()
    #ax.pcolormesh(y,z,salt[:,-1])
    #plt.show()

    #Write the fields to binary
    gm.write_temperature(dy,tdiff,np.transpose(temp))
    gm.write_temperature_restore(dy,tdiff,np.transpose(restore_temp))
    gm.write_mask_restore(dy,np.transpose(mask))
    gm.write_salt(dx,np.transpose(salt))
