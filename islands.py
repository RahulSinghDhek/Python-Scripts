a=[[1, 1, 0, 0, 1],[0, 1, 0, 0, 1],[1, 0, 1, 1, 1],[0, 0, 0, 0, 0],[1, 0, 1, 1, 1]]

def isValid(i,j,visited):
    if i>=0 and i<5 and j>=0 and j<5 and not visited[i][j] and a[i][j]==1:
        return True
    return False

def dfs(i,j,visited):
    row=[(1,0),(-1,0),(1,1),(1,-1),(0,1),(0,-1),(-1,-1),(-1,1)]
#    if visited[i][j]:
#        return
    #print (i,j)
    visited[i][j]=True
    for el in row:
        if isValid(i+el[0],j+el[1],visited):
            dfs(i+el[0],j+el[1],visited)
            
def no_of_path(source,destination):
    count=[[0]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if i==0:
                count[i][j]=1
            elif j ==0:
                count[i][j]=1
            else:
                count[i][j]=count[i-1][j]+count[i][j-1]
    return count[-1][-1]                
            

visited=[[False]*5 for _ in range(5)]
no_of_islands=0

for i in range(5):
    for j in range(5):
        if not visited[i][j] and a[i][j]==1:
            dfs(i,j,visited)
            no_of_islands +=1
            
print (no_of_islands)
print (no_of_path((0,0),(4,4)))