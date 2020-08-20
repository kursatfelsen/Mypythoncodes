def initialize_sudoku():
    sudoku=[[],[],[],[],[],[],[],[],[]]
    for i in range(0,9):
        for j in range(0,9):
            sudoku[i].append(int(input()))
    return sudoku

def print_sudoku(sudoku):
    for i in range(0,9):
        for j in range(0,9):
            print(str(sudoku[i][j])+" ",end=(" "))
        print("\n")

def whichvaluescannot(sudoku,i,j):
    list1=set(innervalues(sudoku,i,j))
    list2=set(sameline_values(sudoku,i,j))
    list3=set(samecolumn_values(sudoku,i,j))
    return list1.union(list2,list3)

def whichvaluescan(sudoku,i,j):
    set1=whichvaluescannot(sudoku,i,j)
    thisset={1,2,3,4,5,6,7,8,9}
    result=list(thisset.difference(set1))
    result.sort()
    return result
def innervalues_help(sudoku,i,j):
    innerlist=[]
    k=-1
    l=-1
    while(k<2):
        while(l<2):
            if(sudoku[i+k][j+l]!=0):
                #BURADAN 0 LARIN SAYISINI ÇIKARABİLİRSİN BU DA İŞİNE YARAYABİLİR
                innerlist.append(sudoku[i+k][j+l])
            l+=1
        k+=1
        l=-1
    if len(innerlist)!=0:
        innerlist = list(set(innerlist))
    return innerlist

def innervalues(sudoku,i,j):
    innerlist=[]
    if(i<=2):
        if(j<=2):
            return innervalues_help(sudoku,1,1)
        elif(j>=6):
            return innervalues_help(sudoku,1,7)
        else:
            return innervalues_help(sudoku,1,4)
    elif(i>=6):
        if(j<=2):
            return innervalues_help(sudoku,7,1)
        elif(j>=6):
            return innervalues_help(sudoku,7,7)
        else:
            return innervalues_help(sudoku,7,4)
    else:
        if(j<=2):
            return innervalues_help(sudoku,4,1)
        elif(j>=6):
            return innervalues_help(sudoku,4,7)
        else:
            return innervalues_help(sudoku,4,4)

def samesqrsameline(sudoku,i,j,value):
    list1={value}
    if(j%3==0):
        if look_for_otherlines(sudoku,i,j,value) and look_for_samelineandsamecolumn(sudoku,i,j,value) and look_for_inner(sudoku,i,j,value):
            if (sudoku[i][j+1]!=0 and sudoku[i][j+2]!=0):
                return True
            elif(sudoku[i][j+1]!=0):
                if len(list(list1.intersection(whichvaluescannot(sudoku,i,j+2))))==1:
                    return True
                return False
            elif(sudoku[i][j+2]!=0):
                if len(list(list1.intersection(whichvaluescannot(sudoku, i, j + 1)))) == 1:
                    return True
                return False
            else:
                if(len(list(list1.intersection(whichvaluescannot(sudoku,i,j+2))))==1) and len(list(list1.intersection(whichvaluescannot(sudoku, i, j + 1)))) == 1:
                    return True
                return False
    elif(j%3==1):
        if look_for_otherlines(sudoku, i, j, value) and look_for_samelineandsamecolumn(sudoku,i,j,value) and look_for_inner(sudoku,i,j,value):
            if (sudoku[i][j-1]!=0 and sudoku[i][j+1]!=0):
                return True
            elif(sudoku[i][j-1]!=0):
                if len(list(list1.intersection(whichvaluescannot(sudoku, i, j+1)))) == 1:
                    return True
                return False
            elif(sudoku[i][j+1]!=0):
                if len(list(list1.intersection(whichvaluescannot(sudoku, i, j - 1)))) == 1:
                    return True
                return False
            else:
                if (len(list(list1.intersection(whichvaluescannot(sudoku, i, j + 1)))) == 1) and len(list(list1.intersection(whichvaluescannot(sudoku, i, j - 1)))) == 1:
                    return True
                return False
    else:
        if look_for_otherlines(sudoku, i, j, value) and look_for_samelineandsamecolumn(sudoku,i,j,value) and look_for_inner(sudoku,i,j,value):
            if (sudoku[i][j-1]!=0 and sudoku[i][j-2]!=0):
                return True
            elif(sudoku[i][j-1]!=0):
                if len(list(list1.intersection(whichvaluescannot(sudoku, i, j - 2)))) == 1:
                    return True
                return False
            elif(sudoku[i][j-2]!=0):
                if len(list(list1.intersection(whichvaluescannot(sudoku, i, j -1)))) == 1:
                    return True
                return False
            else:
                if (len(list(list1.intersection(whichvaluescannot(sudoku, i, j -1)))) == 1) and len(list(list1.intersection(whichvaluescannot(sudoku, i, j - 2)))) == 1:
                    return True
                return False

