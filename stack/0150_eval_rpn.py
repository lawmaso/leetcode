"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
"""

class Solution:
    def brute_eval_rpn(self, tokens: list[str]) -> int:
        while len(tokens) != 1:
            for i in range(len(tokens)):
                if (op := tokens[i]) in "+-*/":
                    a, b = tokens[i - 2], tokens[i - 1]
                    a, b = int(a), int(b)
                    res = int()  # result of operation

                    if op == "+": res = a + b
                    if op == "*": res = a * b
                    if op == "-": res = a - b
                    if op == "/": res = int(a / b)  # truncate towards 0

                    # rebuild list
                    tokens = tokens[:i-2] + [str(res)] + tokens[i+1:]
                    break

        return int(tokens[0])


"""
brute force: linear scan

once an operator is found, grab the two values to its left
and replace all three tokens with the single computed result

ex1:
tokens = ["2","1","+","3","*"]

+ found:
    2, 1
    2 + 1 = 3

tokens = [] + [str(3)] + ["3", "*"]

each pass consumes 3 tokens (a, b, op) and produces 1,
so the list shrinks by 2 tokens per pass

we start with n tokens and end with 1,
so total shrinkage = n - 1 ~= n
divide by 2 per pass -> ~n/2 passes

each pass also costs O(n): scanning to find the operator,
then rebuilding the list via slicing + concatenation

at end of loop, we'll be left with one token,
which is the result of the rpn

return int(tokens[0])

T: O(n^2)  [(~n/2) * n]
S: O(n)   [new list rebuilt each pass, not mutated in place]
"""

