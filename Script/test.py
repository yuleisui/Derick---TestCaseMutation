#!/usr/bin/python

import sys
import re

print('Testing Program')

file_name = sys.argv[1].split('.')
copy_num = sys.argv[2] #number of test case copies to make?
line_inc = 0 #number of lines in file    
class_name = ''

new_file_list = []  


if not copy_num.isdigit():
    copy_num = 1


def analyse_code(code):
    line_count = 0
    mayAlias_count = 0
    notAlias_count = 0
    for line in code:
        #print line
        match_class = re.search("(\w+)* class (\w+)", line)  # Find class name (Doesn't handle extends)
        match_mayAlias = re.search("^\s+ mayAlias",line) # Regex for mayAlias/postive check.
        match_notAlias = re.search("^\s+ notAlias",line) # Regex for notAlias/negative check.
               
        if match_class: # get class_name
            class_name = match_class.group(2)
            new_file_list.append([line_count,'class:'+class_name])
            
            print match_class.group()
            print ('classname:'+class_name)
        elif match_mayAlias:
            mayAlias_count =+ 1
            new_file_list.append([line_count,'mayAlias'])
        elif match_notAlias:
            notAlias_count =+ 1
            new_file_list.append([line_count,'notAlias'])
        
        line_count +=1 # Increment

    print ('mayAlias:'+str(mayAlias_count))
    print ('notAlias:'+str(notAlias_count))
    print (new_file_list)

with open(sys.argv[1], "r") as old_file: #Code opens test case and makes copies.
    curr_num = 0
    #print('test cases created: '+ str(copy_num))
    code = old_file.readlines()
    print(str(len(code)+1)+' lines')
    
    analyse_code(code)
    
    while int(curr_num) < int(copy_num):
        #print('currnum:'+str(curr_num)+', copy_num:'+str(copy_num))
        if curr_num > 10:
            sys.exit()
        curr_num+=1
        new_file = open(file_name[0]+'New'+str(curr_num)+'.'+file_name[1], "w")
        for line in code:
            #print line
            line_inc+=1
            new_file.write(line)
    
     
    old_file.close()
    new_file.close()  
