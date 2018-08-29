##
# check_if_correct:
#
def check_if_correct():
    ''' reusable while loop to check if alarm time is correct '''
    acceptable = False
    while not acceptable:
        alarm_accepted = input('Is this correct [Y/N]: ').lower()

        if alarm_accepted == 'y' or alarm_accepted == 'n':
            return alarm_accepted