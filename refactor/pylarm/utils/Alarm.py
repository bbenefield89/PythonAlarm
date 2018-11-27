from datetime import datetime
import os
import subprocess
import sys
import time

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../../')
from definitions import ROOT_DIR


class Alarm:
    def __init__(self, cli_time_arg=''):
        self.cli_time_arg = cli_time_arg

    def set_alarm(self):
        alarm_time_as_time_struct = self.__format_alarm_time()
        alarm_time_as_sec = self.__convert_alarm_time_as_time_struct_into_sec(
            alarm_time_as_time_struct
        )
        curr_time_as_sec = self.__get_curr_time_as_sec()
        time_remaining = int((alarm_time_as_sec - curr_time_as_sec))
        self.__alarm_countdown(time_remaining)
        self.__call_notification()

    def __alarm_countdown(self, time_remaining):
        while time_remaining > 0:
            time_remaining -= 1
            sys.stdout.write(f'\rTime remaining: {time_remaining}')
            time.sleep(1)

    def __call_notification(self):
        alarm_sound_path = ROOT_DIR + '/pylarm/sounds/alarm-clock-elapsed.oga'
        subprocess.run(['notify-send', 'Pylarm Alarm'])
        subprocess.run(['paplay', alarm_sound_path])

    def __convert_alarm_time_as_time_struct_into_sec(
        self,
        alarm_time_as_time_struct
    ):
        return time.mktime(alarm_time_as_time_struct)

    def __format_alarm_time(self):
        alarm_time_given = self.__ask_user_for_alarm_time()
        curr_time = self.__get_curr_time_as_struct_time()
        (year, month, day) = curr_time[:3]
        time_format = '%d %m %Y %I:%M%p'
        alarm_time = time.strptime(
            f'{day} {month} {year} {alarm_time_given}',
            time_format
        )
        return alarm_time

    def __ask_user_for_alarm_time(self):
        return input('\nWhat time should I set the alarm for: ')

    def __get_curr_time_as_struct_time(self):
        return time.localtime()

    def __get_curr_time_as_sec(self):
        return time.time()
