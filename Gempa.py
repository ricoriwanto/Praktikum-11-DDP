class gempa :
    lokasi = " "
    skala = " "
    
    def __init__(self,lokasi, skala) :
        self.lokasi = lokasi
        self.skala = skala
        
    def dampak (self):
        if self.skala <2 :
            ket = "gempa tidak berasa"
        elif self.skala <2 and self.skala <4 :
            ket = "bangunan retak-retak"
        elif self.skala >4 and self.skala <6:
            ket = "bangunan roboh"
        else :
            ket = "bangunan roboh dan berpotensi tsunami"
        
        print("Lokasi gempa ", self.lokasi, "\nSkala gempa",self.lokasi,"\nskala gempa",ket)
          