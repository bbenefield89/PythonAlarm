import subprocess

##
# call_notification
#
def call_notification():
    # calls the `notify-send` system call
    subprocess.run(['notify-send', 'Pylarm Alarm'])
    # plays .oga sound
    subprocess.run(['paplay', '/usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga'])