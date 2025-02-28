#Nhap so tu nguoi dung
so = int(input("Nhap mot so nguyen: "))
#Kiem tra so do co phai so chan hay khong
if so % 2 == 0:
    print(so, "la so chan.")
else:
    print(so, "khong phai so chan.")