# Basics

> Input-Output

- In order to display the content to standard output console we use 'print' method
- In order to accept the input to standard input console we use 'input' method

    > Operations
    - len(str) - length of the input

> Variables

- It must start with character and can be followed by numbers or characters
- It can be separated with "_" underscore

> Datatypes

- We have int, float, boolean & strings

> Statements

- It is mainly used for operates on condition based situations
- if-else, if-elif-else 

> Random

- utility to generate random numbers
- it is very useful when we want to auto-generate numbers

  > Operations
  - randInt(index, lastIndex): generates random number between the given range
  - choice(): generates floating point number
  - ** random(): generates random numbers in terms of floats & it must be used for any kind of random number generation
  - shuffle(list): shuffles all the data inside the list
  

> Functions

- It is used for defining the method or function which could be repeatedly called
- It must start with 'def' followed by name & list of arguments
- It can return the value 

# Collections

- It stores collection of data or multiple data either ordered or unordered & also it can be sorted or unsorted

> List

- It is represented by []
- It can be accessed by index. index starts with zero [0]

    > Operations
    - len(list) - to find the number of records in it

> Set

- It is represented by ()
- It can be accessed by index. index starts with zero [0]

# Iterations

> for loop
- Basic way of iterating the data is using the for loops
- Upper bound is fixed and prevents infinite loop
- Useful specifically in data modification of each record

> while loop
- Basic way of iterating the data is using the while loops
- **[Dangerous]** if in case the condition is never reached [Infinite loop]
- Useful when we don't care about condition