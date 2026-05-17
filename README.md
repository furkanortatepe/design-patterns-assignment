# Şifreleme Aracı - Tasarım Örüntüleri Ödevi

**Konu Seçimi:** E - Şifreleme Aracı  
**Gerekçe:** Algoritma seçimi constructor'da sabit, runtime değişemiyor. Creational, structural ve behavioral pattern'lerle esneklik sağlanacak.

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
