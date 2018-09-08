import os
import platform
import subprocess
import sys

##
# call_notification
#
def call_notification(path):
    '''
    @summary    Run OS subprocesses

    @desc       When Pylarm ends it will call these two OS subprocesses. "notify-send" sneds a
                notification to a linux based OS. "paplay" will play the specified ".oga" sound
                file.

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
        print('\n\nNEED SUPPORT FOR WINDOWS\n\n')

    else:
        print('\n\nNEED SUPPORT FOR MAC\n\n')