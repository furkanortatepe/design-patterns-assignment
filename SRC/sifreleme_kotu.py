class KotuSifreleme:
    def __init__(self, algoritma="basit"):
        self.algoritma = algoritma
    def sifrele(self, metin):
        if self.algoritma == "basit":
            return ''.join(chr(ord(c)+1) for c in metin)
        elif self.algoritma == "ters":
            return metin[::-1]
        else:
            raise ValueError("Bilinmeyen algoritma")
    def coz(self, sifreli):
        if self.algoritma == "basit":
            return ''.join(chr(ord(c)-1) for c in sifreli)
        elif self.algoritma == "ters":
            return sifreli[::-1]
