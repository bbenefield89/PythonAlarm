##
# check_if_correct:
#
def check_if_correct():
    '''
    @summary    reusable while loop to check if alarm time is correct

    @desc       Infinitely loops as long as the user does not input a "Y" or "N"

    @author     Brandon Benefield
    @since      v1.0.0

    @param      {void}
    @return     {void}
    '''
    while True:
        alarm_accepted = input('Is this correct [Y/N]: ')[:1].lower()

        if alarm_accepted == 'y' or alarm_accepted == 'n':
            return alarm_accepted