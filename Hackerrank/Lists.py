if __name__ == '__main__':
    N = int(input())
    list=[]
    for i in range(N):
        s = input().split()
        command = s[0]
        arguments = s[1:]
        for i in range(len(arguments)):
            arguments[i]=int(arguments[i])
        #print(command)
        #print(arguments)
        if command=='insert':
            list.insert(arguments[0],arguments[1])
        elif command=='print':
            print(list)
        elif command=='remove':
            list.remove(arguments[0])
        elif command=='append':
            list.append(arguments[0])
        elif command=='sort':
            list.sort()
        elif command=='pop':
            list.pop()
        else:
            list.reverse()
        #print(list)
