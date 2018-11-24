import json

def get_cli_options_file(path_to_file):
    return load_cli_options_file(path_to_file)


def load_cli_options_file(path_to_file):
    with open(path_to_file) as data:
        return json.load(data)
