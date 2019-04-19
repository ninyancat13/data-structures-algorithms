#EquationSolver
#Infix to Postfix Conversion

from stacks_queues import *


def precedenceOf(term):
    #return precedence of the operator
    if term == '*' or term == '/':
        return int(2)
    if term == '+' or term == '-':
        return int(1)

def infixToPostfix(equation):
    postfix = DSAQueue(20)
    opStack = DSAStack(20)
    #n = 0

    infix = equation.split(' ') 
           #for i in range(len(infix)):
               #term = infix[i]
    print(infix)    
    for term in infix:
        try:
            #term = infix[n]
            #n += 1

            if term == '(':
                opStack.push(term)
    
            elif term == ')':
                while opStack.top() != '(':
                    postfix.enqueue(opStack.pop())
                opStack.pop()
    
            elif term == '+' or term == '-' or term == '*' or term == '/':
                while (opStack.isEmpty() == False and opStack.top() != '(' and precedenceOf(opStack.top()) >= precedenceOf(term)):
                    postfix.enqueue(opStack.pop())
                opStack.push(term)
            else:
                postfix.enqueue(term)
                #postfix = postfix + term

            postfix.display()
            opStack.display()
            print()
        except ValueError as error:
            return print(error)

    while not (opStack.isEmpty()):
        postfix.enqueue(opStack.pop())
        #postfix = postfix + opStack.pop

    postfix.display()
    opStack.display()
    return postfix

def evaluatePostfix(postfix):
    #Use instanceof to determine if its an operator or operand
    print("created oprStack")
    oprStack = DSAStack(20)
    print("This is what DSAStack(20) will give...", DSAStack(20))
    while postfix.isEmpty() == False:
        firstVal = postfix.peek()
        if firstVal.isdigit():   #if first in queue is a digit
            oprStack.push(postfix.dequeue())
        else:
            opr2 = oprStack.pop()
            opr1 = oprStack.pop()
            op = postfix.dequeue()
            calculated = executeOperation(op, opr1, opr2)
            oprStack.push(calculated)
        oprStack.display()
        postfix.display()
    return oprStack.top()

def executeOperation(op, opr1, opr2):
    #helper function for evaluatePostfix
    #executes the binary operation implied by the content of ()
    #returns the result
    print("op", op, "opr1", opr1, "opr2", opr2)
    if op=='+':
        return float(opr1) + float(opr2)
    if op=='-':
        return float(opr1) - float(opr2)
    if op=='*':
        return float(opr1) * float(opr2)
    if op=='/':
        return float(opr1) / float(opr2)

def solve(equation):
    #Need to call infixToPostfix() then call evaluatePostfix()
    postfix = infixToPostfix(equation)
    print(postfix)
    result = evaluatePostfix(postfix)
    return result
