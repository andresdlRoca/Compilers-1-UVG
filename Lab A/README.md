# Laboratorio 1  
Este laboratorio consiste en la implementacion de un subconjunto de algoritmos basicos de automatas finitos y expresiones regulares. Se debe de desarrollar un programa que acepte como entrada una expresion regular, con la cual se debera construir un AFN (NFA).  

Para este laboratorio se siguieron los siguientes objetivos:

### Objetivos
#### Generales
- Implementacion de algoritmos basicos de automatas finitos no deterministas y expresiones regulares.
- Desarrollar una seccion para la base de la implementacion del generador de analizadores lexicos.
#### Especificos
- Conversion de una expresion regular en notacion infix a notacion postifix. (Puede ser utilizando el algoritmo Shunting Yard).
- Implementacion del algoritmo de Construccion de Thompson.
- Generacion visual de los Automatas Finitos.

### Funcionalidad
#### Entrada
- Una expresion regular.

#### Salida
- Por cada AFN (NFA) generado se de renderizara una imagen con el grafo correspondiente para el Automata Finito generado, mostrando el estado inicial, estados adicionales, estado de aceptacion y las transiciones con sus simbolos correspondientes.

## Prerequisitos
 - Python 3.10.^
 - graphviz 0.20.1 o mayor
## Ejemplo de uso
```
from regex2automata import reg2automata
# NFA Testing
expresion = "(b|b)*abb(a|b)*"

automata = reg2automata(expresion)
print(automata.get_postfix()) #Prints postfix expression

automata.thompson_nfa_construction() # Builds nfa from postfix expression and displays it as a PDF.
```
[Testing file](main.py)

## Autor  
👤 Andrés de la Roca  
- <a href = "https://www.linkedin.com/in/andr%C3%A8s-de-la-roca-pineda-10a40319b/">Linkedin</a>  
- <a href="https://github.com/andresdlRoca">Github</a>  
