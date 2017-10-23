

#!/usr/bin/python

def hash_mutation(curr_muta, mut_list):

    # Generate combinations of unique mutations
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
    
# Sample mutator code for flipping alias checking.
# Can be modified for other variables.
