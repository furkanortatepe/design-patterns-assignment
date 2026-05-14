from strategy import SifrelemeContext
from observer import Konu

class SifrelemeYoneticisi(Konu):
    def __init__(self, strateji):
        super().__init__()
        self.context = SifrelemeContext(strateji)
    
    def sifrele(self, metin):
        self.bildir("sifreleme_basladi", metin)
        sonuc = self.context.sifrele(metin)
        self.bildir("sifreleme_bitti", sonuc)
        return sonuc
    
    def set_strateji(self, strateji):
        self.context.set_strateji(strateji)
