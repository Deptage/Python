if __name__ == '__main__':
    list=[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        list.append([name,score]);
    list.sort(key = lambda x: x[1])
    #print(list)
    nameslist=[]
    min=list[0][0]
    min2=0
    for i in range(len(list)):
        if(list[0][1]!=list[i+1][1]):
            min2=list[i+1][1]
            break
    for i in range(len(list)):
        if(list[i][1]==min2):
            nameslist.append(list[i][0])
    nameslist.sort()
    print(*nameslist, sep = "\n")
