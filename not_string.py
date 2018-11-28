# Given a string, return a new string where "not " has been added to the front.
# However, if the string already begins with "not", return the string unchanged.


def not_string(str):
    if len(str) < 3:
        return 'not ' + str

    if (str[0] == 'n') and (str[2] == 't'):
        return str

    else:
        return 'not ' + str


print(not_string('candy'))
print(not_string('x'))
print(not_string('not bad'))
print(not_string('bad'))
print(not_string('not'))
print(not_string('is not'))
print(not_string('no'))


# the problem i was having here was that the word "no" as a check was fucking up my program.
# I also can't seem to get pycharm to print results using return. This works in jup though.

