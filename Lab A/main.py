from regex2automata import reg2automata

expresion = "(b|b)*abb(a|b)*"

automata = reg2automata(expresion)
print(automata.get_postfix())

# automata.thompsonAFN()