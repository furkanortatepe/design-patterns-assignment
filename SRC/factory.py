class Sifreleme:
    def sifrele(self, metin): raise NotImplementedError
    def coz(self, sifreli): raise NotImplementedError

class BasitSifreleme(Sifreleme):
    def sifrele(self, metin): return ''.join(chr(ord(c)+1) for c in metin)
    def coz(self, sifreli): return ''.join(chr(ord(c)-1) for c in sifreli)

class TersSifreleme(Sifreleme):
    def sifrele(self, metin): return metin[::-1]
    def coz(self, sifreli): return sifreli[::-1]

class SifrelemeFactory:
    @staticmethod
    def create(algoritma):
        if algoritma == "basit":
            return BasitSifreleme()
        elif algoritma == "ters":
            return TersSifreleme()
        else:
            raise ValueError(f"Bilinmeyen algoritma: {algoritma}")
