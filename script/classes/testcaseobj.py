
class TestCaseObject:

    mutationlist = [] # list of precomputed edits  
    
    def _init_(self, testcase, mutatorid):
        self.testcase = testcase
        self.mutatorid = mutatorid
        self.synthesis = None
    
    def set_synthesis_target(syn):
        self.synthesis = syn
    
    def append_mutator(mutator_obj):
        mutationlist.append(mutator_obj)

#List of custom methods in test case.

class MutatorObject:

#list of data objects that stores relevant information
#ctype: type of code (with limited ability to identify syntax information)
#code: code
#line: line number of code

    def _init_(self, ctype, code, line): 
        self.ctype = cytype
        self.code = code
        self.line = line

#testcase

class MutatorOperatorSet:
    #mutator_operator_list: list of MutatorOperatorObjects for parsing.
    mutator_operator_list = []
    
    def _init_(self):
        self.mutator_operator_list = []
   
    def import_list(mutator_operator_list):
        self.mutator_operator_list = mutator_operator_list
        
    def append_mutator_operators(mutator_operator):
        self.mutator_operator_list.append(mutator_operator)

class MutatorOperatorObject:

    #mutator_operator: operators as string literals, '<=','<','>',>='
    #mutator_re: set of regular expressions that identify corresponding
    def_init(self, mutator_operator, mutator_re):
        self.mutator_operator = mutator_operators
        self.mutator_re = mutator_re

