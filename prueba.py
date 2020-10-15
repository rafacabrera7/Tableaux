#-*-coding: utf-8-*-
from random import choice
##############################################################################
# Variables globales
##############################################################################

# Crea las letras minúsculas a-z
letrasProposicionales = [chr(x) for x in range(97, 123)]
# inicializa la lista de interpretaciones
listaInterpsVerdaderas = []
# inicializa la lista de hojas
listaHojas = []

##############################################################################
# Definición de objeto tree y funciones de árboles
##############################################################################

class Tree(object):
	def __init__(self, label, left, right):
		self.left = left
		self.right = right
		self.label = label

def Inorder(f):
    # Imprime una formula como cadena dada una formula como arbol
    # Input: tree, que es una formula de logica proposicional
    # Output: string de la formula
	if f.right == None:
		return f.label
	elif f.label == '-':
		return f.label + Inorder(f.right)
	else:
		return "(" + Inorder(f.left) + f.label + Inorder(f.right) + ")"

def complemento(l):
    if l.label in letrasProposicionales:
        return Tree('-', None, l)
    else:
        return l.right

def par_complementario(l):
    complementos = []
    valor = False
    for x in l:
        complementos.append(complemento(x))

    for i in l:
        for c in complementos:
            if i.label == c.label and i.right == c.right:
                valor = True

    return valor


prueba1 = [Tree('p', None, None), Tree('q',None, None)]
prueba2 = [Tree('p', None, None), Tree('q', None, None), Tree('-', None, Tree('p',None,None))]
prueba3 = [Tree('p', None, None), Tree('q', None, None), Tree('-', None, Tree('p',None,None)), Tree('-', None, Tree('q',None, None))]

a = [Tree('b',None,None), Tree('-',None,Tree('a',None,None)), Tree('-',None,Tree('c',None,None)), Tree('a',None,None), Tree('d',None,None)]
b = [Tree('-',None,Tree('a',None,None)), Tree('b',None,None), Tree('-',None,Tree('c',None,None)), Tree('d',None,None)]
c = [Tree('a',None,None), Tree('b',None,None), Tree('-',None,Tree('c',None,None)), Tree('a',None,None)]
d = [Tree('-',None,Tree('q',None,None)), Tree('-',None,Tree('p',None,None)), Tree('q',None,None), Tree('-',None,Tree('r',None,None))]

def es_literal(f):
	# Esta función determina si el árbol f es un literal
	# Input: f, una fórmula como árbol
	# Output: True/False

	if f.label in letrasProposicionales:
		return True

	if f.label == '-' and f.right.label in letrasProposicionales:
		return True

	return False

prueba1 = Tree('a', None, None)
prueba2 = Tree('-', None, Tree('a', None, None))
prueba3 = Tree('-', None, Tree('-', None, Tree('a', None, None)))
prueba4 = Tree('-', None, Tree('Y', Tree('p',None, None), Tree('q', None, None)))

a = Tree('-',None,Tree('Y',Tree('p',None,None),Tree('q',None,None)))
b = Tree('O',Tree('k',None,None),Tree('Y',Tree('i',None,None),Tree('j',None,None)))
c = Tree('-',None,Tree('p',None,None))
d = Tree('p',None,None)

def no_literales(l):
	# Esta función determina si una lista de fórmulas contiene
	# solo literales
	# Input: l, una lista de fórmulas como árboles
	# Output: None/f, tal que f no es literal
	for x in l:
		if not es_literal(x):
			return True

	return False

prueba1 = [Tree('p',None,None), Tree('q',None,None)]
prueba2 = [Tree('-',None,Tree('p',None,None)), Tree('q',None,None)]
prueba3 = [Tree('p',None,None), Tree('-', None, Tree('-',None,Tree('q',None,None)))]
prueba4 = [Tree('-', None, Tree('-',None,Tree('p',None,None))), Tree('-', None, Tree('Y', Tree('p',None, None), Tree('q', None, None)))]

a = [Tree('-',None,Tree('p',None,None)),Tree('q',None,None),Tree('-',None,Tree('p',None,None)),Tree('r',None,None),Tree('-',None,Tree('q',None,None)),Tree('p',None,None)]
b = [Tree('q',None,None),Tree('-',None,Tree('p',None,None)),Tree('-',None,Tree('-',None,Tree('p',None,None))),Tree('-',None,Tree('q',None,None))]
c = [Tree('-',None,Tree('p',None,None)),Tree('p',None,None),Tree('-',None,Tree('q',None,None)),Tree('q',None,None)]
d = [Tree('p',None,None),Tree('q',None,None),Tree('O',Tree('p',None,None),Tree('q',None,None)),Tree('-',None,Tree('q',None,None)),Tree('-',None,Tree('p',None,None))]

print(no_literales(a))
print(no_literales(b))
print(no_literales(c))
print(no_literales(d))
