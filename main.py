from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# 1. Mevcut açık olan Chrome'a bağlanma ayarları
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

try:
    # Tarayıcıya bağlan (Önce CMD'den Chrome'u hata ayıklama modunda açmış olmalısın)
    driver = webdriver.Chrome(options=chrome_options)
    
    print("Bağlantı başarılı! Veriler kurtarılıyor...")
    time.sleep(2)

    # 2. Sayfa Kaynağını Al ve BeautifulSoup ile İşle
    kaynak = driver.page_source
    corba = BeautifulSoup(kaynak, "html.parser")

    # Formdaki soruları ve seçenekleri temsil eden etiketleri buluyoruz
    metinler = corba.find_all(["div", "span", "p"])
    
    print("\n--- KURTARILAN FORM VERİLERİ ---\n")
    for metin in metinler:
        icerik = metin.get_text().strip()
        # Gereksiz kısa metinleri ve Google'ın sabit yazılarını eliyoruz
        if len(icerik) > 5 and "Seçimi temizle" not in icerik:
            print(f"- {icerik}")

except Exception as e:
    print(f"Hata oluştu: {e}")

finally:
    print("\nİşlem tamamlandı.")
