kullanici_adi = "kodluyoruum"
sifresi = "melike"

while True:
    kullanici = input("Kullanıcı adınızı giriniz: ")
    parola = input("Şifrenizi giriniz: ")

    if kullanici == kullanici_adi and parola == sifresi:
        print("Hoşgeldiniz")
        break

    elif kullanici == kullanici_adi and parola != sifresi:
        print("Şifreniz yanlış\n")

    elif kullanici != kullanici_adi and parola == sifresi:
        print("Kullanıcı adınız yanlış \n")

    else:
        print("Kullanıcı adı ve şifre hatalı\n")
