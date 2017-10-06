import sys

print('Testing Program')

file_name = sys.argv[1].split('.')
copy_num = sys.argv[2]


inc = 0

with open(sys.argv[1], "r") as old_file, open(file_name[0]+'New.'+file_name[1], "w") as new_file:
    for line in old_file.readlines():
        #print line
        inc+=1
        new_file.write(line)
        
    print(str(inc)+' lines')
    old_file.close()
    new_file.close()  



#python commenting


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

#Setting some goals
