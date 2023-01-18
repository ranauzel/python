from tkinter import*

pencere=Tk()
etiket=Label(pencere)
etiket.config(text="kullanıcı adınızı giriniz",bg="gray",font=("Vertana",20))
etiket.place(x=100,y=100)
entry=Entry(pencere)
entry.place(x=100,y=150)
sifre=Label(pencere)
sifre.config(text="şifrenizi giriniz",bg="gray",font=("Vertana",20))
sifre.place(x=100,y=250)
giris=Entry(pencere)
giris=Entry(pencere)
giris.place(x=100,y=300)
buton=Button(pencere)
buton.config(text="Giriş yap",bg="black",fg="white")
buton.place(x=20,y=100)
mainloop()


