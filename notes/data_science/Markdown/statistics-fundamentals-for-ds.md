# Data Science Statistics Notes

## Table of Contents

- [1. Types of Statistics (İstatistik Türleri)](#1-types-of-statistics-i̇statistik-türleri)
- [2. Population and Sample (Popülasyon ve Örneklem)](#2-population-and-sample-popülasyon-ve-örneklem)
- [3. Measures of Central Tendency (Merkezi Eğilim Ölçüleri)](#3-measures-of-central-tendency-merkezi-eğilim-ölçüleri)
- [4. Measures of Spread / Dispersion (Yayılım Ölçüleri)](#4-measures-of-spread--dispersion-yayılım-ölçüleri)
- [5. Population vs Sample Variance (Popülasyon ve Örneklem Varyansı)](#5-population-vs-sample-variance-popülasyon-ve-örneklem-varyansı)
- [6. Variable Types (Değişken Tipleri)](#6-variable-types-değişken-tipleri)
- [Mini Summary Table (Mini Özet Tablo)](#mini-summary-table-mini-özet-tablo)
- [Symbol & Jargon Reference (Sembol ve Terim Kılavuzu)](#symbol--jargon-reference-sembol-ve-terim-kılavuzu)
- [Step-by-Step Worked Examples (Adım Adım Çözümlü Örnekler)](#step-by-step-worked-examples-adım-adım-çözümlü-örnekler)

---

## 1. Types of Statistics (İstatistik Türleri)

**1) Definition (Tanım)**  
Statistics (istatistik), veriyi toplama, düzenleme, özetleme ve yorumlama bilimidir. İki ana dalı vardır: **Descriptive (betimsel)** ve **Inferential (çıkarımsal)**.

**2) Why it matters in Data Science (Veri Biliminde Ne İşe Yarar?)**  
- **Descriptive Statistics (betimsel istatistik):** Veriyi ilk kez gördüğünde özetlemeni sağlar → EDA (Exploratory Data Analysis / Keşifsel Veri Analizi) aşamasında kullanılır.
- **Inferential Statistics (çıkarımsal istatistik):** Küçük bir sample (örneklem) ile büyük bir population (popülasyon) hakkında genelleme yapmanı sağlar → Model sonuçlarını yorumlarken kullanılır.
- Hangi analizi ne zaman kullanacağını bilmek, doğru model seçimi ve doğru yorum için şarttır.

**3) Key Concepts (Anahtar Kavramlar)**  
- **Descriptive Statistics (betimsel istatistik):** Veriyi sayılar ve grafiklerle ÖZETler. Genelleme yapmaz.
- **Inferential Statistics (çıkarımsal istatistik):** Sample (örneklem) verisinden population (popülasyon) hakkında ÇIKARIM yapar.

```
┌─────────────────────────────────────┐
│         STATISTICS (İstatistik)     │
├──────────────────┬──────────────────┤
│   Descriptive    │   Inferential    │
│   (Betimsel)     │   (Çıkarımsal)   │
│                  │                  │
│  → Özetler       │  → Geneller      │
│  → mean, median  │  → sample →      │
│  → tablolar      │    population    │
│  → grafikler     │    tahmini       │
└──────────────────┴──────────────────┘
```

**4) Formulas (Formüller)**  
Bu bölüm doğrudan formül içermez. Formüller ilerleyen konularda verilecektir.

**5) Mini Example (Mini Örnek)**  
Elimizde 1000 kullanıcının uygulama kullanım süresi var:

- **Descriptive:** "Ortalama kullanım süresi 23 dakika, en düşük 2, en yüksek 98 dakika." → Sadece bu veriyi özetliyorsun.
- **Inferential:** "Bu 1000 kişilik sample (örneklem), tüm Türkiye kullanıcılarını temsil eder. Tahmini ortalama kullanım ~23 dakikadır." → Genelleme yapıyorsun.

**6) Common Mistakes (En Sık Hata / Yanlış Yorum)**  
- Descriptive sonuçları genelleme gibi sunmak. "Ortalama 23 dk" demek, tüm kullanıcılar için geçerli değildir; sadece eldeki veri için geçerlidir.
- Inferential sonuçları kesin gerçek gibi söylemek. Çıkarım = tahmin; hata payı vardır.

> **Notebook Note (Deftere Not):** Descriptive = özetle, Inferential = genelle. İkisi aynı şey değildir.

---

## 2. Population and Sample (Popülasyon ve Örneklem)

**1) Definition (Tanım)**  
**Population (popülasyon):** İlgilendiğin konudaki TÜM bireylerin/verilerin kümesi.  
**Sample (örneklem):** Population'dan seçilen bir ALT küme.

**2) Why it matters in Data Science (Veri Biliminde Ne İşe Yarar?)**  
- Gerçek hayatta tüm population'a ulaşmak çoğunlukla imkansızdır (maliyet, zaman, erişim). Bu yüzden sample ile çalışırız.
- Model eğitirken kullandığın dataset (veri seti) aslında bir sample'dır. Modelin population'a genellenebilir olması gerekir.
- Sample'ın population'u temsil edip etmediğini anlamak, **bias (yanlılık)** riskini kontrol etmek demektir.

**3) Key Concepts (Anahtar Kavramlar)**  
- **Population (popülasyon):** N ile gösterilir. Tamamdır.
- **Sample (örneklem):** n ile gösterilir. Bir alt kümedir.
- **Parameter (parametre):** Population'dan hesaplanan değer (ör: μ — population mean (popülasyon ortalaması)).
- **Statistic (istatistik değeri):** Sample'dan hesaplanan değer (ör: x̄ — sample mean (örneklem ortalaması)).
- **Random Sampling (rastgele örnekleme):** Her bireyin eşit seçilme şansı olması.
- **Bias (yanlılık):** Sample'ın population'u doğru temsil etmemesi durumu.

