# Derick---TestCaseMutation

v0.6.
Current test.py script creates takes a .java test file that is compatible with the Druid points-to analyzer.

It currently has two modes, 

1) A simple mutation combination method that creates duplicate test cases which are combinations of the various mayAlias and notAlias stubs used to compare variables

python test.py *testfile.java*

2) (WIP) a basic barebones test case synthesizer that combines two types of test cases into a sythesized test case.

python test.py *testfile.java* [-syn *synthesizedtestcase.java*]

The second uses a custom class that stores information from the test case.

Test Gif:

![alt text](https://github.com/yuleisui/Derick---TestCaseMutation/blob/master/mutation.gif)
