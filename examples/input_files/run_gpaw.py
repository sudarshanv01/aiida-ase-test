from ase import Atoms
from gpaw import GPAW, PW

"""
A simple script to run an H2 calculation
with GPAW using a PW basis and writing outputs
to a specific file called out.txt
"""

# set up the H2 molecule
h2 = Atoms('H2', [(0, 0, 0), (0, 0, 0.74)])
h2.center(vacuum=2.5)

# define the calculator
h2.calc = GPAW(xc='PBE', mode=PW(300), txt='aiida.out')

# One of the ways to "start" the calculation
h2.get_potential_energy()