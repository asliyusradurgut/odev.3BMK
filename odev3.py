sayilar=[3,5,7,2,12,32,45]
#1- sayilar listesindeki her bir elemanı yazdırınız.
for x in sayilar:
    print(x)
#2- sayilar listesinde hangi sayılar 3ün katıdır.
for y in sayilar:
    if((y%3)==0):
        print(y)
#3- sayilar listesinde tüm sayiların toplamı nedir?
toplam = sum(sayilar)
print("Tüm sayıların toplamı:", toplam)
urunler=["iphone", "samsung s4", "samsung s22", "iphone 15", "iphone 14"]
#4-urunler listesinde ki tüm iphone marka ürünleri listeleyiniz. (index ve find komutlarından yararlanınız)
iphone_urunleri = [urun for urun in urunler if urun.find("iphone") != -1]
print("iPhone Ürünleri:", iphone_urunleri)

#5-urunler listesinde kaç adet samsung ürünü vardır. (find metodu)
samsung_sayisi = sum(1 for urun in urunler if urun.find("samsung") != -1)
print("Samsung Ürün Sayısı:", samsung_sayisi)
