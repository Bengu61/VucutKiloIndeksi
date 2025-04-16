print("Merhaba haydi vücut kilo indeksinizi hesaplayalım.")

print("Kilonuzu giriniz:")
kilo=float(input())

print()

print("Boyunuzu giriniz:") 
boy=float(input())

vücutKiloİndeksi=(kilo/((boy)**2))  # Boy "m" cinsinden 1.75 gibi,Kilo "kg" cinsinden 75 gibi.
print("Vücut kilo indeksiniz:"+str(vücutKiloİndeksi))

if(vücutKiloİndeksi<18.5):
    print("Zayıf")

elif(18.5<vücutKiloİndeksi<24.9):
    print("Normal")
    
elif(25<vücutKiloİndeksi<29.9):  
    print("Kilolu")
    
elif(30<vücutKiloİndeksi):
    print("Obez")
    
else:
    print("Morbid obez")
