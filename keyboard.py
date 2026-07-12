#-*- coding: utf-8 -*-
import tkinter as tk
adnan=tk.Tk()
adnan.title("klaviye")
adnan.state('zoomed') 
ilk_sira=tk.Frame(adnan)
ilk_sira.place(x=150,y=150)
butonlar = {}
bizim = tk.Label(adnan, text="---------------------------------------------------keyboard-----------------------------------------------------------", bg="pink", fg="blue", font=("Arial 20 bold"))
bizim.place(x=155, y=20, width=1080, height=40)
yazi = tk.Entry(adnan, font=("Arial 20"))
yazi.place(x=155, y=70, width=1080, height=50)
yazi=tk.Label(text="",bg="grey")
def efekt_yap(event=None, tus_adi=None):
    if event:
        tus_char = event.char
        tus_keysym = event.keysym
        if tus_keysym in ["ISO_Level3_Shift", "Alt_R"] or event.keycode == 17:
            tus_adi = "ISO_Level3_Shift"
            if "Control_R" in butonlar:
                butonlar["Control_R"].config(bg="skyblue")
        elif event.keycode == 91 or tus_keysym in ["Super_L", "Win"]:
            tus_adi = "Super_L"
        elif event.keycode == 93 or tus_keysym in ["Menu", "App"]:
            tus_adi = "Menu"
        elif event.keycode == 96 or tus_keysym == "KP_0":
            tus_adi = "KP_0"
        elif event.keycode == 110 or tus_keysym in ["KP_Delete", "KP_Decimal"]:
            tus_adi = "KP_Delete"
        elif event.keycode == 13 or tus_keysym == "KP_Enter":
            tus_adi = "KP_Enter"

        elif event.keycode == 38 or tus_keysym == "Up":
            tus_adi = "Up"
        elif event.keycode == 40 or tus_keysym == "Down":
            tus_adi = "Down"
        elif event.keycode == 37 or tus_keysym == "Left":
            tus_adi = "Left"
        elif event.keycode == 39 or tus_keysym == "Right":
            tus_adi = "Right"
        elif event.keycode in [97, 35] or tus_keysym in ["KP_1", "KP_End", "End"] or tus_char == "1":
            tus_adi = "KP_1"
        elif event.keycode in [98, 40] or tus_keysym in ["KP_2", "KP_Down", "Down"] or tus_char == "2":
            tus_adi = "KP_2"
        elif event.keycode in [99, 34] or tus_keysym in ["KP_3", "KP_Next", "Next", "PgDn"] or tus_char == "3":
            tus_adi = "KP_3"
        elif event.keycode in [100, 37] or tus_keysym in ["KP_4", "KP_Left", "Left"] or tus_char == "4":
            tus_adi = "KP_4"
        elif event.keycode in [101, 12] or tus_keysym in ["KP_5", "KP_Begin", "Begin"] or tus_char == "5":
            tus_adi = "KP_5"
        elif event.keycode in [102, 39] or tus_keysym in ["KP_6", "KP_Right", "Right"] or tus_char == "6":
            tus_adi = "KP_6"
        elif event.keycode == 103:
            tus_adi = "KP_7"
        elif event.keycode == 104:
            tus_adi = "KP_8"
        elif event.keycode == 105:
            tus_adi = "KP_9"
        elif event.keycode == 111:
            tus_adi = "KP_Divide"
        elif event.keycode == 106:
            tus_adi = "KP_Multiply"
        elif event.keycode == 109:
            tus_adi = "KP_Subtract"
        elif event.keycode == 144:
            tus_adi = "Num_Lock"
        elif event.keycode == 107 or tus_keysym == "KP_Add":
            tus_adi = "KP_Add"
        elif tus_char in butonlar:
            tus_adi = tus_char
        elif tus_char.lower() in butonlar:
            tus_adi = tus_char.lower()
        else:
            tus_adi = tus_keysym                                 
    if tus_adi in butonlar:
        secilen_buton = butonlar[tus_adi]        
        if isinstance(secilen_buton, list):
            for parca in secilen_buton:
                parca.config(bg="lightgreen")
            adnan.after(150, lambda: [parca.config(bg="pink") for parca in secilen_buton])
        else:
            secilen_buton.config(bg="red")
            adnan.after(150, lambda: secilen_buton.config(bg="pink"))
