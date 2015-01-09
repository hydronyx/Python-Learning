#!/usr/bin/env python3

# The infinite monkey theorem : The theorem states that a monkey hitting keys at random on a
# typewriter keyboard for an infinite amount of time will almost surely type a given text,
# such as the complete works of William Shakespeare. Well, suppose we replace a monkey with
# a Python function. How long do you think it would take for a Python function to generate
# just one sentence of Shakespeare?
# The sentence we’ll shoot for is: “methinks it is like a weasel”
# The Program returns the number of iterations spent to hit the target/goal string.

import random

def genRandomString(strlen) :
    letter = "abcdefghijklmnopqrstuvwxyz "; result = ""

    for i in range(strlen) :
        result = result + letter[random.randrange(27)]

    return result


def score(goal, test_string) :
    match_char = 0

    for i in range(len(goal)) :
        if goal[i] == test_string[i] :
            match_char = match_char + 1

    return (match_char / len(goal))


def getLoops(goalstr) :
    loop_count = 0; random_string = genRandomString(len(goalstr))
    
    if goalstr == "exit" :
        print ("\nOhh, I Just saw the dreadful \"Exit\". \n " \
               " I feel I should wish you a Good Bye then, See ya later :)")
        exit()
    else :
        while ( score(goalstr, random_string) < 1.0 ) :
            print (random_string)
            loop_count = loop_count + 1
            random_string = genRandomString(len(goalstr))

    return loop_count


def main():
    print (" \n Python program to implement Infinite monkey theorem \n")
    print ("Loops : ", getLoops(input("Enter string you want to find match for : ")))

main()