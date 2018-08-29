import time

from .check_if_correct import check_if_correct
from .set_alarm import set_alarm
from .call_notification import call_notification
from .manually_set_alarm import manually_set_alarm

##
# does_user_agree
#
def does_user_agree(seconds):
    '''
    @summary    Checks if user input time is correct

    @desc       Check if the time the user has specified is correct. If not then the user has the
                choice to manually set a date and time for the alarm

    @author     Brandon Benefield
    @since      v1.0.0

    @param      int {seconds}
    @return     {void}
    '''
    
    alarm_accepted = check_if_correct()

    if alarm_accepted == 'y':
        curr_time  = int(time.time() * 1)
        alarm_time = int(seconds * 1) - curr_time
        
        print(f'\nThe alarm has been set and will go off at {time.ctime(seconds)}\n')
        set_alarm(alarm_time)
        call_notification()
    elif alarm_accepted == 'n':
        # print('\n\nSET ALARM TO PM\n\n')
        manually_set_alarm()