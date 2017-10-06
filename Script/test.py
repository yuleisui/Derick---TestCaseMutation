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
    
