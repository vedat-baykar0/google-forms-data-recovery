from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# 1. Mevcut açık olan Chrome'a bağlanma ayarları
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

try:
    # Tarayıcıya bağlan
    driver = webdriver.Chrome(options=chrome_options)
    
    print("Bağlantı başarılı! Veriler kurtarılıyor...")
    time.sleep(2)

    # 2. Sayfa Kaynağını Al ve BeautifulSoup ile İşle
    kaynak = driver.page_source
    corba = BeautifulSoup(kaynak, "html.parser")
    metinler = corba.find_all(["div", "span", "p"])
    
    # DOSYA KAYDETME İŞLEMİ BAŞLIYOR
    # "recovered_data.txt" adında bir dosya oluşturup içine yazıyoruz
    with open("recovered_data.txt", "w", encoding="utf-8") as file:
        file.write("--- GOOGLE FORM KURTARILAN VERİLER ---\n\n")
        
        print("\n--- VERİLER İŞLENİYOR ---\n")
        for metin in metinler:
            icerik = metin.get_text().strip()
            
            if len(icerik) > 5 and "Seçimi temizle" not in icerik:
                # Hem ekrana yazdırıyoruz hem dosyaya kaydediyoruz
                print(f"- {icerik}")
                file.write(f"- {icerik}\n")

    print(f"\n[BAŞARILI] Tüm veriler 'recovered_data.txt' dosyasına kaydedildi.")

except Exception as e:
    print(f"Hata oluştu: {e}")

finally:
    print("İşlem tamamlandı.")
