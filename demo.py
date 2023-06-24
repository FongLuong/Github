

# b là kiểu số thực là 1.69 và xuất kiểu dữ liệu là float 
b = 1.69 
print(b)
print(type(b))
# lấy toàn bộ thư viện từ Decimal 
# từ thư viện Deciaml -> import mọi thứ(*) vào
from decimal import*

# lấy tối đa 0 chữ số phần nguyên và chữ số thập phân từ Decimal
getcontext().prec = 3

p = 10/3
print(p)
print(type(p))

b = Decimal(10)/Decimal(3)
print(b)
print(type(b))

