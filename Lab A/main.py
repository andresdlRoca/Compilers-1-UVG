from regex2automata import reg2automata

# NFA Testing
expresion = "(b|b)*abb(a|b)*"
# expresion = '(0|1)*01(0|1)*'
# expresion = 'a(b|c)*d'

# Incorrect testing
# expresion = '((a|ba)'
# expresion = 'b*a||a'
# expresion = '|abb'
# expresion = 'abb|'

automata = reg2automata(expresion)
print(automata.get_postfix())

# automata.thompsonAFN()