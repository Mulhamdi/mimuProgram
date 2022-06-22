binatang = ['Anjing', 'Kucing', 'Babi']
print(binatang)
del binatang[int(input('Index yang ingin dihapus: '))]
print(binatang)
a = int(input('Ketik 0/1 jika ingin menghapus lagi: '))
b = 2
if a < b:
     del binatang[int(input('Index: '))]
     print('Hasilnya: ', binatang)
else:
     print('SELESAI')
