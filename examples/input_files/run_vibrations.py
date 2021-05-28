from ase import Atoms
from gpaw import GPAW, PW
from ase.vibrations import Vibrations

"""
A simple script to run an H2 calculation
with GPAW using a PW basis and perform vibration
calculations using finite difference 
"""

# set up the H2 molecule
h2 = Atoms('H2', [(0, 0, 0), (0, 0, 0.74)])
h2.center(vacuum=2.5)

# define the calculator
h2.calc = GPAW(xc='PBE', mode=PW(300), txt='aiida.out')

# run now a vibrational calculation
vib = Vibrations(h2)
vib.run()

# write the  aiida.txt file
vib.summary(log='aiida.txt')