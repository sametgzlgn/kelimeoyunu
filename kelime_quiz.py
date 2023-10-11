# Samet Güzelgün 04.10.23
import tkinter as tk
from tkinter import messagebox
import requests
import random
import beepy
cevap = ""
anlam = ""
dogru = ""
siklar = []
kontrol_lst = []
puan = 0
def basla():
    yeni_soru()
def set_cevap(cvp):
    global cevap
    cevap = cvp
    kontrol()
def kontrol():
    global kontrol_lst,cevap,dogru,puan,siklar,puan_etkt,anlam
    if kontrol_lst[int(cevap)] == dogru:
        beepy.beep()
        puan += 50
        puan_etkt["text"] = "Puan: " + str(puan)
        siklar.clear()
        yeni_soru()
    else:
        beepy.beep(sound=3)
        puan -= 50
        puan_etkt["text"] = "Puan: " + str(puan)
        dosya = open("yanlis_kelimeler.txt","a")
        dosya.write("\nKelime: {}\nAnlamı: {}".format(dogru,anlam))
        dosya.close()
        messagebox.showinfo("Yanlış!","Doğrusu:{}".format(dogru))
        siklar.clear()
        yeni_soru()
def yeni_soru():
    global buton1,buton2,buton3,siklar,dogru,anlam,anlam_etkt,kontrol_lst
    firefox = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    while len(siklar) < 3:
        a = requests.get("https://sozluk.gov.tr/taramaId?id=" + str(random.randint(0,14488)),headers=firefox)
        b = a.text.split(",")[1].split(":")[1].replace("\"","")
        dogru = b
        anlam = a.text.split(":")[3].split(",")[0].replace("'","").replace("\"","")
        if b not in siklar:
            siklar.append(b)
    anlam_etkt["text"] = "Anlam: " + anlam
    kontrol_lst = siklar
    random.shuffle(siklar)
    buton1["text"] = "A: " + siklar[0]
    buton2["text"] = "B: " + siklar[1]
    buton3["text"] = "C: " + siklar[2]
pencere = tk.Tk()
anlam_etkt = tk.Label(text="Kelime anlamı:")
anlam_etkt.grid(row=0,column=2)
buton1 = tk.Button(text="A:",command=lambda:set_cevap("0"))
buton1.grid(row=5,column=1)
buton2 = tk.Button(text="B:",command=lambda:set_cevap("1"))
buton2.grid(row=5,column=2)
buton3 = tk.Button(text="C:",command=lambda:set_cevap("2"))
buton3.grid(row=5,column=3)
basla_btn = tk.Button(text="Yeni Soru",command=basla)
basla_btn.grid(row=7,column=2)
puan_etkt = tk.Label(text="Puan:")
puan_etkt.grid(row=7,column=3)
pencere.title("Kelime Quiz")
pencere.resizable(0,0)
yeni_soru()
pencere.mainloop()
