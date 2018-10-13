import time

from .check_if_correct import check_if_correct
from .check_alarm import check_alarm
from .manually_set_alarm import manually_set_alarm


##
# does_user_agree
#
def does_user_agree(seconds, path):
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
        print(f'\nThe alarm has been set and will go off at {time.ctime(seconds)}\n')
        check_alarm(seconds, path)
    elif alarm_accepted == 'n':
        manually_set_alarm(seconds, path)
