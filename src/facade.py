from factory import SifrelemeFactory
from decorators import SikistirmaDecorator

class SifrelemeFacade:
    def __init__(self, algoritma_tipi, sikistir=False):
        sifreleyici = SifrelemeFactory.create(algoritma_tipi)
        if sikistir:
            sifreleyici = SikistirmaDecorator(sifreleyici)
        self.sifreleyici = sifreleyici
    
    def sifrele(self, metin):
        return self.sifreleyici.sifrele(metin)
    
    def coz(self, sifreli):
        return self.sifreleyici.coz(sifreli)
