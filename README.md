
* Algoritma seçimi constructor’da sabit, runtime değişime kapalı. Çözüm için creational, structural ve behavioral pattern’ler uygulandı.

Kullanılan Tasarım Örüntüleri
- **Factory Method (Creational)** – `factory.py`
- **Singleton (Creational)** – `logger.py`
- **Decorator (Structural)** – `decorators.py`
- **Facade (Structural)** – `facade.py`
- **Strategy (Behavioral)** – `strategy.py`
- **Observer (Behavioral)** – `observer.py`
- **OCP örneği** – `sezar_strategy.py` eklenirken mevcut kod değişmedi.

## Mimari Diyagram (basit Mermaid)
classDiagram
    class SifrelemeStratejisi {
        <<interface>>
        +sifrele(metin)
        +coz(sifreli)
    }
    BasitStrateji --|> SifrelemeStratejisi
    TersStrateji --|> SifrelemeStratejisi
    SifrelemeContext --> SifrelemeStratejisi
    Konu --> Observer
    SifrelemeIzleyici --|> Observer
    SifrelemeYoneticisi --|> Konu
