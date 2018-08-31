if __name__ == '__main__':
    import sys
    import json
    
    from pylarm import pylarm
    from helpers.print_cli_options_error import print_cli_options_error
    
    
    # opens and converts `cli_options.json` into a dictionary
    with open('./src/cli_options.json') as data:
        arguments = json.load(data)


    if len(sys.argv) == 1:
        pylarm()
        
    elif len(sys.argv) == 2:
        try:
            print(arguments[ '2' ][ sys.argv[1] ][ 'info' ])
        except:
            print_cli_options_error(sys.argv)
            
    elif len(sys.argv) == 3:
        try:
            print(arguments[ '3' ][ sys.argv[2] ][ sys.argv[1] ][ 'info' ])
        except:
            print_cli_options_error(sys.argv)