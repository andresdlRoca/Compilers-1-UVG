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
        raise Exception(f'{regex[0]} is an invalid start of regex on the first position of >{regex[0]}<{regex[1:]}')
    if regex.endswith('|'):
        raise Exception(f'{regex[-1]} is an invalid ending of regex on the last position of {regex[:-1]}>{regex[-1]}<')

    #Check for balanced parentheses
    stack = []
    index = 0
    for char in regex:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                raise Exception(f'Regex not balanced; {regex[0:index]}>{regex[index]}<{regex[index+1:]}')
            stack.pop()
        index += 1
    
    index = 0
    if stack:
        for char in regex:
            if char in stack:
                raise Exception(f'Regex not balanced; {regex[0:index]}>{regex[index]}<{regex[index+1:]}')
        index += 1
    #Check for invalid combinations
    if '**' in regex:
        index = regex.find('**')
        raise Exception(f'Invalid combination of symbols; {regex[0:index]}>{regex[index]}{regex[index+1]}<{regex[index+2:]}')
    if '+*' in regex:
        index = regex.find('+*')
        raise Exception(f'Invalid combination of symbols; {regex[0:index]}>{regex[index]}{regex[index+1]}<{regex[index+2:]}')
    elif '*+' in regex:
        index = regex.find('*+')
        raise Exception(f'Invalid combination of symbols; {regex[0:index]}>{regex[index]}{regex[index+1]}<{regex[index+2:]}')

    #Invalid alternations
    if '||' in regex:
        index = regex.find('||')
        raise Exception(f'Invalid combination of alternations; {regex[0:index]}>{regex[index]}{regex[index+1]}<{regex[index+2:]}')

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



