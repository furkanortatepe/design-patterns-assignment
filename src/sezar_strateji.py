from strategy import SifrelemeStratejisi

class SezarStrateji(SifrelemeStratejisi):
    def __init__(self, kaydirma=3):
        self.kaydirma = kaydirma
    def sifrele(self, metin):
        return ''.join(chr(ord(c)+self.kaydirma) for c in metin)
    def coz(self, sifreli):
        return ''.join(chr(ord(c)-self.kaydirma) for c in sifreli)
