import subprocess

##
# call_notification
#
def call_notification():
    subprocess.run(['notify-send', 'SOUND ALARM!'])