buton_esc = tk.Button(ilk_sira, text="Esc", fg="black", bg="pink", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="Escape"))
buton_esc.pack(side="left", padx=(5, 40), ipadx=10)
butonlar["Escape"] = buton_esc
buton_f1 = tk.Button(ilk_sira, text="F1", fg="black", bg="pink", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="F1"))
buton_f1.pack(side="left", padx=2, ipadx=5)
butonlar["F1"] = buton_f1
buton_f2 = tk.Button(ilk_sira, text="F2", fg="black", bg="pink", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="F2"))
buton_f2.pack(side="left", padx=2, ipadx=5)
butonlar["F2"] = buton_f2
buton_f3 = tk.Button(ilk_sira, text="F3", fg="black", bg="pink", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="F3"))
buton_f3.pack(side="left", padx=2, ipadx=5)
butonlar["F3"] = buton_f3
buton_f4 = tk.Button(ilk_sira, text="F4", fg="black", bg="pink", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="F4"))
buton_f4.pack(side="left", padx=(5, 40), ipadx=5)
butonlar["F4"] = buton_f4
buton_f5 = tk.Button(ilk_sira, text="F5", fg="black", bg="pink", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="F5"))
buton_f5.pack(side="left", padx=2, ipadx=5)
butonlar["F5"] = buton_f5
buton_f6 = tk.Button(ilk_sira, text="F6", fg="black", bg="pink", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="F6"))
buton_f6.pack(side="left", padx=2, ipadx=5)
butonlar["F6"] = buton_f6
buton_f7 = tk.Button(ilk_sira, text="F7", fg="black", bg="pink", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="F7"))
buton_f7.pack(side="left", padx=2, ipadx=5)
butonlar["F7"] = buton_f7
buton_f8 = tk.Button(ilk_sira, text="F8", fg="black", bg="pink", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="F8"))
buton_f8.pack(side="left", padx=(5, 40), ipadx=5)
butonlar["F8"] = buton_f8
buton_f9 = tk.Button(ilk_sira, text="F9", fg="black", bg="pink", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="F9"))
buton_f9.pack(side="left", padx=2, ipadx=5)
butonlar["F9"] = buton_f9
buton_f10 = tk.Button(ilk_sira, text="F10", fg="black", bg="pink", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="F10"))
buton_f10.pack(side="left", padx=2, ipadx=5)
butonlar["F10"] = buton_f10
buton_f11 = tk.Button(ilk_sira, text="F11", fg="black", bg="pink", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="F11"))
buton_f11.pack(side="left", padx=2, ipadx=5)
butonlar["F11"] = buton_f11
buton_f12 = tk.Button(ilk_sira, text="F12", fg="black", bg="pink", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="F12"))
buton_f12.pack(side="left", padx=(2, 30), ipadx=5)
butonlar["F12"] = buton_f12
buton_PS = tk.Button(ilk_sira, text="PS", fg="black", bg="pink", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="Print"))
buton_PS.pack(side="left", padx=2, ipadx=10)
butonlar["Print"] = buton_PS
butonlar["Sys_Req"] = buton_PS
butonlar["Snapshot"] = buton_PS
buton_SL = tk.Button(ilk_sira, text="SL", fg="black", bg="pink", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="Scroll_Lock"))
buton_SL.pack(side="left", padx=2, ipadx=10)
butonlar["Scroll_Lock"] = buton_SL
buton_PB = tk.Button(ilk_sira, text="PB", fg="black", bg="pink", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="Pause"))
buton_PB.pack(side="left", padx=2, ipadx=10)
butonlar["Pause"] = buton_PB
#-----------------------ikici sıra--------------------------------#
ikinci_sira = tk.Frame(adnan)
ikinci_sira.place(x=150, y=200)
buton_caps = tk.Button(ikinci_sira, text="é", fg="black", bg="skyblue", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="é"))
buton_caps.pack(side="left", padx=5, ipadx=5)
butonlar["quotedbl"] = buton_caps 
butonlar["é"] = buton_caps  
buton_1 = tk.Button(ikinci_sira, text="1", fg="black", bg="skyblue", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="1"))
buton_1.pack(side="left", padx=5, ipadx=10)
butonlar["1"] = buton_1
butonlar["exclam"] = buton_1
buton_2 = tk.Button(ikinci_sira, text="2", fg="black", bg="skyblue", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="2"))
buton_2.pack(side="left", padx=5, ipadx=10)
butonlar["2"] = buton_2
butonlar["apostrophe"] = buton_2
butonlar["sterling"] = buton_2
buton_3 = tk.Button(ikinci_sira, text="3", fg="black", bg="skyblue", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="3"))
buton_3.pack(side="left", padx=5, ipadx=10)
butonlar["3"] = buton_3
butonlar["asciicircum"] = buton_3
butonlar["numbersign"] = buton_3
buton_4 = tk.Button(ikinci_sira, text="4", fg="black", bg="skyblue", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="4"))
buton_4.pack(side="left", padx=5, ipadx=10)
butonlar["4"] = buton_4
butonlar["plus"] = buton_4
butonlar["dollar"] = buton_4
buton_5 = tk.Button(ikinci_sira, text="5", fg="black", bg="skyblue", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="5"))
buton_5.pack(side="left", padx=5, ipadx=10)
butonlar["5"] = buton_5
butonlar["percent"] = buton_5
butonlar["onehalf"] = buton_5
buton_6 = tk.Button(ikinci_sira, text="6", fg="black", bg="skyblue", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="6"))
buton_6.pack(side="left", padx=5, ipadx=10)
butonlar["6"] = buton_6
butonlar["ampersand"] = buton_6
buton_7 = tk.Button(ikinci_sira, text="7", fg="black", bg="skyblue", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="7"))
buton_7.pack(side="left", padx=5, ipadx=10)
butonlar["7"] = buton_7
butonlar["slash"] = buton_7
butonlar["braceleft"] = buton_7
buton_8 = tk.Button(ikinci_sira, text="8", fg="black", bg="skyblue", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="8"))
buton_8.pack(side="left", padx=5, ipadx=10)
butonlar["8"] = buton_8
butonlar["parenleft"] = buton_8
butonlar["bracketleft"] = buton_8
buton_9 = tk.Button(ikinci_sira, text="9", fg="black", bg="skyblue", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="9"))
buton_9.pack(side="left", padx=5, ipadx=10)
butonlar["9"] = buton_9
butonlar["parenright"] = buton_9
butonlar["bracketright"] = "../../.." 
butonlar["bracketright"] = buton_9
buton_0 = tk.Button(ikinci_sira, text="0", fg="black", bg="skyblue", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="0"))
buton_0.pack(side="left", padx=5, ipadx=10)
butonlar["0"] = buton_0
butonlar["equal"] = buton_0
butonlar["braceright"] = buton_0
buton_ç = tk.Button(ikinci_sira, text="*", fg="black", bg="skyblue", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="asterisk"))
buton_ç.pack(side="left", padx=5, ipadx=10)
butonlar["*"] = buton_ç
butonlar["asterisk"] = buton_ç
butonlar["question"] = buton_ç
butonlar["backslash"] = buton_ç
buton_e = tk.Button(ikinci_sira, text="-", fg="black", bg="skyblue", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="minus"))
buton_e.pack(side="left", padx=5, ipadx=10)
butonlar["-"] = buton_e
butonlar["minus"] = buton_e
butonlar["underscore"] = buton_e
butonlar["bar"] = buton_e
buton_sil = tk.Button(ikinci_sira, text="◀—", fg="black", bg="skyblue", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="BackSpace"))
buton_sil.pack(side="left", padx=5, ipadx=18)
butonlar["BackSpace"] = buton_sil
sag_blok = tk.Frame(adnan)
sag_blok.place(x=875, y=200)
buton_ins = tk.Button(sag_blok, text="Ins", fg="black", bg="pink", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="Insert"))
buton_ins.pack(side="left", padx=2, ipadx=10)
butonlar["Insert"] = buton_ins
buton_home = tk.Button(sag_blok, text="Home", fg="black", bg="pink", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="Home"))
buton_home.pack(side="left", padx=2, ipadx=1)
butonlar["Home"] = buton_home
buton_pgup = tk.Button(sag_blok, text="PgUp", fg="black", bg="pink", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="Prior"))
buton_pgup.pack(side="left", padx=2, ipadx=3)
butonlar["Prior"] = buton_pgup