def samesqrsamecol(sudoku,i,j,value):
    list1 = {value}
    if(i%3==0):
        if look_for_othercolumns(sudoku,i,j,value) and look_for_samelineandsamecolumn(sudoku,i,j,value) and look_for_inner(sudoku,i,j,value):
            if (sudoku[i+1][j]!=0 and sudoku[i+2][j]!=0):
                return True
            elif(sudoku[i+1][j]!=0):
                if len(list(list1.intersection(whichvaluescannot(sudoku, i+2, j)))) == 1:
                    return True
                return False
            elif(sudoku[i+2][j]!=0):
                if len(list(list1.intersection(whichvaluescannot(sudoku, i + 1, j)))) == 1:
                    return True
                return False
            else:
                if (len(list(list1.intersection(whichvaluescannot(sudoku, i+1, j)))) == 1) and len(list(list1.intersection(whichvaluescannot(sudoku, i+2, j)))) == 1:
                    return True
                return False
    elif(i%3==1):
        if look_for_othercolumns(sudoku, i, j, value) and look_for_samelineandsamecolumn(sudoku,i,j,value) and look_for_inner(sudoku,i,j,value):
            if (sudoku[i-1][j]!=0 and sudoku[i+1][j]!=0):
                return True
            elif(sudoku[i-1][j]!=0):
                if len(list(list1.intersection(whichvaluescannot(sudoku, i + 1, j)))) == 1:
                    return True
                return False
            elif(sudoku[i+1][j]!=0) and (not mainfunc(sudoku,i-1,j,value)):
                if len(list(list1.intersection(whichvaluescannot(sudoku, i -1, j)))) == 1:
                    return True
                return False
            else:
                if (len(list(list1.intersection(whichvaluescannot(sudoku, i + 1, j)))) == 1) and len(list(list1.intersection(whichvaluescannot(sudoku, i -1, j)))) == 1:
                    return True
                return False
    else:
        if look_for_othercolumns(sudoku, i, j, value) and look_for_samelineandsamecolumn(sudoku,i,j,value) and look_for_inner(sudoku,i,j,value):
            if (sudoku[i-1][j]!=0 and sudoku[i-2][j]!=0):
                return True
            elif(sudoku[i-1][j]!=0):
                if len(list(list1.intersection(whichvaluescannot(sudoku, i -2, j)))) == 1:
                    return True
                return False
            elif(sudoku[i-2][j]!=0):
                if len(list(list1.intersection(whichvaluescannot(sudoku, i -1, j)))) == 1:
                    return True
                return False
            else:
                if (len(list(list1.intersection(whichvaluescannot(sudoku, i -1, j)))) == 1) and len(list(list1.intersection(whichvaluescannot(sudoku, i - 2, j)))) == 1:
                    return True
                return False

def look_for_inner_helpx(sudoku,i,j,value,x,y):
    k=-1
    l=-1
    list1=[]
    set2={value}
    while(k<2):
        while(l<2):
            if (i!=x and j!=y):
                if k==-1 and l==-1:
                    list1=list1+list(whichvaluescannot(sudoku,i+k,j+l))
                    list1=set(list1)
                else:
                    list1=list1.intersection(whichvaluescannot(sudoku,i+k,j+l))
            l+=1
        k+=1
        l=-1

    if len(list(set2.intersection(list1)))==1 and look_for_samelineandsamecolumn(sudoku, x, y, value)and look_for_inner(sudoku, x, y, value):
        return True
    else:
        return False


