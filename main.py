#from asyncio.windows_events import NULL
from Node import  Node
from BreadthFirstSearch import BreadthFirstSearch
#from Jarra import Jarra
#from Puzzle import Puzzle

from PuzzleTradicional import PuzzleTradicional

def main():
    #inicial=Node((3,1,2,4))
    
    #para problema de puzzle lineal
    #inicial=Node((3,1,4,2))
    #final=Node((1,2,3,4))

    #para problema de puzzle tradiconal
    inicial=Node([[8,1,3],[2,4,5],[0,7,6]]) 
    final=Node([[1,2,3],[8,0,4],[7,6,5]])

    puzzle=PuzzleTradicional(inicial,final)
    bfs=BreadthFirstSearch(puzzle)
    solution=bfs.run()
    print(solution)
    
if __name__ == "__main__":
    main()
