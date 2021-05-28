[![Build Status](https://github.com/aiidateam/aiida-ase3/workflows/ci/badge.svg?branch=master)](https://github.com/aiidateam/aiida-ase3/actions)
[![Coverage Status](https://coveralls.io/repos/github/aiidateam/aiida-ase3/badge.svg?branch=master)](https://coveralls.io/github/aiidateam/aiida-ase3?branch=master)
[![Docs status](https://readthedocs.org/projects/aiida-ase3/badge)](http://aiida-ase3.readthedocs.io/)
[![PyPI version](https://badge.fury.io/py/aiida-ase3.svg)](https://badge.fury.io/py/aiida-ase3)

# aiida-ase3

A very simple possible plugin setup for using ASE with AiiDA beyond what is currently implemented. Largely a testing ground currently.

This plugin does the following 
1. Ask for a `SinglefileData` for a fully functional ASE input file. 
2. Gets back an output file in the form of `SinglefileData`

## Features

 * Add input files using `SinglefileData`:
   ```python
   SinglefileData = DataFactory('singlefile')
   inputs['input_file'] = SinglefileData(file='/path/to/input_file')
   inputs['output_filename'] = Str('file_name_from_ase.txt')
   ```

## Examples

These are the two simplest test cases 
1. `example_01.py`: Perform an SCF calculation with ASE with a GPAW calculator
2. `example_02.py`: Perform a vibrations calculation with ASE

