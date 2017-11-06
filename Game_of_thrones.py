def potential_groups(arr):
    rows = len(arr)
    columns = len(arr[0])
    visited = []
    for i in range(rows):
        visited.append([])
        for j in range(columns):
            visited[i].append(False)

    count = 0
    for i in range(rows):
        for j in range(columns):
            if arr[i][j] == 1 and not visited[i][j]:
                dfs(arr,i,j,visited)
                count += 1
    #print(count)
    return count


def dfs(arr,r,c,visited):
    row_num = [-1,-1,-1,0,0,1,1,1]
    col_num = [-1,0,1,-1,1,-1,0,1]
    visited[r][c] = True

    for k in range(0,8):
        if isSafe(arr,r+row_num[k],c+col_num[k],visited):
            dfs(arr,r+row_num[k],c+col_num[k],visited)


def isSafe(arr,r,c,visited):
    return (r >= 0) and (r < len(arr)) and (c >= 0) and (c < len(arr[0])) and (arr[r][c] == 1 and not visited[r][c])

#potential_groups([[0,0,0],[0,1,0],[0,0,1]])
#potential_groups([[0,0,0,0,1,0,0,0],[0,0,1,0,0,0,0,1],[0,1,1,1,0,0,0,0]])