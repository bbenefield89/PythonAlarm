import subprocess

##
# call_notification
#
def call_notification():
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
    # calls the `notify-send` system call
    subprocess.run(['notify-send', 'Pylarm Alarm'])
    # plays .oga sound
    subprocess.run(['paplay', '/usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga'])