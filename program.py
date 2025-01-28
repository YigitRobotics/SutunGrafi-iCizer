import matplotlib.pyplot as plt
import pandas as pd
import time
import colorama

# kodu kendinize göre düzenleyebilirsiniz sadece basit bir test kodudur.

grafik_verisi = {
    "İsimler": ["Yiğit","Berkay","Mirza","Serdar"],
    "Notlar": [100,90,80,70]
}

class AnaProgram:
    def __init__(self):
        self.veri = grafik_verisi

    def anaislemler(self):
        df = pd.DataFrame(self.veri)
        plt.bar(df["İsimler"], df["Notlar"])
        plt.title("Sütün Grafiği (Not)")
        plt.show()

program = AnaProgram()

program.anaislemler()
