



''' 1- Bir listeyi düzleştiren (flatten) fonksiyon yazın.
Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir.
Örnek olarak:
input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output: [1,'a','cat',2,3,'dog',4,5]'''
li=[]
def flatten(n):
     for i in n:
         if isinstance(i,list):#Kontrol ediyor liste mi diye
          flatten(i)
         else:
          li.append(i)#Eğer liste değilse boş olan li elemanına ekliyor


liste=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flatten(liste)
print(li)

''' 2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. 
Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. 
Örnek olarak:
input: [[1, 2], [3, 4], [5, 6, 7]]
output: [[[7, 6, 5], [4, 3], [2, 1]]'''

def reverse_list(n):
 n = n[::-1]
 n = [i[::-1] for i in n]
 return n

liste1=[[1, 2], [3, 4], [5, 6, 7]]


print(reverse_list(liste1))






















