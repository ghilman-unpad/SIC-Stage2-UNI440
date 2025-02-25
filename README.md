# UNI440 - Tugas SIC Tahap 2

Proyek ini menggunakan ESP32 yang terhubung ke sensor DHT11 untuk mengukur suhu dan kelembaban secara real-time. Data dari sensor dikirim ke server melalui REST API/MQTT, lalu disimpan ke database MongoDB dan divisualisasikan di dashboard Ubidots. ESP32 akan membaca data dari DHT11 secara berkala, kemudian mengirimkannya ke cloud agar bisa dipantau dari mana saja. Dengan integrasi ini, pengguna bisa mendapatkan informasi lingkungan secara akurat dan otomatis tanpa perlu membaca sensor secara manual. 🚀🌡📡
