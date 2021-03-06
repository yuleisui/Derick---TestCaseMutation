#!/usr/bin/python

from classes import testcaseobj
import sys
import re
import itertools
import copy
import os.path

print('testmutation.py mutation script \n#python test.py "test_case_filepath" [-re]')
if len(sys.argv) <2:
    sys.exit()
elif not os.path.isfile(sys.argv[1]):
    print ('invalid file path/file: ' + sys.argv[1])
    sys.exit()

subdirectory = sys.path[0]+"/mutatedcases"
test_case_path = sys.argv[1].split('/') 
class_name = (test_case_path[len(test_case_path)-1]).split('.')[0]

syn_flag = False
testre_flag = False

print len(sys.argv)
if len(sys.argv) >= 3:
    if sys.argv[2] == "-syn":
        syn_flag = True #synthesis flag
    elif sys.argv[2] == "-re": #testing RE code
        testre_flag = True
        syn_flag = False
    else:
        syn_flag = False
        testre_flag = False
        
    if syn_flag is True:    
        syn_test_case_name = sys.argv[3] #synthesiser test_case
        copy_num = sys.argv[4] #number of test case copies to make? (optional)
else:
    copy_num = 0

line_inc = 0 #number of lines in original test_case

    
new_file_list = []  #stores synthesis/mutation test_case information.
instant_list = [] #stores class instantiation code from test case
mutation_list = []  #stores only mayAlias/notAlias checks
# mutation_list,instant_list stores custom class objects consisting of [line_number, code]


argvlist = sys.argv
def check_flag(argvlist): #check for input correctness (to be added later)
    print(argvlist)

def analyse_code(code,class_name): #grab test_case information for later use
    line_count = 1
    mayAlias_count = 0
    notAlias_count = 0
    print('\ntest_case filename: '+ str(sys.argv[1]))
    print(str(len(code)+1)+' lines')
    new_file_list.append(['', 'mut_code'])
    
    
    for line in code:
        if line.strip(): # Ignore empty lines
            match_class = re.search("(\w+\s)*class (\w+)", line)  # Find class name (Doesn't handle extends)
            match_instant = re.search("^\s*"+class_name[0]+" (\w+) =", line)
            match_mayAlias = re.search("^\s*mayAlias\(\s*\w+\s*,\w+\s*\)",line) # Regex for mayAlias/postive check.
            match_notAlias = re.search("^\s*notAlias\(\s*\w+\s*,\s*\w+\s*\)",line) # Regex for notAlias/negative check.
                   
            if match_class: # get class_name
                class_name = match_class.group(2)
                new_file_list.append([line_count, line])
                print match_class.group()
                print ('classname:'+class_name)
            elif match_instant:
                instant_list.append([line_count, line])
            elif match_mayAlias:
                mayAlias_count += 1
                new_file_list[0][0] += '1'
                mutation_list.append([line_count,line])
            elif match_notAlias:
                notAlias_count += 1
                new_file_list[0][0] += '0'
                mutation_list.append([line_count,line])
            
        line_count +=1 # Increment
    
    print ('mayAlias:'+str(mayAlias_count))
    print ('notAlias:'+str(notAlias_count))
    print new_file_list
    return hash_mutation(mutation_list,new_file_list[0][0])

# Use dictionary hashtable for mutation
# Alternate method of applying combinations to mutations in python
def hash_mutation(curr_muta, mut_list):
    combination_hash = {}
    combination_list = ["".join(seq) for seq in itertools.product("01", repeat=len(mut_list))] 
    # get all combinations of binary string literal via cartesian product function
    
    for binary in combination_list:
        if not binary == mut_list:
            # for every char (1,1 in 11)
            new_curr_muta = curr_muta #Clone list   
            inner_mut_element = 0
            for char in list(binary):
                if char == '1':
                    new_curr_muta[inner_mut_element][1] = re.sub('notAlias','mayAlias',new_curr_muta[inner_mut_element][1])
                elif char == '0':
                    new_curr_muta[inner_mut_element][1] = re.sub('mayAlias','notAlias',new_curr_muta[inner_mut_element][1])
                inner_mut_element+=1
            combination_hash[binary] = copy.deepcopy(new_curr_muta)
            
    #print ("combination_hash:", combination_hash)
    return combination_hash    

def name_replace(newclassname, line):
    return re.sub(class_name,newclassname,line)


if testre_flag is True: #RE debugger
    test_re = re.search("^\s*notAlias",'notAlias(c,b);')
    #test_re = re.search("^\s* notAlias\(\w+,\w+\)",'notAlias(c,b);')

    print test_re

else:
    with open(sys.argv[1], "r") as old_file: #Code opens test case

        code = old_file.readlines()
        
        mutation_dict = analyse_code(code,class_name)
        
        print (str(len(mutation_dict))+' unique combinations created')
        #print new_file_list
        #print('currnum:'+str(curr_num)+', copy_num:'+str(copy_num))
        #iterate through combinations, create new file for each combination
        for mut_combination in mutation_dict:
            class_flag = 0
            #print mut_combination
            #print mutation_dict.get(mut_combination)
            
            new_filename = class_name+'-Mut'+str(mut_combination)+'.java'
            new_file = open(os.path.join(subdirectory,new_filename), "w")
            with new_file:
                line_inc = 1
                #print mut_combination
                for line in code:
                    mut_flag = 0
                    inst_flag = 0     
                    if line_inc == new_file_list[1][0]:
                        new_file.write(name_replace(new_filename.split('.')[0],new_file_list[1][1]))
                        line_inc+=1
                        mut_flag = 2
                        continue
                        
                    else: # code can be simplified in definition (todo)
                        for inst_line in instant_list:
                            if line_inc == inst_line[0]:
                                new_file.write(name_replace(new_filename.split('.')[0],inst_line[1]))
                                #print(line_inc,'inst')
                                inst_flag = 1
                                break
                        for mut_line in mutation_dict.get(mut_combination):
                            #for each value in mutation_dict
                            if line_inc == mut_line[0]:
                                new_file.write(mut_line[1])
                                #print(line_inc,'mut')
                                mut_flag = 1
                                break
                    #print(mut_flag,inst_flag)            
                    if mut_flag == 0 and inst_flag == 0:
                        new_file.write(line)
                        #print(line_inc,'norm')
                    #print mut_combination
                    line_inc+=1         
            
            #print mutation_dict[mut_combination]            

