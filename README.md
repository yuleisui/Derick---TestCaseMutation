# Derick---TestCaseMutation

Important directories/subdirectories/files:

pta - collected and modified test suites for Druid, organised into subfolders.  pta/utils contains class objects used in testing.
script/classes - folder containing code snippets and class objects imported into
script/mutablecases - selected Druid-compatible test cases used in testing script.
script/mutatedcases - destination folder for mutated test cases.
script/demofolder - examples of mutated test cases.

test.py - test mutation script
runmutdemo - bash script to run test.py on every .java file in location and first level of subdirectories.





v0.6.
Current test.py script creates takes a .java test file that is compatible with the Druid points-to analyzer.

It currently has two modes,

1) A simple mutation combination method that creates unique test cases which are combinations of the various mayAlias and notAlias stubs used to compare variables.

python test.py *testfile.java*

2) a basic Regular expression tester for debugging purposes

python test.py *testfile.java* [-re]

3) (WIP) a basic framework for a test case synthesizer that uses the mutation combination method for possible synthesis.

python test.py *testfile.java* [-syn *synthesizedtestcase.java*]


Test Gif:

![alt text](https://github.com/yuleisui/Derick---TestCaseMutation/blob/master/mutation.gif)
