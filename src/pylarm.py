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
    alarm_time   = input('\nWhat time: ')
    curr_time    = time.localtime()
    # alarm will attempt to set this for AM
    p_alarm_time = time.strptime(f'{curr_time[1]} {curr_time[2]} {curr_time[0]} {alarm_time}am', '%m %d %Y %I:%M%p')
    mk_time      = time.mktime(p_alarm_time)

    if int(mk_time * 1000) <= int(time.time() * 1000):
        # use the same values but for PM
        p_alarm_time = time.strptime(f'{curr_time[1]} {curr_time[2]} {curr_time[0]} {alarm_time}pm', '%m %d %Y %I:%M%p')
        mk_time      = time.mktime(p_alarm_time)

        if int(mk_time * 1000) <= int(time.time() * 1000):
            '''
            an error occurs at the end of each month where Pylarm attempts to set the day, curr_time[2], to a day
            that doesnt exist in that month, e.g. January 32
            this try/except will catch that error and increase the month by 1 and reset the day to 1
            i.e. January 32 => February 1
            '''
            try:
                # use the original values in the AM but for the next day: curr_time[2] + 1
                p_alarm_time = time.strptime(f'{curr_time[1]} {curr_time[2] + 1} {curr_time[0]} {alarm_time}pm', '%m %d %Y %I:%M%p')

            except:
                p_alarm_time = time.strptime(f'{curr_time[1] + 1} 01 {curr_time[0]} {alarm_time}pm', '%m %d %Y %I:%M%p')

            
            mk_time = time.mktime(p_alarm_time)

            print(f'\nThe alarm is set to go off at {time.ctime(mk_time)}\n\n')

            does_user_agree(mk_time, path)

        # if setting alarm to PM allowed
        # check if user is okay with this time
        # e.g. August 25 2018 4:40pm
        else:
            does_user_agree(mk_time, path)
    else:
        does_user_agree(mk_time, path)