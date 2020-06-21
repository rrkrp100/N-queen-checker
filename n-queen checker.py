#!Python3
is_test = int(input("Enter 0 to run sample test, Anything else to input ur own data:  ") )
queens = list()
row = list()
col = list()

if is_test==0:
    n=6
    queens = [ [0,1],[1,3],[2,0],[3,5],[4,2],[5,4] ]
    row = [-1,-1,-1,-1,-1,-1]
    col = [-1,-1,-1,-1,-1,-1]

else:
    n = int(input("Enter the number of queens for NxN board:  "))
    for i in range(n):
        queens.append(input("Enter Coordinates of queen: ").split())
        row.append(-1)
        col.append(-1)

## Lets check row and col safety
for queen in queens:
    if(row[queen[0]]!=-1 or col[queen[1]]!=-1):
        print("Unsafe..!")
        exit()
    else:
        row[queen[0]]=1 
        col[queen[1]]=1

##Lets check diagonal safety
TopDwn_diagonal = [[-1] for i in range(2*n)]  #list of lists
BtmUp_diagonal = [-1 for i in range(2*n)]   #list of int

for i,queen in enumerate(queens):
    sum = queen[0] + queen[1]
    diff = abs(queen[0] - queen[1])
    if TopDwn_diagonal[diff][0]==-1:
        TopDwn_diagonal[diff][0] = i

    elif TopDwn_diagonal[diff][0] != -1:
        for q in TopDwn_diagonal[diff]:                                 #this may seem like another loop, but it cannot have have more than 2 elements, so its 2N not n^2
            if queens[q][0]-queen[0] == queens[q][1]-queen[1] :
                print("Unsafe")
                exit()
    
    if BtmUp_diagonal[sum]==-1:
        BtmUp_diagonal[sum]=i
    else:
        print("Unsafe")
        exit()