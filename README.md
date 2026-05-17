
# Şifreleme Aracı - Tasarım Örüntüleri Ödevi

**Konu Seçimi:** E - Şifreleme Aracı  
**Gerekçe:** Algoritma seçimi constructor'da sabit, runtime değişemiyor. Creational, structural ve behavioral pattern'lerle esneklik sağlanacak.

## Proje ne yapar?
Basit metin şifreleme/çözme aracı. Farklı algoritmaları runtime değiştirebilir, olayları izleyebilir.

## Kullanılan örüntüler (tüm fazlar)
- **Factory Method** (Faz 1) - Algoritma nesnesi yaratma
- **Singleton** (Faz 1) - Logger tek nesne
- **Decorator** (Faz 2) - Sıkıştırma ekleme
- **Facade** (Faz 2) - Basit arayüz
- **Strategy** (Faz 3) - Runtime algoritma değişimi
- **Observer** (Faz 3) - Olay izleme

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