def infix2postfix(infix_expression: str):
    infix_expression = format_expression(infix_expression)
    check_regex(infix_expression)
    
    postfix_exp = []
    stack = []
    symbols = ['|', '.', '*']

    for i in infix_expression:
        if i == '(':
            stack.append(i)
        elif i == ')':
            while stack[-1] != "(":
                postfix_exp.append(stack.pop())
            stack.pop()
        elif i in symbols:
            while stack and stack[-1] != '(' and precedence(i) <= precedence(stack[-1]):
                postfix_exp.append(stack.pop())
            stack.append(i)
        else:
            postfix_exp.append(i)
    
    while stack:
        postfix_exp.append(stack.pop())
    
    result = ''.join(postfix_exp)
    if len(result) < 1:
        raise Exception('Value Empty')
    else:
        return result


def format_expression(infix_expression:str):
    valid_symbols = ["|", "+", "*", "?"]
    binary_operators = ["|"]
    stack = []

    for i, char in enumerate(infix_expression):
        stack.append(char)
        if i + 1 < len(infix_expression):
            nextChar = infix_expression[i+1]
            if char != '(' and nextChar != ')' and \
                nextChar not in valid_symbols and \
                    char not in binary_operators:
                    stack.append('.')
    
    formatted_expression = ''.join(stack)
    return formatted_expression

#Check some common regex errors
def check_regex(regex:str):

    valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789().+*?|"
    index = 0
    for i in regex:
        if i not in valid_chars:
            raise Exception(f'Invalid character; {regex[0:index]}>{regex[index]}<{regex[index+1:]}')
        index += 1

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

    invalid_combinations = ['**', '+*', '*+', '(|', '|)', '||', '(.', '.)', '..', '++', '.+', '(*', '(+', '??']
    #Check for invalid combinations
    for i in invalid_combinations:
        if i in regex:
            index = regex.find(i)
            raise Exception(f'Invalid combination of symbols; {regex[0:index]}>{regex[index]}{regex[index+1]}<{regex[index+2:]}')

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



