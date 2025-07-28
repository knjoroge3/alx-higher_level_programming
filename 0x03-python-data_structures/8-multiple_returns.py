#!/usr/bin/python3

def multiple_returns(sentence):

    first_character = sentence[0]

    if len(sentence) == 0:
        return (0, None)
    else:
        return (len(sentence), first_character)
