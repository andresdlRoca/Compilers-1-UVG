def infix2postfix(infix_expression: str):
    check_regex(infix_expression)
    
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
    
    result = ''.join(postfix_exp)
    if len(result) < 1:
        raise Exception('Value Empty')
    else:
        return result


#Check some common regex errors
def check_regex(regex:str):
    # Check if the regex starts or ends with a quantifier or alternation symbol
    if regex.startswith("*") or regex.startswith("+") or regex.startswith("|"):
        raise Exception('Invalid start of regex')
    if regex.endswith('|'):
        raise Exception('Invalid end of regex')

    #Check for balanced parentheses
    stack = []
    for char in regex:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                raise Exception('Regex not balanced')
            stack.pop()
    
    if stack:
        raise Exception('Regex not balanced')
    
    #Check for invalid combinations
    if '**' in regex:
        raise Exception('Invalid combination of symbols')
    if '+*' in regex or '*+' in regex:
        raise Exception('Invalid combination of symbols')

    #Invalid alternations
    if '||' in regex:
        raise Exception('Invalid alternations')

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



