import time 
hedef_ipler = ["192.168.1.15", "10.0.2.4", "172.16.0.8"]
wordlist = ["123456", "admin", "qwerty", "toor"]
while True :
    İşlem = input("İşlem seçin (keşif,saldırı,çıkış): ")
    match İşlem :
        case "çıkış":
            print("Çıkış yapılıyor...")
            break
        case "keşif":
            for ip in hedef_ipler:
                print(f"Taranıyor: {ip}")
                time.sleep(1.5)
        case "saldırı":
            seçilen_ip = input("Hedef ip girin: ")
            if seçilen_ip not in hedef_ipler :
                print("Hata: Bu IP yetki alanımızda yok.")
            else :
                while True :
                    try :
                        Port = int(input("Port numarası giriniz: "))
                    except ValueError :
                        print("Sadece sayı giriniz")
                        continue
                    if Port == 21 or Port == 22 :
                        for sifre in wordlist:
                            print(f"Deneme yapılıyor: {sifre}")
                            time.sleep(1)
                            if sifre == "toor":
                                print(f"BAŞARILI: {secilen_ip} sistemine sızıldı, şifre: toor")
                                break
                        
                            elif Port > 1000 and Port < 5000:
                                print("Zafiyet yok.")
                            else:
                                print("Bağlantı koptu.")
            