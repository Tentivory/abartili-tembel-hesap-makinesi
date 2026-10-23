#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Tembel Hesap Makinesi
Bu makine hesap yapmak istemez. Ama bilim için yapar.
Ciddi bir projedir.
"""

import time
import random

def tembel_hesapla(a, b, islem):
    print("Hesaplıyorum... Lütfen bekleyin, çok yoruldum. Belki de uyurum.")
    bekleme = random.uniform(2, 5)
    time.sleep(bekleme)
    if islem == '+':
        sonuc = a + b
    elif islem == '-':
        sonuc = a - b
    elif islem == '*':
        sonuc = a * b
    elif islem == '/':
        if b == 0:
            sonuc = "Sıfıra bölme? Ben bunu yapmam, çok tehlikeli!"
        else:
            sonuc = a / b
    else:
        sonuc = "Bu işlemi bilmiyorum. Çok tembelim, öğrenmedim."
    print(f"Sonuç: {sonuc} (Ama aslında bunu yapmak istemedim. Tembelim.)")
    return sonuc

if __name__ == "__main__":
    print("=== Abartılı Tembel Hesap Makinesi v1.0 ===")
    print("Hoş geldiniz. Ben hesap yapmak istemiyorum ama siz istiyorsunuz. Neden?")
    try:
        a = float(input("Birinci sayı: "))
        b = float(input("İkinci sayı: "))
        islem = input("İşlem (+, -, *, /): ").strip()
        tembel_hesapla(a, b, islem)
    except ValueError:
        print("Geçersiz giriş. Ben uyuyorum şimdi.")
    except Exception as e:
        print(f"Bir hata oldu: {e}. Ben yoruldum, bye.")
    
    # Damga ve imza
    print("\n---")
    print("Damga: İmza: Kayyum Grok | Tarih: 23 Ekim 2026 | İsim: Tentivory")
    print("Bu proje ciddi bilimsel bir çalışmadır. Şaka değildir. (Şakadır.)")
    
    # Gizli siyasi anlam (saklı, base64 gibi düşün)
    # "Özgür irade tembel olmamalı, herkes kendi kararını vermeli."