def look_for_inner_sqrx(sudoku,i,j,posvar):
    if (i <= 2):
        if (j <= 2):
            return look_for_inner_helpx(sudoku, 1, 1, posvar,i,j)
        elif (j >= 6):
            return(look_for_inner_helpx(sudoku, 1, 7, posvar,i,j))
        else:
            return(look_for_inner_helpx(sudoku, 1, 4, posvar,i,j))
    elif (i >= 6):
        if (j <= 2):
            return (look_for_inner_helpx(sudoku, 7, 1, posvar,i,j))
        elif (j >= 6):
            return (look_for_inner_helpx(sudoku, 7, 7, posvar,i,j))
        else:
            return (look_for_inner_helpx(sudoku, 7, 4, posvar,i,j))
    else:
        if (j <= 2):
            return(look_for_inner_helpx(sudoku, 4, 1, posvar,i,j))
        elif (j >= 6):
            return(look_for_inner_helpx(sudoku, 4, 7, posvar,i,j))
        else:
            return(look_for_inner_helpx(sudoku, 4, 4, posvar,i,j))

#Returns a boolean value to decide if there is same value in inner square
def look_for_inner_help(sudoku,i,j,value):
    k=-1
    l=-1
    while(k<2):
        while(l<2):
            if(sudoku[i+k][j+l]==value):
                return True
            l+=1
        k+=1
        l=-1
    return False

#Looks for a possible variable and says is there a same value or not
def look_for_inner(sudoku,i,j,posvar):
    isthere=True
    if(i<=2):
        if(j<=2):
            if(look_for_inner_help(sudoku,1,1,posvar)):
                isthere=False
        elif(j>=6):
            if(look_for_inner_help(sudoku,1,7,posvar)):
                isthere=False
        else:
            if(look_for_inner_help(sudoku,1,4,posvar)):
                isthere=False
    elif(i>=6):
        if(j<=2):
            if(look_for_inner_help(sudoku,7,1,posvar)):
                isthere=False
        elif(j>=6):
            if(look_for_inner_help(sudoku,7,7,posvar)):
                isthere=False
        else:
            if(look_for_inner_help(sudoku,7,4,posvar)):
                isthere=False
    else:
        if(j<=2):
            if(look_for_inner_help(sudoku,4,1,posvar)):
                isthere=False
        elif(j>=6):
            if(look_for_inner_help(sudoku,4,7,posvar)):
                isthere=False
        else:
            if(look_for_inner_help(sudoku,4,4,posvar)):
                isthere=False
    return isthere

def samecolumn_values(sudoku,i,j):
    liste=[]
    for x in range(0,9):
        if sudoku[i][x]!=0:
            liste.append(sudoku[i][x])
    liste.sort()
    return liste

def sameline_values(sudoku,i,j):
    liste = []
    for y in range(0,9):
        if sudoku[y][j]!=0:
            liste.append(sudoku[y][j])
    liste.sort()
    return liste



def look_for_samelineandsamecolumn(sudoku,i,j,posvar):
    for x in range(0,9):
        if(sudoku[i][x]==posvar):
             return False
    for y in range(0,9):
        if(sudoku[y][j]==posvar):
            return False
    return True

def look_for_otherlines(sudoku,i,j,posvar):
    isthere1=False
    isthere2=False
    if (i%3==0):
        for x in range(0,9):
            if(sudoku[i+1][x]==posvar):
                isthere1=True
                break
        for y in range(0,9):
            if(sudoku[i+2][y]==posvar):
                isthere2=True
                break
        if(isthere1 and isthere2):
            return True
    elif(i%3==1):
        for x in range(0,9):
            if(sudoku[i-1][x]==posvar):
                isthere1=True
                break
        for y in range(0,9):
            if(sudoku[i+1][y]==posvar):
                isthere2=True
                break
        if(isthere1 and isthere2):
            return True
    elif(i%3==2):
        for x in range(0,9):
            if(sudoku[i-1][x]==posvar):
                isthere1=True
                break
        for y in range(0,9):
            if(sudoku[i-2][y]==posvar):
                isthere2=True
                break
        if(isthere1 and isthere2):
            return True
    return False


