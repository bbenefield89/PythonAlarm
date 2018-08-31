def print_cli_options_error(cli_args):
    if len(cli_args) == 2:
        print(f'\npylarm: option {cli_args[1]}: unexpected option')
        print('\npylarm: try \'pylarm --help\' or \'pylarm --manual\' for more information\n')
    elif len(cli_args) == 3:
        print(f'\npylarm: option {cli_args[1]} {cli_args[2]}: unexpected options')
        print('\npylarm: try \'pylarm --help\' or \'pylarm --manual\' for more information\n')