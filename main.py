import subprocess
import time

alarm_time   = input('\nWhat time: ')
curr_time    = time.localtime()
# alarm will attempt to set this for AM
p_alarm_time = time.strptime(f'{curr_time[1]} {curr_time[2]} {curr_time[0]} {alarm_time}am', '%m %d %Y %I:%M%p')
mk_time      = time.mktime(p_alarm_time)

##
# check_if_correct:
#   reusable while loop to check if alarm time is correct
#
def check_if_correct():
    acceptable = False
    while not acceptable:
        alarm_accepted = input('Is this correct [Y/N]: ').lower()

        if alarm_accepted == 'y' or alarm_accepted == 'n':
            return alarm_accepted


##
# set_alarm
#
def set_alarm(seconds):
    time.sleep(seconds)
    
    
##
# call_notification
#
def call_notification():
    subprocess.run(['notify-send', 'SOUND ALARM!'])


##
# does_user_agree
#
def does_user_agree(seconds):
    alarm_accepted = check_if_correct()

    if alarm_accepted == 'y':
        curr_time  = int(time.time() * 1)
        alarm_time = int(seconds * 1) - curr_time
        
        print(f'\nThe alarm has been set and will go off at {time.ctime(seconds)}\n')
        set_alarm(alarm_time)
        call_notification()
    elif alarm_accepted == 'n':
        print(f'\nSET TIME TO PM\n\n')


##
# main
#
if __name__ == '__main__':
    if int(mk_time * 1000) <= int(time.time() * 1000):
        # use the same values but for PM
        p_alarm_time = time.strptime(f'{curr_time[1]} {curr_time[2]} {curr_time[0]} {alarm_time}pm', '%m %d %Y %I:%M%p')
        mk_time      = time.mktime(p_alarm_time)

        if int(mk_time * 1000) <= int(time.time() * 1000):
            # use the original values in the AM but for the next day: curr_time[2] + 1
            p_alarm_time = time.strptime(f'{curr_time[1]} {curr_time[2] + 1} {curr_time[0]} {alarm_time}pm', '%m %d %Y %I:%M%p')
            mk_time      = time.mktime(p_alarm_time)

            print(f'\nThe alarm is set to go off at {time.ctime(mk_time)}\n\n')

            does_user_agree(mk_time)

        # if setting alarm to PM allowed
        # check if user is okay with this time
        # e.g. August 25 2018 4:40pm
        else:
            does_user_agree(mk_time)
    else:
        does_user_agree(mk_time)