# Vigorous_lateral_export
The numerical code used for the experiments in "Vigorous lateral export of the meltwater outflow from beneath an Antarctic ice shelf", Naveira-Garabato et al. can be found in this repository.
There are two parts to the repo.  The first part
"generate_inputs" folder contains the python code used to generate the binary files for
the model initial condition.  The second part "mitgcm" contains the MITgcm model code.

## Generate_inputs
The generate_inputs folder has the python files used to generate the model input
files i.e. temperature, salinity, bathymetry and restoring fields.

The file pigs_initparams.py is used to set the appropriate experiment parameters.
The file pigs_initialconds.py is imported to pigs_initparams.py as a module, while
genpigs.py is imported into pigs_initialconds.py as a module.  

In practice, pigs_initparams.py is edited to set the desired experiment parameters.
This script is called as 'python pigs_initparams.py' and the input files are
generated.

##mitgcm
This folder contains the model code.  The model code is found in 'model'.  The
compile_time_options allows the packages and grid to be specified.  The
optfile used for the paper is tools/build_options/linux_archer_gfortran2.
This would obviously have to be adapted for your own machine. The
input files are then found in the directory 'run'.  

If the experiment is run in a series of
jobs on a cluster, the bash script crd.sh allows the generation of a series of input
data files.  When crd.sh is run in the terminal, the first and last job numbers
are requested.  The script then creates a sequency of files called, say,
data000, data001 etc..  These files have the appropriate iteration number for
the pickup files for that point in the sequence.
