#Tao mot danh sach rong de luu ket qua
j=[]
#Duyet cac so doan tu 2000 den 3200, kiem tra so i co chia het cho 7 va khong phai la boi so cua 5 hay khong
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        j.append(str(i))
print(','.join(j))