def neighbors(node):
    # nodelist=['0','0','0','1','1','1']
    # nodelist=['0','0','0','0','0','0']
    # nodelist=['0','1','1','1','1','1']
    nodelist=list(node)
    string="".join(nodelist)
    changedlist=[]
    leng=len(nodelist)

    for i in range(leng-1,-1,-1):
        c=str(1-int(nodelist[i]))
        mylist=list(string)
        mylist[i]=c
        changedlist.append("".join(mylist))


    for i in range(leng-2,-1,-1):
        mylist = list(string)
        for j in range(i,leng):
            c = str(1 - int(nodelist[j]))
            # mylist = list(string)
            mylist[j] = c
        changedlist.append("".join(mylist))

    # print(changedlist)
    return changedlist

# def test():
def test(nodes):
    # nodes = ['01111', '00011']
    # nodes=['00000','01111','00011']
    # nodes = ['0000000', '0001111', '0000011','0111111']
    # nodes = ['0000', '0011', '1111', '1100']
    # nodes = ['0000000','0111111', '0001111', '0000011']
    # nodes = ['000000', '000111', '011111', '011000']#n=6,k=4
    # nodes = ['0000000', '0001111', '0111111', '0110000']
    # nodes = ['00000', '00011', '01111', '01100']#n=5,k=4
    # nodes = ['000000', '000011', '001111', '001100','111111']  #
    # nodes = ['00000', '00111', '01111', '01000']
    # nodes = ['00000', '00111', '01111', '11111']
    # nodes = ['000000', '000011','001111', '111100', '111111']#n=6,k=5,complementEdges=2
    allneighbors=[]
    for node in nodes:
        allneighbors+=[node]+neighbors(node)

    nodesNumber=len(nodes)
    neighborsNumber=len(list(set(allneighbors)))-nodesNumber

    # print(neighborsNumber)
    # print(allneighbors)
    return neighborsNumber

if __name__ == '__main__':
    nodes = ['00000', '01100']
    neighborsNum=test(nodes)
    print(neighborsNum)