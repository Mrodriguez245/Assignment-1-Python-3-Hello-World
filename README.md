# Assignment #1: Learning Python 3

This assignment will get you up to speed on some Python3 basics, which should help with learning Django later this semester that is built upon Python and will require you to write your web server backend in Python3.

We are using Python3 vs Python2 as it is where the industry is going and projects are starting to support both with the expectation that a shift to Python3 will happen soon.


#Part 1: Dictionary

This problem is inspired by: https://www.hackerrank.com/challenges/defaultdict-tutorial

Your method should take in values representing the following:

* aList = list of strings

Your method called *stringCount* should print out a sorted alphabetically list of the strings and the number of that string in the list separated by a space on each line.

For an example:

```python
alist = ["Hello", "Hello", "Bob"]
print(stringCount(alist))
```

This should print:

```
Bob 1
Hello 2
```

#Part 2: Is Float

This problem is inspired by: https://www.hackerrank.com/challenges/introduction-to-regex

Your method *isFloat* should take in a string *value* and return a boolean if the given string is a Float or not. It is recommended that you leverage the python regular expression library for this; however, it is not required.

```python
isFloat("4.0O0") #returns False
isFloat("-1.00") #returns True
isFloat("+4.54") #Returns True
```

#Part 3: Data-structures

The last part of this assignment will be building a simple linked list with two python3 classes called *LinkedList* and *Node*. We won't be directly interacting with the *Node* class so you could call that whatever you wish; however, that's what I would recommend. For reference you should look at the documentation for classes in Python3: https://docs.python.org/3/tutorial/classes.html

An example of your linked list class being used:

```python
ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.printLL()
ll.delete(2)
ll.printLL()
if ll.search(2):
	print("Value 2 found")
else:
	print("Value 2 not found")
if ll.search(1):
	print("Value 1 found")
else:
	print("Value 1 not found")
ll.insert(4)
ll.printLL()
print(str(ll.size()))
```

This simple test of your *LinkedList* should output the following:

```
2 1
1
Value 2 not found
Value 1 found
4 1
2
```

#Submitting code

You should write all of your code in the *assignment1.py* file and submit it to Tyson's Turnin System by the submission date for grading.