numpad_ust_sira = tk.Frame(adnan)
numpad_ust_sira.place(x=1060, y=200)
buton_num = tk.Button(numpad_ust_sira, text="Num", fg="black", bg="skyblue", font=("Arial 9"), command=lambda: efekt_yap(tus_adi="Num_Lock"))
buton_num.pack(side="left", padx=2, ipadx=0)
butonlar["Num_Lock"] = buton_num
buton_bolme = tk.Button(numpad_ust_sira, text="/", fg="black", bg="skyblue", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="KP_Divide"))
buton_bolme.pack(side="left", padx=2, ipadx=10)
butonlar["KP_Divide"] = buton_bolme
buton_carpm = tk.Button(numpad_ust_sira, text="*", fg="black", bg="skyblue", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="KP_Multiply"))
buton_carpm.pack(side="left", padx=2, ipadx=10)
butonlar["KP_Multiply"] = buton_carpm
buton_cikar = tk.Button(numpad_ust_sira, text="-", fg="black", bg="skyblue", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="KP_Subtract"))
buton_cikar.pack(side="left", padx=2, ipadx=10)
butonlar["KP_Subtract"] = buton_cikar

#-------------------------üçüncü satır---------------------------------#
ucuncu_sira = tk.Frame(adnan)
ucuncu_sira.place(x=150, y=240)
buton_tab = tk.Button(ucuncu_sira, text="TAB", fg="black", bg="skyblue", font=("Arial 10"))
buton_tab.pack(side="left", padx=5, ipadx=8)
butonlar["Tab"] = buton_tab
l=tk.Frame(adnan)
l.place(x=800,y=260)
buton_enter = tk.Button( text="Enter", fg="black", bg="skyblue", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="Return"))
buton_enter.place(x=800,y=240)
butonlar["Return"] = buton_enter
da=tk.Label(l,text="",bg="skyblue",width=5)
da.pack(padx=1,ipady=13)

