tabledata=[['apples','oranges','cherries','banana'],
           ['alice','bob','carol','david'],
           ['dogs','cats','moose','goose']]
#print(tabledata)
def printtable(a):
    colwidths=[0]*len(a)
    for y in range(len(a)):
        for x in a[y]:
            if colwidths[y]<len(x):
                colwidths[y]=len(x)
    for x in range(len(a[0])):
        for y in range(len(a)):
            print(a[y][x].rjust(colwidths[y]),end=' ')
        print()
   # print(colwidths)
printtable(tabledata)
