while True:
    try:
        ip = input().split('.')
        number = int(input())
        binary = ""
        for item in ip:
            b = str(bin(int(item)))
            bu = b[2:]
            bb = ''
            if len(bu) < 8:
                length = 8 - len(bu)
                for i in range(length):
                    bb += '0'
            bb += bu
            binary += bb
        print(int(binary, 2))
        baString = str(bin(number))[2:]
        bString=''
        if len(baString)<32:
            length=32-len(baString)
            for item in range(length):
                bString+='0'
            bString+=baString
        i = 1
        bList = []
        bz = ''
        for item in bString:
            if i % 8 == 0:
                bz+= item
                bList.append(bz)
                bz=''
            else:
                bz += item
            i+=1
        bbList = []
        for item in bList:
            bbList.append(str(int(item, 2)))
        print(".".join(bbList))



    except:
        break