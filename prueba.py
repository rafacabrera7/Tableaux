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


def inorder_to_tree(inorder):
	if len(inorder) == 1:
		return Tree(inorder[0], None, None)
	elif inorder[0] == '-':
		return Tree(inorder[0], None, inorder_to_tree(inorder[1:]))
	elif inorder[0] == "(":
		counter = 0 #Contador de parentesis
		for i in range(1, len(inorder)):
			if inorder[i] == "(":
				counter += 1
			elif inorder[i] == ")":
				counter -=1
			elif (inorder[i] in ['Y', 'O', '>', '=']) and (counter == 0):
				return Tree(inorder[i], inorder_to_tree(inorder[1:i]), inorder_to_tree(inorder[i + 1:-1]))
	else:
		return -1

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

def clasificacion(f):
	if f.label == '-':
		if f.right.label == '-':
			return '1ALFA'
		elif f.right.label == 'O':
			return '3ALFA'
		elif f.right.label == '>':
			return '4ALFA'
		elif f.right.label == 'Y':
			return '1BETA'
	elif f.label == 'Y':
		return '2ALFA'
	elif f.label == 'O':
		return '2BETA'
	elif f.label == '>':
		return '3BETA'

prueba1 = inorder_to_tree('--(-(pOq)Y-(r>s))')
prueba2 = inorder_to_tree('((-(pOq))Y(-(r>s)))')
prueba3 = inorder_to_tree('-((-(r>s))Oq)')
prueba4 = inorder_to_tree('-(r>-(pOq))')
prueba5 = inorder_to_tree('-(pY(r>s))')
prueba6 = inorder_to_tree('(-(pYq)O(r>s))')
prueba7 = inorder_to_tree('(r>(sOq))')

a = Tree('O',Tree('-',None,Tree('s',None,None)),Tree('Y',Tree('t',None,None),Tree('>',Tree('u',None,None),Tree('v',None,None))))
b = Tree('-',None,Tree('>',Tree('-',None,Tree('a',None,None)),Tree('Y',Tree('-',None,Tree('c',None,None)),Tree('b',None,None))))
c = Tree('-',None,Tree('O',Tree('>',Tree('m',None,None),Tree('n',None,None)),Tree('-',None,Tree('l',None,None))))
d = Tree('-',None,Tree('-',None,Tree('-',None,Tree('O',Tree('p',None,None),Tree('q',None,None)))))
e = Tree('Y',Tree('>',Tree('x',None,None),Tree('z',None,None)),Tree('O',Tree('-',None,Tree('w',None,None)),Tree('-',None,Tree('y',None,None))))
f = Tree('-',None,Tree('pq>',None,None))
g = Tree('-',None,Tree('Y',Tree('-',None,Tree('a',None,None)),Tree('-',None,Tree('b',None,None))))
h = Tree('>',Tree('Y',Tree('p',None,None),Tree('>',Tree('p',None,None),Tree('q',None,None))),Tree('q',None,None))




def clasifica_y_extiende(f, h):
	# Extiende listaHojas de acuerdo a la regla respectiva
	# Input: f, una fórmula como árbol
	# 		 h, una hoja (lista de fórmulas como árboles)
	# Output: no tiene output, pues modifica la variable global listaHojas

	global listaHojas

	print("Formula:", Inorder(f))
	print("Hoja:", imprime_hoja(h))

	assert(f in h), "La formula no esta en la lista!"

	clase = clasificacion(f)
	print("Clasificada como:", clase)


f = inorder_to_tree('(pYq)')

h = [f, inorder_to_tree('-q')]

listaHojas = [h]

clasifica_y_extiende(f, h)

imprime_listaHojas(listaHojas)
