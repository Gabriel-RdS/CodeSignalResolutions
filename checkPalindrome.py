"""
https://app.codesignal.com/arcade/intro/level-1/s5PbmwxfECC52PWyQ
"""


def checkPalindrome(inputString):
    if inputString[::-1] == inputString:
        return True
    else:
        return False
