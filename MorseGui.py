import tkinter as tk
from tkinter import ttk

morse_alfabesi = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.',
    '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-',
    '@': '.--.-.'
}

def metni_morse_cevir(metin):
    morse_metni = ''
    for karakter in metin:
        if karakter.upper() in morse_alfabesi:
            morse_metni += morse_alfabesi[karakter.upper()] + ' '
        elif karakter == ' ':
            morse_metni += ' '
    return morse_metni.strip()

def morseyi_metne_cevir(morse_metni):
    metin = ''
    siradaki_karakter = ''
    for i in morse_metni:
        if i != ' ':
            siradaki_karakter += i
        else:
            if siradaki_karakter in morse_alfabesi.values():
                metin += list(morse_alfabesi.keys())[list(morse_alfabesi.values()).index(siradaki_karakter)]
            else:
                metin += ' '
            siradaki_karakter = ''
    return metin

def morse_cevirici():
    girilen_metin = metin_giris.get("1.0",'end-1c')
    morse_metni = metni_morse_cevir(girilen_metin)
    morse_label.config(text=f"Morse kodu: {morse_metni}")

def metin_cevirici():
    girilen_morse = morse_giris.get()
    cozulmus_metin = morseyi_metne_cevir(girilen_morse)
    metin_label.config(text=f"Çözülen metin: {cozulmus_metin}")

# Tkinter penceresini oluştur
pencere = tk.Tk()
pencere.title("Morse Çevirici")

# Giriş ve çıkış alanları
metin_giris_label = tk.Label(pencere, text="Metin Girin:")
metin_giris = tk.Text(pencere, height=4, width=50)
morse_giris_label = tk.Label(pencere, text="Morse Kodu Girin:")
morse_giris = tk.Entry(pencere, width=50)

# Çevirme butonları
morse_cevir_btn = tk.Button(pencere, text="Metni Morse'a Çevir", command=morse_cevirici)
metin_cevir_btn = tk.Button(pencere, text="Morse'u Metne Çevir", command=metin_cevirici)

# Sonuç etiketleri
morse_label = tk.Label(pencere, text="Morse kodu: ")
metin_label = tk.Label(pencere, text="Çözülen metin: ")

# Grid düzeni
metin_giris_label.grid(row=0, column=0, pady=5)
metin_giris.grid(row=1, column=0, pady=5)
morse_cevir_btn.grid(row=2, column=0, pady=5)
morse_giris_label.grid(row=3, column=0, pady=5)
morse_giris.grid(row=4, column=0, pady=5)
metin_cevir_btn.grid(row=5, column=0, pady=5)
morse_label.grid(row=6, column=0, pady=5)
metin_label.grid(row=7, column=0, pady=5)

# Tkinter penceresini çalıştır
pencere.mainloop()
