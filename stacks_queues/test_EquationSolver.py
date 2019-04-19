from EquationSolver import *
from stacks_queues import *
import numpy as np

infix="9 * 2 - ( 1 + 3 )"
print("\nThis is the equation: ", infix)
postfix_value = infixToPostfix(infix)
print("\n\nThis is the postfix value: ", postfix_value)
answer = evaluatePostfix(postfix_value)
print("\n\nThis is the answer to the equation:", answer)


infix="5 - 3"
print("\nThis is the equation: ", infix)
postfix_value = infixToPostfix(infix)
print("\n\nThis is the postfix value: ", postfix_value)
answer = evaluatePostfix(postfix_value)
print("\n\nThis is the answer to the equation:", answer)


infix="9 * 2"
print("\nThis is the equation: ", infix)
postfix_value = infixToPostfix(infix)
print("\n\nThis is the postfix value: ", postfix_value)
answer = evaluatePostfix(postfix_value)
print("\n\nThis is the answer to the equation:", answer)


infix="1 + 3"
print("\nThis is the equation: ", infix)
postfix_value = infixToPostfix(infix)
print("\n\nThis is the postfix value: ", postfix_value)
answer = evaluatePostfix(postfix_value)
print("\n\nThis is the answer to the equation:", answer)


infix="9 / 3"
print("\nThis is the equation: ", infix)
postfix_value = infixToPostfix(infix)
print("\n\nThis is the postfix value: ", postfix_value)
answer = evaluatePostfix(postfix_value)
print("\n\nThis is the answer to the equation:", answer)
