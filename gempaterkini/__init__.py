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
        tnw = tnw.text.split(', ')

        tanggal = tnw[0]
        waktu = tnw[1]

        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = 3.5
        hasil['kedalaman'] = '6 km'
        hasil['lokasi'] = '2.93 LS - 119.40 BT'
        hasil['pusat'] = 'berada di darat 8 km Tenggara Mamasa'
        hasil['dirasakan'] = 'III Mamasa'
        return hasil
    else:
        return None

def tampilkan_data(result):
    if result is None:
        print('tidak bisa menemukan data yang dimaksud')
        return
    print('\nGempa terakhir berdasarkan BMKG')
    print(f"Tanggal : {result['tanggal']}")
    print(f"Waktu : {result['waktu']}")
    print(f"Magnitudo : {result['magnitudo']}")
    print(f"Kedalaman : {result['kedalaman']}")
    print(f"Lokasi : {result['lokasi']}")
    print(f"Pusat Gempa : {result['pusat']}")
    print(f"Dirasakan : {result['dirasakan']}")

# if __name__ == "__main__" :
#     print('ini adalah package')