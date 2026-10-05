
while True :
    try :
        urun_fiyatı = int(input("Almak istediğiniz ürün fiyatını giriniz: "))
        urun_için_verilen_para = int(input("Ürün için vereceğiniz parayı giriniz: "))
        break
    except ValueError : 
        print("Gireceğiniz fiyat sayı olmalıdır.")