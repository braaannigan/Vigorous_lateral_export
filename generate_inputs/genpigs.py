import numpy as np

#Write binary files with big endian entries
def writefield(file_name,data):
    import sys
    print 'write to file: '+ file_name
    print np.shape(data)
    if sys.byteorder == 'little': data.byteswap(True)
    fid = open(file_name,"wb")
    data.tofile(fid)
    fid.close()

def gen_grid(dx,dy,nx,ny,z):
    x=np.arange(0.5*dx,nx*dx+0.5*dx,dx)
    y=np.arange(0.5*dy,ny*dy+0.5*dy,dy)
    bottom_depth = z[-1]*np.ones( (nx,ny) )
    return x, y, bottom_depth

def write_topography(dx,dy,nx,ny,bottom_depth):
    file_name = 'dx' + str(dx) + 'nx' + str(nx) + 'ny' + str(ny) +'topog.bin'
    writefield(file_name, bottom_depth)

def write_temperature(dx,tdiff,temp):
    file_name = 'dx' + str(dx) + 'tdiff' +str(tdiff) + 'PoTemp.bin'
    writefield(file_name, temp)

def write_temperature_restore(dx,tdiff,temp):
    file_name = 'RBCSdx' + str(dx) + 'tdiff' +str(tdiff) + 'PoTemp.bin'
    writefield(file_name, temp)

def write_salt(dx,salt):
    file_name = 'dx' + str(dx) +'Salt.bin'
    writefield(file_name, salt)

def write_mask_restore(dx,mask):
    file_name = 'RBCSdx' + str(dx) + 'Mask.bin'
    writefield(file_name, mask)
