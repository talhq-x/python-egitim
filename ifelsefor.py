import time
while True :
    Kullanıcı_adi = input("\nLütfen kullanıcı adını giriniz (Çıkmak için çıkış yazınız): ")
    match Kullanıcı_adi :
        case "çıkış":
            print("Çıkış yapılıyor...")
            break
        case "root":
            Şifre = input("Lütfen şifreyi giriniz: ")
            match Şifre :
                case "toor":
                    print("Sisteme erişim sağlandı.")
                case "çıkış":
                    print("Çıkış yapılıyor.")
                    break
                case _:
                    print("Şifre hatalı Erişim engellendi.")
                    time.sleep(1)
        case _:
            print(f"{Kullanıcı_adi} adında bir kullanıcı bulunamadı.")
            time.sleep(1)