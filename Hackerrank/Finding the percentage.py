if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    list=[]
    list=student_marks[query_name]
    #max=0
    #how_many=0
    #for i in range(len(list)):
    #    max+=list[i]
    #    how_many+=1
    result=round((sum(list)/len(list)),2)
    print("{:.2f}".format(result))
