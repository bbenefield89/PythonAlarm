if __name__ == '__main__':
    import json
    import os
    import sys

    from helpers.print_cli_options_error import print_cli_options_error
    from pylarm import pylarm


    # opens and converts `cli_options.json` into a dictionary
    cli_options_file_path = os.path.dirname(os.path.realpath(__file__)) + '/cli_options.json'

    with open(cli_options_file_path) as data:
        possible_cli_arguments = json.load(data)


    cli_arguments = sys.argv
    number_of_cli_arguments = len(cli_arguments)
    path_to_src_folder = os.path.dirname(os.path.realpath(__file__))
    
    if number_of_cli_arguments == 1:
        pylarm(path_to_src_folder)

    elif number_of_cli_arguments == 2:
        try:
            # passed argument is in cli_options.json
            if cli_arguments[1] in possible_cli_arguments['2']:
                print(possible_cli_arguments['2'][cli_arguments[1]]['info'])
        
            else:
                s = cli_arguments[1].split(":")
              
                if len(s) == 2 and s[0].isdigit() and s[1].isdigit():
                    pylarm(path_to_src_folder, given_time=cli_arguments[1])
                    
                else:
                    print_cli_options_error(cli_arguments)
                    
        except KeyError:
            print_cli_options_error(cli_arguments)

    elif number_of_cli_arguments == 3:
        try:
            print(possible_cli_arguments['3'][cli_arguments[2]][cli_arguments[1]]['info'])

        except KeyError:
            print_cli_options_error(cli_arguments)
