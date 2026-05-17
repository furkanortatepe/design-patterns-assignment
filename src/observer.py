from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, olay, veri): pass

class Konu:
    def __init__(self):
        self._gozlemciler = []
    def ekle(self, gozlemci):
        self._gozlemciler.append(gozlemci)
    def cikar(self, gozlemci):
        self._gozlemciler.remove(gozlemci)
    def bildir(self, olay, veri):
        for g in self._gozlemciler:
            g.update(olay, veri)

class SifrelemeIzleyici(Observer):
    def update(self, olay, veri):
        print(f"[IZLEYICI] {olay}: {veri}")
