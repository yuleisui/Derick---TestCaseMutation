#!/usr/bin/python

# Sample mutator code for flipping alias checking.
# Can be modified for other variables and further improved.
def hash_mutation(curr_muta, mut_list):

    # Generate combinations of unique mutations
    combination_hash = {}
    combination_list = ["".join(seq) for seq in itertools.product("01", repeat=len(mut_list))] 
    for binary in combination_list:
        if not binary == mut_list:
            new_curr_muta = curr_muta #Clone list   
            inner_mut_element = 0
            for char in list(binary):
                if char == '1':
                    new_curr_muta[inner_mut_element] = re.sub(notAlias_var,mayAlias_var,new_curr_muta[inner_mut_element])
                elif char == '0':
                    new_curr_muta[inner_mut_element] = re.sub(mayAlias_var,notAlias_var,new_curr_muta[inner_mut_element])
                inner_mut_element+=1
            # Generate Hashtable entries for unique string mutators in test cases
            combination_hash[binary] = copy.deepcopy(new_curr_muta) 
            
return combination_hash    

# generic binary mutator for single class of mutation operator
# Preprocessing data representing what to modify in the test suite.

def generic_binary_mutation(current_mutation, mutation_test_case_list, notAlias_var, mayAlias_var):

# current_mutation: list of mutated code lines in test suite code for specific operator.
# mutation_test_case_list: binary string representation of mutators in current test suite
# combination: binary string representation of a combination in combination_list
# combination_list: set of all possible combinations available for mutator generated using cartesian production function
# may_var: String constant representing first of 2 binary mutators.
# not_var: String constant representing second of 2 binary mutators.
# combination_binary: hashtable object to store modified mutation_list for later modification.

    # Generate combinations of unique mutations via cartesian product function
    combination_binary = {}
    combination_list = ["".join(seq) for seq in itertools.product([0,1], repeat=len(mutation_test_case_list))] 
    for combination in combination_list:
        if not combination == mutation_test_case_list:
            new_current_mutation = current_mutation #Clone list   
            inner_mut_element = 0
            for integer in list(binary):
                if integer == 1:
                    new_current_mutation[inner_mut_element] = re.sub(not_var,may_var,new_current_mutation[inner_mut_element])
                elif integer == 0:
                    new_current_mutation[inner_mut_element] = re.sub(may_var,not_var,new_current_mutation[inner_mut_element])
                inner_mut_element+=1
            # Generate Hashtable entries for unique string mutators in test cases
            combination_binary[binary] = copy.deepcopy(new_current_mutation) 
            
return combination_binary

# function to replace all possible variations of mutator operators to a single operator. (e.g, setting <=,=,> to >=)
def generic_re(old_line, base, *mutator_list):
    mutated_line = old_line
    for x in range(0, len(mutator_list)):
        mutated_line = re.sub(mutator_list[i-1], mutator_list[base], old_line)
return mutated_line



def generic_trinary_mutation(current_mutation, mutation_test_case_list, *mutator_list):
#mutator_list: list of mutator operators in class e.g ['<=','<','>','>=','==']

    # Generate combinations of unique mutations via cartesian product function
    combination_hash = {}
    combination_list = ["".join(seq) for seq in itertools.product([0,1,2], repeat=len(mutation_test_case_list))] 
    for generic_binary in combination_list:
        if not generic_binary == mutation_test_case_list:
            new_current_mutation = current_mutation #Clone list   
            inner_mut_element = 0
            for integer in list(new_current_mutation):
                if integer == 0:
                    new_current_mutation[inner_mut_element] = generic_re(new_current_mutation[inner_mut_element], 0, mutator_list)
                elif integer == 1:
                    new_current_mutation[inner_mut_element] = generic_re(new_current_mutation[inner_mut_element], 1, mutator_list)
                elif integer == 2:
                    new_current_mutation[inner_mut_element] = generic_re(new_current_mutation[inner_mut_element], 2, mutator_list)
                
                inner_mut_element+=1
            # Generate Hashtable entries for unique string mutators in test cases
            combination_binary[binary] = copy.deepcopy(new_current_mutation)
           
return combination_binary   

#hypothetical code to simulate mutations of any type for a single operator.
def generic_mutation(current_mutation, mutation_test_case_list, *mutator_list):
#mutator_list: list of mutator operators in class e.g ['<=','<','>','>=','==']

    # Generate combinations of unique mutations via cartesian product function
    combination_hash = {}
    combination_list = ["".join(seq) for seq in itertools.product(range(len(mutator_list)), repeat=len(mutation_test_case_list))] 
    for generic_binary in combination_list:
        if not generic_base == mutation_list:
            new_current_mutation = current_mutation #Clone list   
            inner_mut_element = 0
            for integer in list(generic_base):
                generic_mutation_switch_re(new_current_mutation,inner_mut_element, integer, mutator_list)
                
                if integer == 0:
                    new_current_mutation[inner_mut_element] = generic_re(new_current_mutation[inner_mut_element], 0, mutator_list)
                elif integer == 1:
                    new_current_mutation[inner_mut_element] = generic_re(new_current_mutation[inner_mut_element], 1, mutator_list)
                elif integer == 2:
                    new_current_mutation[inner_mut_element] = generic_re(new_current_mutation[inner_mut_element], 2, mutator_list)
                
                inner_mut_element+=1
            # Generate Hashtable entries for unique string mutators in test cases
            combination_binary[binary] = copy.deepcopy(new_current_mutation)
           
return combination_binary 

#function to simulate dynamically sized if statement block for mutation flipping
def generic_mutation_switch_re(new_current_mutation, inner_mut_element, flag, *mutator_list):
    for i in range(len(mutator_list)): # (iterates an ascending array of [0, 1, 2, 3...] depending on how many mutator operators
        if integer == i:
            new_current_mutation[inner_mut_element] = generic_re(new_current_mutation[inner_mut_element], i, mutator_list)
            break



