if __name__ == '__main__':
    import sys
    import json
    
    from pylarm import pylarm
    
    
    # opens and converts `cli_options.json` into a dictionary
    with open('./src/cli_options.json') as data:
        arguments = json.load(data)


    def print_cli_options_error(cli_args):
        if len(cli_args) == 2:
            print(f'\npylarm: option {cli_args[1]}: unexpected option')
            print('\npylarm: try \'pylarm --help\' or \'pylarm --manual\' for more information\n')
        elif len(cli_args) == 3:
            print(f'\npylarm: option {cli_args[1]} {cli_args[2]}: unexpected options')
            print('\npylarm: try \'pylarm --help\' or \'pylarm --manual\' for more information\n')


    if len(sys.argv) == 1:
        pylarm()
    elif len(sys.argv) == 2:
        if hasattr(arguments[ '2' ], sys.argv[1]) == False:
            print_cli_options_error(sys.argv)
        else:
            print(arguments[ '2' ][ sys.argv[1] ][ 'info' ])
    elif len(sys.argv) == 3:
        try:
            print(arguments[ '3' ][ sys.argv[2] ][ sys.argv[1] ][ 'info' ])
        except:
            print_cli_options_error(sys.argv)