# Explain usage of try-except and assert keywords.

"""
try() is used in Error and Exception Handling
There are two kinds of errors:
  - Syntax Error: Also known as Parsing Errors, most basic.
                  Arise when the Python parser is unable to understand a line of code.
  - Exception:    Errors which are detected during execution. eg - ZeroDivisonError.

List of Exception Errors:
  - IOError:           if file can't be opened.
  - KeyboardInterrupt: when an unrequired key is pressed by the user.
  - ValueError:        when built-in function receives a wrong argument.
  - EOFError:          if End-Of-File is hit without reading any data.
  - ImportError:       if it is unable to find the module.

Now, here comes the task to handle these errors within our code in Python. 
So here we need try-except statements:
Basic Syntax:
  try:
    // Code
  except:
    // Code

How try() works?
- First try clause is executed i.e. the code between try and except clause.
- If there is no exception, then only try clause run, except clause is finished.
- If any exception occured, try clause will be skipped and except clause will run.
- If any exception occurs, but the except clause within the code doesn't handle it, it is passed on to the outer try statements. 
- If the exception left unhandled, then the execution stops.
- A try statement can have more than one except clause.
"""


########## Case 1: No exception, so try clause will run. ##########
# Python code to illustrate working of try block.
def divide_case1(x, y):
    try:
        # Floor Division: Gives only Fractional Part as Answer
        result = x // y
        print(f"Yeah ! Your answer is : {result}")
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")


# Look at parameters and note the working of Program
print("Case: 1 Try Block")
divide_case1(3, 2)


########## Case 2: There is an exception so only except clause will run. ##########
# Python code to illustrate working of except block.
def divide_case2(x, y):
    try:
        # Floor Division: Gives only Fractional Part as Answer
        result = x // y
        print(f"Yeah ! Your answer is : {result}")
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")


# Look at parameters and note the working of Program
print("Case: 2 Except Block")
divide_case2(3, 0)


"""
# Python Assert Keyword
Python assert keyword is defined as a debugging tool that tests a condition. The assertions are mainly the assumption that asserts or state a fact confidently in the program.
For example, while writing a division function, the divisor should not be zero, and you assert that divisor is not equal to zero.

It is simply a boolean expression that has a condition or expression checks if the conditon returns true or false. 
If it is true, the program does not do anything, and it moves to the next line of code. 
But if it is false, it raises an AssertionError exception with an optional error message.

The main task of assertions is to inform the developers about unrecoverable errors in the program like "file not found", 
and it is right to say that assertions are internal self-checks for the program.
They work by declaring some conditions as impossible in your code. If one of the condition does not hold, that means that is a bug in the program.

# Why Assertion is used
It is a debugging tool, and its primary task is to check the condition. 
If it finds that condition is true, it moves to the next line of code, and If not then stops all its operaions and throws an error. 
It points out the error in the code.

# Where Assertion in Python used
- Checking the outputs of the functions.
- Used for testing the code.
- In checking the values of arguments.
- Checking the valid input.

# Syntax
assert condition, error_message(optional)
"""


########## Case 3: This example shows the working of assert with the error message. ##########
def avg(scores):
    assert len(scores) != 0, "The List is empty."
    return sum(scores)/len(scores)


scores2 = [67, 59, 86, 75, 92]
print(f"The Average of scores2: {avg(scores2)}")

scores1 = []
print(f"The Average of scores1: {avg(scores1)}")

"""
Explanation: In Case 3, we have passed a non-empty list scores2 and an empty list scores1 to the avg() function. 
We received an output for scores2 list successfully, but after that, we got an error AssertionError: List is empty.
The assert condition is satisfied by the scores2 list and lets the program to continue to run. 
However, scores1 doesn't satisfy the condition and gives an AssertionError.
"""
