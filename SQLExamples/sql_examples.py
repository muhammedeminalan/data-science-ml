import sqlite3  # Python'un yerleşik SQLite veritabanı kütüphanesi
import os       # Dosya işlemleri için işletim sistemi kütüphanesi


def create_dataBase():
    # Eğer students.db dosyası zaten varsa sil (temiz başlangıç)
    if os.path.exists("students.db"):
        os.remove("students.db")
    # Yeni bir SQLite veritabanı dosyası oluştur ve bağlantı kur
    conn = sqlite3.connect("students.db")
    # Veritabanı üzerinde SQL komutları çalıştırmak için cursor (imleç) oluştur
    cursor = conn.cursor()
    # Bağlantı ve cursor nesnesini geri döndür
    return conn, cursor

def create_table(cursor):
    # students tablosunu oluştur; DDL (Data Definition Language) komutu
    cursor.execute('''CREATE TABLE students
                      (
                      id INTEGER PRIMARY KEY,   -- benzersiz kimlik, otomatik artar
                       name VARCHAR NOT NULL,    -- isim alanı, boş bırakılamaz
                       age INTEGER,              -- yaş, tam sayı
                       email VARCHAR UNIQUE,     -- e-posta, tabloda tekrar edemez
                       city VARCHAR              -- şehir bilgisi
                       )''')
    # courses tablosunu oluştur; ikinci tablo tanımı
    cursor.execute('''CREATE TABLE courses
                      (
                      id INTEGER PRIMARY KEY,    -- benzersiz kimlik
                       courses_name VARCHAR NOT NULL, -- ders adı, zorunlu alan
                       age INTEGER,              -- yaş (ders süresi olabilir)
                       instructor TEXT,          -- eğitmen adı
                       credits INTEGER           -- kredi değeri
                       )''')


def insert_data(cursor):
    # Eklenecek öğrenci verilerini tuple listesi olarak tanımla
    students = [
        (1, "Alice", 20, "alice@gmail.com", "New York"),      # 1. öğrenci
        (2, "Bob", 22, "bob@gmail.com", "Los Angeles"),       # 2. öğrenci
        (3, "Charlie", 19, "charlie@gmail.com", "Chicago"),   # 3. öğrenci
        (4, "David", 21, "david@gmail.com", "Houston"),       # 4. öğrenci
        (5, "Eve", 20, "eve@gmail.com", "Phoenix"),           # 5. öğrenci
    ]
    # executemany: listedeki tüm kayıtları tek seferde tabloya ekler (CREATE)
    # ? işaretleri SQL injection'a karşı parametreli sorgu kullanımını sağlar
    cursor.executemany(
        "INSERT INTO students VALUES (?, ?, ?, ?, ?)", students
    )
    print("✅ Veriler eklendi.")  # Ekleme başarılı mesajı


def read_data(cursor):
    print("\n--- TÜM ÖĞRENCİLER (SELECT *) ---")
    # SELECT *: tablodaki tüm sütun ve satırları getirir (READ)
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()  # tüm sonuçları liste olarak döndürür
    for row in rows:          # her satırı döngüyle ekrana yazdır
        print(row)

    print("\n--- SADECE İSİM VE ŞEHİR (SELECT belirli sütun) ---")
    # SELECT col1, col2: sadece istenen sütunları getirir, gereksiz veri çekilmez
    cursor.execute("SELECT name, city FROM students")
    for row in cursor.fetchall():  # sonuçları tek tek yazdır
        print(row)

    print("\n--- YAŞI 20'DEN BÜYÜK ÖĞRENCİLER (WHERE) ---")
    # WHERE: koşula uyan satırları filtreler, age > 20 olan kayıtlar gelir
    cursor.execute("SELECT * FROM students WHERE age > 20")
    for row in cursor.fetchall():  # filtrelenmiş sonuçları yazdır
        print(row)

    print("\n--- YAŞA GÖRE SIRALI (ORDER BY) ---")
    # ORDER BY: sonuçları belirtilen sütuna göre sıralar (DESC = azalan, ASC = artan)
    cursor.execute("SELECT * FROM students ORDER BY age DESC")
    for row in cursor.fetchall():  # sıralı sonuçları yazdır
        print(row)

    print("\n--- SADECE İLK 3 KAYIT (LIMIT) ---")
    # LIMIT: dönen satır sayısını kısıtlar, büyük tablolarda performans için önemli
    cursor.execute("SELECT * FROM students LIMIT 3")
    for row in cursor.fetchall():  # sadece ilk 3 kaydı yazdır
        print(row)



