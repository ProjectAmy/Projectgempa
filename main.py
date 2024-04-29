"""
ini adalah project pembuatan aplikasi gempa
"""
import gempaterkini

if __name__ == '__main__':

    gempaindo = gempaterkini.infogempa('http://bmkg.go.id')
    print("Deskripsi :", gempaindo.description)
    gempaindo.run()

    banjirindo = gempaterkini.infobanjir('http://bmkg.go.id')
    print("Deskripsi :", banjirindo.description)
    banjirindo.run()
