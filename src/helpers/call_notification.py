import subprocess

##
# call_notification
#
def call_notification():
    # plays .oga sound
    subprocess.run(['paplay', '/usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga'])
    # calls the `notify-send` system call
    subprocess.run(['notify-send', 'Pylarm Alarm'])