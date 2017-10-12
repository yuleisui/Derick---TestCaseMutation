
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
#ctype = type of code (with limited ability to identify syntax information)
#code = code
#line = line number of code

    def _init_(self, ctype, code, line): 
        self.ctype = cytype
        self.code = code
        self.line = line

#testcase