numpad_ust_alt = tk.Frame(adnan)
numpad_ust_alt.place(x=875, y=240)
buton_del = tk.Button(numpad_ust_alt, text="Del", fg="black", bg="pink", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="Num_Lock"))
buton_del.pack(side="left", padx=2, ipadx=9)
butonlar["Delete"]=buton_del
buton_end = tk.Button(numpad_ust_alt, text="End", fg="black", bg="pink", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="Num_Lock"))
buton_end.pack(side="left", padx=2, ipadx=6)
butonlar["End"]=buton_end
buton_PG = tk.Button(numpad_ust_alt, text="PgDn", fg="black", bg="pink", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="Num_Lock"))
buton_PG.pack(side="left", padx=2, ipadx=3)
butonlar["End"]=buton_PG

numpad_789_sira = tk.Frame(adnan)
numpad_789_sira.place(x=1060, y=240)
buton_kp7 = tk.Button(numpad_789_sira, text="7", fg="black", bg="skyblue", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="KP_7"))
buton_kp7.pack(side="left", padx=2, ipadx=10)
butonlar["KP_7"] = buton_kp7
buton_kp8 = tk.Button(numpad_789_sira, text="8", fg="black", bg="skyblue", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="KP_8"))
buton_kp8.pack(side="left", padx=2, ipadx=8)
butonlar["KP_8"] = buton_kp8
buton_kp9 = tk.Button(numpad_789_sira, text="9", fg="black", bg="skyblue", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="KP_9"))
buton_kp9.pack(side="left", padx=2, ipadx=8)
butonlar["KP_9"] = buton_kp9
a = tk.Frame(adnan)
a.place(x=1185, y=240)
buton_a = tk.Button(a, text="+", fg="black", bg="skyblue", font="Arial 10", width=3)
buton_a.pack(side="left", padx=2, ipady=20) 
butonlar["KP_Add"] = buton_a

q_satiri = ["q", "w", "e", "r", "t", "y", "u", "ı", "o", "p", "ğ", "ü"]

for harf in q_satiri:
    btn = tk.Button(ucuncu_sira, text=harf.upper(), fg="black", bg="skyblue", font=("Arial 10"), command=lambda h=harf: efekt_yap(harf))
    btn.pack(side="left", padx=5, ipadx=9)
    butonlar[harf.lower()] = btn
    butonlar[harf.upper()] = btn
#--------------------dort satır------------------------#
dort = tk.Frame(adnan)
dort.place(x=150, y=280)

