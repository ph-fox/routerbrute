#!/usr/bin/python

import requests, sys, os, re, optparse, time

read = optparse.OptionParser()
read.add_option('-t', '--target',dest='url',help='Enter Target ip/url')
read.add_option('-w', '--wordlist',dest='WORDLIST',help='Enter wordlist path')
read.add_option('-v', '--verbose',action='store_true',dest='verbose',default=False,help='VERBOSE')

(values, key) = read.parse_args()
url = values.url

WORDLIST = values.WORDLIST
verbose = values.verbose

if verbose == True:
    verbose = 0
else:
    verbose = .5


pattern = r'http'
pat = r's'
try:

    if re.match(pattern, url):
        url = re.sub(pat,'',url)
        pass
    else:
        url = 'http://'+url


    def data():
        global WORDLIST
        if WORDLIST is None:
            WORDLIST = 'list.txt'
        uzerl = open(WORDLIST, 'r')
        paszl = open(WORDLIST, 'r')
        uzer = uzerl.read().splitlines()
        pasz = paszl.read().splitlines()
        return uzer, pasz

    
    uzer, pasz = data()

    for user in uzer:
        for password in pasz:
            time.sleep(verbose)
            r = requests.get(url,auth=(user,password))
            status = r.status_code
            print("|============AL104==============")
            print("|| code: ",status)
            print("|| User: "+user)
            print("|| Password: "+password)
            print("||")
            if(status == 200):
                os.system('clear')
                print("-------------------------------------------")
                print("<<<<<<<<<<<<<<<<---------->>>>>>>>>>>>>>>>>")
                print("||============PASSWORD-FOUND============>>>")
                print("|| status = ",status)                    
                print("|| User: "+user)                       
                print("|| Password: "+password)
                print("||")
                print("||=================AL104================>>>")
                print("<<<<<<<<<<<<<<<<<<---------->>>>>>>>>>>>>>>")
                print("-------------------------------------------")
                sys.exit()

    os.system("clear")
    print
    print
    print("PASSWORD NOT FOUND!!")
    print("ERROR!!")
    print("user/password may not be on wordlist!!")
    print("pls use or create another wordlist")

except TypeError:
    os.system('python3 rbrute -h')

