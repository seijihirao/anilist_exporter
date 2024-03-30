import argparse
import os
import sys
import importlib.util

from lib.anilist_client import AnilistExporter
from lib.exporters import letterboxd

EXPORTERS_DIR = 'lib/exporters'

def main():
    # Adding current dir to sys path
    sys.path.insert(0, './')


    parser = argparse.ArgumentParser(description='Export your anilist to any format')
    parser.add_argument('-u', '--user', '--username', 
                        action='store', 
                        help='Sets anilist username to export.')
    parser.add_argument('-e', '--exporter', 
                        action='store',
                        help='Selects exporter script file from lib/exporters.')

    args = parser.parse_args()

    anilist_exporter = AnilistExporter(args.user)

    # Gets exporter module
    spec = importlib.util.spec_from_file_location(
        args.exporter,
        os.path.join('.', EXPORTERS_DIR, f'{args.exporter}.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    anilist_exporter.export(module.Exporter())
