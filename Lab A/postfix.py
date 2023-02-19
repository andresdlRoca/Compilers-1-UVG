def infix2Postfix(infix_expression:str):
    stack = []
    postfix_exp = []
    special_chars = ['|', '(', ')', '*', '?']

    for i in infix_expression:
        try: 
            if i in special_chars:
                stack.append(i)
                
                if i == ')':
                    a = len(stack)-2
                    while(stack[a] != "("):
                        postfix_exp.append(stack[a])
                        stack[a]=""
                        a = a-1
                    stack[a] = ""
                    stack[stack.index(")")] = ""
                    while "" in stack:
                        stack.remove("")
            
                elif i == '?':
                    if len(stack) > 1 :
                        if stack[-2] == '*':
                            postfix_exp.append(stack.pop(len(stack)-2))
                        elif stack[-2] =='?':
                            postfix_exp.append(stack.pop(len(stack)-2))
                
                elif i == '|':
                    if len(stack) > 1:
                        if stack[-2] == '*':
                            postfix_exp.append(stack.pop(len(stack)-2))
                        elif stack[-2] == '?':
                            postfix_exp.append(stack.pop(len(stack)-2))
                        elif stack[-2] == '|':
                            postfix_exp.append(stack.pop(len(stack)-2))
                
                elif i == '*':
                    if len(stack) > 1:
                        if stack[-2] == '*':
                            postfix_exp.append(stack.pop(len(stack)-2))
                    
            else:
                try:
                    if i.isalnum():
                        postfix_exp.append(i)
                except:
                    print('El caracter ingresado no es alfanumerico')
        except:
            print('El caracter especial ingresado no existe')
    
    while(len(stack) > 0):
        postfix_exp.append(stack.pop(len(stack)-1))

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




