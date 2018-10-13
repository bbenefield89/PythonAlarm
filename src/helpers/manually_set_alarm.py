import time

from .check_alarm import check_alarm


##
# manually_set_alarm
#
def manually_set_alarm(mk_time, path):
    '''
    @summary    let the user manually set the alarm

    @desc       When user continuously denies the alarms attempted to be set by Pylarm then the
                user will now have the option to set their own alarm in the format of
                "MM DD YYYY HH:MM(am/pm)" e.g. "08 03 2019 10:45pm"

    @author     Brandon Benefield
    @since      v1.0.0

    @param      {void}
    @return     {void}
    '''
    # have user manually set their alarm
    alarm_time = input('Manually set the alarm(MM DD YYYY HH:MM): ')
    # parse the alarm string into datetime tuple
    p_alarm_time = time.strptime(alarm_time, '%m %d %Y %H:%M')
    # parse datetime tuple into integer of seconds
    mk_time = time.mktime(p_alarm_time)
    # get time when alarm should go off

    print(f'\nThe alarm has been set and will go off at {time.ctime(mk_time)}\n')
    check_alarm(mk_time, path)
