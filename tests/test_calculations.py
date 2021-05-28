# -*- coding: utf-8 -*-
""" Tests for calculations

"""
import os
from aiida.plugins import DataFactory, CalculationFactory
from aiida.engine import run
from aiida.orm import SinglefileData, Str

from . import TEST_DIR


def test_process(ase3_code):
    """Test running a calculation
    note this does not test that the expected outputs are created of output parsing"""

    # Prepare input parameters
    Ase3Parameters = DataFactory('ase3')

    input_file = SinglefileData(
        file=os.path.join(TEST_DIR, 'input_files', 'run_gpaw.py'))

    # set up calculation
    inputs = {
        'code': ase3_code,
        'input_file': input_file,
        'operation_mode':Str('inout'),
        'metadata': {
            'options': {
                'max_wallclock_seconds': 30
            },
        },
    }

    result = run(CalculationFactory('ase3'), **inputs)
    computed_diff = result['ase3'].get_content()

    assert 'ase3_output' in computed_diff
