if __name__ == '__main__':
    import json
    import os
    import sys
    
    from helpers.print_cli_options_error import print_cli_options_error
    from pylarm import pylarm
    
    
    # opens and converts `cli_options.json` into a dictionary
    cli_options_file_path = os.path.dirname(os.path.realpath(__file__)) + '/cli_options.json'
    
    with open(cli_options_file_path) as data:
        arguments = json.load(data)


    argv_len = len(sys.argv)

    if argv_len == 1:
        pylarm()
        
    elif argv_len == 2:
        try:
            print(arguments[ '2' ][ sys.argv[1] ][ 'info' ])
            
        except KeyError:
            print_cli_options_error(sys.argv)
            
    elif argv_len == 3:
        try:
            print(arguments[ '3' ][ sys.argv[2] ][ sys.argv[1] ][ 'info' ])
            
        except KeyError:
            print_cli_options_error(sys.argv)