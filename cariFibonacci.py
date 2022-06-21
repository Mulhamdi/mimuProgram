# Pencarian angka ke-10.000 dalam deret Fibonacci dengan panjang 2.090 digit

x=[0]*10005;              #inisialisasi array 0 sebanyak 10005; x[0]=0
x[1]=1;                   #x[1]=1
 
for j in range(2,10001):
      x[j]=x[j-1]+x[j-2]  # Fibonacci
print(x[10000])
