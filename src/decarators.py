from factory import Sifreleme

class SifrelemeDecorator(Sifreleme):
    def __init__(self, sifreleyici):
        self._sifreleyici = sifreleyici
    
    def sifrele(self, metin):
        return self._sifreleyici.sifrele(metin)
    
    def coz(self, sifreli):
        return self._sifreleyici.coz(sifreli)

class SikistirmaDecorator(SifrelemeDecorator):
    def sifrele(self, metin):
        sikistirilmis = self._sikistir(metin)
        return self._sifreleyici.sifrele(sikistirilmis)
    
    def coz(self, sifreli):
        cozulmus = self._sifreleyici.coz(sifreli)
        return self._ac(cozulmus)
    
    def _sikistir(self, metin):
        if not metin:
            return ""
        sonuc = ""
        say = 1
        for i in range(1, len(metin)):
            if metin[i] == metin[i-1]:
                say += 1
            else:
                sonuc += metin[i-1] + str(say)
                say = 1
        sonuc += metin[-1] + str(say)
        return sonuc
    
    def _ac(self, sikistirilmis):
        sonuc = ""
        i = 0
        while i < len(sikistirilmis):
            harf = sikistirilmis[i]
            i += 1
            say = ""
            while i < len(sikistirilmis) and sikistirilmis[i].isdigit():
                say += sikistirilmis[i]
                i += 1
            sonuc += harf * int(say)
        return sonuc