buton_cabs = tk.Button(dort, text="Caps Lock", fg="black", bg="skyblue", font=("Arial 10"))
buton_cabs.pack(side="left", padx=5, ipadx=0)
butonlar["Caps_Lock"] = buton_cabs
a_satiri = ["a", "s", "d", "f", "g", "h", "j", "k", "l", "ş", "i"]

for harf in a_satiri:
    btn = tk.Button(dort, text=harf.upper(), fg="black", bg="skyblue", font=("Arial 10"), command=lambda h=harf: efekt_yap(tus_adi=h))
    btn.pack(side="left", padx=5, ipadx=9)
    butonlar[harf.lower()] = btn
    butonlar[harf.upper()] = btn
buton_comma = tk.Button(dort, text=",", fg="black", bg="skyblue", font=("Arial 10"))
buton_comma.pack(side="left", padx=5, ipadx=10)
butonlar["comma"] = buton_comma
butonlar[","] = buton_comma 
sayilar456=tk.Frame(adnan)
sayilar456.place(x=1064,y=280)
sayi4 = tk.Button(sayilar456, text="4", bg="skyblue", fg="black", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="KP_4"))
sayi4.pack(side="left", padx=0, ipadx=10)
butonlar["KP_4"] = sayi4
sayi5 = tk.Button(sayilar456, text="5", bg="skyblue", fg="black", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="KP_5"))
sayi5.pack(side="left", padx=2, ipadx=8)
butonlar["KP_5"] = sayi5
sayi6 = tk.Button(sayilar456, text="6", bg="skyblue", fg="black", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="KP_6"))
sayi6.pack(side="left", padx=2, ipadx=8)
butonlar["KP_6"] = sayi6

#--------------------------becıncı sayı-----------------------------#
bes = tk.Frame(adnan)
bes.place(x=150, y=320)
buton_shift = tk.Button(bes, text="Shift", fg="black", bg="skyblue", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="Shift_L"))
buton_shift.pack(side="left", padx=4, ipadx=15)
butonlar["Shift_L"] = buton_shift
buton_less = tk.Button(bes, text="<", fg="black", bg="skyblue", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="less"))
buton_less.pack(side="left", padx=4, ipadx=10)
butonlar["less"] = buton_less
butonlar["<"] = buton_less
z_satiri = ["z", "x", "c", "v", "b", "n", "m", "ö", "ç"]
for harf in z_satiri:
    btn = tk.Button(bes, text=harf.upper(), fg="black", bg="skyblue", font=("Arial 10"), command=lambda h=harf: efekt_yap(tus_adi=h))
    btn.pack(side="left", padx=4, ipadx=9)
    butonlar[harf.lower()] = btn
    butonlar[harf.upper()] = btn
