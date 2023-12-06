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
# strip fonksiyonu cümlenin varsa başındaki ve sonundaki boşlukları siler.

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

# Örnek kullanım
metin = "Merhaba ben umut !"
morse_metni = metni_morse_cevir(metin)
print(f"{metin} metni Morse koduna çevrildi: {morse_metni}")

cozulmus_metin = morseyi_metne_cevir(morse_metni)
print(f"{morse_metni} Morse kodu çözüldü: {cozulmus_metin}")
