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


def par_complementario(l):
    def complemento(l):
        if l.label in letrasProposicionales:
            return Tree('-', None, l)
        else:
            return l.right

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
print(par_complementario(prueba3))
