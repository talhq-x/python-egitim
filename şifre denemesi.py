import time 
takipteki_coinler = ["BTC","ETH","SOL","AVAX","TRU"]
while True:
    işlem = input("Yapmak istediğiniz işlemi seçin (cuzdan,fiyat,risk,çıkış): ")
    match işlem :
        case "çıkış" :
            print("çıkış yapılıyor...")
            break
        case "cuzdan" :
            for coin in takipteki_coinler:
                print(f"Takip edilen parite: {coin}")
                time.sleep(1)
        case "fiyat":
            parite_adı = input("Parite adını giriniz: ")
            if parite_adı not in takipteki_coinler:
                print("Bu partie takip listesinde değil.")
            else :
                print(f"Sistem aktif.{parite_adı} verileri çekiliyor...")
        case "risk":
            while True :
                try :
                    giriş_fiyatı = float(input("İşleme giriş fiyatını yazın: "))
                    stop_fiyatı = float(input("Stop-loss fiyatını yazın: "))
                except :
                    print("Sadece sayı giriniz.")
                    continue
                break
            if stop_fiyatı >= giriş_fiyatı :
                print("Mantık hatası.Long işlemde stop fiyatı giriş fiyatından büyük olamaz.")
            elif giriş_fiyatı - stop_fiyatı >= 1000 :
                print("Stop mesafesi çok geniş.Kayıp riski")
            else :
                print("Risk parametreleri normal,işleme onay verildi")
        case _:
            print("Geçersiz komut")
                     


            