#!/usr/bin/python3
def multiple_returns(sentence):
    own_tuple = ()
    if len(sentence) == 0:
        own_tuple = 0, "None"
    else:
        own_tuple = len(sentence), sentence[0]
    return own_tuple
