from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, olay, veri):
        pass

class Konu:
    def __init__(self):
        self._gozlemciler = []
    
    def ekle(self, gozlemci):
        self._gozlemciler.append(gozlemci)
    
    def cikar(self, gozlemci):
        self._gozlemciler.remove(gozlemci)
    
    def bildir(self, olay, veri):
        for gozlemci in self._gozlemciler:
            gozlemci.update(olay, veri)

class SifrelemeIzleyici(Observer):
    def update(self, olay, veri):
        if olay == "sifreleme_basladi":
            print(f"[IZLEYICI] Şifreleme başladı: {veri}")
        elif olay == "sifreleme_bitti":
            print(f"[IZLEYICI] Şifreleme bitti. Sonuç: {veri}")
