if __name__ == '__main__':
    import sys
    import json
    
    from pylarm import pylarm
    from helpers.print_cli_options_error import print_cli_options_error
    
    
    # opens and converts `cli_options.json` into a dictionary
    with open('./src/cli_options.json') as data:
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