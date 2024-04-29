import requests
from bs4 import BeautifulSoup

class bencana:

    def __init__(self, url, description):
    # init adalah tempat untuk menampung attribute (variable) yang dibutuhkan class
        self.description = description
        self.result = None
        self.url = url

    def ekstrasi_data(self):
        pass

    def tampilkan_data(self):
        pass

    def run(self):
        self.ekstrasi_data()
        self.tampilkan_data()

class infobanjir(bencana):
    def __init__(self, url):
        super(infobanjir, self).__init__(url, "ini adalah info terakhir banjir terkini")

class infogempa(bencana): # Parent nya adalah bencana
    def __init__(self, url):
        super(infogempa, self).__init__(url, "ini adalah info terakhir gempa terkini")

    def ekstrasi_data(self): # Semua method harus ada atribute self

        try:
            content = requests.get(self.url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
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

            for res in ket: # menampilkan semua children dalam bentuk list
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
            self.result =  hasil
        else:
            return None

    def tampilkan_data(self):
        if self.result is None:
            print('tidak bisa menemukan data yang dimaksud')
            return
        print('\nIni adalah aplikasi untuk update info bencana terakhir\n')
        print(f"Tanggal : {self.result['tanggal']}")
        print(f"Waktu : {self.result['waktu']}")
        print(f"Magnitudo : {self.result['magnitudo']}")
        print(f"Kedalaman : {self.result['kedalaman']}")
        print(f"Koordinat : {self.result['koordinat']}")
        print(f"Lokasi : {self.result['lokasi']}")
        print(f"Skala : {self.result['skala']}")

    # def run(self):
    #     self.ekstrasi_data()
    #     self.tampilkan_data()

# if __name__ == "__main__" :
#     print('ini adalah package')