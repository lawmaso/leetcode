"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int value) pushes the element value onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
"""

class MinStack:
    """
    Approach: two separate stacks

    One for global minima and the other for the actual
    stack that is ordered

    ex1:
        min  = [-2, -2, -3]
        main = [-2, 0, -3]

    .getMin() -> -3
    .pop()    -> remove -3 from main and -3 from min

        min  = [-2, -2]
        main = [-2, 0]

    .top()    -> main stack's top is 0
    .getMin() -> -1 (min stack's top)

    T: O(1) per operation [list push/pops are O(1) amortized]
    S: O(pushes - pops) ~= O(n)
    """
    min_: list[int]
    main: list[int]

    def __init__(self):
        self.min_ = []
        self.main = []        

    def push(self, value: int):
        # add to main stack (no check needed)
        self.main.append(value)

        # add to min (must check for global minima)
        self.min_.append(min(
            value,
            self.min_[-1] if self.min_ else float("inf")  # current global minimum
        ))

    def pop(self):
        # pop from both stacks
        self.main.pop()
        self.min_.pop()

    def top(self) -> int:
        # get from the main stack
        return self.main[-1]

    def getMin(self) -> int:
        return self.min_[-1]
