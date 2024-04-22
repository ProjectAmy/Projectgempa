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

    content = requests.get('https://www.bmkg.go.id/')
    print(content.status_code)
    # soup = BeautifulSoup(content)
    # print(soup.prettify())

    hasil = dict()
    hasil['tanggal'] = '19 April 2024'
    hasil['waktu'] = '14:22:55 WIB'
    hasil['magnitudo'] = 3.5
    hasil['kedalaman'] = '6 km'
    hasil['lokasi'] = '2.93 LS - 119.40 BT'
    hasil['pusat'] = 'berada di darat 8 km Tenggara Mamasa'
    hasil['dirasakan'] = 'III Mamasa'
    return hasil


def tampilkan_data(result):
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