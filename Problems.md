# Şifreleme Aracı - Tasarım Örüntüleri Ödevi
**Konu Seçimi:** E - Şifreleme Aracı  
**Gerekçe:** Algoritma constructor'da sabit, runtime değişemez.


- Decorator ile sıkıştırma eklendi.
- Facade ile basit arayüz sağlandı.

## Çalıştırma
```bash
cd src
python -c "from facade import SifrelemeFacade; f=SifrelemeFacade('basit', sikistir=True); print(f.sifrele('aaa'))"
