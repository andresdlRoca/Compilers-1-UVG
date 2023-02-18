def infix2Postfix(infix_expression:str):
    stack = []
    stack.append('#')
    postfix_exp = []

    for i in infix_expression:
        # print('stack', stack)
        # print('expression', postfix_exp)
        if i.isalnum():
            postfix_exp.append(i)
        elif i == '(':
            stack.append('(')
        elif i == '^':
            stack.append('^')
        elif i == ')':
            while stack[-1] != '#' and stack[-1] != '(':
                postfix_exp.append(stack.pop())
        else:
            if precedence(i) > precedence(stack[-1]):
                stack.append(i)
            else:
                while stack[-1] != '#' and precedence(i) <= precedence(stack[-1]):
                    postfix_exp.append(stack.pop())
                stack.append(i)

    while(stack[-1] != '#'):
        postfix_exp.append(stack.pop())
    
    while '(' in postfix_exp:
        postfix_exp.remove('(')
    
    return postfix_exp
            

def precedence(char):
    if char in ['+', '-']:
        return 1
    elif char in ['*', '/']:
        return 2
    elif char in ['^']:
        return 3
    else: 
        return 0




