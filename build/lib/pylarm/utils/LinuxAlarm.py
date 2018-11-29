import os
import subprocess
import sys

from utils.Alarm import Alarm
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../../')
from definitions import ROOT_DIR


class LinuxAlarm(Alarm):
    def __init__(self, cli_time_arg=''):
        super().__init__(cli_time_arg)

    def _call_notification(self):
        alarm_sound_path = ROOT_DIR + '/pylarm/sounds/alarm-clock-elapsed.oga'
        subprocess.run(['notify-send', 'Pylarm Alarm'])
        subprocess.run(['paplay', alarm_sound_path])
