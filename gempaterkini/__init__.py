import requests
from bs4 import BeautifulSoup


def ekstrasi_data():
    """
    Tanggal : 19 April 2024
    Waktu : 14:22:55 WIB
    Magnituoda : 3.5
    Kedalaman : 6 km
    Lokasi : 2.93 LS - 119.40 BT
    Pusat gempa : berada di darat 8 km Tenggara Mamasa
    Dirasakan (Skala MMI): III Mamasa
    :return:
    """
    try:
        content = requests.get('https://bmkg.go.id/', headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        tnw = soup.find('span', {'class':'waktu'})
        tnw = tnw.text.split(', ') # membuat array dengan pemisah

        tanggal = tnw[0]
        waktu = tnw[1]

        ket = soup.find('div', {'class':'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        ket = ket.findChildren('li') # mencari children / turunan

        # variable standar
        i = 0
        magnitudo = None
        kedalaman = None
        koordinat = None
        lokasi = None
        skala = None

        for res in ket: #menampilkan semua children dalam bentuk list
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                skala = res.text
            i = i + 1

        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = koordinat
        hasil['lokasi'] = lokasi
        hasil['skala'] = skala
        return hasil
    else:
        return None

def tampilkan_data(result):
    if result is None:
        print('tidak bisa menemukan data yang dimaksud')
        return
    print('\nGempa terakhir berdasarkan BMKG\n')
    print(f"Tanggal : {result['tanggal']}")
    print(f"Waktu : {result['waktu']}")
    print(f"Magnitudo : {result['magnitudo']}")
    print(f"Kedalaman : {result['kedalaman']}")
    print(f"Koordinat : {result['koordinat']}")
    print(f"Lokasi : {result['lokasi']}")
    print(f"Skala : {result['skala']}")

# if __name__ == "__main__" :
#     print('ini adalah package')