import math
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


# 八位数整形
def size(string):
    return string.zfill(8)
# 获得文本二进制字符串
def get_key(tra):
    arr = tra
    f = open(arr,'rb')
    a = ""
    s = f.read()
    for i in range(len(s)):
        a = a+size(bin(s[i]).replace('0b',''))
    return a

# r进制转十进制
def rary_tenary(tra,r):
    return int(tra,r)

# 十进制转r进制
def tenary_rary(n,r):
    num = int(n)
    b = []
    while num:
        c = num % r
        b.append(c)
        num = num // r
    return ''.join([str(x) for x in b[::-1]])

# 嵌入函数
def func(photo1,txt,n,k):
    # 灰度图
    img = Image.open(photo1).convert('L')
    width = img.size[0]
    height = img.size[1]
    # 二维数组
    img_ary = np.array(img)
    img_arry = img_ary.flatten()
    infoma = get_key(txt)
    # print(infoma)
    # print(str2)
    len_infoma = len(infoma)
    infoma_arrynum = math.ceil(len_infoma/k)
    infoma_ary = np.zeros((infoma_arrynum,k),dtype=np.int64)
    # print(infoma_ary,infoma_arrynum)
    # print(img_ary)
    i = 0
    while i < infoma_arrynum:
        for j in range(0, k):
            if i * k + j < len_infoma:
                infoma_ary[i, j] = infoma[i * k + j]
        i = i + 1
    data = []
    # d为获取的秘密数字
    for i in range(0, infoma_arrynum):
        d = 0
        for j in range(0, k):
            d += infoma_ary[i, j] * (2 ** (k - 1 - j))
        temp = tenary_rary(d, 2 * n + 1).zfill(1)
        data.append(temp)


    backupinfo = img_arry.copy()
    for i in range(0,infoma_arrynum):
        g = int(data[i])
        p = img_arry[i]
        if 0<= p <=1:
            for q in range(0,(2*n+1)):
                f = (p+q)%(2*n+1)
                if f==g:
                    backupinfo[i] = p+q
                    break
        elif 254<=p<=255:
            for q in range(-(2*n),1):
                f =(p+q)%(2*n+1)
                if f==g:
                    backupinfo[i] = p+q
                    break
        else:
            for q in range(-n,(n+1)):
                f = (p + q) % (2*n+1)
                if f == g:
                    backupinfo[i] = p + q
                    break

    print("隐藏完成")
    img_put = backupinfo.flatten()
    img_result = img_put.reshape(height,width)
    plt.figure(figsize=(4, 2))  # 设置窗口大小
    plt.suptitle('cat and dog')  # 图片名称
    plt.subplot(1, 2, 1), plt.title('orginal')  # subplot(1, 2, 1)中的三个参数分别表示行数、列数、索引值
    plt.imshow(img, cmap='gray'), plt.axis('off')  # 这里显示灰度图要加cmap，否则显示的是伪彩色图像
    plt.subplot(1, 2, 2), plt.title('embed')
    plt.imshow(img_result, cmap='gray'), plt.axis('off')
    plt.show()
# 提取数据
    recoverdata = []
    for i in range(0,infoma_arrynum):
        e = backupinfo[i]%(2*n+1)
        recoverdata.append(str(e))
    strr = ''
    for i in range(0,infoma_arrynum):
        team = rary_tenary(recoverdata[i],2*n+1)
        strr += tenary_rary(team,2).zfill(2)
    tra = ''
    for i in range(0,len(strr),8):
        c = rary_tenary(strr[i:i+8],2)
        tra += chr(c)
    print("提取的秘密信息：")
    print(tra.encode('raw_unicode_escape').decode('utf-8', 'ignore'))


old = "E:/reproduction/photo1.jpg"
enc = "E:/reproduction/infomation.txt"


func(old,enc,2,2)



