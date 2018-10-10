import platform
import subprocess
import ctypes
import sys

##
# call_notification
#
def call_notification(path):
    '''
    @summary    Run OS subprocesses

    @desc       When Pylarm ends it will call these two OS subprocesses.

                Linux:
                    "notify-send" sends a notification to a linux based OS.
                    "paplay" will play the specified ".oga" sound file.
                macOS:
                    "osascript" uses applescript to send a notification using
                    native macOS notifications API.
                    "afplay" will play the specified ".aiff" sound file.

    @author     Brandon Benefield
    @since      v1.0.0

    @param      {void}
    @return     {void}
    '''
    if platform.system() == 'Linux':
        alarm_sound_path = path + '/sounds/alarm-clock-elapsed.oga'
        # calls the `notify-send` system call
        subprocess.run(['notify-send', 'Pylarm Alarm'])
        # plays .oga sound
        subprocess.run(['paplay', alarm_sound_path])

    elif platform.system() == 'Windows':
        import winsound
        winsound.PlaySound(path + "/sounds/alarm-clock-elapsed.wav",winsound.SND_ASYNC|winsound.
        SND_LOOP)
        messageBox = ctypes.windll.user32.MessageBoxW
        returnValue = messageBox(None,"Your alarm went off!","Pylarm",0x40 | 0x0)


    elif platform.system() == 'Darwin':  # aka 'macOS/ OSX'
        # Use .aiff files for macOS. `afplay` system call does not support .oga
        alarm_sound_path = path + '/sounds/alarm-clock-elapsed.aiff'

        # Calls native macOS natification using applescript
        subprocess.run([
            'osascript',
            '-e display notification \"Your alarm went off!\" with title \"Pylarm\"'
        ])

        # plays .aiff sound
        subprocess.run(['afplay', alarm_sound_path])

    else:
        print('\n\nUNSUPPORTED OPERTING SYSTEM\n\n')
