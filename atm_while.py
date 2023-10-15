import random

kullanici = ['Ahmet','Mehmet','Ali','Veli','Ayşe','Fatma','Hayriye']
bakiye = 100

while True:

    pick = random.choice(kullanici)
    print(f'Merhaba Sayın {pick}, Hoşgeldiniz! \nLüften yapmak istediğiniz işlemi seçiniz')
    yapilmak_istenilen_islem = input('1-Bakiye Sorgu \n2-Para Çekme \n3-Para Yatırma \n4-Çıkış \n')

    if yapilmak_istenilen_islem == '1':
        print('Güncel Bakiye: {}'.format(bakiye))

    elif yapilmak_istenilen_islem == '2':
        tutar_cek = int(input('Çekmek istediğiniz Tutar: '))
        if bakiye - tutar_cek < 0:
            print(f'Sayın {pick}, Bakiyeniz yetersizdir')
            yapilmak_istenilen_islem = input('1-Bakiye Sorgu \n2-Para Çekme \n3-Para Yatırma \n4-Çıkış \n')
        else:
            bakiye -= tutar_cek
            print(f'Güncel Bakiye: {bakiye}')

    elif yapilmak_istenilen_islem == '3':
        tutar_yatir = int(input('Yatırmak istediğiniz tutar: '))
        bakiye+=tutar_yatir
        print(f'Güncel Bakiye: {bakiye}')
 
    elif yapilmak_istenilen_islem == '4':
        print(f'Sayın {pick}, Başarıyla Çıkış Yaptınız!')
    else:
        print(f'Sayın {pick}, Lütfen bir seçim yapınız')
        yapilmak_istenilen_islem = input('1-Bakiye Sorgu \n2-Para Çekme \n3-Para Yatırma \n4-Çıkış \n') 
    break