```
┌──────────────────────────────────────┐
│       POPULATION (Popülasyon)        │
│              N = tümü                │
│    parametre: μ (gerçek değer)       │
│                                      │
│    ┌────────────────────┐            │
│    │  SAMPLE (Örneklem) │            │
│    │      n < N         │            │
│    │  statistic: x̄      │            │
│    │  (tahmin değeri)   │            │
│    └────────────────────┘            │
│                                      │
└──────────────────────────────────────┘
```

**4) Formulas (Formüller)**  
Doğrudan bu bölüme ait bir formül yok. Ancak iki sembol kritik:

| Sembol | Adı | Anlamı |
|--------|-----|--------|
| N | Population size (popülasyon büyüklüğü) | Tüm veri sayısı |
| n | Sample size (örneklem büyüklüğü) | Seçilen veri sayısı |
| μ | Population mean (popülasyon ortalaması) | Gerçek ortalama |
| x̄ | Sample mean (örneklem ortalaması) | Tahmini ortalama |

**5) Mini Example (Mini Örnek)**  
Türkiye'deki TÜM mobil uygulama kullanıcıları = **Population** (diyelim 60 milyon).  
Anket ile ulaştığın 2000 kullanıcı = **Sample**.

Bu 2000 kişinin ortalama ekran süresi x̄ = 4.2 saat ise, population ortalamasının da μ ≈ 4.2 saat civarında olduğunu **tahmin** edersin.

**6) Common Mistakes (En Sık Hata / Yanlış Yorum)**  
- Sample'ı küçük veya yanlı seçip sonucu tüm population'a genellemek (ör: sadece İstanbul'dan örneklem alıp "Türkiye ortalaması" demek).
- Sample size (örneklem büyüklüğü) ile population size (popülasyon büyüklüğü) arasındaki farkı karıştırmak.
- n ve N sembollerini birbirine karıştırmak: N = popülasyon, n = örneklem.

> **Notebook Note (Deftere Not):** Elindeki veri her zaman bir sample'dır. Gerçek μ değerini neredeyse hiç bilemezsin, x̄ ile tahmin edersin.

---

## 3. Measures of Central Tendency (Merkezi Eğilim Ölçüleri)

**1) Definition (Tanım)**  
Verinin "ortasını" veya "tipik değerini" tek bir sayıyla ifade etme yöntemleridir.  
Üç temel ölçü: **mean (aritmetik ortalama)**, **median (medyan / ortanca)**, **mode (mod / tepe değer)**.

**2) Why it matters in Data Science (Veri Biliminde Ne İşe Yarar?)**  
- EDA'da verinin genel eğilimini hızlıca anlamak için kullanılır.
- Outlier (aykırı değer) olup olmadığını anlamak: mean ile median arasındaki fark büyükse → outlier var demektir.
- Feature engineering (öznitelik mühendisliği) sırasında missing value (eksik veri) doldururken mean veya median kullanılır.

**3) Key Concepts (Anahtar Kavramlar)**  
- **Mean (aritmetik ortalama):** Tüm değerlerin toplamının, değer sayısına bölünmesi. Outlier'lara duyarlıdır.
- **Median (medyan / ortanca):** Veriler sıralandığında tam ortadaki değer. Outlier'lara dayanıklıdır.
- **Mode (mod / tepe değer):** En sık tekrar eden değer. Categorical (kategorik) veride de kullanılır.
- **Outlier (aykırı değer):** Diğer değerlerden çok farklı olan uç veri noktası.

**4) Formulas (Formüller)**

**Mean (Aritmetik Ortalama):**

```
x̄ = Σxᵢ / n
```

- `x̄` → sample mean (örneklem ortalaması)
- `Σxᵢ` → tüm değerlerin toplamı
- `n` → değer sayısı

**Median (Medyan):**

```
Veriyi küçükten büyüğe sırala.
  n tek ise  → ortadaki değer = x[(n+1)/2]
  n çift ise → ortadaki iki değerin ortalaması = (x[n/2] + x[n/2 + 1]) / 2
```

**Mode (Mod):**

```
En çok tekrar eden değer. Formül yok, saymaya dayalı.
```

**5) Mini Example (Mini Örnek)**  
Data (veri): `[2, 4, 4, 6, 9]` → n = 5

**Mean:**  
`x̄ = (2 + 4 + 4 + 6 + 9) / 5 = 25 / 5 = 5.0`

**Median:**  
Sıralı: `2, 4, 4, 6, 9` → n = 5 (tek) → ortadaki = 3. değer = **4**

**Mode:**  
4 iki kez geçiyor → mode = **4**

Şimdi outlier ekleyelim: `[2, 4, 4, 6, 100]`

- Mean = (2+4+4+6+100)/5 = 116/5 = **23.2** → aşırı yükseldi!
- Median = **4** → değişmedi.

→ Outlier varsa **median** daha güvenilirdir.

**6) Common Mistakes (En Sık Hata / Yanlış Yorum)**  
- Mean'i her zaman "en iyi özet" sanmak. Outlier varsa mean yanıltıcıdır.
- Median hesaplarken veriyi sıralamayı unutmak.
- Mode'un sadece categorical veri için olduğunu düşünmek; numerical (sayısal) veride de mode olabilir.

