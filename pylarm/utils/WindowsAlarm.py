import os
import subprocess
import sys

from utils.Alarm import Alarm
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../../')
from definitions import ROOT_DIR


class WindowsAlarm(Alarm):
    def __init__(self, cli_time_arg=''):
        super().__init__(cli_time_arg)

    def _call_notification(self):
        import winsound
        import ctypes

        winsound.PlaySound(
            alarm_sound_path + "/sounds/alarm-clock-elapsed.wav",
            winsound.SND_ASYNC | winsound.SND_LOOP
        )
        messageBox = ctypes.windll.user32.MessageBoxW
        returnValue = messageBox(
            None,
            "Your alarm went off!",
            "Pylarm",
            0x40 | 0x0
        )
