

## Faz 3 - Behavioral Örüntüler

### Strategy
- **Nerede:** `strategy.py` - `SifrelemeStratejisi`, `BasitStrateji`, `TersStrateji`, `SifrelemeContext`
- **Neden:** Şifreleme algoritmasını runtime’da değiştirebilmek için.
- **Kazanım:** Algoritmalar birbirinden bağımsız, yeni strateji eklemek kolay.

### Observer
- **Nerede:** `observer.py` - `Konu`, `SifrelemeIzleyici`
- **Neden:** Şifreleme başlangıcı ve bitişi gibi olayları izlemek için.
- **Kazanım:** Gelecekte dosyaya log yazma veya e-posta gönderme gibi yeni observer'lar eklenebilir.

### Açık/Kapalı Prensibi (OCP) Örneği
- `sezar_strategy.py` sınıfı eklenirken `strategy.py` veya başka hiçbir mevcut kod değişmedi.
- # AI Log - Faz 3

## Pair programming oturumu 
AI ile Strategy ve Observer pattern’lerini tartıştık. AI Strategy önerdi çünkü runtime algoritma değişimi gerekiyor. Observer ise olay izleme için uygun.

## AI olmadan ne kadar sürerdi?
Tahminen 8 saat. AI ile 4 saat.

## AI’ın yanılttığı noktalar
- AI observer yerine sadece Singleton log önerdi, ama ödevde 2 behavioral pattern istendiği için Observer ekledim.
- AI sıkıştırma için hazır kütüphane (zlib) önerdi, ancak ben basit run-length encoding yaptım.
- AI Facade'den bahsetmedi, ben Phase 2'de eklemiştim.
- 
