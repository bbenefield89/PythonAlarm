# py modules
import time

# custom modules
from helpers.does_user_agree import does_user_agree


def pylarm(path):
    '''
    @summary    Function containing main logic for Pylarm

    @desc       User inputs a specific time, e.g. 10:45, and the Pylarm will determine the nearest
                possible time within ~24hours that the alarm can be set to. If Pylarm can not find
                a time with ~24hours that is when the helper function, manually_set_alarm(), will
                be called and the user is given the option to enter a date and time to set the
                alarm in the format of "MM DD YYYY HH:MM(am/pm)", e.g. "08 03 2019 10:45pm"

    @author     Brandon Benefield
    @since      v1.0.0

    @param      {void}
    @return     {void}
    '''
    alarm_time = input('\nWhat time (hh:mm): ')
    local_time = time.localtime()
    alarm_time = time.strptime(f'{local_time[1]} {local_time[2]} {local_time[0]} {alarm_time}am', '%m %d %Y %I:%M%p')

    if local_time < alarm_time:  # time is in the am, and has not passed
        does_user_agree(alarm_time, path)
    else:  # set alarm to pm and try again
        alarm_time = alarm_time[0:3] + (alarm_time[3] + 12,) + alarm_time[4:]  # alternate way to add 12 hrs
        if local_time < alarm_time:  # alarm is in the pm and has not passed
            does_user_agree(alarm_time, path)
        else:  # alarm is in the pm and has passed
            alarm_time = alarm_time[0:2] + (alarm_time[2] + 1,) + (alarm_time[3] - 12,) + alarm_time[4:]  # +1d, -12h
            does_user_agree(alarm_time, path)