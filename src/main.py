if __name__ == '__main__':
    import json
    import sys

    from helpers.print_cli_options_error import print_cli_options_error
    from pylarm import pylarm

    # Run the arguments passed
    with open('./cli_options.json') as data:  # . represents the current directory.
        arguments = json.load(data)

    args_passed = len(sys.argv)
    if args_passed == 1:
        pylarm()

    elif args_passed == 2:
        try:
            print(arguments['2'][sys.argv[1]]['info'])
        except KeyError:
            print_cli_options_error(sys.argv)

    elif args_passed == 3:
        try:
            print(arguments['3'][sys.argv[2]][sys.argv[1]]['info'])

        except KeyError:
            print_cli_options_error(sys.argv)
