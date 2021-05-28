#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Run a test calculation on localhost.

Usage: ./example_01.py
"""
from os import path
import click
from aiida import cmdline, engine
from aiida.plugins import DataFactory, CalculationFactory
from aiida_ase3 import helpers

INPUT_DIR = path.join(path.dirname(path.realpath(__file__)), 'input_files')


def test_run(ase3_code):
    """Run a calculation on the localhost computer.

    Uses test helpers to create AiiDA Code on the fly.
    """
    if not ase3_code:
        # get code
        computer = helpers.get_computer()
        ase3_code = helpers.get_code(entry_point='ase3', computer=computer)

    # Prepare input parameters
    SinglefileData = DataFactory('singlefile')
    input_file = SinglefileData(
        file=path.join(INPUT_DIR, 'run_gpaw.py'))

    # set up calculation
    inputs = {
        'code': ase3_code,
        'input_file': input_file,
        'operation_mode':Str('inout'),
        'metadata': {
            # 'dry_run':True,
            # 'store_provenance':False,
            'description': 'Test job submission with the aiida_ase3 plugin',
            'options': {
                'max_wallclock_seconds': 120
            },
        },
    }

    # Note: in order to submit your calculation to the aiida daemon, do:
    # from aiida.engine import submit
    # future = submit(CalculationFactory('ase3'), **inputs)
    result = engine.run(CalculationFactory('ase3'), **inputs)

    # computed_diff = result['ase3'].get_content()


@click.command()
@cmdline.utils.decorators.with_dbenv()
@cmdline.params.options.CODE()
def cli(code):
    """Run example.

    Example usage: $ ./example_01.py --code diff@localhost

    Alternative (creates diff@localhost-test code): $ ./example_01.py

    Help: $ ./example_01.py --help
    """
    test_run(code)


if __name__ == '__main__':
    cli()  # pylint: disable=no-value-for-parameter
