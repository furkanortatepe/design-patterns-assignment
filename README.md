
**Konu Seçimi:** E - Şifreleme Aracı  
**Gerekçe:** Algoritma seçimi constructor'da sabit, runtime değişime kapalı. Çözüm için creational, structural ve behavioral pattern'ler uygulandı.

## Proje ne yapar?
Basit metin şifreleme/çözme aracı. Farklı algoritmaları runtime değiştirebilir, olayları izleyebilir.

## Kullandığım yazılım örüntüleri
- **Factory Method** (Faz 1) - Algoritma nesnesi yaratma
- **Singleton** (Faz 1) - Logger tek nesne
- **Decorator** (Faz 2) - Sıkıştırma ekleme
- **Facade** (Faz 2) - Basit arayüz
- **Strategy** (Faz 3) - Runtime algoritma değişimi
- **Observer** (Faz 3) - Olay izleme
- **OCP örneği** – `sezar_strategy.py` eklenirken mevcut kod değişmedi örneği kullanmış oldum

## Faz 2 - Structural Örüntüler
Bu fazda Decorator ve Facade uygulanmıştır.
- Decorator: Şifrelemeye sıkıştırma özelliği ekler.
- Facade: Karmaşık alt sistemi (Factory + Decorator) basit arayüzde toplar.
  

## Nasıl çalıştırılır?
```bash
cd src
python
>>> from facade import SifrelemeFacade
>>> f = SifrelemeFacade("basit", sikistir=True)
>>> f.sifrele("aaaabbb")
classDiagram
    class SifrelemeStratejisi {
        <<interface>>
        +sifrele(metin)
        +coz(sifreli)
    }
    class BasitStrateji
    class TersStrateji
    SifrelemeStratejisi <|.. BasitStrateji
    SifrelemeStratejisi <|.. TersStrateji
    class SifrelemeContext {
        -strateji
        +set_strateji()
        +sifrele()
    }
    SifrelemeContext o--> SifrelemeStratejisi
    class Konu {
        +ekle()
        +bildir()
    }
    class Observer {
        <<interface>>
        +update()
    }
    class SifrelemeIzleyici
    Observer <|.. SifrelemeIzleyici
    SifrelemeYoneticisi --|> Konu
