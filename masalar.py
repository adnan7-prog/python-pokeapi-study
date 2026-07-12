import tkinter as tk
adnan=tk.Tk()
adnan.title("adnan ")
adnan.state("zoomed")
masa=tk.Label(adnan,text="⚜🕳MASA SEÇİNİZ🕳⚜",bg="pink",fg="black",font="arial 20 bold")
masa.pack(ipadx=40,ipady=5,pady=10)
entry=tk.Entry(adnan,font="arial 15 bold",bg="skyblue",fg="red")
entry.pack(ipadx=5)
basilan_tuslar = ""  
zamanlayici_id = None 

def masa_kontrol_et():
    global basilan_tuslar, zamanlayici_id
    if basilan_tuslar in masalar:
        secilen_masa = masalar[basilan_tuslar]
        secilen_masa.config(bg="green", fg="white", text=f"✅ {basilan_tuslar}")
    basilan_tuslar = ""
    zamanlayici_id = None

def masa_doldur(event):
    global basilan_tuslar, zamanlayici_id
    
    tus = event.char
    if tus.isdigit():
        basilan_tuslar += tus 
        if zamanlayici_id is not None:
            adnan.after_cancel(zamanlayici_id)
        zamanlayici_id = adnan.after(500, masa_kontrol_et)
ilk_sira=tk.Frame(adnan)
ilk_sira.place(x=10,y=90)
ilk_masa=tk.Button(ilk_sira,text="🔲 1",bg="pink",fg="red",font="arial 15 bold")
ilk_masa.pack(ipadx=40,ipady=40)
ikinci_masa=tk.Button(ilk_sira,text="🔲 2",bg="pink",fg="red",font="arial 15 bold")
ikinci_masa.pack(ipadx=40,ipady=40,pady=20)
üçüncu_masa=tk.Button(ilk_sira,text="🔲 3",bg="pink",fg="red",font="arial 15 bold")
üçüncu_masa.pack(ipadx=40,ipady=40,pady=20)
dörtüncü_masa=tk.Button(ilk_sira,text="🔲 4",bg="pink",fg="red",font="arial 15 bold")
dörtüncü_masa.pack(ipadx=40,ipady=40,pady=20)

ikinci_sira=tk.Frame(adnan)
ikinci_sira.place(x=300,y=90)
beşinci_masa=tk.Button(ikinci_sira,text="🔲 5",bg="pink",fg="red",font="arial 15 bold")
beşinci_masa.pack(ipadx=40,ipady=40)
altinci_masa=tk.Button(ikinci_sira,text="🔲 6",bg="pink",fg="red",font="arial 15 bold")
altinci_masa.pack(ipadx=40,ipady=40,pady=20)
yedinci_masa=tk.Button(ikinci_sira,text="🔲 7",bg="pink",fg="red",font="arial 15 bold")
yedinci_masa.pack(ipadx=40,ipady=40,pady=20)
sekizinci_masa=tk.Button(ikinci_sira,text="🔲 8",bg="pink",fg="red",font="arial 15 bold")
sekizinci_masa.pack(ipadx=40,ipady=40,pady=20)

ikinci_sira=tk.Frame(adnan)
ikinci_sira.place(x=600,y=110)
dokuzuncu_masa=tk.Button(ikinci_sira,text="🔲 9",bg="pink",fg="red",font="arial 15 bold")
dokuzuncu_masa.pack(ipadx=40,ipady=30)
onuncu_masa=tk.Button(ikinci_sira,text="🔲 10",bg="pink",fg="red",font="arial 15 bold")
onuncu_masa.pack(ipadx=40,ipady=40,pady=20)
on_birinci_masa=tk.Button(ikinci_sira,text="🔲 11",bg="pink",fg="red",font="arial 15 bold")
on_birinci_masa.pack(ipadx=40,ipady=40,pady=20)
on_ikinci_masa=tk.Button(ikinci_sira,text="🔲 12",bg="pink",fg="red",font="arial 15 bold")
on_ikinci_masa.pack(ipadx=40,ipady=40,pady=20)

üçüncü_sira=tk.Frame(adnan)
üçüncü_sira.place(x=900,y=90)
on_ucuncu_masa=tk.Button(üçüncü_sira,text="🔲 13",bg="pink",fg="red",font="arial 15 bold")
on_ucuncu_masa.pack(ipadx=40,ipady=40)
on_dortuncu_masa=tk.Button(üçüncü_sira,text="🔲 14",bg="pink",fg="red",font="arial 15 bold")
on_dortuncu_masa.pack(ipadx=40,ipady=40,pady=20)
on_besinci_masa=tk.Button(üçüncü_sira,text="🔲 15",bg="pink",fg="red",font="arial 15 bold")
on_besinci_masa.pack(ipadx=40,ipady=40,pady=20)
on_altinci_masa=tk.Button(üçüncü_sira,text="🔲 16",bg="pink",fg="red",font="arial 15 bold")
on_altinci_masa.pack(ipadx=40,ipady=40,pady=20)

dortuncu_sira=tk.Frame(adnan)
dortuncu_sira.place(x=1200,y=90)
on_yedinci_masa=tk.Button(dortuncu_sira,text="🔲17",bg="pink",fg="red",font="arial 15 bold")
on_yedinci_masa.pack(ipadx=40,ipady=40)
on_sekizinci_masa=tk.Button(dortuncu_sira,text="🔲18",bg="pink",fg="red",font="arial 15 bold")
on_sekizinci_masa.pack(ipadx=40,ipady=40,pady=20)
on_dokuzuncu_masa=tk.Button(dortuncu_sira,text="🔲19",bg="pink",fg="red",font="arial 15 bold")
on_dokuzuncu_masa.pack(ipadx=40,ipady=40,pady=20)
on_yirmi_masa=tk.Button(dortuncu_sira,text="🔲20",bg="pink",fg="red",font="arial 15 bold")
on_yirmi_masa.pack(ipadx=40,ipady=40,pady=20)

masalar={
    "1":ilk_masa,
    "2":ikinci_masa,
    "3":üçüncu_masa,
    "4":dörtüncü_masa,
    "5":beşinci_masa,
    "6":altinci_masa,
    "7":yedinci_masa,
    "8":sekizinci_masa,
    "9":dokuzuncu_masa,
    "10":onuncu_masa,
    "11":on_birinci_masa,
    "12":on_ikinci_masa,
    "13":on_ucuncu_masa,
    "14":on_dortuncu_masa,
    "15":on_besinci_masa,
    "16":on_altinci_masa,
    "17":on_yedinci_masa,
    "18":on_sekizinci_masa,
    "19":on_dokuzuncu_masa,
    "20":on_yirmi_masa  
}

adnan.bind("<Key>", masa_doldur)
adnan.mainloop()