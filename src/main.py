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
    src_path = os.path.dirname(os.path.realpath(__file__))
    
    if argv_len == 1:
        pylarm(src_path)
        
    elif argv_len == 2:
        try:
            # passed argument is in cli_options.json
            if sys.argv[ 1 ] in arguments[ '2' ]:
                print(arguments[ '2' ][ sys.argv[1] ][ 'info' ])
            else:
                s = sys.argv[1].split(":")
                if len(s) == 2 and s[0].isdigit() and s[1].isdigit():
                    pylarm(src_path, given_time=sys.argv[1])
                else:
                    print_cli_options_error(sys.argv)
            
        except KeyError:
            print_cli_options_error(sys.argv)
            
    elif argv_len == 3:
        try:
            print(arguments[ '3' ][ sys.argv[2] ][ sys.argv[1] ][ 'info' ])
            
        except KeyError:
            print_cli_options_error(sys.argv)
