from datetime import datetime
import sys
import time


class Alarm:
    _cli_time_arg = None

    def __init__(self, cli_time_arg=''):
        self._cli_time_arg = cli_time_arg

    def set_alarm(self):
        alarm_time_as_time_struct = self.__format_alarm_time()
        alarm_time_as_sec = self.__convert_alarm_time_as_time_struct_into_sec(
            alarm_time_as_time_struct
        )
        curr_time_as_sec = self.__get_curr_time_as_sec()
        time_remaining = int((alarm_time_as_sec - curr_time_as_sec))
        self.__alarm_countdown(time_remaining)
        self._call_notification()

    def __alarm_countdown(self, time_remaining):
        while time_remaining > 0:
            time_remaining -= 1
            sys.stdout.write(f'\rTime remaining: {time_remaining}')
            time.sleep(1)

    def _call_notification(self):
        '''
        Protected method that each sub-alarm class will need to create the body
        of this method on their own. Each operating system Pylarm supports,
        Linux, Darwin, Windows, has their own way of pushing notifications to
        the desktop and playing audio files.
        '''

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
