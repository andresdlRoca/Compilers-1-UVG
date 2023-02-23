from regex2automata import reg2automata

# NFA Testing
# input = "abbba"
expresion = "(b|b)*abb(a|b)*"
# expresion = 'ab*ab*'

# Incorrect testing
# expresion = "(|ab)"
# expresion = '((a|ba)aba'
# expresion = 'a(a|ba)a)aaa'
# expresion = 'b*a||a'
# expresion = '|abb'
# expresion = 'abb|'
# expresion = 'a||'
# expresion = '*abbbbbb'
# expresion = 'ab|e|'

automata = reg2automata(expresion)
print(automata.get_postfix())

automata.thompson_nfa_construction()