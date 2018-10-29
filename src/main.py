import argparse
import json
import os

from pylarm import pylarm


def time_valid(time_str):
    parts = time_str.split(':')
    return len(parts) == 2 and all(part.isdigit() for part in parts)


if __name__ == '__main__':
    option_help = {
        'alarms': ('List all pre-set alarms\n\n'
                   'Example usage:'
                   '\n\t{} --alarms'),
        'new-preset': ('Create a new pre-set alarm that can be activated by name. '
                       'You can also overwrite old ones\n\n'
                       'Example usage:'
                       '\n\t{0} --new-preset'),
        'launch': ('Launch an alarm either by name or by specified time\n\n'
                   'Example usage:'
                   '\n\t{0} --launch 13:37  # will start an alarm for 13:37'
                   '\n\t{0} --launch eggs   # will start a preset alarm "eggs"')
    }

    parser = argparse.ArgumentParser(
        description='Python script for quick alarms'
    )
    subparsers = parser.add_subparsers()
    help_args = subparsers.add_parser('help',
                                      help='displays info about particular commands')

    help_args.add_argument('option',
                           help='instructions for a particular option',
                           choices=['alarms', 'new-preset', 'launch'])

    main_opts = parser.add_mutually_exclusive_group()
    main_opts.add_argument('-a', '--alarms',
                           help='list existing presets',
                           action='store_true')
    main_opts.add_argument('-n', '--new-preset',
                           help='create a new pre-set alarm',
                           action='store_true')
    main_opts.add_argument('-l', '--launch',
                           help='launch a particular alarm',)

    args = parser.parse_args()
    src_path = os.path.dirname(os.path.realpath(__file__))

    if hasattr(args, 'option'):
        print(option_help[args.option].format(__file__))
    else:
        if os.path.exists('presets.json'):
            with open('presets.json') as presets_file:
                presets = json.load(presets_file)
        else:
            presets = {}

        if args.alarms:
            if presets:
                for preset_name, preset_time in presets.items():
                    print('* "{}": {}'.format(preset_name, preset_time))
            else:
                print('No presets to display')
        elif args.new_preset:
            new_name = input('Enter new preset name: ')
            new_time = input('Enter new preset duration: ')
            if not time_valid(new_name) and time_valid(new_time):
                presets[new_name] = new_time
                with open('presets.json', 'w') as presets_file:
                    json.dump(presets, presets_file)
                print('Preset successfully created!')
            else:
                print('Please, enter a valid duration in the format HH:MM and do not use'
                      'an HH:MM format for names')
        elif args.launch:
            if time_valid(args.launch):
                pylarm(src_path, given_time=args.launch)
            else:
                pylarm(src_path, given_duration=presets[args.launch])
        else:
            pylarm(src_path)
