#!/usr/bin/python
 
import subprocess
import random
import re
import os
from twython import Twython
 
twitter = Twython("YOUR API KEY",
                  "YOUR API SECRET",
                  "YOUR ACCESS TOKEN",
                  "YOUR ACCESS TOKEN SECRET")
 
def output_tweet(text):
    print text
    #uncomment to enable tweets
    #twitter.update_status(status=text)
    os._exit(0)
 
lengthoftweet = 999
# string to build tweet
tweet = ""
 
while lengthoftweet > 140:
    tweet = ""
    rev = subprocess.check_output("ABSOLUTE PATH TO REVIEW GENERATOR")

    if len(tweet + rev.rstrip()) < 141:
        output_tweet(tweet + rev.rstrip())
    # if it is too long, try to use the first
    # sentence only (using regex)
    rev = re.search("(.+?\.).*", rev).group(1)
    tweet += rev.rstrip()
    lengthoftweet = len(tweet)
     
output_tweet(tweet)
os._exit(0)