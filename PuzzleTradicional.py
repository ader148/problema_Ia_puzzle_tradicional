from Problem import Problem
from Node import Node
import copy


class PuzzleTradicional(Problem):
    def __init__(self, initial, goal):
      super().__init__(initial, goal)

    #este metodo nos permite sacar los hijos del nodo
    def expand(self, node):
        children = []

        l = self.izquierda(node)
        if l is not None:
                children.append(l)

        r = self.derecha(node)
        if r is not None:
                children.append(r)

        u = self.arriba(node)
        if u is not None:
                children.append(u)

        d = self.abajo(node)
        if d is not None:
                children.append(d)

        return children


    #metodos para optener los hijos 
    def izquierda(self,node):
        state=node.state
        i,j=self.es_posible_movimiento(state)
        if(i>-1 and j>-1 and j<2):
                newstate=copy.deepcopy(state)
                valor=newstate[i][j+1]
                newstate[i][j+1]=0
                newstate[i][j]=valor
                newnode=Node(newstate,node,'left')
                return newnode
        else:
                return None

    def derecha(self,node):
        state=node.state
        i,j=self.es_posible_movimiento(state)
        if(i>-1 and j>-1 and j>0):
                newstate=copy.deepcopy(state)
                valor=newstate[i][j-1]
                newstate[i][j-1]=0
                newstate[i][j]=valor
                newnode=Node(newstate,node,'right')
                return newnode
        else:
                return None

    def arriba(self,node):
        state=node.state
        i,j=self.es_posible_movimiento(state)
        if(i>-1 and j>-1 and i<2):
                newstate=copy.deepcopy(state)
                valor=newstate[i+1][j]
                newstate[i+1][j]=0
                newstate[i][j]=valor
                newnode=Node(newstate,node,'up')
                return newnode
        else:
                return None

    def abajo(self,node):
        state=node.state
        i,j=self.es_posible_movimiento(state)
        if(i>-1 and j>-1 and i>0):
                newstate=copy.deepcopy(state)
                valor=newstate[i-1][j]
                newstate[i-1][j]=0
                newstate[i][j]=valor
                newnode=Node(newstate,node,'down')
                return newnode
        else:
                return None

    #este metodo nos permite saber si el moviento es valido
    #si no es valido nos regresa un -1,-1, si es valido nos regresa la poscicion 
    def es_posible_movimiento(self, state):
        for i, row in enumerate(state):
          for j, col in enumerate(row):
           if col==0 :
            return i, j
        return -1,-1