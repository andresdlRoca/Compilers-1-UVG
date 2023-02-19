def infix2postfix(infix_expression: str):
    postfix_exp = []
    stack = []

    for i in infix_expression:
        if i.isalnum():
            postfix_exp.append(i)
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                postfix_exp.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence(i) <= precedence(stack[-1]):
                postfix_exp.append(stack.pop())
            stack.append(i)
    
    while stack:
        postfix_exp.append(stack.pop())
    
    return ''.join(postfix_exp)

def precedence(char:str):
    if char == '*':
        return 3
    elif char == '.':
        return 2
    elif char == '|':
        return 1
    elif char == '(':
        return 0
    else:
        return 0



