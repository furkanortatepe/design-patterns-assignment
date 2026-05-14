from abc import ABC, abstractmethod

class SifrelemeStratejisi(ABC):
    @abstractmethod
    def sifrele(self, metin):
        pass
    @abstractmethod
    def coz(self, sifreli):
        pass

class BasitStrateji(SifrelemeStratejisi):
    def sifrele(self, metin):
        return ''.join(chr(ord(c)+1) for c in metin)
    def coz(self, sifreli):
        return ''.join(chr(ord(c)-1) for c in sifreli)

class TersStrateji(SifrelemeStratejisi):
    def sifrele(self, metin):
        return metin[::-1]
    def coz(self, sifreli):
        return sifreli[::-1]

class SifrelemeContext:
    def __init__(self, strateji=None):
        self._strateji = strateji
    
    def set_strateji(self, strateji):
        self._strateji = strateji
    
    def sifrele(self, metin):
        if not self._strateji:
            raise ValueError("Strateji seçilmedi")
        return self._strateji.sifrele(metin)
    
    def coz(self, sifreli):
        if not self._strateji:
            raise ValueError("Strateji seçilmedi")
        return self._strateji.coz(sifreli)
