import os
import sys
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../')

from helpers.get_cli_options_file import get_cli_options_file


def test_load_cli_options_file():
    path_to_cli_options_file = os.path.dirname(os.path.realpath(__file__))  + '/../cli_options.json'
    cli_options_file = get_cli_options_file(path_to_cli_options_file)

    assert type(cli_options_file) == dict