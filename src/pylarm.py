# py modules
import time

# custom modules
from helpers.does_user_agree import does_user_agree


def pylarm(path, given_time=None):
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

    alarm_time   = input('\nWhat time? (HH:MM)[24Hrs format]: ')

    curr_time    = time.localtime()
    
    p_alarm_time = time.strptime(f'{curr_time[1]} {curr_time[2]} {curr_time[0]} {alarm_time}', '%m %d %Y %H:%M')
    mk_time      = time.mktime(p_alarm_time)

    if curr_time[3]<int(alarm_time[0]+alarm_time[1]):
        p_alarm_time = time.strptime(f'{curr_time[1]} {curr_time[2]} {curr_time[0]} {alarm_time}', '%m %d %Y %H:%M')
        mk_time      = time.mktime(p_alarm_time)
        does_user_agree(mk_time, path)

    elif curr_time[3]==int(alarm_time[0]+alarm_time[1]):
        if curr_time[4]<=int(alarm_time[3]+alarm_time[4]):
            p_alarm_time = time.strptime(f'{curr_time[1]} {curr_time[2]} {curr_time[0]} {alarm_time}', '%m %d %Y %H:%M')
            mk_time      = time.mktime(p_alarm_time)
            does_user_agree(mk_time, path)

        else:
            p_alarm_time = time.strptime(f'{curr_time[1]} {curr_time[2]+1} {curr_time[0]} {alarm_time}', '%m %d %Y %H:%M')
            mk_time      = time.mktime(p_alarm_time)
            does_user_agree(mk_time, path)




    else:
        p_alarm_time = time.strptime(f'{curr_time[1]} {curr_time[2]+1} {curr_time[0]} {alarm_time}', '%m %d %Y %H:%M')
        mk_time = time.mktime(p_alarm_time)

        does_user_agree(mk_time, path)
