# coding: utf-8
import os
import sys
import time
import datetime
import urllib
import ConfigParser

PATH = os.path.dirname(os.path.abspath(sys.argv[0]))




def get_input():
    global QUERY
    # print "Opening dictation.txt"
    f = open(PATH + "\dictation.txt", 'r')
    # print "Got it.."
    x = f.read()
    # print "Reading search string.."
    # print "Search string: " + x + "Closing dictation.txt"
    f.close()
    QUERY = x
    return x


def build_url(_phrase):
    # print "---------------"
    # print "Building URL"
    phrase = _phrase.replace(" ", "+")
    url = "https://en.wikipedia.org/w/api.php?format=json&action=query&redirects=1" \
          "&prop=extracts&exintro=&explaintext=&titles=_replace_"
    w_url = url.replace("_replace_", phrase)
    # print "Url: " + w_url + "----------------"
    return w_url


def write_history(i):
    f = open(PATH + '\history.txt', 'a')
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    a = st + ": " + i
    # print a
    f.write(a)
    f.write('\n')
    f.close()


def talk(port, key, text):
    # THIS URL NEEDS TO BE SET TO YOUR PORT AND KEY ACCORDINGLY
    # THIS PART ONLY WORK IF YOU HAVE LINKS WEB REQUEST SETTINGS ON DEFAULT
    url = 'http://127.0.0.1:port/?action=[Speak("placeholder")]&key=passkey&request=enable'
    addport = url.replace("port", port)
    addkey = addport.replace("passkey", key)
    finalurl = addkey.replace("placeholder", text)  # fill in text to be spoken
    # print finalurl
    urllib.urlopen(finalurl)
