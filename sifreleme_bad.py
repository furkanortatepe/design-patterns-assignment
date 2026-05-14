class SifrelemeAraci:
    def __init__(self, algoritma):
        if algoritma == "basit":
            self.algoritma = "basit"
        elif algoritma == "ters":
            self.algoritma = "ters"
        else:
            self.algoritma = "basit"
    
    def sifrele(self, metin):
        if self.algoritma == "basit":
            sonuc = ""
            for harf in metin:
                sonuc += chr(ord(harf) + 1)
            return sonuc
        elif self.algoritma == "ters":
            return metin[::-1]
    
    def coz(self, sifreli):
        if self.algoritma == "basit":
            sonuc = ""
            for harf in sifreli:
                sonuc += chr(ord(harf) - 1)
            return sonuc
        elif self.algoritma == "ters":
            return sifreli[::-1]
