test1 = "([])[]({})" #True
test2 = "((()" #False

def is_balanced(string):
    # Propositions:
    # Si len(string) = 2n + 1 faux obligé
    # Faire un compteur pour chaque type de bracket
    # Ok, en fait c'est des piles

    # Faire 1 pile des ouvrante
    # Quand fermante, pop dans lifo ouvrante et si ca match c bon si ca match c pas bon
    # Quand on pop dans la fermante ça doit matcher le dernier de l'ouvrante
    lifo = []
    open = ['(', '[', '{']
    for k in range(len(string)):
        if string[k] in open:
            lifo.append(string[k])
        else:
            if len(lifo) == 0:
                return False
            else:
                if string[k] == ')' and lifo[-1] == '(':
                    lifo.pop(-1)
                elif string[k] == '}' and lifo[-1] ==  '{':
                    lifo.pop(-1)
                elif string[k] == ']' and lifo[-1] == '[':
                    lifo.pop(-1)
                else: return False
    if len(lifo) == 0: return True
    else: return False

print(is_balanced(test1))
print(is_balanced(test2))

