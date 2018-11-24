import os
import sys

from utils.CLIOptions import CLIOptions


sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../pylarm')
path_to_cli_options = os.path.dirname(os.path.realpath(__file__)) + '/../pylarm/cli_options.json'

def test_CLIOptions_get_cli_arg_info():
    cli_options = CLIOptions(path_to_cli_options)

    assert type(cli_options.get_cli_arg_info('--help')) == str
    assert type(cli_options.get_cli_arg_info('--alarms')) == str
    assert type(cli_options.get_cli_arg_info('--new-preset')) == str


def test_CLIOptions_get_cli_arg_help_info():
    cli_options = CLIOptions(path_to_cli_options)
    alarm_help_info = '\n--alarms help'
    new_preset_help_info = '\n--new-preset help'

    assert type(cli_options.get_cli_arg_help_info('--alarms')) == str
    assert cli_options.get_cli_arg_help_info('--alarms') == alarm_help_info

    assert type(cli_options.get_cli_arg_help_info('--new-preset')) == str
    assert cli_options.get_cli_arg_help_info('--new-preset') == new_preset_help_info