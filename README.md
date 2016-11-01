# Vigorous_lateral_export
Numerical code used for the experiments in "Vigorous lateral export of the meltwater outflow from beneath an Antarctic ice shelf", Naveira-Garabato et al., Nature

This repository holds code which allows the numerical experiments described in
the paper to be reproduced.  There are two parts to the repo.  The first part
"generate_inputs" folder contains the python code used to generate the binary files for
the model initial condition.  The second part contains the MITgcm model code.

## Generate_inputs
The generate_inputs folder has the python files used to generate the model input
files i.e. temperature, salinity, bathymetry and restoring fields.

The file pigs_initparams.py is used to set the appropriate experiment parameters.
The file pigs_initialconds.py is imported to pigs_initparams.py as a module, while
genpigs.py is imported into pigs_initialconds.py as a module.  

In practice, pigs_initparams.py is edited to set the desired experiment parameters.
This script is called as 'python pigs_initparams.py' and the input files are
generated.