> **Notebook Note (Deftere Not):** Outlier şüphesi varsa mean ve median'ı yan yana koy. Fark büyükse → aykırı değer var.

---

## 4. Measures of Spread / Dispersion (Yayılım Ölçüleri)

**1) Definition (Tanım)**  
Verinin merkeze göre ne kadar "dağıldığını" ölçer. Central tendency (merkezi eğilim) tek başına yetmez; verinin yayılımı da bilinmelidir.

**2) Why it matters in Data Science (Veri Biliminde Ne İşe Yarar?)**  
- İki dataset'in mean'i aynı olabilir ama dağılımları çok farklı olabilir. Model buna göre farklı davranır.
- Feature scaling (öznitelik ölçekleme) yaparken standard deviation (standart sapma) kullanılır (ör: Standardization / Z-score normalization).
- Outlier detection (aykırı değer tespiti): IQR yöntemi ile outlier belirlenir.

**3) Key Concepts (Anahtar Kavramlar)**  
- **Range (açıklık):** max − min. En basit yayılım ölçüsü, ama outlier'a çok duyarlı.
- **IQR — Interquartile Range (çeyrekler arası açıklık):** Q3 − Q1. Verinin ortadaki %50'sinin yayılımı. Outlier tespitinde kullanılır.
- **Variance (varyans):** Her değerin mean'den farklarının karelerinin ortalaması. Yayılımın "karesini" ölçer.
- **Standard Deviation (standart sapma):** Variance'ın karekökü. Verinin orijinal birimi ile aynı birimde yayılımı gösterir.
- **Q1 (1. Quartile / 1. çeyrek):** Verinin alt %25'lik sınırı.
- **Q3 (3. Quartile / 3. çeyrek):** Verinin üst %75'lik sınırı.

```
Yayılım Ölçüleri (Basit → Gelişmiş):

Range          IQR            Variance         Std Dev
(Açıklık)    (Çeyrek Açık.)  (Varyans)        (Standart Sapma)
max - min     Q3 - Q1        Σ(xᵢ-x̄)²/n      √Variance
  ↓              ↓               ↓                ↓
En basit    Outlier'a        Birim kareli     Orijinal birimde
            dayanıklı
```

**4) Formulas (Formüller)**

**Range (Açıklık):**
```
Range = max(x) - min(x)
```

**IQR (Çeyrekler Arası Açıklık):**
```
IQR = Q3 - Q1

Outlier sınırı:
  Alt sınır = Q1 - 1.5 × IQR
  Üst sınır = Q3 + 1.5 × IQR
  → Bu sınırların dışındaki değerler outlier sayılır.
```

**Variance (Varyans) — Population (Popülasyon):**
```
σ² = Σ(xᵢ - μ)² / N
```
- `σ²` → population variance (popülasyon varyansı)
- `xᵢ` → her bir veri noktası
- `μ` → population mean (popülasyon ortalaması)
- `N` → population size (popülasyon büyüklüğü)

**Standard Deviation (Standart Sapma) — Population:**
```
σ = √σ² = √[Σ(xᵢ - μ)² / N]
```

**5) Mini Example (Mini Örnek)**  
Data: `[3, 5, 7, 8, 12]` → n = 5

**Range:**  
`12 - 3 = 9`

**Mean (önce hesapla):**  
`x̄ = (3+5+7+8+12)/5 = 35/5 = 7`

**Variance (population formülü ile):**
```
(3-7)² = 16
(5-7)² = 4
(7-7)² = 0
(8-7)² = 1
(12-7)² = 25
────────────
Toplam  = 46

σ² = 46 / 5 = 9.2
```

**Standard Deviation:**  
`σ = √9.2 ≈ 3.03`

**IQR (basitleştirilmiş):**  
Sıralı: `3, 5, 7, 8, 12`  
Q1 = 5 (alt yarının medyanı), Q3 = 8 (üst yarının medyanı) *(basit yöntem ile, n=5 için alt yarı: [3,5], üst yarı: [8,12])*  
Q1 = (3+5)/2 = 4, Q3 = (8+12)/2 = 10  
`IQR = 10 - 4 = 6`

Outlier sınırları:  
Alt = 4 − 1.5×6 = −5, Üst = 10 + 1.5×6 = 19  
→ Tüm veriler [−5, 19] arasında → **outlier yok**.

**6) Common Mistakes (En Sık Hata / Yanlış Yorum)**  
- Variance'ın birimini unutmak: eğer veri "dakika" ise variance "dakika²" birimindedir. Yorumlamak için standard deviation kullan.
- Range'i tek başına yeterli sanmak; tek bir outlier range'i dramatik şekilde büyütür.
- IQR hesaplarken Q1 ve Q3 değerlerini yanlış bulmak (veriyi sıralamayı unutmak).

> **Notebook Note (Deftere Not):** Yayılımı yorumlarken standard deviation kullan çünkü birimi veriyle aynıdır. Variance ara hesaptır.

---

## 5. Population vs Sample Variance (Popülasyon ve Örneklem Varyansı)

**1) Definition (Tanım)**  
Population variance (popülasyon varyansı) **N** ile bölerken, sample variance (örneklem varyansı) **n−1** ile böler.  
Bu düzeltmeye **Bessel's Correction (Bessel düzeltmesi)** denir.

