import xlrd
import time
import os
start_time = time.ctime()
print("start time:" + start_time)
file = os.listdir("E:/excl")
count = len(file)
k = 0
while k < count:
    A = xlrd.open_workbook("E:/excl/" + file[k])
    sh = A.sheet_by_name("Sheet1")
    col = sh.ncols
    row = sh.nrows
    c = []
    i = 0
    while i < row:
        m =float(sh.cell_value(i,9))
        c.append(m.__round__(9))
        i = i + 1
    j = 0
    length = len(c)
    st = []
    if(length >= 2648):
        while j < 61: #定义举证的列数
            st.append(str(c[j]) + " " + str(c[j+61]) + " " + str(c[j+61*2]) + " " + str(c[j+61*3]) + " " + str(c[j+61*4]) + " " + str(c[j+61*5]) + " " +
                  str(c[j+61*6]) + " " + str(c[j+61*7]) + " " + str(c[j+61*8]) + " " + str(c[j+61*9]) + " " + str(c[j+61*10]) + " " + str(c[j+61*11]) + " " +
                  str(c[j+61*12]) + " " + str(c[j+61*13]) + " " + str(c[j+61*14]) + " " + str(c[j+61*15]) + " " + str(c[j+61*16]) + " " + str(c[j+61*17]) + " " +
                  str(c[j+61*18]) + " " + str(c[j+61*19]) + " " + str(c[j+61*20]) + " " + str(c[j+61*21]) + " " + str(c[j+61*22]) + " " + str(c[j+61*23]) + " " +
                  str(c[j+61*24]) + " " + str(c[j+61*25]) + " " + str(c[j+61*26]) + " " + str(c[j+61*27]) + " " + str(c[j+61*28]) + " " + str(c[j+61*29]) + " " +
                  str(c[j+61*30]) + " " + str(c[j+61*31]) + " " + str(c[j+61*32]) + " " + str(c[j+61*33]) + " " + str(c[j+61*34]) + " " + str(c[j+61*35]) + " " +
                  str(c[j+61*36]) + " " + str(c[j+61*37]) + " " + str(c[j+61*38]) + " " + str(c[j+61*39]) + " " + str(c[j+61*40]) + " " + str(c[j+61*41]) + " " +
                  str(c[j+61*42]) + " " + str(c[j+61*43]))
            j = j + 1
    if(length <= 2640):
        while j < 60:#的不优雅,但测试运行时间最短
            st.append(str(c[j]) + " " + str(c[j+60]) + " " + str(c[j+60*2]) + " " + str(c[j+60*3]) + " " + str(c[j+61*4]) + " " + str(c[j+60*5]) + " " +
                  str(c[j+60*6]) + " " + str(c[j+60*7]) + " " + str(c[j+60*8]) + " " + str(c[j+60*9]) + " " + str(c[j+60*10]) + " " + str(c[j+60*11]) + " " +
                  str(c[j+60*12]) + " " + str(c[j+60*13]) + " " + str(c[j+60*14]) + " " + str(c[j+60*15]) + " " + str(c[j+60*16]) + " " + str(c[j+60*17]) + " " +
                  str(c[j+60*18]) + " " + str(c[j+60*19]) + " " + str(c[j+60*20]) + " " + str(c[j+60*21]) + " " + str(c[j+60*22]) + " " + str(c[j+60*23]) + " " +
                  str(c[j+60*24]) + " " + str(c[j+60*25]) + " " + str(c[j+60*26]) + " " + str(c[j+60*27]) + " " + str(c[j+60*28]) + " " + str(c[j+60*29]) + " " +
                  str(c[j+60*30]) + " " + str(c[j+60*31]) + " " + str(c[j+60*32]) + " " + str(c[j+60*33]) + " " + str(c[j+60*34]) + " " + str(c[j+60*35]) + " " +
                  str(c[j+60*36]) + " " + str(c[j+60*37]) + " " + str(c[j+60*38]) + " " + str(c[j+60*39]) + " " + str(c[j+60*40]) + " " + str(c[j+60*41]) + " " +
                  str(c[j+60*42]) + " " + str(c[j+60*43]))
            j = j + 1
    T = open("E:/test/" + str(file[k])[0:7] + ".txt", 'w')
    q = 0
    while q < len(st):
        T.writelines(str(st[q])+"\n")
        q = q + 1
    k = k + 1
end_time = time.ctime()
print("end time:" + end_time)
print("######写入成功##########")
