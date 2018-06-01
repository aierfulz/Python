A = open("E:/out1.txt", 'r')
B = open("E:/out2.txt", 'r')
C = open("E:/2001048_lz_4_2684.0.txt", 'r')
D = open("E:/test/1.txt", 'w')
c_a = A.readlines()
c_b = B.readlines()
c = C.readlines()
c_u =c_a + c_b
i = len(c_u)
    #读取文件集合
j = len(c)
m = 0
k = 0
last = [] #起一个程序处理前的文本文件
pro = [] #后一个程序处理后的文件
data = []
while m < j:
    l = "".join(c[m]).lstrip()[13:20] + "".join(c[m]).lstrip()[0:8]
    m = m + 1
    last.append(l)
while k < i:
    lines = str(float("".join(c_u[k]).lstrip()[0:8]).__round__(4)) + "".join(c_u[k]).lstrip()[11:19]
    d = "".join(c_u[k]).lstrip()[92:102]
    k = k + 1
    pro.append(lines) #源程序处理前的数据的经度纬度
    data.append(d) #对应数据的气溶胶的浓度
la_l = len(last)
pr_l = len(pro)
#匹配前后相同的值
s = 0
n = 0
st = []
while s < la_l:
    while n < pr_l:
        if(pro[n] == last[s]):
            st.append(last[s]+data[n]) #匹配相同的项，如果相同，跳出循环
            break
        if(n == pr_l - 1 and pro[n] != last[s]):#匹配一个周期，如果没有相同的就将该数据输出并加上0
            st.append(last[s] + "0.00000000")
            break
        n = n + 1
    s = s + 1
    n = 0
#格式化打印
length = len(st)
d = 0
while d < length:
    s = "".join(st[d]).lstrip()[0:7] + " " + "".join(st[d]).lstrip()[7:15] + " " + "".join(st[d]).lstrip()[15:28]
    d = d + 1
    D.writelines(s+"\n")
print("####写入成功####")
