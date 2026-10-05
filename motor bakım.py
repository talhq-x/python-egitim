import time 
sistemdeki_parcalar = ["zincir","yağ","fren","lastik","buji"]
while True:
    İşlem = input("\nİşlem seçiniz (sürüş,bakım,parçalar,çıkış): ")
    match İşlem :
        case "çıkış":
            print("Çıkış yapılıyor...")
            break
        case "parçalar":
            for parca in sistemdeki_parcalar:
                print(f"Kontrol edilcek parça {parca}")
                time.sleep(1)
        case "bakım":
            secilen_parca = input("Hangi parçaya bakım yapıldı ?\n")
            if secilen_parca not in sistemdeki_parcalar :
                print("Bu parça sistemde kayıtlı değil.")
            else :
                print(f"Sistem güncellendi.{secilen_parca} bakımı yapıldı.")
        case "sürüş":
            while True:
                try :
                    Km = int(input("Yapılan Km yi giriniz: "))
                except ValueError :
                    print("Km sayı cinsinden olmalıdır.")
                    continue
                break
            if Km == 0 or Km <= 0 :
                print("Geçersiz mesefe.")
            elif Km >= 300 :
                print("Uzun yol yapılmış.Motosikletin zinciri yağlamayı ve mekanik kontrolleri yapmayı unutma.")
            else:
                print(f"{Km} Km sisteme kaydedildi. ")
        case _:
            print("Geçersiz İşlem girdiniz.")