**2) Why it matters in Data Science (Veri Biliminde Ne İşe Yarar?)**  
- Veri biliminde neredeyse her zaman sample ile çalışırsın. Bu yüzden variance hesabında n−1 kullanman gerekir.
- n ile bölersen variance'ı sistematik olarak KÜÇÜK hesaplarsın → model parametreleri yanlış olur.
- İstatistiksel modellerin çoğu (linear regression, t-test vb.) arka planda n−1 kullanır.

**3) Key Concepts (Anahtar Kavramlar)**  
- **Population Variance σ² (popülasyon varyansı):** Gerçek varyans. N ile böl.
- **Sample Variance s² (örneklem varyansı):** Tahmini varyans. n−1 ile böl.
- **Bessel's Correction (Bessel düzeltmesi):** n yerine n−1 kullanarak bias'ı (yanlılığı) düzeltme.
- **Degrees of Freedom (serbestlik derecesi):** n−1 değeri. Sample mean'i hesapladıktan sonra kaç değer "özgürce" değişebilir.
- **Unbiased Estimator (yansız tahmin edici):** n−1 ile elde edilen sample variance, population variance'ın yansız tahminidir.

**4) Formulas (Formüller)**

**Population Variance (Popülasyon Varyansı):**
```
σ² = Σ(xᵢ - μ)² / N
```

**Sample Variance (Örneklem Varyansı):**
```
s² = Σ(xᵢ - x̄)² / (n - 1)
```

- `s²` → sample variance (örneklem varyansı)
- `x̄` → sample mean (örneklem ortalaması)
- `n - 1` → degrees of freedom (serbestlik derecesi) = Bessel's Correction

**Neden n−1?**
```
Sample mean (x̄) hesaplandıktan sonra, n değerden
sadece (n-1) tanesi bağımsız kalır.
Son değer = x̄'ı tutturmak için zorunlu olarak belirlenir.

Örnek: 3 sayının ortalaması 10 ise ve ilk iki sayı 8, 12 ise
→ üçüncü sayı ZORUNLU olarak 10'dur. Özgür değil.
→ Serbestlik derecesi = 3 - 1 = 2
```

**5) Mini Example (Mini Örnek)**  
Data (sample): `[4, 8, 6, 2, 10]` → n = 5

**Step 1:** x̄ = (4+8+6+2+10)/5 = 30/5 = 6

**Step 2:** Farkların kareleri:
```
(4-6)² = 4
(8-6)² = 4
(6-6)² = 0
(2-6)² = 16
(10-6)² = 16
──────────
Toplam  = 40
```

**Population variance (N ile):**  
`σ² = 40 / 5 = 8.0`

**Sample variance (n−1 ile):**  
`s² = 40 / 4 = 10.0`

→ Farka dikkat: s² > σ². Sample variance daha büyüktür çünkü küçük örneklemden gelen belirsizliği telafi eder.

**6) Common Mistakes (En Sık Hata / Yanlış Yorum)**  
- Sample variance hesaplarken n ile bölmek (Bessel's Correction'ı unutmak).
- "n−1 her zaman daha doğrudur" demek: eğer elinde gerçekten tüm population varsa N ile bölersin.
- Degrees of freedom kavramını sadece formül olarak ezberleyip mantığını anlamamak.

> **Notebook Note (Deftere Not):** Sample ile çalışıyorsan → n−1. Population ile çalışıyorsan (nadirdir) → N. Şüpheye düşersen n−1 kullan.

---

## 6. Variable Types (Değişken Tipleri)

**1) Definition (Tanım)**  
Değişkenler (variables), verideki her bir sütunun tipini tanımlar. Tip bilmek, hangi istatistiksel yöntemi veya modeli kullanacağını belirler.

**2) Why it matters in Data Science (Veri Biliminde Ne İşe Yarar?)**  
- Yanlış variable type seçimi → yanlış model, yanlış metric, yanlış sonuç.
- Categorical (kategorik) veriyi modele vermeden önce encoding (kodlama) gerekir (ör: one-hot encoding).
- Continuous (sürekli) ve discrete (kesikli) ayrımı, hangi distribution (dağılım) ve hangi istatistiksel testi kullanacağını belirler.

**3) Key Concepts (Anahtar Kavramlar)**

```
                    VARIABLE TYPES (Değişken Tipleri)
               ─────────────────────────────────────────
                  │                               │
            Categorical                       Numerical
            (Kategorik)                       (Sayısal)
            ─────────────                     ──────────────
            │           │                     │            │
        Nominal     Ordinal              Discrete     Continuous
        (İsimsel)   (Sıralı)            (Kesikli)     (Sürekli)
```

- **Categorical (kategorik):** Gruplara/etiketlere ayrılan veri. Matematiksel işlem yapılamaz.
  - **Nominal (isimsel/adsal):** Sıralama YOK. Ör: renk (kırmızı, mavi), şehir (İstanbul, Ankara), kan grubu.
  - **Ordinal (sıralı):** Doğal sıralama VAR ama aradaki fark ölçülemez. Ör: eğitim seviyesi (lise < lisans < yüksek lisans), müşteri memnuniyeti (düşük < orta < yüksek).

- **Numerical (sayısal):** Matematiksel işlem yapılabilir.
  - **Discrete (kesikli):** Sayılabilen, tam sayı değerler. Ör: bir uygulamadaki tıklama sayısı (0, 1, 2, 3…), oda sayısı.
  - **Continuous (sürekli):** Ölçülebilen, sonsuz ara değer alabilen. Ör: sıcaklık (36.6°C), kullanım süresi (4.73 dakika), ağırlık.

