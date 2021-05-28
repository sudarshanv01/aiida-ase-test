# -*- coding: utf-8 -*-
"""
Calculations provided by aiida_ase3.

Register calculations via the "aiida.calculations" entry point in setup.json.
"""
from aiida.common import datastructures
from aiida.engine import CalcJob
from aiida.orm import SinglefileData, Str
from aiida.plugins import DataFactory

DiffParameters = DataFactory('ase3')


class Ase3Calculation(CalcJob):
    """
    ASE calculation which operates currently on:
    1. inout: This mode takes the input file and reads in 
              the output file, nothing fancy does what it is 
              asked to do - Thanks to Leopold for this idea!

    Other possibilities: 
    2. gpaw-ready: A gpaw compatibility based setup which 
              will automatically take care of a bunch of parsing
              and input output options

    """
    @classmethod
    def define(cls, spec):
        """Define inputs and outputs of the calculation."""
        # yapf: disable
        super(Ase3Calculation, cls).define(spec)

        # set default values for AiiDA options
        spec.inputs['metadata']['options']['resources'].default = {
            'num_machines': 1,
            'num_mpiprocs_per_machine': 1,
        }
        spec.inputs['metadata']['options']['parser_name'].default = 'ase3'

        # new ports
        spec.input('metadata.options.output_filename', valid_type=str, default='aiida.out')
        spec.input('operation_mode', valid_type=Str, default=lambda: Str('inout'))
        spec.input('input_file', valid_type=SinglefileData, help='Input file which will be used', required=False)
        spec.input('output_filename', valid_type=Str, default=lambda: Str('aiida.txt'), help='AiiDA output file by default')

        # outputs
        spec.output('ase3_output', valid_type=SinglefileData, help='Output file which will be read in')

        # Error messages
        spec.exit_code(100, 'ERROR_MISSING_OUTPUT_FILES', message='Calculation did not produce all expected output files.')


    def prepare_for_submission(self, folder):
        """
        Create input files.
        TODO: Currently implemented only for input-output options

        :param folder: an `aiida.common.folders.Folder` where the plugin should temporarily place all files
            needed by the calculation.
        :return: `aiida.common.datastructures.CalcInfo` instance
        """
        codeinfo = datastructures.CodeInfo()
        codeinfo.code_uuid = self.inputs.code.uuid
        codeinfo.stdout_name = self.metadata.options.output_filename
        codeinfo.withmpi = self.inputs.metadata.options.withmpi

        codeinfo.cmdline_params = ['python', self.inputs.input_file.filename]

        # Prepare a `CalcInfo` to be returned to the engine
        calcinfo = datastructures.CalcInfo()
        calcinfo.codes_info = [codeinfo]
        calcinfo.local_copy_list = [
            (self.inputs.input_file.uuid, self.inputs.input_file.filename, self.inputs.input_file.filename),
        ]
        calcinfo.retrieve_list = [self.metadata.options.output_filename, self.inputs.output_filename.value]

        return calcinfo
