from regex2NFA import reg2NFA

expresion = "(b|b)*abb(a|b)*"

automata = reg2NFA(expresion)
print(automata.get_regex())