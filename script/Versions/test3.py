import sys

print('Testing Program')

file_name = sys.argv[1].split('.')
copy_num = sys.argv[2] #number of test case copies to make?
line_inc = 0 #number of lines in file

if not copy_num.isdigit():
    copy_num = 1

with open(sys.argv[1], "r") as old_file:
    curr_num = 0
    print(copy_num)
    while curr_num <= copy_num:
        if curr_num > 10:
            sys.exit()
        curr_num+=1
        new_file = open(file_name[0]+'New'+str(curr_num)+'.'+file_name[1], "w")
    
        for line in old_file.readlines():
            #print line
            line_inc+=1
            new_file.write(line)
    
    print(str(line_inc)+' lines')
     
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
    
#Setting some framework for reading test cases
    
