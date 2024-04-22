"""
ini adalah project pembuatan aplikasi gempa
"""
import gempaterkini

if __name__ == '__main__':
    print("aplikasi utama")
    result = gempaterkini.ekstrasi_data()
    gempaterkini.tampilkan_data(result)