import re


def strongPWD(apwd):
    # if len(apwd) >= 8:
    #     validatePWD = re.compile(r'''(
    #     (\d+.*[a-z]+.*[A-Z]+)|
    #     (\d+.*[A-Z]+.*[a-z]+)|
    #     ([a-z]+.*[A-Z]+.*\d+)|
    #     ([A-Z]+.*[a-z]+.*\d+)|
    #     ([A-Z]+.*\d+.*[a-z]+)|
    #     ([a-z]+.*\d+.*[A-Z]+)
    #     )''', re.VERBOSE)
    #     pwdMatch = validatePWD.search(apwd)
    #     if pwdMatch is not None:
    #         print(pwdMatch.group())
    #         print('validate pwd')
    #     else:
    #         print('invalidate rule')
    # else:
    #     print('8 character at least')
    len_regex = re.compile(r'.{8,}')
    len_match = len_regex.search(apwd)
    a_regex = re.compile(r'[a-z]+')
    a_match = a_regex.search(apwd)
    A_regex = re.compile(r'[A-Z]+')
    A_match = A_regex.search(apwd)
    num_regex = re.compile(r'\d+')
    num_match = num_regex.search(apwd)

    if len_match and a_match and A_match and num_match:
        print(len_match.group())
        print('validate pwd')
    else:
        print('invalidate pwd')


myPwd = 'f+Y+_9+++'
strongPWD(myPwd)