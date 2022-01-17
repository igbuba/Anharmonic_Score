# Anharmonic_Score
Compute the anharmonic score of a material at finite temperature based on Carbogno et al., (2020) Phy.Rev.Materials. 
The anharmonic score measures the standard deviation of the distribution of anharmonic force components F_ANH from the ab initio forces F_AI and their harmonic approximation F_HA, where F_ANH = F_AI - F_HA
<\script $\alpha$
# File requirements:
Output files with ab-initio, harmonic, and anharmobic forces.
All the forces are given as norms in the different columns 

## Examples
Examples are given for Al at 300K and Zr at 100K,400K, and 800K.

## How to run
Change the "file_name" with the required file containing the forces in the "run.py" file and then use the command

$ ./run.py

This will print the anharmonic score to the screen