buton_dot = tk.Button(bes, text=".", fg="black", bg="skyblue", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="period"))
buton_dot.pack(side="left", padx=4, ipadx=10)
butonlar["period"] = buton_dot
butonlar["."] = buton_dot
buton_shift_r = tk.Button(bes, text="Shift", fg="black", bg="skyblue", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="Shift_R"))
buton_shift_r.pack(side="left", padx=4, ipadx=30)
butonlar["Shift_R"] = buton_shift_r
numpad_123_sira = tk.Frame(adnan)
numpad_123_sira.place(x=1060, y=320)
buton_kp1 = tk.Button(numpad_123_sira, text="1", fg="black", bg="skyblue", font=("Arial 9"), width=4, command=lambda: efekt_yap(tus_adi="KP_1"))
buton_kp1.pack(side="left", padx=4,ipady=1)
butonlar["KP_1"] = buton_kp1
buton_kp2 = tk.Button(numpad_123_sira, text="2", fg="black", bg="skyblue", font=("Arial 9"), width=3,command=lambda: efekt_yap(tus_adi="KP_2"))
buton_kp2.pack(side="left", padx=0,ipadx=2,ipady=1)
butonlar["KP_2"] = buton_kp2
buton_kp3 = tk.Button(numpad_123_sira, text="3", fg="black", bg="skyblue", font=("Arial 9"), width=3, command=lambda: efekt_yap(tus_adi="KP_3"))
buton_kp3.pack(side="left", padx=3,ipadx=3)
butonlar["KP_3"] = buton_kp3
yon_ust_frame = tk.Frame(adnan)
yon_ust_frame.place(x=915, y=320)
buton_up = tk.Button(yon_ust_frame, text="↑", fg="black", bg="pink", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="Up"))
buton_up.pack(side="left", padx=16, ipadx=13)
butonlar["Up"] = buton_up
alt_satir = tk.Frame(adnan)
alt_satir.place(x=150, y=360)
buton_ctrl_l = tk.Button(alt_satir, text="Ctrl", fg="black", bg="skyblue", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="Control_L"))
buton_ctrl_l.pack(side="left", padx=5, ipadx=10)
butonlar["Control_L"] = buton_ctrl_l
buton_win = tk.Button(alt_satir, text="Win", fg="black", bg="skyblue", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="Win"))
buton_win.pack(side="left", padx=5, ipadx=8)
butonlar["Super_L"] = buton_win
buton_alt_l = tk.Button(alt_satir, text="Alt", fg="black", bg="skyblue", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="Alt_L"))
buton_alt_l.pack(side="left", padx=5, ipadx=10)
butonlar["Alt_L"] = buton_alt_l
buton_space = tk.Button(alt_satir, text="Space", fg="black", bg="skyblue", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="space"))
buton_space.pack(side="left", padx=5, ipadx=110,ipady=2)
butonlar["space"] = buton_space
buton_alt_r = tk.Button(alt_satir, text="AltGr", fg="black", bg="skyblue", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="Alt_R"))
buton_alt_r.pack(side="left", padx=5, ipadx=8)
butonlar["ISO_Level3_Shift"] = buton_alt_r
butonlar["Alt_R"] = buton_alt_r
buton_fn = tk.Button(alt_satir, text="Fn", fg="black", bg="skyblue", font=("Arial 10"))
buton_fn.pack(side="left", padx=5, ipadx=10)
buton_menu = tk.Button(alt_satir, text="▤", fg="black", bg="skyblue", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="Menu"))
buton_menu.pack(side="left", padx=5, ipadx=10)
butonlar["Menu"] = buton_menu
buton_ctrl_r = tk.Button(alt_satir, text="Ctrl", fg="black", bg="skyblue", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="Control_R"))
buton_ctrl_r.pack(side="left", padx=5, ipadx=10)
butonlar["Control_R"] = buton_ctrl_r

yon_alt_frame = tk.Frame(adnan)
yon_alt_frame.place(x=882, y=360)

buton_left = tk.Button(yon_alt_frame, text="←", fg="black", bg="pink", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="Left"))
buton_left.pack(side="left", padx=1, ipadx=10,ipady=1)
butonlar["Left"] = buton_left

buton_down = tk.Button(yon_alt_frame, text="↓", fg="black", bg="pink", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="Down"))
buton_down.pack(side="left", padx=3, ipadx=12,ipady=1)
butonlar["Down"] = buton_down

buton_right = tk.Button(yon_alt_frame, text="→", fg="black", bg="pink", font=("Arial 10"), command=lambda: efekt_yap(tus_adi="Right"))
buton_right.pack(side="left", padx=2, ipadx=10,ipady=1)
butonlar["Right"] = buton_right
numpad_son_sira = tk.Frame(adnan)
numpad_son_sira.place(x=1060, y=360)
buton_kp0 = tk.Button(numpad_son_sira, text="0", fg="black", bg="skyblue", font=("Arial 10"), width=9, command=lambda: efekt_yap(tus_adi="KP_0"))
buton_kp0.pack(side="left", padx=0)
butonlar["KP_0"] = buton_kp0
buton_kp_dot = tk.Button(numpad_son_sira, text=".", fg="black", bg="skyblue", font=("Arial 10"), width=3, command=lambda: efekt_yap(tus_adi="KP_Delete"))
buton_kp_dot.pack(side="left", padx=4)
butonlar["KP_Delete"] = buton_kp_dot
butonlar["KP_Separator"] = buton_kp_dot

numpad_enter_frame = tk.Frame(adnan)
numpad_enter_frame.place(x=1188, y=320)
buton_kp_enter = tk.Button(numpad_enter_frame, text="Enter", fg="black", bg="skyblue", font=("Arial 7"), command=lambda: efekt_yap(tus_adi="KP_Enter"))
buton_kp_enter.pack(side="left", padx=0, ipadx=1, ipady=23)
butonlar["KP_Enter"] = buton_kp_enter
adnan.bind("<Key>", efekt_yap)
adnan.mainloop()