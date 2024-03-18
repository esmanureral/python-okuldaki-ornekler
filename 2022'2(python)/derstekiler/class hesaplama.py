class hesaplama():
    def _init_(self,x,y):
        self.x=x
        self.y=y 
        self.sonuç=self.x+self.y 
        def işlem1(self):
            self.x+=self.sonuç
            self.y=self.x-1
            self.sonuç=self.x*self.y
        def işlem2(self):
            self.x=pow(self.x,2)
            self.y=round(self.x/2)
            self.sonuç=self.y-self.x
        def ekranayazdir(self):
            self.islem1()
            self.islem2()
            print(self.sonuç)
        Yhesapla=hesapla(1,2)
        Yhesapla=ekranayazdir()