from PIL import Image
import math


# 八位数整形
def size(string):
    return string.zfill(8)

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

# 十进制转2进制
def tenary_binary(n):
    num = int(n)
    b = []
    while num:
        c = num % 2
        b.append(c)
        num = num // 2
    return ''.join([str(x) for x in b[::-1]])

def LSB(tra):
    return tra[-1]

def f(num1,num2):
    bina = math.floor(num1/2.0)+num2
    out = str(tenary_binary(bina))
    return LSB(out)

def func(str1,str2,str3):
    img = Image.open(str1).convert('L')
    width = img.size[0]
    height = img.size[1]
    information = get_key(str2)
    len_infoma = len(information)
    # print(len_infoma)
    count = 0
    for p in range(0,height):
        for q in range(0,width):
            piexl1 = img.getpixel((q,p))
            piexl2 = img.getpixel((q+1,p))
            if count == len_infoma:
                break
            if information[count] == LSB(tenary_binary(piexl1)):
                print("lsb=",LSB(tenary_binary(piexl1)),"count= ",count)
                if information[count+1] != f(piexl1,piexl2):
                    img.putpixel((q+1,p),piexl2+1)
                else:
                    img.putpixel((q+1,p),piexl2)
                img.putpixel((q,p),piexl1)
            else:
                if information[count+1] == f(piexl1-1,piexl2):
                    img.putpixel((q,p),piexl1-1)
                else:
                    img.putpixel((q, p), piexl1 + 1)
                img.putpixel((q,p),piexl2)
            count +=2
    img.show()
    img.save(str3)
    print("隐藏完成")

old ="E:/reproduction/photo1.jpg"
enc ="E:/reproduction/infomation.txt"
new = "E:/reproduction/photo1_test.jpg"

func(old,enc,new)


