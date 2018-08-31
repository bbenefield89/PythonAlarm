import sys
import time

from .call_notification import call_notification

##
# check_alarm
#
def check_alarm(seconds):
    '''
    @summary    calls time.sleep()

    @desc       Calls the time.sleep() method and suspends Pylarm for "seconds" amount of time

    @author     Brandon Benefield
    @since      v1.0.0

    @param      int {seconds}
    @return     {void}
    '''
    
    # time.sleep(seconds)
    done = False
    time_remaining = int(seconds - time.time()) * 1
    
    while not done:
        time_remaining -= 1
        
        if time_remaining <= -1:
            print('\n')
            return call_notification()
        # this odd check is needed because without it whenever the time goes below a double digit
        # the terminal will update with a trailing `s` character e.g. `Alarm will go off in 9 secondss`
        elif time_remaining >= 10:
            sys.stdout.write(f'\rAlarm will go off in {time_remaining} seconds')
        else:
            sys.stdout.write(f'\rAlarm will go off in 0{time_remaining} seconds')

        time.sleep(1)