import time

from .set_alarm import set_alarm
from .call_notification import call_notification

##
# manually_set_alarm
#
def manually_set_alarm():
    ''' let the user manually set the alarm '''
    # have user manually set their alarm
    alarm_time = input('Manually set the alarm: MM DD YYYY HH:MM(am/pm)')
    # parse the alarm string into datetime tuple
    p_alarm_time = time.strptime(alarm_time, '%m %d %Y %I:%M%p')
    # parse datetime tuple into integer of seconds
    mk_time = time.mktime(p_alarm_time)
    # get time when alarm should go off
    seconds_until_alarm = int(mk_time * 1) - int(time.time() * 1)

    print(f'\nThe alarm has been set and will go off at {time.ctime(mk_time)}\n')
    set_alarm(seconds_until_alarm)
    call_notification()