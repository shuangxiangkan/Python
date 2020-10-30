import itertools

while True:
    try:
        s=input()
        sList=s.split()
        number1=sList[0]
        number2=int(sList[-1])
        c=sList[-2]
        words=sList[1:-1]
        cList=list(c)
        cCombinations=itertools.permutations(cList,len(cList))
        Co=[]
        for i in cCombinations:
            if ''.join(i)!=''.join(cList):
                Co.append(''.join(i))
        Co=list(set(Co))
        print(Co)

        myList=[]
        for word in words:
            if word in Co:
                myList.append(word)

        print(myList)
        print(len(myList))

        myList=sorted(myList)

        num=1
        for item in myList:
            if number2==num:
                #string+=' '+item
                print(item)
                break
            else:
                num+=1
    except:
        break