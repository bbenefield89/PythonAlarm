import time

##
# set_alarm
#
def set_alarm(seconds):
    '''
    @summary    calls time.sleep()

    @desc       Calls the time.sleep() method and suspends Pylarm for "seconds" amount of time

    @author     Brandon Benefield
    @since      v1.0.0

    @param      int {seconds}
    @return     {void}
    '''
    
    time.sleep(seconds)