**4) Formulas (Formüller)**  
Bu bölümde formül yoktur. Ayrım mantıksal/kavramsal bir sınıflandırmadır.

**Karar Tablosu:**

| Soru | Evet → | Hayır → |
|------|--------|---------|
| Matematiksel işlem yapılabilir mi? | Numerical (sayısal) | Categorical (kategorik) |
| Kategoriler arasında sıra var mı? | Ordinal (sıralı) | Nominal (isimsel) |
| Değer arada her değeri alabilir mi? | Continuous (sürekli) | Discrete (kesikli) |

**5) Mini Example (Mini Örnek)**

Bir mobil uygulama veri setindeki sütunlar:

| Sütun | Değer Örneği | Tip |
|-------|-------------|-----|
| Uygulama adı | "Instagram" | Nominal (kategorik) |
| Kullanıcı puanı (1-5 yıldız) | 4 | Ordinal (kategorik) |
| İndirme sayısı | 50000 | Discrete (sayısal) |
| Uygulama boyutu (MB) | 148.7 | Continuous (sayısal) |
| Kategori | "Sosyal Medya" | Nominal (kategorik) |
| Günlük kullanım süresi (dk) | 42.3 | Continuous (sayısal) |

**6) Common Mistakes (En Sık Hata / Yanlış Yorum)**  
- Ordinal veriyi continuous gibi işlemek. "Memnuniyet: 1, 2, 3" diye yazılması onu sayısal yapmaz; aradaki fark eşit değildir.
- Zip code (posta kodu), telefon numarası gibi sayılarla yazılan ama aslında **nominal** olan verileri numerical sanmak.
- Discrete ve continuous ayrımını önemsememek; bu ayrım doğru istatistiksel test ve dağılım seçimi için kritiktir.

> **Notebook Note (Deftere Not):** Her sütunu modele vermeden önce tipini belirle. Sayı gibi görünen her şey numerical değildir (ör: posta kodu).

---

## Mini Summary Table (Mini Özet Tablo)

| Topic (Konu) | When to use? (Ne zaman kullanırım?) | 1 Critical Formula/Rule (1 Kritik Formül/Kural) | 1 Common Mistake (1 Sık Hata) |
|---|---|---|---|
| **Types of Statistics** (İstatistik Türleri) | Analizin amacını belirlerken: özetlemek mi, genellemek mi? | Descriptive = özetler, Inferential = geneller | Descriptive sonucu genelleme gibi sunmak |
| **Population & Sample** (Popülasyon & Örneklem) | Veri toplarken ve sonuçları yorumlarken | N = popülasyon, n = örneklem, μ vs x̄ | Küçük/yanlı sample ile genelleme yapmak |
| **Central Tendency** (Merkezi Eğilim) | Verinin "tipik değerini" tek sayıyla özetlerken | x̄ = Σxᵢ / n | Outlier varken mean'e güvenmek |
| **Spread / Dispersion** (Yayılım) | Verinin ne kadar dağıldığını ölçerken | σ = √[Σ(xᵢ−μ)² / N] | Variance'ın birimini (kare) unutmak |
| **Pop. vs Sample Variance** (Pop. vs Örneklem Varyansı) | Sample ile variance hesaplarken | s² = Σ(xᵢ−x̄)² / (n−1) → Bessel's | Sample variance'ta n ile bölmek |
| **Variable Types** (Değişken Tipleri) | Her sütunun tipini belirlerken (EDA başında) | Sayı gibi görünen her şey numerical değildir | Ordinal veriyi continuous gibi işlemek |

---

## Symbol & Jargon Reference (Sembol ve Terim Kılavuzu)

Bu bölümde, döküman boyunca geçen **tüm** semboller, formül notasyonları ve istatistik terimleri eksiksiz olarak listelenmiştir.

### A) Mathematical Symbols (Matematiksel Semboller)

| Sembol | Okunuşu | Anlamı (Türkçe) | Kullanıldığı Yer |
|--------|---------|------------------|-------------------|
| x̄ | x-bar | Sample mean (örneklem ortalaması) | Central Tendency, Variance |
| μ | mu (mü) | Population mean (popülasyon ortalaması) | Population & Sample, Variance |
| σ | sigma (küçük) | Population standard deviation (popülasyon standart sapması) | Spread / Dispersion |
| σ² | sigma-kare | Population variance (popülasyon varyansı) | Spread, Pop. vs Sample Variance |
| s | s | Sample standard deviation (örneklem standart sapması) | Sample Variance |
| s² | s-kare | Sample variance (örneklem varyansı) | Pop. vs Sample Variance |
| Σ | sigma (büyük) | Toplam (summation) — tüm değerleri topla | Mean, Variance formülleri |
| xᵢ | x-i | i. veri noktası (her bir değer) | Tüm formüllerde |
| N | büyük N | Population size (popülasyon büyüklüğü — tüm veri sayısı) | Population Variance |
| n | küçük n | Sample size (örneklem büyüklüğü — seçilen veri sayısı) | Sample Mean, Sample Variance |
| n−1 | n eksi 1 | Degrees of freedom (serbestlik derecesi) — Bessel's Correction | Sample Variance |
| √ | karekök | Square root (karekök) | Standard Deviation |
| Q1 | Q-bir | 1st Quartile (1. çeyrek — alt %25 sınırı) | IQR, Outlier tespiti |
| Q3 | Q-üç | 3rd Quartile (3. çeyrek — üst %75 sınırı) | IQR, Outlier tespiti |

