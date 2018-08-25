import time

alarm_time   = input('What time: ')
curr_time    = time.localtime()
# alarm will attempt to set this for AM
p_alarm_time = time.strptime(f'{curr_time[1]} {curr_time[2]} {curr_time[0]} {alarm_time}am', '%m %d %Y %I:%M%p')
mk_time      = time.mktime(p_alarm_time)

# reusable while loop to check if alarm time is correct
def check_if_correct():
    acceptable = False
    while not acceptable:
        alarm_accepted = input('\n\nIs this correct [Y/N]: ').lower()

        if alarm_accepted == 'y' or alarm_accepted == 'n':
            return alarm_accepted


def does_user_agree():
    alarm_accepted = check_if_correct()

    if alarm_accepted == 'y':
        print(f'\n\nThe alarm has been set and will go off at {time.ctime(mk_time)}\n\n')
    elif alarm_accepted == 'n':
        print(f'\n\nSET TIME TO PM\n\n')

if int(mk_time * 1000) <= int(time.time() * 1000):
    print(f'\n\nWRONG TIME 1 {time.ctime(mk_time)}\n\n')
    # use the same values but for PM
    p_alarm_time = time.strptime(f'{curr_time[1]} {curr_time[2]} {curr_time[0]} {alarm_time}pm', '%m %d %Y %I:%M%p')
    mk_time      = time.mktime(p_alarm_time)

    if int(mk_time * 1000) <= int(time.time() * 1000):
        print(f'\n\nWRONG TIME 2 {time.ctime(mk_time)}\n\n')
        # use the original values in the AM but for the next day: curr_time[2] + 1
        p_alarm_time = time.strptime(f'{curr_time[1]} {curr_time[2] + 1} {curr_time[0]} {alarm_time}pm', '%m %d %Y %I:%M%p')
        mk_time      = time.mktime(p_alarm_time)

        print(f'\n\nThe alarm is set to go off at {time.ctime(mk_time)}\n\n')

        does_user_agree()
        
    # if setting alarm to PM allowed
    # check if user is okay with this time
    # e.g. August 25 2018 4:40pm
    else:
        print(f'\n\nCHECK IF THIS IS RIGHT 2\n\n')

else:
    print(f'\n\nCHECK IF THIS IS RIGHT 1\n\n')

# ===============
# alarm_time += meridiem

# # parse the alarm_time string into a format python understands
# parsed_alarm_time = time.strptime(alarm_time, '%I:%M%p')
# # convert alarm_time tuple into string
# string_alarm_time = time.strftime('%I:%M%p', parsed_alarm_time)
# # current time since epoch
# curr_time = int(time.time() * 1000.0)

# print(parsed_alarm_time)
# ===============

# print(alarm_time);

# if meridiem == 'am':
#     alarm_format = '%I:%M'
# elif meridiem == 'pm':
#     alarm_format = '%H:%M'

# alarm_time = time.strptime(alarm_time, alarm_format)
# alarm_format = '    '

# print(f'The alarm will go off at {time.strftime(alarm_time, '')}')

# # time.sleep((alarm_time - now).total_seconds())

# print("Hello")