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