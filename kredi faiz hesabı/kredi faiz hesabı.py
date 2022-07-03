def print_duration(ay): # zaman hesaplama
    yıl = int(ay / 12)
    kalan_ay = ay % 12
    print("-> yıl:", yıl, "ay:", kalan_ay)


def print_money(para):
    para = round(para, 2)
    # para=round(para,1) şeklinde yazınca çıktının küsüratının en sağını aldı o yüzden böyle yazdım
    # örn çıktı:6.555557    para=round(para,1) diye yazınca 6.7 çıktıını verdi
    print(para)


def print_entry(kredi_tutarı, int_rate, ay): #kredi hesabı
    print("-" * 50)
    print_duration(ay)
    faız = float(round((kredi_tutarı / 100) * (int_rate / 12) * ay + kredi_tutarı))
    aylık_odeme = (faız / ay)
    print("Total payment:")
    print_money(faız)
    print("Month payment:")
    print_money(aylık_odeme)
    print("-" * 50)


def print_full_report(kredi_tutarı, int_rate, maks_yıl, maks_ay, yineleme): #bütün fonksiyonlarla birlikte kullanıcıdan alınan verilere göre genel hesap
    x = yineleme
    maks_sure = maks_yıl * 12 + maks_ay
    while yineleme <= maks_sure:
        ay = yineleme
        print_entry(kredı_tutarı, ınt_rate, ay)
        yineleme = yineleme + x


print("." * 50) #giriş kısmı
print(".*.*.*.*.*Welcome to Interest Calculator*.*.*.*.*.")
print("." * 50)
name = input("Please enter your name:")
kredı_tutarı = float(input("Loan amount(anapara):"))
ınt_rate = float(input("Interest rate (yıllık faiz oranı)"))
print("-> TIME LENGTH")
y = int(input("   Load term in years(en fazla yıl):"))
m = int(input("   Load term in months(en fazla ay):"))
ıı = int(input("   Iteration term in months(yineleme aralığı):"))
toplam_ay = (y * 12) + m 
while m > 11: #doğru input sorgulama (ay)
    print("Ay sayısı 11'den büyük olamaz lütfen tekrar girin")
    y = int(input("   Load term in years:"))
    m = int(input("   Load term in months:"))
    ıı = int(input("   Iteration term in months:"))

while toplam_ay % ıı != 0: #doğru input sorgulama (bölünebilirlik)
    print("Lütfen yineleme aralığını toplam süreyi tam bölebilen bir değer girin ")
    y = int(input("   Load term in years:"))
    m = int(input("   Load term in months:"))
    ıı = int(input("   Iteration term in months:"))

print("Report for", name)
print_full_report(kredı_tutarı, ınt_rate, y, m, ıı)