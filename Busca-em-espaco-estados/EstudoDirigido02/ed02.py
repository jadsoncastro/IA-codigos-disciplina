from pyamaze import maze, agent
from random import randint
from bfs import *

def execucaoMaze(tamanho=30, possibilidadeCaminhos=100, algoritmo="bfs"):
    
    goalX, goalY = randint(1,tamanho), 1
    
    m=maze(tamanho,tamanho)
    m.CreateMaze(goalX, goalY, loopPercent=possibilidadeCaminhos)
    
    # Inclusao do agente no ambiente
    a=agent(m,footprints=True, shape="arrow")
    b=agent(m,footprints=True, color='red', filled=True)

    #m.run()
    
    if algoritmo=="bfs":
        print("Executando a busca em largura")
        path1=bfs(m)
        path2=bfs(m)
    else:
        path = m.path
    #elif algoritmo=="dfs":
    #    path=dfs(m)
    #elif algoritmo=="aStar":
    #    path=aStar(m)
  
    m.tracePath({a:path1, b:path2})
    m.run()





if __name__=='__main__':
    execucaoMaze(tamanho=100, algoritmo="bfs")