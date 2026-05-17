# Problems - Faz 0 (Başlangıç Kodu)

1. Algoritma seçimi constructor'da sabit, runtime değişemez.
2. Yeni algoritma eklemek için if-else bloğunu değiştirmek gerekir (OCP ihlali).
3. Şifreleme ve çözme aynı sınıfta, tek sorumluluk değil.
4. Test edilmesi zor, algoritmalar birbirine bağımlı.
5. Nesne yaratma esnek değil, her seferinde tip kontrolü yapılıyor.

## AI'nın gördükleri (ChatGPT/Claude'ye sor ve yapıştır)
AI, Strategy ve Factory Method önerdi. Ayrıca if-else zincirinin OCP ihlali olduğunu söyledi.

## Karşılaştırma
Benim listemde 5 sorun vardı, AI ek olarak "test edilebilirlik" ve "bağımlılık" konularını vurguladı. Fark: AI Strategy önerdi, ben Factory Method tercih ettim çünkü daha basit.