'''
#!/usr/bin/python

import sys
import socket
import ssl
import keyutils
from datetime import datetime
import os.path
import threading
import re
from Crypto.PublicKey import RSA
from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_OAEP

def verify_certificate_all(ca,cert): # 1,2,3 failed certificate verification, 0 = success
    if keyutils.verify_certificate(ca,cert) == 0: # Verify signature
        return 1
    if keyutils.read_issuer(cert) != keyutils.read_subject(ca): # Verify issuer
        return 2
    if (datetime.strptime(keyutils.read_notafter(cert),'%Y%m%d%H%M%SZ') < datetime.now()): # Compare Expiry Date to current Date.
        return 3
    return 0

def verify_certificate_cn(t,cert): #1 CN=minissl, 2 CN=minissl-ca, 3 CN=minissl-SERVER
    if t == 1:
        cn = re.findall('/CN=minissl/',keyutils.read_subject(cert))
    elif t == 2:
        cn = re.findall('/CN=minissl-ca/',keyutils.read_subject(cert))
    elif t == 3:
        cn = re.findall('/CN=minissl-SERVER/',keyutils.read_subject(cert))
    if len(cn) == 1:
        return True
    else:
        return False
    

def check_file_validity(filepath):
    return os.path.isfile(filepath)

if (len(sys.argv)!=6): #Check if inputs are valid.  Saves alot of time at the end.
     print "Usage ./server.py listen_port servercert serverprivkey {SimpleAuth,ClientAuth} payload.txt"
     print len(sys.argv)
     exit()
     
if sys.argv[1].isdigit() == False:
    print "Error:Invalid Port Number"
    exit()     
     
if check_file_validity(sys.argv[2])==True:
    scert = open(sys.argv[2],'r').read()
else:
    print "Error:Invalid Server Certificate"
    exit()
    
if check_file_validity(sys.argv[3])==True:
    sprk = open(sys.argv[3],'r').read()
else:
    print "Error:Invalid Server Private Key file"
    exit()

if check_file_validity(sys.argv[5])==True:
    payload = open(sys.argv[5],'r').read()
else:
    print "Error:Invalid Server Data"
    exit()
        
if (sys.argv[4]!='SimpleAuth' and sys.argv[4]!='ClientAuth'):
    print "Error:Invalid Mode"
    exit()
else:
    mode = sys.argv[4]

capath = 'minissl-ca.pem'

if check_file_validity(capath) == True:
    ca = open(capath,'r').read() # ca is fetched from client?

noncec = None 
nonces = None


#Cert verification - Only need three for client verification

#1) verify_certicate(ca,scert) == 1 #check signature
#2) issuer(cert) == subject(ca)     #check issuer
#3) notafter(ca) > notafter(scert)  #check expiration
#rsa = keyutils.read_privkey_from_pem(spk)

#print rsa
#verify is 0 for fail, 1 for succession.
#print keyutils.verify_certificate(ca,scert)



print socket.getfqdn()

class ClientThread(threading.Thread): # Create a new ClientThread for each Client
    def __init__(self,host,port,clientsocket):
        threading.Thread.__init__(self)
        self.clientsocket = clientsocket
        self.host = host
        self.port = int(port)
        print "New Thread Created"
    
    def run(self): # Do I need loop?
        noncec = None # Store session nonce for client and server here
        nonces = None
        encrypt = None
        init = None # Internal Integrity Checkers init/mcv to ensure payload cannot be sent unless specific checks are validated (hypothetical injection attack)
        mcv = None
        laststate = 0 # Last State tells you what part of handshake/miniget the client/server is at. 1 ClientInit 2 ServerInit 3 ClientKex 4 ServerKex 5 Request 6 Payload
        while True:
            try:
                rmsg = ''
                temp = ''
                
                temp = self.clientsocket.recv(1024)
                rmsg += temp
                while temp.endswith('|b|end') == False: # Loop to collect entire messsage from sendall(), concat message into string
                    temp = self.clientsocket.recv(1024)
                    rmsg += temp
                    
                #print rmsg
                data = rmsg.split('|b|') #Use a delimiter with more than one char to accomadate nonce symbols
                if data[0]=='ClientInit': # ClientInit noncec AES-HMAC - Protocol Step 2
                    laststate = 1
                    print 'ClientInit'
                    clientinit = rmsg
                    noncec = data[1]
                    
                    nonces = keyutils.generate_nonce()
                     
                    smsg = 'ServerInit'+'|b|'+nonces+'|b|'+data[2]+'|b|'+scert # Got it wrong        
                    
                    if (mode == 'ClientAuth'):
                        smsg+='|b|CertReq|b|end'
                    else:
                        smsg+= '|b|end'
                    serverinit = smsg
                    init = 1
                    laststate = 2
                    print laststate
                elif data[0]=='ClientKex': #ClientKex ES(p)[0] ES(p)[1] ES(p)[2] mc [CertC SigC(ns) ES(p)] - Protocol Step 4
                    clientkex = rmsg
                    laststate = 3
                # If SimpleAuth, no need for client authentication
                    print 'ClientKex'
                    if mode=='ClientAuth': # Verify client first
                        verify = verify_certificate_all(ca,data[5])
                        if verify == 1:
                            print ('Certificate Verification Failed, Verify Error:%d laststate:%d' %verify %laststate)
                            self.clientsocket.close()
                            continue
                    
                    #decrypt p with sprk -- Incorrect Padding?? keyutils secretly already implemented RSA.import
                    rsa_key = keyutils.read_privkey_from_pem(sprk) #RSA_Cipher Object, opposite of spub
                    aesmsg = data[1] # get aes hybrid
                    iv = data[2]
                    cipher_aes = data[3]
    
                    rsa_cipher = PKCS1_OAEP.new(rsa_key)
                    aes_key = rsa_cipher.decrypt(cipher_aes) # Separate tuples
                    print len(aes_key)
                    new_aes_cipher = AES.new(aes_key, AES.MODE_CFB, iv) # Create new AES key
                    p = new_aes_cipher.decrypt(aesmsg)
    
                    #generate k1,k2
                    k1 = noncec+nonces+'00000000'
                    k2 = noncec+nonces+'11111111'
                    #print k1
                    #print k2
                    k1hash = keyutils.create_hmac(p,k1)
                    k2hash = keyutils.create_hmac(p,k2)
                    mc = keyutils.create_hmac(k2hash,clientinit+serverinit) # should work for both simpleauth and clientauth
                    print data[4]
                    print mc
                    if (mc != data[4]): # Check if mc calculated from server is same as client
                        print ('HMAC Verification Failed - mc, laststate %d' % laststate)
                        self.clientsocket.close()
                    else:
                        ms = keyutils.create_hmac(k2hash,clientkex)
                        smsg = 'ServerKex|b|'+ms+'|b|end'
                        mcv = 1
                    
                    laststate = 4
                
                elif (data[0]=='Request'): # Final - Handshake Completed
                    laststate = 5
                    if (init == 1 and mcv == 1) : # Checker
                        ivpayload = keyutils.generate_random(16)
                        print len(keyutils.create_hmac(payload,k2))
                        k1aes = AES.new(k1[:len(k1)/2], AES.MODE_CFB, ivpayload) # Encrypt payload with AES and part of k1 as 256 bit key.
                        
                        smsg = 'Payload|b|'+k1aes.encrypt(payload)+'|b|'+ivpayload+'|b|'+keyutils.create_hmac(payload,k2)+'|b|end'
                        print 'Sent Payload'
                        laststate = 6
                    else:
                        print ('Failed Protocol Integrity Check, laststate %d' % laststate)
                        self.clientsocket.close()
                elif (data[0] == 'end'):
                    print 'Payload Delivered'
                    self.clientsocket.close()
                    return
                  
                #print smsg
                if (len(smsg) != 0):    
                    self.clientsocket.sendall(smsg)
            except KeyboardInterrupt:
                print 'Forced Exit'
                raise
                sys.exit(0)
            except Exception as ex:
                print('Exception occured after laststate %d' % laststate)
                print ex
                sock.close()
                sys.exit(0)


sock = socket.socket()
port = int(sys.argv[1])
hostname = socket.gethostname()    
threads = [] # Thread list
try:
    sock.bind((hostname,port)) # Create first listening socket
    sock.listen(5)
except Exception as ex:
    print(ex)   
    sock.close()
    exit()

while True:
    try:
        clientsock, addr = sock.accept()
        newthread = ClientThread(hostname,sys.argv[1],clientsock) # Create new ClientThread for each sock.accept
        newthread.daemon == True
        newthread.start()
        threads.append(newthread) # Can be used to join() if needed
    except KeyboardInterrupt:
        print 'Exit'
        raise
        sys.exit(0)
    except Exception as ex:
        print('Exception:')
        print ex
        sys.exit(0)
'''        
        
#print keyutils.read_privkey_from_pem(sprk)
#print keyutils.read_subject(scert)
#print keyutils.read_subject(ca)
#sprint len(re.findall(r'/CN=minissl-SERVER/',str(keyutils.read_subject(scert)))) 
#cnpattern = re.compile('/CN[.]*/')
#print keyutils.read_issuer(scert)
#print keyutils.read_notafter(ca)
#print keyutils.read_notafter(scert)
#print datetime.strptime(keyutils.read_notafter(scert),'%Y%m%d%H%M%SZ')
#print datetime.now()
#if datetime.now() < datetime.strptime(keyutils.read_notafter(scert),'%Y%m%d%H%M%SZ'):
#    print '1'


# Identify which code line to mark for editing.
# Store information on what to edit in test case



    
# Task: generate a copy of the test code.
# Breakdown test case code. Collect important indentifiers.
    # Class name
    # Suite of points-to tests


#Gather Data
#Open test case (java)
#Read test case
    #Collect test case data
        #Line
        #Number of case data

#Create modified test case.
    #Copy Alias stubs
    #Copy import/package
    #Modify test case based on criteria
    
#Bug fixes, test case reading and interpretation. Add debug code
    
