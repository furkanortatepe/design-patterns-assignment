class Sifreleme:
    def sifrele(self, metin):
        pass
    def coz(self, sifreli):
        pass

class BasitSifreleme(Sifreleme):
    def sifrele(self, metin):
        sonuc = ""
        for harf in metin:
            sonuc += chr(ord(harf) + 1)
        return sonuc
    def coz(self, sifreli):
        sonuc = ""
        for harf in sifreli:
            sonuc += chr(ord(harf) - 1)
        return sonuc

class TersSifreleme(Sifreleme):
    def sifrele(self, metin):
        return metin[::-1]
    def coz(self, sifreli):
        return sifreli[::-1]

class SifrelemeFactory:
    @staticmethod
    def create(algoritma_tipi):
        if algoritma_tipi == "basit":
            return BasitSifreleme()
        elif algoritma_tipi == "ters":
            return TersSifreleme()
        else:
            raise ValueError("Bilinmeyen algoritma")