### B) Formula Notation (Formül Notasyonları)

| Notasyon | Ne Anlama Gelir |
|----------|-----------------|
| `Σxᵢ` | Tüm x değerlerini topla: x₁ + x₂ + ... + xₙ |
| `Σ(xᵢ − x̄)²` | Her değerin mean'den farkını al, karele, hepsini topla |
| `Σ(xᵢ − μ)²` | Yukarıdakinin aynısı, ama population mean (μ) ile |
| `Σ(xᵢ − x̄)² / (n−1)` | Sample variance formülünün tamamı |
| `Σ(xᵢ − μ)² / N` | Population variance formülünün tamamı |
| `√[Σ(xᵢ − μ)² / N]` | Population standard deviation — variance'ın karekökü |
| `Q3 − Q1` | IQR (çeyrekler arası açıklık) |
| `Q1 − 1.5 × IQR` | Outlier alt sınırı |
| `Q3 + 1.5 × IQR` | Outlier üst sınırı |
| `max(x) − min(x)` | Range (açıklık) — en büyük eksi en küçük |

### C) Key Terms Glossary (Temel Terimler Sözlüğü)

| English Term | Türkçe Karşılığı | Kısa Açıklama |
|---|---|---|
| Statistics | İstatistik | Veriyi toplama, özetleme ve yorumlama bilimi |
| Descriptive Statistics | Betimsel istatistik | Veriyi özetler, genelleme yapmaz |
| Inferential Statistics | Çıkarımsal istatistik | Sample'dan population hakkında çıkarım yapar |
| Population | Popülasyon | İlgilenilen TÜM bireylerin/verilerin kümesi |
| Sample | Örneklem | Population'dan seçilen alt küme |
| Parameter | Parametre | Population'dan hesaplanan değer (ör: μ) |
| Statistic | İstatistik değeri | Sample'dan hesaplanan değer (ör: x̄) |
| Random Sampling | Rastgele örnekleme | Her bireyin eşit seçilme şansının olması |
| Bias | Yanlılık | Sample'ın population'u doğru temsil etmemesi |
| Mean | Aritmetik ortalama | Tüm değerlerin toplamı / değer sayısı |
| Median | Medyan / Ortanca | Sıralı verinin tam ortasındaki değer |
| Mode | Mod / Tepe değer | En sık tekrar eden değer |
| Outlier | Aykırı değer | Diğer değerlerden çok uzak olan uç nokta |
| Range | Açıklık | max − min |
| IQR (Interquartile Range) | Çeyrekler arası açıklık | Q3 − Q1, verinin ortadaki %50'sinin yayılımı |
| Quartile | Çeyrek | Veriyi %25'lik dilimlere bölen değerler |
| Variance | Varyans | Mean'den farkların karelerinin ortalaması |
| Standard Deviation | Standart sapma | Variance'ın karekökü, orijinal birimde yayılım |
| Bessel's Correction | Bessel düzeltmesi | Sample variance'ta n yerine n−1 ile bölme |
| Degrees of Freedom | Serbestlik derecesi | n−1; bağımsız hareket edebilen değer sayısı |
| Unbiased Estimator | Yansız tahmin edici | Population parametresini yanlılık olmadan tahmin eden istatistik |
| Categorical | Kategorik | Gruplara/etiketlere ayrılan değişken tipi |
| Numerical | Sayısal | Matematiksel işlem yapılabilen değişken tipi |
| Nominal | İsimsel / Adsal | Sıralaması olmayan kategorik veri (ör: renk, şehir) |
| Ordinal | Sıralı | Doğal sıralaması olan kategorik veri (ör: düşük < orta < yüksek) |
| Discrete | Kesikli | Sayılabilen, tam sayı değerler (ör: tıklama sayısı) |
| Continuous | Sürekli | Sonsuz ara değer alabilen ölçüm (ör: sıcaklık, süre) |
| Variable | Değişken | Verideki her bir sütun / özellik |
| Dataset | Veri seti | Analiz için toplanan verilerin bütünü |
| EDA (Exploratory Data Analysis) | Keşifsel veri analizi | Veriyi ilk kez inceleyip özetleme aşaması |
| Feature Engineering | Öznitelik mühendisliği | Model için yeni değişkenler türetme süreci |
| Missing Value | Eksik veri | Veri setinde boş olan hücre/değer |
| Encoding | Kodlama | Kategorik veriyi sayısal forma çevirme (ör: one-hot) |
| Feature Scaling | Öznitelik ölçekleme | Değişkenleri aynı ölçeğe getirme (ör: standardization) |
| Standardization (Z-score) | Standartlaştırma | Veriyi mean=0, std=1 olacak şekilde dönüştürme |
| Distribution | Dağılım | Verinin nasıl yayıldığını gösteren yapı |
| Metric | Metrik / Ölçüt | Performansı veya sonucu ölçen sayısal değer |

### D) Population vs Sample — Symbol Comparison (Sembol Karşılaştırma)

| Ölçü | Population (Popülasyon) | Sample (Örneklem) |
|------|------------------------|-------------------|
| Büyüklük | N | n |
| Mean (Ortalama) | μ (mu) | x̄ (x-bar) |
| Variance (Varyans) | σ² (sigma-kare), N ile böl | s² (s-kare), n−1 ile böl |
| Std Deviation (Standart Sapma) | σ (sigma) | s |
| Nitelik | Parameter (parametre) — gerçek değer | Statistic (istatistik değeri) — tahmin |

