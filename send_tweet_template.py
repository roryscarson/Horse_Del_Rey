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
    twitter.update_status(status=text)
    os._exit(0)
 

tweet = subprocess.check_output(['python', '.\\tweet_generator.py']) 
output_tweet(tweet)

os._exit(0)