from Problem import Problem
from Node import Node

class Puzzle(Problem):
    def __init__(self, initial, goal):
      super().__init__(initial, goal)

    def expand(self, node):
        children = [] 
        
        v_izquierda = self.izquierda(node)
        if v_izquierda is not None: 
            children.append(v_izquierda)
        
        v_centro = self.centro(node)
        if v_centro is not None: 
            children.append(v_centro)

        v_derecha = self.derecha(node)
        if v_derecha is not None: 
            children.append(v_derecha)

        return children 

    def izquierda(self, node):
        state = node.state
        
        newState = (state[1],state[0],state[2],state[3])
        return Node(newState, node, 'Izquierda')

    def derecha(self, node):
        state = node.state
        
        newState = (state[0],state[1],state[3],state[2])
        return Node(newState, node, 'Derecha')

    def centro(self, node):
        state = node.state
        
        newState = (state[0],state[2],state[1],state[3])
        return Node(newState, node, 'Centro')
    