> **Notebook Note (Deftere Not):** Bu tabloyu defterin ilk veya son sayfasına yaz. Formül çözerken hangi sembolün ne olduğunu unutursan buraya bak.

---

---

## Step-by-Step Worked Examples (Adım Adım Çözümlü Örnekler)

Bu bölümde tek bir dataset (veri seti) üzerinden **tüm formüller** sırasıyla uygulanır. Her adım açıkça gösterilir.

### Senaryo

Bir mobil uygulamanın 8 kullanıcısının **günlük ekran süresi (dakika)** ölçülmüş:

```
Data (veri): [12, 25, 18, 30, 22, 15, 28, 50]
n = 8 (bu bir sample / örneklem)
```

> Bu 8 kişi tüm kullanıcıları temsil etmiyor → **sample** ile çalışıyoruz.

---

### Step 1: Variable Type (Değişken Tipini Belirle)

```
Soru: "Günlük ekran süresi (dakika)" ne tip bir değişken?

→ Matematiksel işlem yapılabilir mi?  EVET → Numerical (sayısal)
→ Arada her değeri alabilir mi?       EVET → Continuous (sürekli)
  (22.5 dk, 18.73 dk gibi değerler mümkün)

Sonuç: Continuous Numerical Variable (sürekli sayısal değişken)
```

---

### Step 2: Mean (Aritmetik Ortalama)

**Formül:** `x̄ = Σxᵢ / n`

```
Adım 2a — Tüm değerleri topla (Σxᵢ):
  12 + 25 + 18 + 30 + 22 + 15 + 28 + 50 = 200

Adım 2b — Değer sayısına böl (n):
  x̄ = 200 / 8

Adım 2c — Sonuç:
  x̄ = 25.0 dakika
```

> **Yorum:** Kullanıcılar ortalama günde 25 dakika harcıyor. Ama 50 değeri şüpheli görünüyor (outlier olabilir).

---

### Step 3: Median (Medyan / Ortanca)

**Kural:** Veriyi küçükten büyüğe sırala → ortadaki değeri bul.

```
Adım 3a — Sırala:
  [12, 15, 18, 22, 25, 28, 30, 50]

Adım 3b — n tek mi çift mi?
  n = 8 → ÇİFT

Adım 3c — Ortadaki iki değeri bul:
  Pozisyonlar: n/2 = 4. değer, n/2+1 = 5. değer
  4. değer = 22
  5. değer = 25

Adım 3d — İkisinin ortalamasını al:
  Median = (22 + 25) / 2

Adım 3e — Sonuç:
  Median = 23.5 dakika
```

> **Yorum:** Mean = 25.0, Median = 23.5. Fark var ama dramatik değil. 50 değeri mean'i biraz yukarı çekmiş.

---

### Step 4: Mode (Mod / Tepe Değer)

**Kural:** En çok tekrar eden değer.

```
Adım 4a — Her değerin tekrar sayısını say:
  12 → 1 kez
  15 → 1 kez
  18 → 1 kez
  22 → 1 kez
  25 → 1 kez
  28 → 1 kez
  30 → 1 kez
  50 → 1 kez

Adım 4b — Sonuç:
  Hiçbir değer birden fazla tekrar etmiyor.
  → Mode YOK (no mode).
```

> **Yorum:** Continuous (sürekli) verilerde mode genellikle olmaz veya anlamsızdır. Mode daha çok categorical veride işe yarar.

---

### Step 5: Range (Açıklık)

**Formül:** `Range = max(x) − min(x)`

```
Adım 5a — En büyük ve en küçük değeri bul:
  max = 50
  min = 12

Adım 5b — Çıkar:
  Range = 50 − 12

Adım 5c — Sonuç:
  Range = 38 dakika
```

> **Yorum:** Veri 38 dakikalık bir aralığa yayılmış. Ama range tek bir uç değere çok duyarlı (50 olmasaydı range = 30 − 12 = 18 olurdu).

---

### Step 6: IQR (Çeyrekler Arası Açıklık) ve Outlier Tespiti

**Formül:** `IQR = Q3 − Q1`

```
Sıralı veri: [12, 15, 18, 22, 25, 28, 30, 50]
                ─────────────  ─────────────
                  Alt yarı        Üst yarı

Adım 6a — Veriyi ikiye böl (n=8, çift):
  Alt yarı: [12, 15, 18, 22]
  Üst yarı: [25, 28, 30, 50]

Adım 6b — Q1 = Alt yarının medyanı:
  Alt yarı: [12, 15, 18, 22] → ortadaki iki: 15, 18
  Q1 = (15 + 18) / 2 = 16.5

Adım 6c — Q3 = Üst yarının medyanı:
  Üst yarı: [25, 28, 30, 50] → ortadaki iki: 28, 30
  Q3 = (28 + 30) / 2 = 29.0

Adım 6d — IQR hesapla:
  IQR = Q3 − Q1 = 29.0 − 16.5 = 12.5

Adım 6e — Outlier sınırlarını hesapla:
  Alt sınır = Q1 − 1.5 × IQR = 16.5 − 1.5 × 12.5 = 16.5 − 18.75 = −2.25
  Üst sınır = Q3 + 1.5 × IQR = 29.0 + 1.5 × 12.5 = 29.0 + 18.75 = 47.75

Adım 6f — Outlier kontrolü:
  Sınırlar: [−2.25, 47.75]
  Veri:     [12, 15, 18, 22, 25, 28, 30, 50]
                                           ^^
  50 > 47.75 → 50 bir OUTLIER!
```

