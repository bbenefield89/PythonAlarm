import json
import os

class CLIOptions:
    def __init__(self, path_to_file):
        self.__path_to_file = path_to_file
        self.__cli_options = self.__get_cli_options_data()

    def get_cli_arg_info(self, arg):
        try:
            return self.__cli_options['2'][arg]
        except KeyError as err:
            self.__print_cli_arg_info_error_text(err)
            raise

    def __print_cli_arg_info_error_text(self, err):
        print('\n\nPylarm Error Handling:')
        print(f'"{err}" does not appear to be a valid command for Pylarm.')
        print('Try using the "--help" command for a full list of available commands.\n')
        print('Example: pylarm --help\n\n')

    def get_cli_arg_help_info(self, arg):
        try:
            return self.__cli_options['3']['help'][arg]
        except KeyError as err:
            self.__print_cli_arg_help_info_error_text(err)
            raise
        
    def __print_cli_arg_help_info_error_text(self, err):
        print('\n\nPylarm Error Handling:')
        print(f'You appear to be looking for help on a specific command, {err}, but this command')
        print('does not contain a help file. For more information on commands that do contain a')
        print('help file please use the "--help" command for a full list of available commands.\n')
        print('Example: pylarm --help\n\n')

    def __get_cli_options_data(self):
        with open(self.__path_to_file) as data:
            return json.load(data)