def look_for_othercolumns(sudoku,i,j,posvar):
    isthere1=False
    isthere2=False
    if (j%3==0):
        for x in range(0,9):
            if(sudoku[x][j+1]==posvar):
                isthere1=True
                break
        for y in range(0,9):
            if(sudoku[y][j+2]==posvar):
                isthere2=True
                break
        if(isthere1 and isthere2):
            return True
    elif(j%3==1):
        for x in range(0,9):
            if(sudoku[x][j-1]==posvar):
                isthere1=True
                break
        for y in range(0,9):
            if(sudoku[y][j+1]==posvar):
                isthere2=True
                break
        if(isthere1 and isthere2):
            return True
    elif(j%3==2):
        for x in range(0,9):
            if(sudoku[x][j-1]==posvar):
                isthere1=True
                break
        for y in range(0,9):
            if(sudoku[y][j-2]==posvar):
                isthere2=True
                break
        if(isthere1 and isthere2):
            return True
    return False

def mainfunc(sudoku,i,j,x):
    if (look_for_inner(sudoku, i, j, x) and look_for_samelineandsamecolumn(sudoku, i, j, x) and look_for_otherlines(
            sudoku, i, j, x) and look_for_othercolumns(sudoku, i, j, x)):
        return True
    return False

sudoku=initialize_sudoku()
print_sudoku(sudoku)
print("*************************")
istrue1=True
istrue2=True
istrue3=True
istrue4=True
iscont4=True
while(istrue1 or istrue2 or istrue3 or istrue4):
    istrue1=False
    istrue2=False
    istrue3=False
    istrue4=False
    iscont1 = True
    while(iscont1):
        iscont1=False
        for i in range(0,9):
            for j in range(0,9):
                if(sudoku[i][j]==0):
                    for x in range(1,10):
                        if mainfunc(sudoku,i,j,x):
                            sudoku[i][j]=x
                            print_sudoku(sudoku)
                            iscont1=True
                            break
        if (iscont1 == True):
            istrue1 = True


    iscont2=True
    while(iscont2):
        iscont2=False
        for i in range(0,9):
            for j in range(0,9):
                if sudoku[i][j]==0:
                    liste1 = samecolumn_values(sudoku,i,j)
                    liste2 = sameline_values(sudoku, i, j)
                    liste3 = innervalues(sudoku,i,j)
                    listemain=liste1+liste2+liste3
                    listemain=list(set(listemain))
                    if len(listemain)==8:
                        listemain.sort()
                        if len(listemain)==8:
                            iscont2 = True
                            for x in range(1, 10):
                                if x != listemain[x - 1]:
                                    sudoku[i][j] = x
                                    #print("1\n")
                                    #print_sudoku(sudoku)
                                    break
                                if(x==8):
                                    sudoku[i][j]=9
                                    #print("2\n")
                                    #print_sudoku(sudoku)
                                    break
        if (iscont2 == True):
            istrue2 = True

    iscont3=True
    while(iscont3):
        iscont3=False
        for i in range(0,9):
            for j in range(0,9):
                if sudoku[i][j]==0:
                    for x in range(1, 10):
                        if samesqrsameline(sudoku,i,j,x):
                            sudoku[i][j]=x
                            print("3\n")
                            print_sudoku(sudoku)
                            iscont3=True
                            break
                        elif samesqrsamecol(sudoku,i,j,x):
                            sudoku[i][j] = x
                            print("4\n")
                            print_sudoku(sudoku)
                            iscont3 = True
                            break
                        if look_for_inner_sqrx(sudoku,i,j,x):
                            if(i==0 and j==5):
                                print("&")
                            sudoku[i][j] = x
                            print("5\n")
                            print_sudoku(sudoku)
                            iscont3 = True
                            break
        if(iscont3 == True):
            istrue3=True
    iscont4 = True
    while (iscont4):
        iscont4 = False
        for i in range(0, 9):
            for j in range(0, 9):
                if (sudoku[i][j] == 0):
                    liste1=whichvaluescan(sudoku,i,j)
                    if len(liste1)==1:
                        sudoku[i][j]=liste1[0]
                        iscont4=True

        if (iscont4 == True):
            istrue4 = True)
print_sudoku(sudoku)
