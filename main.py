"""
    * Restoran Uygulaması
        * corbalar, balıklar, etler, makarnalar
        * menüde yemek adı ve fiyat bulunacak
        * en az 3 masa olacak
        * program çalışınca yeni müşteri / hesap isteyen / günü bitir
            * yeni müşteri
                - kaç kişi olduğu sorulacak
                - müşterilere sıra ile menü gösterilip istekleri sorulacak
                - boş masa yoksa gelen müşteri geri çevrilecek
            * hesap isteyen
                - hangi masa hesap istiyor
                - hesap nasıl ödenecek (alman usulü / eşit ödeme / ağanın eli tutulmaz)
                    - alman usulü seçilirse: her müşteri için fiyat listelenecek
                    - eşit ödeme seçilirse toplam fiyat ve kişi başına düşen fiyat belirtilecek
                    - ağa seçilirse toplam fiyat belirtilecek
            * günü bitir
                - bütün boş olmalı
                - gün boyu elde edilen kazanç ekrana yazdırılacak
"""

menu = { # menüde bulunan yemekler ve fiyatları
    1: {
        "başlık": "Çorbalar",
        "liste" : {
            1: {"isim": "Domates Çorbası", "fiyat": 10},
            2: {"isim": "Ezo Gelin Çorbası", "fiyat": 8},
            3: {"isim": "Yuvalama Çorba", "fiyat": 12},
            4: {"isim": "Mercimek Çorbası", "fiyat": 6},
            5: {"isim": "Süt Çorbası", "fiyat": 14},
            6: {"isim": "Prenses Çorbası", "fiyat": 12},
            7: {"isim": "Nohutlu Gurcu Çorbası", "fiyat": 12},
            8: {"isim": "Analı Kızlı Çorbası", "fiyat": 14},
        }
    },
    2: {
        "başlık": "Balıklar",
        "liste" : {
            1: {"isim": "Çupra", "fiyat": 40},
            2: {"isim": "Levrek", "fiyat": 38},
            3: {"isim": "Levrek pane", "fiyat": 46},
            4: {"isim": "Hamsi", "fiyat": 30},
            5: {"isim": "İstavrit", "fiyat": 44},
            6: {"isim": "Palamut", "fiyat": 46},
            7: {"isim": "Uskumru", "fiyat": 38},
            8: {"isim": "Somon", "fiyat": 40},
            9: {"isim": "Lüfer", "fiyat": 50},
            10: {"isim": "Barbun", "fiyat": 48},
            11: {"isim": "Deniz levrek", "fiyat": 46},
            12: {"isim": "Deniz çuprası", "fiyat": 48},
            13: {"isim": "Kalkan", "fiyat": 40},
            14: {"isim": "Kılıç", "fiyat": 56},
            15: {"isim": "Fener", "fiyat": 52},
            16: {"isim": "Dil", "fiyat": 50},
            17: {"isim": "Böcek", "fiyat": 44},
            18: {"isim": "Istakoz", "fiyat": 52},
            19: {"isim": "Balık buğlama", "fiyat": 40},
            20: {"isim": "Tuzda balık", "fiyat": 42},
            21: {"isim": "Karışık balık", "fiyat": 36},
        }
    },
    3: {
        "başlık": "Et Yemekleri",
        "liste" : {
            1: {"isim": "Kuzu Külbastı", "fiyat": 56},
            2: {"isim": "Kağıt Kebabı", "fiyat": 38},
            3: {"isim": "Güvec Kapama", "fiyat": 48},
            4: {"isim": "Sebzeli Soslu Antrikot", "fiyat": 68},
            5: {"isim": "Hünkar Beğendi", "fiyat": 66},
            6: {"isim": "Beef Stroganoff", "fiyat": 52},
            7: {"isim": "Domates Soslu Jülyen Et Sote", "fiyat": 52},
            8: {"isim": "Arpacık Soğanlı Yahni", "fiyat": 50},
            9: {"isim": "Şaşlık Kebabı", "fiyat": 46},
            10: {"isim": "Patlıcan Kapama", "fiyat": 40},
            11: {"isim": "Kuzu Kaburga", "fiyat": 50},
            12: {"isim": "Belen Tava", "fiyat": 48},
        }
    },
    4: {
        "başlık": "Makarnalar",
        "liste" : {
            1: {"isim": "Fırın Makarna Sade", "fiyat": 13},
            2: {"isim": "Fırın Makarna Tavuklu", "fiyat": 19},
            3: {"isim": "Fırın Makarna Kıymalı", "fiyat": 22},
            4: {"isim": "Spagetti Bolognesse", "fiyat": 18},
            5: {"isim": "Fettuccine Alfredo", "fiyat": 22},
            6: {"isim": "Chef Penne", "fiyat": 18},
            7: {"isim": "Penne Di Mami", "fiyat": 22},
            8: {"isim": "Spagetti Di Mare", "fiyat": 20},
            9: {"isim": "Penne Della Nonna", "fiyat": 23},
            10: {"isim": "Top Köfteli Spagetti", "fiyat": 21},
            11: {"isim": "Ev Mantısı", "fiyat": 21},
        }
    }
}

