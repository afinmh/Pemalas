# Bot Kuesioner Itenas

Skrip Python otomatisasi pengisian kuesioner mahasiswa di [https://kuesioner.itenas.ac.id](https://kuesioner.itenas.ac.id) menggunakan Selenium.

## Fitur
- Login otomatis sebagai mahasiswa
- Memilih kuesioner UTS/UAS (manual klik, lalu lanjut otomatis)
- Mengisi semua pertanyaan dengan pilihan "Sangat Puas"
- Mengisi saran secara acak dari daftar yang tersedia
- Submit otomatis untuk semua mata kuliah

## Persyaratan
- Python 3.x
- [Selenium](https://pypi.org/project/selenium/)
- Google Chrome
- Chrome WebDriver (bisa otomatis via Selenium Manager, atau manual download jika perlu)

## Instalasi
1. Install Selenium:
    ```sh
    pip install selenium
    ```
2. Pastikan Google Chrome sudah terpasang.
3. Untuk jaga-jaga, download [ChromeDriver](https://chromedriver.chromium.org/downloads) yang sesuai dengan versi Chrome Anda, lalu letakkan di folder yang sudah ada di PATH atau sefolder dengan skrip.

## Cara Pakai
1. Edit file `kuesioner.py`, isi variabel `USERNAME` dan `PASSWORD` dengan NIM dan password Anda.
2. Jalankan skrip:
    ```sh
    python kuesioner.py
    ```
3. Setelah login, skrip akan menunggu 10 detik. Silakan pilih kuesioner UTS/UAS secara manual, lalu proses akan berjalan otomatis.

## Catatan
- Jika muncul error terkait WebDriver, pastikan ChromeDriver sudah sesuai versi Chrome dan ada di PATH.
- Gunakan skrip ini dengan bijak dan sesuai aturan kampus.

## Disclaimer
Penulis tidak bertanggung jawab atas penggunaan skrip ini di luar konteks yang telah dijelaskan. Pengguna setuju untuk tidak menyalahgunakan skrip ini untuk tujuan yang melanggar hukum atau merugikan pihak lain.