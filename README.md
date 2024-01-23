# codewars

# Double char

Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
```python

def double_char(s):
    return "".join(i * 2 for i in s)
```
# String repeat

Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.
Examples (input -> output)
6, "I"     -> "IIIIII"
5, "Hello" -> "HelloHelloHelloHelloHello"

```python
def repeat_str(repeat, string):
    return str(string * repeat)
```

You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel is running out and the nearest pump is 50 miles away! You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.

Considering these factors, write a function that tells you if it is possible to get to the pump or not.

Function should return true if it is possible and false if not.

