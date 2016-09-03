"""lst = [
[_ _ _ _ _ _ _ _ _]
[_ _ _ _ _ _ _ _ _]
[_ _ _ _ _ _ _ _ _]
[_ _ _ _ _ _ _ _ _]
[_ _ _ _ _ _ _ _ _]
[_ _ _ _ _ _ _ _ _]
[_ _ _ _ _ _ _ _ _]
[_ _ _ _ _ _ _ _ _]
[_ _ _ _ _ _ _ _ _]




[00,01,02,10,11,12,20,21,22]
[30,31,32,40,41,42,50,51,52]
]
"""
def sudoku_check(lst):
    #check1
    for i in range(9):
        check = [k for k in range(1,10)]
        for j in range(9):
            if lst[i][j] in check:
                check.remove(lst[i][j])
            else:
                return False
    #check2
    for i in range(9):
        check = [k for k in range(1,10)]
        for j in range(9):
            if lst[j][i] in check:
                check.remove(lst[j][i])
            else:
                return False
    #check3
    checkarr = []
    for l in range(0,7,3):
        arr = sudoku[l:l+3]
        i=0
        j=0
        #print arr
        while True:
            if i==9:
                i=0
                break
            #checkarea

            #print i,j
            checkarr.append(arr[j][i])
            if j%3!=2:
                j+=1
            else:
                if i%3==2:
                    j+= 1
                else:
                    j-=2
                i += 1
                if i%3==0:
                    j=0
            if len(checkarr)%9==0:
                check = [z for z in range(1,10)]
                for k in checkarr:
                    if k in check:
                        check.remove(k)
                    else:
                        return False
                checkarr = []

        #final result
        return True

print("""[[_ _ _ _ _ _ _ _ _],[_ _ _ _ _ _ _ _ _],[_ _ _ _ _ _ _ _ _],\
[_ _ _ _ _ _ _ _ _],[_ _ _ _ _ _ _ _ _],[_ _ _ _ _ _ _ _ _],\
[_ _ _ _ _ _ _ _ _],[_ _ _ _ _ _ _ _ _],[_ _ _ _ _ _ _ _ _]]"""")
sudoku = input("Enter the sudoku in the given format: ")
print sudoku_check(sudoku)
#00,01,
