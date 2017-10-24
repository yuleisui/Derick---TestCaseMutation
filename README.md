# Derick---TestCaseMutation

Important directories/subdirectories/files:

pta - collected and modified test suites for Druid, organised into subfolders.  pta/utils contains class objects used in testing.
script/classes - folder containing code snippets and class objects
script/mutablecases - selected Druid-compatible test cases used in testing script.
script/mutatedcases - destination folder for mutated test cases.
script/demofolder - examples of mutated test cases.

testmutation.py - test mutation script
runmutdemo - bash script to run testmutation.py on every .java file in subdirectories of current filepath, for testing purposes.
mutatorstub.py - Test functions for generic and specific mutations.


Current test.py script creates takes a .java test file that is compatible with the Druid static analyzer.

It currently has two modes,

1) A simple mutation combination method that creates unique test cases which are combinations of the various mayAlias and notAlias stubs used for alias analysis.

python testmutation.py *testfile.java*

2) a basic Regular expression tester for debugging purposes

python testmutation.py *testfile.java* [-re]

and.

3) (WIP) a basic framework for a test case synthesizer that uses the mutation combination method for possible synthesis.

python testmutation.py *testfile.java* [-syn *synthesizedtestcase.java*]


Test Gif on using script:

![alt text](https://github.com/yuleisui/Derick---TestCaseMutation/blob/master/mutation.gif)
