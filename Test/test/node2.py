import itertools
import node

def dimension(n):
    total=pow(2,n)
    nodesList=[]
    for item in range(total):
        node=bin(item)
        nodeString=str(node)
        nodeList=list(nodeString)
        del nodeList[0]
        del nodeList[0]
        nodeN=[]
        for i in range(n-len(nodeList)):
            nodeN.append('0')
        for j in nodeList:
            nodeN.append(j)
        nodeDecimal="".join(nodeN)
        nodesList.append(nodeDecimal)

    # print(nodesList)
    return nodesList

def comb(nodesList,n):
    # print(list(itertools.combinations(nodesList,n)))
    return list(itertools.combinations(nodesList,n))

def output(results,minDistance):
    for result in results:
        combList=list(result)
        ################## if minDistance==node.test(combList):
        #     print(result)
        if minDistance>node.test(combList):
            print(result)


if __name__ == '__main__':
    dimen=6
    n=6
    nodesList=dimension(dimen)
    results=comb(nodesList,n)

    print("组合总个数："+str(len(results)))
    neighborsList=[]
    for result in results:
        combList=list(result)
        neighborsList.append(node.test(combList))


    minDistance=min(neighborsList)


    print(minDistance)

    ########################## output(results, minDistance)
    output(results, 24)