from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

import time

# === KONFIGURASI AKUN ===
USERNAME = "isi nim"
PASSWORD = "isi password"

# === SETUP DRIVER ===
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

# === 1. BUKA BERANDA ===
driver.get("https://kuesioner.itenas.ac.id")

# === 2. KLIK TOMBOL MAHASISWA ===
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Mahasiswa')]"))).click()

# === 3. LOGIN ===
wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys(USERNAME)
driver.find_element(By.ID, "password").send_keys(PASSWORD)
driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()


# === GERAKAN TAMBAHAN ===
time.sleep(10)  # Untuk memilih kuesioner UTS / UAS


# === 4. KLIK TOMBOL MULAI & PINDAH TAB ===
wait.until(EC.element_to_be_clickable((By.ID, "btn-start"))).click()
time.sleep(1)
tabs = driver.window_handles
driver.switch_to.window(tabs[-1])

# === 5. LOOP UNTUK TIAP MATA KULIAH ===
while True:
    try:
        # === PILIH MATA KULIAH (selalu pilih paling atas)
        select_matkul = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "select2-selection")))
        time.sleep(1)
        driver.execute_script("arguments[0].scrollIntoView();", select_matkul)
        time.sleep(1) 
        driver.execute_script("window.scrollBy(0, -100);") 
        time.sleep(1)
        select_matkul.click()
        time.sleep(1)
        options = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".select2-results__option")))
        time.sleep(2)
        
        # Kalau tidak ada lagi mata kuliah, keluar dari loop
        if len(options) == 0:
            print("🎓 Semua mata kuliah sudah diisi.")
            break

        first_option = options[0]
        first_option.click()

        # === PILIH SEMUA RADIO "Sangat Puas"
        labels = driver.find_elements(By.XPATH, "//label[contains(., 'Sangat Puas')]")
        for label in labels:
            try:
                radio_input = label.find_element(By.TAG_NAME, "input")
                driver.execute_script("arguments[0].click();", radio_input)
            except:
                pass
        time.sleep(3)

        # === ISI SARAN ===
        saran_list = [
            "Terima kasih, materi perkuliahan sangat membantu.",
            "Dosen mengajar dengan jelas dan mudah dipahami.",
            "Sangat bermanfaat ilmunya."
        ]
        saran_field = driver.find_element(By.ID, "saran")
        time.sleep(1) 
        driver.execute_script("arguments[0].scrollIntoView();", saran_field)
        time.sleep(2)
        saran_field.clear()
        saran_field.send_keys(random.choice(saran_list))

        # === SUBMIT FORM ===
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit' and contains(text(), 'Submit')]")
        submit_button.click()

        # === DELAY DAN KLIK OK ===
        time.sleep(5)
        ok_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "swal2-confirm")))
        time.sleep(1)
        ok_button.click()

        time.sleep(2)

    except Exception as e:
        print("❌ Terjadi kesalahan:", e)
        break

# === SELESAI ===
print("✅ Semua kuesioner telah diisi.")
time.sleep(2)
driver.quit()