> **Yorum:** IQR yöntemi ile 50 dakika outlier olarak tespit edildi. Bu kullanıcı diğerlerinden çok farklı davranıyor.

---

### Step 7: Sample Variance (Örneklem Varyansı)

**Formül:** `s² = Σ(xᵢ − x̄)² / (n − 1)`

> **DİKKAT:** Sample ile çalışıyoruz → **n−1** kullanıyoruz (Bessel's Correction).

```
x̄ = 25.0 (Step 2'den)

Adım 7a — Her değerin mean'den farkını al (xᵢ − x̄):
  12 − 25 = −13
  25 − 25 =   0
  18 − 25 =  −7
  30 − 25 =   5
  22 − 25 =  −3
  15 − 25 = −10
  28 − 25 =   3
  50 − 25 =  25

Adım 7b — Farkları karele (xᵢ − x̄)²:
  (−13)² = 169
  (  0)² =   0
  ( −7)² =  49
  (  5)² =  25
  ( −3)² =   9
  (−10)² = 100
  (  3)² =   9
  ( 25)² = 625
           ────
  Toplam  = 986

Adım 7c — (n − 1) ile böl:
  s² = 986 / (8 − 1) = 986 / 7

Adım 7d — Sonuç:
  s² = 140.86 dakika²
```

> **Yorum:** Birim "dakika²" — doğrudan yorumlamak zor. Bu yüzden standard deviation'a ihtiyacımız var.

**Karşılaştırma — Eğer n ile bölseydik (yanlış):**
```
σ² = 986 / 8 = 123.25 dakika²

Fark: 140.86 vs 123.25
→ n ile bölmek varyansı küçük gösterir (underestimate).
→ Sample ile çalışırken HER ZAMAN n−1 kullan.
```

---

### Step 8: Sample Standard Deviation (Örneklem Standart Sapması)

**Formül:** `s = √s²`

```
Adım 8a — Variance'ın karekökünü al:
  s = √140.86

Adım 8b — Sonuç:
  s ≈ 11.87 dakika
```

> **Yorum:** Kullanıcılar ortalama 25 dakika harcıyor ve tipik sapma ±11.87 dakika. Yani çoğu kullanıcı kabaca 13–37 dakika arasında (x̄ ± s).

---

### Step 8 Sonrası: Tüm Sonuçların Özeti

```
┌──────────────────────────────────────────────────┐
│  DATA: [12, 25, 18, 30, 22, 15, 28, 50]  n = 8   │
├──────────────────────────────────────────────────┤
│  Variable Type  : Continuous Numerical           │
│  Mean (x̄)       : 25.0 dk                        │
│  Median         : 23.5 dk                        │
│  Mode           : Yok (no mode)                  │
│  Range          : 38 dk                          │
│  Q1             : 16.5                           │
│  Q3             : 29.0                           │
│  IQR            : 12.5                           │
│  Outlier(s)     : 50 (üst sınır 47.75'i aşıyor)  │
│  Variance (s²)  : 140.86 dk²                     │
│  Std Dev (s)    : 11.87 dk                       │
├──────────────────────────────────────────────────┤
│  Mean > Median → veri sağa çarpık (right-skewed) │
│  → Outlier (50) mean'i yukarı çekmiş             │
│  → Bu durumda median daha güvenilir              │
└──────────────────────────────────────────────────┘
```

---

### Bonus: Outlier Çıkarılınca Ne Olur?

Outlier olan 50'yi çıkarıp aynı hesapları tekrar yapalım:

```
Yeni data: [12, 15, 18, 22, 25, 28, 30]  n = 7

Mean  = (12+15+18+22+25+28+30) / 7 = 150 / 7 ≈ 21.43 dk
Median = 22 dk (sıralı verinin ortası, 4. değer)
Range  = 30 − 12 = 18 dk

Variance:
  Farkların kareleri toplamı:
  (12−21.43)² = 88.92
  (15−21.43)² = 41.34
  (18−21.43)² = 11.76
  (22−21.43)² =  0.33
  (25−21.43)² = 12.74
  (28−21.43)² = 43.16
  (30−21.43)² = 73.39
  Toplam = 271.64

  s² = 271.64 / (7−1) = 271.64 / 6 = 45.27 dk²
  s  = √45.27 ≈ 6.73 dk
```

**Karşılaştırma tablosu:**

```
┌──────────────┬──────────────────┬──────────────────┐
│   Ölçü       │  Outlier DAHİL   │  Outlier HARİÇ   │
│              │  n=8             │  n=7             │
├──────────────┼──────────────────┼──────────────────┤
│  Mean        │  25.00 dk        │  21.43 dk        │
│  Median      │  23.50 dk        │  22.00 dk        │
│  Range       │  38 dk           │  18 dk           │
│  Variance    │  140.86 dk²      │  45.27 dk²       │
│  Std Dev     │  11.87 dk        │  6.73 dk         │
└──────────────┴──────────────────┴──────────────────┘

→ Mean:     25.00 → 21.43  (3.57 dk düştü → %14 fark)
→ Median:   23.50 → 22.00  (1.50 dk düştü → %6 fark)
→ Std Dev:  11.87 → 6.73   (neredeyse yarıya indi!)

SONUÇ: Tek bir outlier mean'i ve std dev'i dramatik etkiler.
        Median ise neredeyse yerinde kaldı → outlier'a dayanıklı.
```
