def dfs(graph,current,visited):
    if(current not in visited):
        visited.append(current)
        for neighbours in graph[current]:
            dfs(graph,neighbours,visited)
    else:
        return
graph={'A':['B','S'],'B':['A'],
       'C':['D','E','F','S'],'D':['C'],
       'E':['C','H'],'F':['C','G'],
       'G':['F','H','S'],'H':['E','G'],
       'S':['A','G','C']
    }
list1=list()
start=(input("Enter start node:")).upper();
dfs(graph,start,list1)
for node in list1:
    print(node,end=" ")
