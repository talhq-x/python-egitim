while True:
    try :
        port = int (input("Taranacak portu girin (Çıkış için 0): "))
    except ValueError :
        print ("Lütfen sadece sayı girin: ")
        continue 
    if port == 0:
            print("Çıkış yapılıyor...")
            break
    elif port <= 1023 :
            print("Kritik sistem portu")
    elif port >= 1024 and port <= 4051 :
            print("Kayıtlı port aralığı.")
    else : 
            print("Dinamik port aralığı.")