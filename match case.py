while True :
    try :
        Saniyedeki_paket_sayısı = int(input("Saniyedeki paket sayısı giriniz: "))
    except ValueError : 
        print ("Lütfen sadece sayı girin.")
        continue
    if Saniyedeki_paket_sayısı == 0:
            print("Sistem dengeleme modülü kapatılıyor...")
            break
    elif Saniyedeki_paket_sayısı >= 10001:
            print("Kritik uyarı:DDoS şüphesi Trafik engelleniyor...")
            break
    elif Saniyedeki_paket_sayısı >= 5000 and Saniyedeki_paket_sayısı <=10000:
            print("Sarı Alarm: Trafik yoğun.")
    elif Saniyedeki_paket_sayısı <=4999 :
            print(f"{Saniyedeki_paket_sayısı} paket/sn. Trafik normal.")
