import sys

from utils.CLIOptions import CLIOptions


if __name__ == '__main__':
    cli_options = CLIOptions('./cli_options.json')
    cli_args = sys.argv
    cli_args_count = str(len(cli_args))


    if cli_args_count == '1':
        print('NO ARGUMENTS GIVEN')

    elif cli_args_count == '2':
        arg = cli_args[1]
        print(cli_options.get_cli_arg_info(arg))

    elif cli_args_count == '3':
        arg = cli_args[1]
        print(cli_options.get_cli_arg_help_info(arg))

    else:
        print(cli_options.get_cli_arg_info('--help'))
