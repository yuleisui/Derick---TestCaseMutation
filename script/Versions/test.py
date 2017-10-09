import sys

print('Testing Program')

filename = sys.argv[1].split('.')
inc = 0

with open(sys.argv[1], "r") as oldfile, open(filename[0]+'New.'+filename[1], "w") as newfile:
    for line in oldfile.readlines():
        #print line
        inc+=1
        newfile.write(line)
        
    print(str(inc)+' lines')
    oldfile.close()
    newfile.close()  
      
#python commenting


#Start
