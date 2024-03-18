class kare():
    def _init_(self,kenar):
        self.kenar=kenar
        self.alan=0
        self.çevre=0
    def kare_alan(self):
        self.alan=self.kenar*self.kenar
    def kare_çevre(self):
        self.çevre=4*self.kenar
    def bilgileriyazdir(self):
        self.kare_alan()
        self.kare_çevre()
        print("kenar=",self.kenar)
        print("alan=",self.alan)
        print("çevre=",self.çevre)
kare1=kare(5)
kare1.bilgileriyazdir()
    