def update_data(cursor):
    print("\n--- GÜNCELLEME (UPDATE) ---")
    # UPDATE ... SET ... WHERE: koşula uyan satırın belirtilen sütununu günceller
    # WHERE olmadan tüm satırlar güncellenir, dikkatli kullanılmalı!
    cursor.execute("UPDATE students SET city = 'San Francisco' WHERE name = 'Alice'")
    # rowcount: etkilenen (güncellenen) satır sayısını verir
    print(f"✅ Etkilenen satır: {cursor.rowcount}")
  


def delete_data(cursor):
    print("\n--- SİLME (DELETE) ---")
    # DELETE FROM ... WHERE: koşula uyan satırı tablodan kalıcı olarak siler
    # WHERE olmadan tüm tablo silinir, dikkatli kullanılmalı!
    cursor.execute("DELETE FROM students WHERE id = 5")
    # rowcount: silinen satır sayısını verir
    print(f"✅ Silinen satır: {cursor.rowcount}")


def aggregate_functions(cursor):
    print("\n--- AGGREGATE (TOPLU) FONKSİYONLAR ---")

    # COUNT(*): tablodaki toplam satır (kayıt) sayısını döndürür
    cursor.execute("SELECT COUNT(*) FROM students")
    print(f"Toplam öğrenci sayısı (COUNT): {cursor.fetchone()[0]}")

    # SUM(col): belirtilen sütunun tüm değerlerinin toplamını hesaplar
    cursor.execute("SELECT SUM(age) FROM students")
    print(f"Yaşların toplamı   (SUM)  : {cursor.fetchone()[0]}")

    # AVG(col): belirtilen sütunun aritmetik ortalamasını hesaplar
    cursor.execute("SELECT AVG(age) FROM students")
    print(f"Ortalama yaş       (AVG)  : {cursor.fetchone()[0]:.2f}")  # 2 ondalık basamak

    # MIN(col): belirtilen sütundaki en küçük değeri döndürür
    cursor.execute("SELECT MIN(age) FROM students")
    print(f"En küçük yaş       (MIN)  : {cursor.fetchone()[0]}")

    # MAX(col): belirtilen sütundaki en büyük değeri döndürür
    cursor.execute("SELECT MAX(age) FROM students")
    print(f"En büyük yaş       (MAX)  : {cursor.fetchone()[0]}")

    print("\n--- GROUP BY (şehre göre öğrenci sayısı) ---")
    # GROUP BY: aynı değere sahip satırları gruplar
    # COUNT(*) ile birlikte her şehirdeki öğrenci sayısını hesaplar
    cursor.execute("SELECT city, COUNT(*) as ogrenci_sayisi FROM students GROUP BY city")
    for row in cursor.fetchall():  # her şehir ve öğrenci sayısını yazdır
        print(f"  {row[0]}: {row[1]} öğrenci")

    print("\n--- HAVING (1'den fazla öğrencisi olan şehirler) ---")
    # HAVING: GROUP BY sonucuna filtre uygular
    # WHERE satır bazlı filtreler, HAVING ise grup bazlı filtreler
    cursor.execute(
        "SELECT city, COUNT(*) as sayi FROM students GROUP BY city HAVING sayi > 1"
    )
    rows = cursor.fetchall()
    # Sonuç varsa yazdır, yoksa bilgi mesajı göster
    print(rows if rows else "  Sonuç bulunamadı.")


def main():
    # Veritabanı ve cursor oluştur
    conn, cursor = create_dataBase()
    try:
        create_table(cursor)   # tabloları oluştur (DDL)
        conn.commit()          # değişiklikleri veritabanına kalıcı kaydet
        print("✅ Veritabanı oluşturuldu.")

        insert_data(cursor)    # CREATE - veri ekle
        conn.commit()          # ekleme işlemini kaydet

        read_data(cursor)      # READ - veri oku

        update_data(cursor)    # UPDATE - veri güncelle
        conn.commit()          # güncellemeyi kaydet

        delete_data(cursor)    # DELETE - veri sil
        conn.commit()          # silmeyi kaydet

        aggregate_functions(cursor)  # AGGREGATE - toplu hesaplamalar

    except sqlite3.Error as e:
        # Herhangi bir SQL hatası oluşursa yakala ve ekrana yazdır
        print(f"SQL ERROR: {e}")
    finally:
        # Hata olsa da olmasa da cursor ve bağlantıyı kapat (kaynak serbest bırak)
        cursor.close()
        conn.close()


# Bu dosya doğrudan çalıştırıldığında main() fonksiyonunu başlat
if __name__ == "__main__":
    main()
