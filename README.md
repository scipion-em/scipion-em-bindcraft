# scipion-em-bindcraft
Scipion plugin to design proteins using BindCraft (pipeline based on AlphaFold2 backpropagation, MPNN, and PyRosetta )

as the pipeline requires significant amount of GPU memory to run for larger target+binder complexes, the authors of this method highly recommend to run it using a local installation and at least 32 Gb of GPU memory.

Always try to trim the input target PDB to the smallest size possible! It will significantly speed up the binder generation and minimise the GPU memory requirements.

Be ready to run at least a few hundred trajectories to see some accepted binders, for difficult targets it might even be a few thousand. 

For additional information go to https://github.com/martinpacesa/BindCraft