# masalar = {
#     1: {},
#     2: {},
#     3: {},
#     4: {},
#     5: {}
# }
masalar = { #Masa adisyonlarını saklama yeri
    1: {  # 1. masada 2 müşteri var
        1: {  # 1. müşteri siparişleri Çorba no: 2, balık no: 16 makarna no: 6
            1: [2, 4], 2: [16], 4: [6]
        },
        2: {  # 2. müşteri siparişleri Çorba no: 3, et no: 12 makarna no: 10
            1: [3], 3: [12], 4: [10]
        }
    },
    2: {  # 2. masada 1 müşteri var
        1: {  # 1. müşteri siparişleri Çorba no: 5 ve 7, et no: 10
            1: [5, 7], 3: [10]
        }
    },
    3: {}, # Masa boş
    4: {},
    5: {}
}

kasa = 0  # Gün boyu kazanılan para saklanacak

while True:
    olay = input("Olay seçimi \n\t\t1: Yeni müşteri\n\t\t2: Hesap al\n\t\t3: Günü bitir\n\t\t\t seçiminiz : ")
    if olay == "1":
        masa_no = 0
        for i in masalar:
            if len(masalar[i]) == 0:
                masa_no = i
                break
        else:
            print("Ne yazık ki müsait masamız bulunmamaktadır")
        if masa_no != 0:
            kisi = input("Hoş geldiniz, kaç kişiyiz? ")
            for i in range(1, int(kisi) + 1): # i: müşteri numarası
                masalar[masa_no][i] = dict()
                while True:
                    # masa_no. masadaki i. kişiye yemek çeşidi seçtir:
                    print(f"\tMüşteri {i} için menü listeleniyor: ")
                    print("\tYemek çeşitlerimiz : ")
                    for j in menu: # j: çeşit numarası
                        print(f"\t\t {j} - {menu[j]['başlık']} ")
                    secilen_cesit = int(input("\t Seçiminiz: "))
                    # print(f"Çesit: {menu[secilen_cesit]}")
                    # print(f"masalar[masa_no]: {masalar[masa_no]}")
                    # print(f"masalar[masa_no][i]: {masalar[masa_no][i]}")

                    # Seçilen çeşide göre yemeği seçtir.
                    print(f"\tMüşteri {i} için {menu[secilen_cesit]['başlık']} listeleniyor: ")
                    for yemek_no, yemek in menu[secilen_cesit]["liste"].items():
                        print("\t\t" + str(yemek_no).rjust(2) + "\t" + yemek["isim"].ljust(30) +
                              str(yemek["fiyat"]).rjust(3) + " TL")
                    secilen_yemek = int(input("\t Seçiminiz: "))

                    # Seçilen yemeği ekle
                    if secilen_cesit not in masalar[masa_no][i].keys():
                        # Eğer bu müşteri bu çeşitte bir yemeği daha önce SEÇMEMİŞ ise
                        masalar[masa_no][i][secilen_cesit] = list()
                    masalar[masa_no][i][secilen_cesit].append(secilen_yemek)

                    # i. kişiye başka isteğiniz var mı diye sor.
                    tekrar = input("Başka bir arzunuz var mı? E/h ").lower()
                    if tekrar == "h":
                        break
    elif olay == "2":
        # print(masalar)
        print("Dolu Masalar")
        tum_masalar_bos = True
        for i in masalar.keys():
            if len(masalar[i]) > 0:
                tum_masalar_bos = False
                print(f"\t{i}. masada {len(masalar[i])} müşteri var.")
        masa_no = int(input("\t\tHangi masa hesap istiyor: "))
        masa_hesap = 0
        if len(masalar[masa_no]) > 1: #masada birden fazla müşteri varsa nasıl ödeneceği seçilecek
            print("\t\tÖdeme seçenekleri:\n\t\t\t1 - Alman usulü\n\t\t\t2 - Eşit Ödeme\n\t\t\t3 - Hepsi beraber")
            odeme_tipi = input("\t\tNasıl ödeme yapılacak? ")
            if odeme_tipi == "1":
                for musteri in masalar[masa_no].keys():
                    musteri_hesap = 0
                    for yemek_tipi in masalar[masa_no][musteri].keys():
                        for yemek in masalar[masa_no][musteri][yemek_tipi]:
                            # print(f"masa_no\t\t{masa_no}")
                            # print(f"musteri\t\t{musteri}")
                            # print(f"yemek_tipi\t{yemek_tipi}")
                            # print(f"yemek\t\t{yemek}")
                            # print(f"{menu[yemek_tipi]['liste'][yemek]['isim']}")
                            # print(f"{menu[yemek_tipi]['liste'][yemek]['fiyat']}")
                            musteri_hesap += menu[yemek_tipi]['liste'][yemek]['fiyat']
                    print(f"\t\t\t{musteri}. müşteri hesap ederi: {musteri_hesap} TL ")
                    kasa += musteri_hesap
            elif odeme_tipi == "2":
                masa_hesap = 0
                for musteri in masalar[masa_no].keys():
                    for yemek_tipi in masalar[masa_no][musteri].keys():
                        for yemek in masalar[masa_no][musteri][yemek_tipi]:
                            masa_hesap += menu[yemek_tipi]['liste'][yemek]['fiyat']
                print(f"\t\t\tMasa {masa_no}, kişi başı hesap ederi: {masa_hesap / len(masalar[masa_no])} TL ")
                kasa += masa_hesap
            else:
                masa_hesap = 0
                for musteri in masalar[masa_no].keys():
                    for yemek_tipi in masalar[masa_no][musteri].keys():
                        for yemek in masalar[masa_no][musteri][yemek_tipi]:
                            masa_hesap += menu[yemek_tipi]['liste'][yemek]['fiyat']
                print(f"\t\t\tMasa {masa_no}, toplam hesap ederi: {masa_hesap} TL ")
                kasa += masa_hesap
        else: # Masada tek bir müşteri varsa ödeme tipi seçimi yapılmayacak
            masa_hesap = 0
            for yemek_tipi in masalar[masa_no][1].keys():
                for yemek in masalar[masa_no][1][yemek_tipi]:
                    masa_hesap += menu[yemek_tipi]['liste'][yemek]['fiyat']
            print(f"\t\t\tMasa {masa_no}, toplam hesap ederi: {masa_hesap} TL")
            kasa += masa_hesap
        # hesap ödenen masayı boşalt
        masalar[masa_no] = dict()
    elif olay == "3":
        tum_masalar_bos = True
        for i in masalar.keys():
            if len(masalar[i]) > 0:
                tum_masalar_bos = False
                break
        if tum_masalar_bos:
            print(f"Bugün toplam {kasa} TL gelir elde edildi.")
            break
        else:
            print("günü bitirmek için tüm masalar boş olmalıdır.")
    else:
        print("Hatalı Seçim")




