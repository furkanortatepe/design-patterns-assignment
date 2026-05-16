# Tasarım Örüntüleri - Şifreleme Aracı

## Faz 1 - Creational
- **Factory Method** (`src/factory.py`): Algoritma nesnelerini oluşturmak için.
- **Singleton** (`src/logger.py`): Loglama için tek nesne.

## Faz 2 - Structural
- **Decorator** (`src/decorators.py`): Şifrelemeye sıkıştırma eklemek için.
- **Facade** (`src/facade.py`): Karmaşık alt sistemi basit arayüzle kullanmak için.

## Faz 3 - Behavioral
- **Strategy** (`src/strategy.py`): Runtime algoritma değişimi.
- **Observer** (`src/observer.py`): Şifreleme olaylarını izleme.
- **OCP örneği**: `src/sezar_strategy.py` eklenirken mevcut kodlar değişmedi.
