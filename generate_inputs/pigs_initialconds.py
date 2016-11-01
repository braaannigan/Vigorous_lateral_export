import numpy as np
import genpigs as gm
import matplotlib.pyplot as plt

def create_pigs_binary(z,dx, dy, nx, ny, f, rhs_restore_width,lhs_restore_width, max_temp, min_temp, temp_diff_from_surf):

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
    y = np.arange(0,dy*ny,ny) 
    x,y, bottom_depth = gm.gen_grid(dx,dy,nx,ny,z)
    bottom_depth[:,-1] = 0
    gm.write_topography(dx,dy,nx,ny,np.transpose(bottom_depth))

    #Experiment parameters
    #f = 1.4e-4
    g = 9.81

#    temp=repmat(linspace(max_temp,1,nz)',[1 nx])
    temp = np.tile(np.linspace(max_temp,min_temp,nz),(ny,1))
    print np.shape(temp)
    temp[-rhsw/dy:,-3:] = np.transpose(np.tile(np.linspace(min_temp,max_temp-tdiff,rhsw/dy),(3,1)))
    #Restore to the state with no initial perturbation
    restore_temp = temp
    
    temp = temp + 1e-3*np.random.rand(ny,nz)
 
    salt = np.zeros((ny,nz))
    salt[-rhsw/dy:,-3:] = np.transpose(np.tile(np.linspace(0,1,rhsw/dy),(3,1)))

    mask = np.zeros( (ny, nz) )
    mask[-rhsw/dy:,-3:] = np.ones(np.shape(mask[-rhsw/dy:,-3:]))
    mask[0:lhsw/dy,:] = np.transpose(np.tile(np.linspace(1,0,lhsw/dy),(nz,1)))
    print salt.max()
    plt.figure()
    ax = plt.subplot()
    ax.plot(salt[:,-1])
    plt.show()
    #Write the fields to binary
#    temp = np.transpose( temp, (2,1,0))
    gm.write_temperature(dy,tdiff,np.transpose(temp))
    gm.write_temperature_restore(dy,tdiff,np.transpose(restore_temp))
    gm.write_mask_restore(dy,np.transpose(mask))

#    salt = np.transpose( salt, (2,1,0))
    gm.write_salt(dx,np.transpose(salt))
#    U = np.transpose( U, (2,1,0))
#    gm.write_uvel(dx,H1,U)
#    eta = np.transpose( eta, (1,0))
#    gm.write_eta(dx,H1,eta)
