from tkinter import *
from tkinter import ttk
from matplotlib import pyplot as plt ##прописать в командной строке "pip install matplotlib"##

root = Tk()

root.title ("ГЛАВНОЕ ОКНО")
root.geometry ("550x700")

###сохранение данных###

itogi = []
baza = []

pol = IntVar()
god = IntVar()
rost = IntVar()
ves = IntVar()

anketa = []
kategorii = ["история ССС", "образ жизни", "стресс", "сон", "сахар", "боли", "питание"]

quest1 = IntVar()
quest2 = IntVar()

quest3 = IntVar()
quest4 = IntVar()
quest5 = IntVar()
quest6 = IntVar()
quest7 = IntVar()
quest8 = IntVar()

quest9 = IntVar()
quest10 = IntVar()
quest11 = IntVar()
quest12 = IntVar()

quest13 = IntVar()
quest14 = IntVar()

quest15 = IntVar()
quest16 = IntVar()

quest17 = IntVar()
quest18 = IntVar()

quest19 = IntVar()
quest20 = IntVar()
quest21 = IntVar()
quest22 = IntVar()
quest23 = IntVar()
quest24 = IntVar()
quest25 = IntVar()
quest26 = IntVar()
quest27 = IntVar()
quest28 = IntVar()


analizi = []

lpvp = StringVar()
lpnp = StringVar()
trgl = StringVar()
artdav = StringVar()
cbelok = StringVar()
gmtsst = StringVar()
fbrn = StringVar()
ttg = StringVar()
glkz = StringVar()
krtzl = StringVar()
###сохранение данных###


### ОКНО1 (ОСНОВНЫЕ ДАННЫЕ) ###
def anketa_1():
    new_root_1 = Toplevel(root)
    new_root_1.title("ОСНОВНЫЕ ДАННЫЕ")
    new_root_1.geometry("400x300")

    r1 = ttk.Radiobutton(new_root_1, text="МУЖЧИНА", value = 0, variable = pol)
    r2 = ttk.Radiobutton(new_root_1, text="ЖЕНЩИНА", value = 1, variable = pol)
    r1.place(x=110, y=35)
    r2.place(x=210, y=35)

    my_label = Label(new_root_1, text = "ГОД РОЖДЕНИЯ", font = 16)
    my_label.place(x=0, y=70)
    label2 = ttk.Entry(new_root_1, font = 18, textvariable=god)
    label2.place(x=170, y=70)

    my_label3 = Label(new_root_1, text="РОСТ", font=18)
    my_label3.place(x=0, y=100)
    label3 = ttk.Entry(new_root_1, font=18, textvariable=rost)
    label3.place(x=170, y=100)

    my_label4 = Label(new_root_1, text="ВЕС", font=18)
    my_label4.place(x=0, y=130)
    label4 = ttk.Entry(new_root_1, font=18, textvariable=ves)
    label4.place(x=170, y=130)

    btnanketa0 = Button(new_root_1, text="ВВЕСТИ", font=35, command = baza_vvod)
    btnanketa0.place(x=150, y=170)
### ОКНО1 (ОСНОВНЫЕ ДАННЫЕ) ###

def baza_vvod():
    baza.append(int(pol.get()))
    age = (2025 - int(god.get()))
    baza.append(age)
    baza.append(int(rost.get()))
    baza.append(int(ves.get()))   

### ОКНО 2.1(ИСТОРИЯ ССС) ###    
def anketa_2_1():
    new_root_21 = Toplevel(root)
    new_root_21.title("АНКЕТИРОВАНИЕ_ИСТОРИЯССС")
    new_root_21.geometry("1000x300")

    label = Label(new_root_21, text = "ГОВОРИЛ ЛИ ВАМ ВРАЧ, ЧТО У ВАС ДИАГНОСТИРОВАНЫ КАКИЕ - ТО ИЗ ЭТИХ ЗАБОЛЕВАНИЙ?", font = 16)
    label.place(x=20, y=20)
    r21 = ttk.Radiobutton(new_root_21, text="ЗАБОЛЕВАНИЯ ССС, ГИПЕРТОНИЧЕСКАЯ БОЛЕЗНЬ, ИШЕМИЧЕСКАЯ БОЛЕЗНЬ СЕРДЦА", value=100, variable=quest1)
    r22 = ttk.Radiobutton(new_root_21, text="НИЧЕГО ИЗ ВЫШЕПЕРЕЧИСЛЕННОГО", value=0, variable=quest1)
    r21.place(x=20, y=50)
    r22.place(x=20, y=70)

    label = Label(new_root_21, text = "БЫЛИ ЛИ ДИАГНОСТИРОВАНЫ ЗАБОЛЕВАНИЯ ССС У ВАШИХ БЛИЗКИХ РОДСТВЕННИКОВ?", font = 16)
    label.place(x=20, y=100)
    r21 = ttk.Radiobutton(new_root_21, text="МАТЬ/РОДНЫЕ СЕСТРЫ ДО 65 ЛЕТ С ЗАБОЛЕВАНИЯМИ ССС", value=15, variable=quest2)
    r22 = ttk.Radiobutton(new_root_21, text="ОТЕЦ/РОДНЫЕ СЕСТРЫ ДО 55 ЛЕТ С ЗАБОЛЕВАНИЯМИ ССС", value=14, variable=quest2)
    r23 = ttk.Radiobutton(new_root_21, text="РОДИТЕЛИ С САХАРНЫМ ДИАБЕТОМ 2 ТИПА", value=13, variable=quest2)
    r24 = ttk.Radiobutton(new_root_21, text="НИЧЕГО ИЗ ВЫШЕПЕРЕЧИСЛЕННОГО", value=0, variable=quest2)
    r21.place(x=20, y=130)
    r22.place(x=20, y=150)
    r23.place(x=20, y=170)
    r24.place(x=20, y=190)

    btn = Button(new_root_21, text = "ВВЕСТИ", font=35, command = total1)
    btn.place(x=450, y=220) 
### ОКНО 2.1 (ИСТОРИЯ ССС) ###

def total1():
    total1_1=int(quest1.get())+int(quest2.get())
    anketa.append(total1_1)

### ОКНО 2.2 (ОБРАЗ ЖИЗНИ) ###
def anketa_2_2():
    new_root_22 = Toplevel(root)
    new_root_22.title("АНКЕТИРОВАНИЕ_ОБРАЗЖИЗНИ")
    new_root_22.geometry("925x1000")


    label = Label(new_root_22, text = "КАК ЧАСТО ВЫ ЗАНИМАЕТЕСЬ СПОРТОМ?", font = 16)
    label.place(x=20, y=20)
    r21 = ttk.Radiobutton(new_root_22, text="1 РАЗ В НЕДЕЛЮ", value=20, variable=quest3)
    r22 = ttk.Radiobutton(new_root_22, text="2-3 РАЗА В НЕДЕЛЮ", value=10, variable=quest3)
    r23 = ttk.Radiobutton(new_root_22, text="4-5 РАЗ В НЕДЕЛЮ", value=-10, variable=quest3)
    r24 = ttk.Radiobutton(new_root_22, text="5 И БОЛЕЕ РАЗ В НЕДЕЛЮ", value=-20, variable=quest3)
    r21.place(x=20, y=50)
    r22.place(x=20, y=70)
    r23.place(x=20, y=90)
    r24.place(x=20, y=110)

    label = Label(new_root_22, text = "КУРИТЕ ЛИ ВЫ?", font = 16)
    label.place(x=20, y=140)
    r21 = ttk.Radiobutton(new_root_22, text="НИКОГДА НЕ КУРИЛ", value=0, variable=quest4)
    r22 = ttk.Radiobutton(new_root_22, text="КУРИЛ РАННЕЕ, НО БРОСИЛ", value=10, variable=quest4)
    r23 = ttk.Radiobutton(new_root_22, text="ВЫКУРИВАЮ МЕНЕЕ 20 СИГАРЕТ В ДЕНЬ", value=50, variable=quest4)
    r24 = ttk.Radiobutton(new_root_22, text="ВЫКУРИВАЮ БОЛЕЕ 20 СИГАРЕТ В ДЕНЬ", value=80, variable=quest4)
    r21.place(x=20, y=170)
    r22.place(x=20, y=190)
    r23.place(x=20, y=210)
    r24.place(x=20, y=230)

    label = Label(new_root_22, text = "КУРИТЕ ЛИ ВЫ ПАССИВНО?", font = 16)
    label.place(x=20, y=260)
    r21 = ttk.Radiobutton(new_root_22, text="ДА", value=25, variable=quest5)
    r22 = ttk.Radiobutton(new_root_22, text="НЕТ", value=0, variable=quest5)
    r21.place(x=20, y=290)
    r22.place(x=20, y=310)

    label = Label(new_root_22, text = "КАК ЧАСТО ВЫ УПОТРЕБЛЯЕТЕ АЛКОГОЛЬНЫЕ НАПИТКИ?", font = 16)
    label.place(x=20, y=340)
    r21 = ttk.Radiobutton(new_root_22, text="НИКОГДА", value=0, variable=quest6)
    r22 = ttk.Radiobutton(new_root_22, text="1 РАЗ В НЕДЕЛЮ", value=5, variable=quest6)
    r23 = ttk.Radiobutton(new_root_22, text="2-3 РАЗА В НЕДЕЛЮ", value=10, variable=quest6)
    r24 = ttk.Radiobutton(new_root_22, text="4-5 РАЗ В НЕДЕЛЮ", value=20, variable=quest6)
    r25 = ttk.Radiobutton(new_root_22, text="5 И БОЛЕЕ РАЗ В НЕДЕЛЮ", value=50, variable=quest6)
    r21.place(x=20, y=370)
    r22.place(x=20, y=390)
    r23.place(x=20, y=410)
    r24.place(x=20, y=430)
    r25.place(x=20, y=450)

    label = Label(new_root_22, text = "КАКОЕ КОЛИЧЕСТВО АЛКОГОЛЬНЫХ НАПИТКОВ ВЫ ВЫПИВАЕТЕ ОБЫЧНО ЗА ОДИН РАЗ?", font = 16)
    label.place(x=20, y=480)
    r21 = ttk.Radiobutton(new_root_22, text="0 ПОРЦИЙ", value=0, variable=quest7)
    r22 = ttk.Radiobutton(new_root_22, text="1-2 ПОРЦИИ", value=10, variable=quest7)
    r23 = ttk.Radiobutton(new_root_22, text="3-4 ПОРЦИИ", value=20, variable=quest7)
    r24 = ttk.Radiobutton(new_root_22, text="5-6 ПОРЦИЙ", value=30, variable=quest7)
    r25 = ttk.Radiobutton(new_root_22, text="7-9 ПОРЦИЙ", value=40, variable=quest7)
    r21.place(x=20, y=510)
    r22.place(x=20, y=530)
    r23.place(x=20, y=550)
    r24.place(x=20, y=570)
    r25.place(x=20, y=590) 

    label = Label(new_root_22, text = "КАК ЧАСТО ВЫ УПОТРЕБЛЯЕТЕ 6 ИЛИ БОЛЕЕ ПОРЦИЙ АЛКОГОЛЯ?", font = 16)
    label.place(x=20, y=620)
    r21 = ttk.Radiobutton(new_root_22, text="НИКОГДА", value=0, variable=quest8)
    r22 = ttk.Radiobutton(new_root_22, text="РАЗ В МЕСЯЦ ИЛИ РЕЖЕ", value=20, variable=quest8)
    r23 = ttk.Radiobutton(new_root_22, text="2-4 РАЗА В МЕСЯЦ", value=50, variable=quest8)
    r24 = ttk.Radiobutton(new_root_22, text="2-3 РАЗА В НЕДЕЛЮ", value=70, variable=quest8)
    r25 = ttk.Radiobutton(new_root_22, text="БОЛЕЕ 4 РАЗ В НЕДЕЛЮ", value=90, variable=quest8)
    r21.place(x=20, y=650)
    r22.place(x=20, y=670)
    r23.place(x=20, y=690)
    r24.place(x=20, y=710)
    r25.place(x=20, y=730)

    btn = Button(new_root_22, text = "ВВЕСТИ", font=35, command = total2)
    btn.place(x=400, y=750) 
### ОКНО2.2 (ОБРАЗ ЖИЗНИ) ###


def total2():
    total2_1=int(quest3.get())+int(quest4.get())+int(quest5.get())+int(quest6.get())+int(quest7.get())+int(quest8.get())   
    anketa.append(total2_1)

### ОКНО2.3 (СТРЕСС В ЖИЗНИ) ###
def anketa_2_3():
    new_root_23 = Toplevel(root)
    new_root_23.title("АНКЕТИРОВАНИЕ_СТРЕССВЖИЗНИ")
    new_root_23.geometry("1100x550")

    label = Label(new_root_23, text = "ИСПЫТЫВАЛИ ЛИ ВЫ КАКОЕ-ТО ИЗ ЭТИХ ЧУВСТВ В ПОСЛЕДНЕЕ ВРЕМЯ(ТРЕВОГА/БЕСПОКОЙСТВО/СТРАХ)?", font = 16)
    label.place(x=20, y=20)
    r21 = ttk.Radiobutton(new_root_23, text="ЕЖЕНЕДЕЛЬНО ИЛИ ЧАЩЕ", value=40, variable=quest9)
    r22 = ttk.Radiobutton(new_root_23, text="ЕЖЕМЕСЯЧНО ИЛИ РЕЖЕ", value=20, variable=quest9)
    r23 = ttk.Radiobutton(new_root_23, text="НИКОГДА", value=0, variable=quest9)
    r21.place(x=20, y=50)
    r22.place(x=20, y=70)
    r23.place(x=20, y=90)

    label = Label(new_root_23, text = "ИСПЫТЫВАЛИ ЛИ ВЫ КАКОЕ-ТО ИЗ ЭТИХ ЧУВСТВ В ПОСЛЕДНЕЕ ВРЕМЯ(ДЕПРЕССИЯ/АПАТИЯ/ГРУСТЬ)?", font = 16)
    label.place(x=20, y=120)
    r21 = ttk.Radiobutton(new_root_23, text="ЕЖЕНЕДЕЛЬНО ИЛИ ЧАЩЕ", value=40, variable=quest10)
    r22 = ttk.Radiobutton(new_root_23, text="ЕЖЕМЕСЯЧНО ИЛИ РЕЖЕ", value=20, variable=quest10)
    r23 = ttk.Radiobutton(new_root_23, text="НИКОГДА", value=0, variable=quest10)
    r21.place(x=20, y=150)
    r22.place(x=20, y=170)
    r23.place(x=20, y=190)

    label = Label(new_root_23, text = "ВЫ ЛЕГКО ВПАДАЕТЕ В ГНЕВ И/ИЛИ ИСПЫТЫВАЕТЕ ЧУВСТВО ОБИДЫ К ОКРУЖАЮЩИМ?", font = 16)
    label.place(x=20, y=220)
    r21 = ttk.Radiobutton(new_root_23, text="ЕЖЕНЕДЕЛЬНО ИЛИ ЧАЩЕ", value=40, variable=quest11)
    r22 = ttk.Radiobutton(new_root_23, text="ЕЖЕМЕСЯЧНО ИЛИ РЕЖЕ", value=20, variable=quest11)
    r23 = ttk.Radiobutton(new_root_23, text="НИКОГДА", value=0, variable=quest11)
    r21.place(x=20, y=250)
    r22.place(x=20, y=270)
    r23.place(x=20, y=290)

    label = Label(new_root_23, text = "ПРОИСХОДИЛО ЛИ КАКОЕ-ТО ИЗ ЭТИХ СОБЫТИЙ В ВАШЕЙ ЖИЗНИ В ПОСЛЕДНЕЕ ВРЕМЯ?", font = 16)
    label.place(x=20, y=320)
    r21 = ttk.Radiobutton(new_root_23, text="СМЕРТЬ СУПРУГА/СУПРУГИ", value=30, variable=quest12)
    r22 = ttk.Radiobutton(new_root_23, text="РАЗВОД", value=20, variable=quest12)
    r23 = ttk.Radiobutton(new_root_23, text="СИЛЬНОЕ ЗАБОЛЕВАНИЕ/ТРАВМА", value=19, variable=quest12)
    r24 = ttk.Radiobutton(new_root_23, text="ЛИЧНЫЕ ТРУДНОСТИ", value=3, variable=quest12)
    r25 = ttk.Radiobutton(new_root_23, text="НИЧЕГО ИЗ ВЫШЕПЕРЕЧИСЛЕННОГО", value=0, variable=quest12)
    r21.place(x=20, y=350)
    r22.place(x=20, y=370)
    r23.place(x=20, y=390)
    r24.place(x=20, y=410)
    r25.place(x=20, y=430)

    btn = Button(new_root_23, text = "ВВЕСТИ", font=35, command = total3)
    btn.place(x=400, y=450) 
### ОКНО2.3 (СТРЕСС В ЖИЗНИ) ###

def total3():
    total3_1=int(quest9.get())+int(quest10.get())+int(quest11.get())+int(quest12.get())
    anketa.append(total3_1)

### ОКНО 2.4 (КАЧЕСТВО СНА) ###    
def anketa_2_4():
    new_root_24 = Toplevel(root)
    new_root_24.title("АНКЕТИРОВАНИЕ_КАЧЕСТВОСНА")
    new_root_24.geometry("550x340")

    label = Label(new_root_24, text = "СКОЛЬКО ЧАСОВ В СРЕДНЕМ ВЫ СПИТЕ?", font = 16)
    label.place(x=20, y=20)
    r21 = ttk.Radiobutton(new_root_24, text="0 - 4 ЧАСА", value=6, variable=quest13)
    r22 = ttk.Radiobutton(new_root_24, text="5 - 6 ЧАСОВ", value=3, variable=quest13)
    r23 = ttk.Radiobutton(new_root_24, text="7 - 8 ЧАСОВ", value=0, variable=quest13)
    r24 = ttk.Radiobutton(new_root_24, text="БОЛЕЕ 8 ЧАСОВ", value=-4, variable=quest13)
    r21.place(x=20, y=50)
    r22.place(x=20, y=70)
    r23.place(x=20, y=90)
    r24.place(x=20, y=110)

    label = Label(new_root_24, text = "ИСПЫТЫВАЛИ ЛИ ВЫ БЕССОНИЦУ, АПНОЭ и пр.?", font = 16)
    label.place(x=20, y=140)
    r21 = ttk.Radiobutton(new_root_24, text="ХРАП", value=4, variable=quest14)
    r22 = ttk.Radiobutton(new_root_24, text="АПНОЭ", value=10, variable=quest14)
    r23 = ttk.Radiobutton(new_root_24, text="БЕССОННИЦА", value=3, variable=quest14)
    r24 = ttk.Radiobutton(new_root_24, text="НИЧЕГО ИЗ ВЫШЕПЕРЕЧИСЛЕННОГО", value=0, variable=quest14)
    r21.place(x=20, y=170)
    r22.place(x=20, y=190)
    r23.place(x=20, y=210)
    r24.place(x=20, y=230)

    btn = Button(new_root_24, text = "ВВЕСТИ", font=35, command = total4)
    btn.place(x=225, y=265) 
### ОКНО 2.4 (КАЧЕСТВО СНА) ###

def total4():
    total4_1=int(quest13.get())+int(quest14.get())
    anketa.append(total4_1)

### ОКНО 2.5 (САХАР В КРОВИ) ###    
def anketa_2_5():
    new_root_25 = Toplevel(root)
    new_root_25.title("АНКЕТИРОВАНИЕ_САХАРВКРОВИ")
    new_root_25.geometry("675x300")

    label = Label(new_root_25, text = "ИСПЫТЫВАЕТЕ ЛИ ВЫ ТЯГУ К СЛАДКОМУ ИЛИ ШОКОЛАДУ?", font = 16)
    label.place(x=20, y=20)
    r21 = ttk.Radiobutton(new_root_25, text="ДА", value=10, variable=quest15)
    r22 = ttk.Radiobutton(new_root_25, text="НЕТ", value=0, variable=quest15)
    r21.place(x=20, y=50)
    r22.place(x=20, y=70)

    label = Label(new_root_25, text = "ЕСТЬ ЛИ У ВАС САХАРНЫЙ ДИАБЕТ?", font = 16)
    label.place(x=20, y=100)
    r21 = ttk.Radiobutton(new_root_25, text="ДА", value=100, variable=quest16)
    r22 = ttk.Radiobutton(new_root_25, text="НЕТ", value=0, variable=quest16)
    r21.place(x=20, y=130)
    r22.place(x=20, y=150)

    btn = Button(new_root_25, text = "ВВЕСТИ", font=35, command = total5)
    btn.place(x=400, y=200) 
### ОКНО 2.5 (САХАР В КРОВИ) ###

def total5():
    total5_1=int(quest15.get())+int(quest16.get())
    anketa.append(total5_1)

### ОКНО 2.6 (ВОСПАЛЕНИЕ И БОЛИ) ###    
def anketa_2_6():
    new_root_26 = Toplevel(root)
    new_root_26.title("АНКЕТИРОВАНИЕ_ВОСПАЛЕНИЯИБОЛИ")
    new_root_26.geometry("850x300")

    label = Label(new_root_26, text = "ИСПЫТЫВАЕТЕ ЛИ ВЫ КАКОЕ - ТО ИЗ ЭТИХ ЧУВСТВ ЧАЩЕ, ЧЕМ РАЗ ЗА МЕСЯЦ?", font = 16)
    label.place(x=20, y=20)
    r21 = ttk.Radiobutton(new_root_26, text="СВИСТЯЩЕЕ ДЫХАНИЕ, ЧИХАНИЕ, НАСМОРК, БОЛЬ В ГОРЛЕ, КАШЕЛЬ/ЗАЛОЖЕННОСТЬ НОСА", value=5, variable=quest17)
    r22 = ttk.Radiobutton(new_root_26, text="ГОЛОВНЫЕ БОЛИ ПОСЛЕ УПОТРЕБЛЕНИЯ НЕКОТОРЫХ ПРОДУКТОВ", value=4, variable=quest17)
    r23 = ttk.Radiobutton(new_root_26, text="НИЧЕГО ИЗ ВЫШЕПЕРЕЧИСЛЕННОГО", value=0, variable=quest17)
    r21.place(x=20, y=50)
    r22.place(x=20, y=70)
    r23.place(x=20, y=90)

    label = Label(new_root_26, text = "КАК ЧАСТО ВЫ ИСПЫТЫВАЕТЕ ПЕРИОДИЧЕСКИЕ БОЛИ?", font = 16)
    label.place(x=20, y=120)
    r21 = ttk.Radiobutton(new_root_26, text="ЕЖЕДНЕВНО", value=30, variable=quest18)
    r22 = ttk.Radiobutton(new_root_26, text="ЕЖЕНЕДЕЛЬНО", value=15, variable=quest18)
    r23 = ttk.Radiobutton(new_root_26, text="ЕЖЕМЕСЯЧНО ИЛИ РЕЖЕ", value=5, variable=quest18)
    r24 = ttk.Radiobutton(new_root_26, text="НИКОГДА", value=0, variable=quest18)
    r21.place(x=20, y=150)
    r22.place(x=20, y=170)
    r23.place(x=20, y=190)
    r24.place(x=20, y=210)

    btn = Button(new_root_26, text = "ВВЕСТИ", font=35, command = total6)
    btn.place(x=400, y=250) 
### ОКНО 2.6 (ВОСПАЛЕНИЕ И БОЛИ) ###

def total6():
    total6_1=int(quest17.get())+int(quest18.get())
    anketa.append(total6_1)

### ОКНО 2.7 (ПИТАНИЕ) ###
def anketa_2_7():
    new_root_27 = Toplevel(root)
    new_root_27.title("АНКЕТИРОВАНИЕ_ПИТАНИЕ")
    new_root_27.geometry("1200x1000")

    label = Label(new_root_27, text = "Как часто Вы употребляете жареную пищу?", font = 16)
    label.place(x=20, y=20)
    r21 = ttk.Radiobutton(new_root_27, text="МЕНЬШЕ, ЧЕМ РАЗ В НЕДЕЛЮ", value=0, variable=quest19)
    r22 = ttk.Radiobutton(new_root_27, text="1-2 РАЗА В НЕДЕЛЮ", value=1, variable=quest19)
    r23 = ttk.Radiobutton(new_root_27, text="3-6 РАЗ В НЕДЕЛЮ", value=5, variable=quest19)
    r24 = ttk.Radiobutton(new_root_27, text="КАЖДЫЙ ДЕНЬ", value=10, variable=quest19)
    r21.place(x=20, y=50)
    r22.place(x=20, y=70)
    r23.place(x=20, y=90)
    r24.place(x=20, y=110)

    label = Label(new_root_27, text = "Сколько порций продуктов с крахмалом Вы съедаете ежедневно?", font = 16)
    label.place(x=20, y=140)
    r21 = ttk.Radiobutton(new_root_27, text="0-2 ПОРЦИЙ ЕЖЕДНЕВНО", value=0, variable=quest20)
    r22 = ttk.Radiobutton(new_root_27, text="3 ПОРЦИИ ЕЖЕДНЕВНО", value=2, variable=quest20)
    r23 = ttk.Radiobutton(new_root_27, text="4 И БОЛЕЕ ПОРЦИЙ ЕЖЕДНЕВНО", value=4, variable=quest20)
    r21.place(x=20, y=170)
    r22.place(x=20, y=190)
    r23.place(x=20, y=210)

    label = Label(new_root_27, text = "КАК ЧАСТО В ДЕНЬ ВЫ УПОТРЕБЯЕТЕ СЛАДКОЕ?", font = 16)
    label.place(x=20, y=240)
    r21 = ttk.Radiobutton(new_root_27, text="НЕ УПОТРЕБЛЯЮ", value=0, variable=quest21)
    r22 = ttk.Radiobutton(new_root_27, text="1-2 ПОРЦИИ ЕЖЕДНЕВНО", value=2, variable=quest21)
    r23 = ttk.Radiobutton(new_root_27, text="БОЛЕЕ 2 ПОРЦИЙ ЕЖЕДНЕВНО", value=8, variable=quest21)
    r21.place(x=20, y=270)
    r22.place(x=20, y=290)
    r23.place(x=20, y=310)

    label = Label(new_root_27, text = "СКОЛЬКО ЧАЙНЫХ ЛОЖЕК ВЫ ДОБАВЛЯЕТЕ В ЕДУ/НАПИТКИ?", font = 16)
    label.place(x=20, y=340)
    r21 = ttk.Radiobutton(new_root_27, text="от 0 до 3", value=0, variable=quest22)
    r22 = ttk.Radiobutton(new_root_27, text="от 4 до 6", value=1, variable=quest22)
    r23 = ttk.Radiobutton(new_root_27, text="ОТ 7 до 9", value=4, variable=quest22)
    r24 = ttk.Radiobutton(new_root_27, text="10 И БОЛЕЕ", value=7, variable=quest22)
    r21.place(x=20, y=370)
    r22.place(x=20, y=390)
    r23.place(x=20, y=410)
    r24.place(x=20, y=430)

    label = Label(new_root_27, text = "КАК ЧАСТО ВЫ ЕДИТЕ РЫБУ?", font = 16)
    label.place(x=20, y=460)
    r21 = ttk.Radiobutton(new_root_27, text="РЕДКО", value=0, variable=quest23)
    r22 = ttk.Radiobutton(new_root_27, text="1-2 РАЗА В НЕДЕЛЮ", value=-2, variable=quest23)
    r23 = ttk.Radiobutton(new_root_27, text="3-6 РАЗ В НЕДЕЛЮ", value=-5, variable=quest23)
    r24 = ttk.Radiobutton(new_root_27, text="КАЖДЫЙ ДЕНЬ", value=-10, variable=quest23)
    r21.place(x=20, y=490)
    r22.place(x=20, y=510)
    r23.place(x=20, y=530)
    r24.place(x=20, y=550)

    label = Label(new_root_27, text = "СКОЛЬКО ФРУКТОВ(штук) ВЫ СЪЕДАЕТЕ?", font = 16)
    label.place(x=20, y=580)
    r21 = ttk.Radiobutton(new_root_27, text="ОБЫЧНО НИСКОЛЬКО", value=0, variable=quest24)
    r22 = ttk.Radiobutton(new_root_27, text="ОТ 1 ДО 3 ЕЖЕДНЕВНО", value=-2, variable=quest24)
    r23 = ttk.Radiobutton(new_root_27, text="4 И БОЛЕЕ ЕЖЕДНЕВНО", value=-4, variable=quest24)
    r21.place(x=20, y=610)
    r22.place(x=20, y=630)
    r23.place(x=20, y=650)

    label = Label(new_root_27, text = "СКОЛЬКО ОВОЩЕЙ(штук) ВЫ СЪЕДАЕТЕ?", font = 16)
    label.place(x=650, y=20)
    r21 = ttk.Radiobutton(new_root_27, text="ОБЫЧНО НИСКОЛЬКО", value=0, variable=quest25)
    r22 = ttk.Radiobutton(new_root_27, text="1-2 ЕЖЕДНЕВНО", value=-3, variable=quest25)
    r23 = ttk.Radiobutton(new_root_27, text="3-4 ЕЖЕДНЕВНО", value=-5, variable=quest25)
    r24 = ttk.Radiobutton(new_root_27, text="5 И БОЛЕЕ ЕЖЕДНЕВНО", value=-10, variable=quest25)
    r21.place(x=650, y=50)
    r22.place(x=650, y=70)
    r23.place(x=650, y=90)
    r24.place(x=650, y=110)

    label = Label(new_root_27, text = "СКОЛЬКО ЧАШЕК КОФЕ ВЫ ВЫПИВАЕТЕ ЗА ДЕНЬ?", font = 16)
    label.place(x=650, y=140)
    r21 = ttk.Radiobutton(new_root_27, text="ОБЫЧНО НИСКОЛЬКО", value=0, variable=quest26)
    r22 = ttk.Radiobutton(new_root_27, text="1-2 ЕЖЕДНЕВНО", value=2, variable=quest26)
    r23 = ttk.Radiobutton(new_root_27, text="3-4 ЕЖЕДНЕВНО", value=6, variable=quest26)
    r24 = ttk.Radiobutton(new_root_27, text="5 И БОЛЕЕ ЕЖЕДНЕВНО", value=10, variable=quest26)
    r21.place(x=650, y=170)
    r22.place(x=650, y=190)
    r23.place(x=650, y=210)
    r24.place(x=650, y=230)

    label = Label(new_root_27, text = "СКОЛЬКО МЛ ГАЗИРОВКИ ВЫ ОБЫЧНО ВЫПИВЕТЕ?", font = 16)
    label.place(x=650, y=260)
    r21 = ttk.Radiobutton(new_root_27, text="МЕНЕЕ 500МЛ В НЕДЕЛЮ", value=0, variable=quest27)
    r22 = ttk.Radiobutton(new_root_27, text="1000-2000 МЛ В НЕДЕЛЮ", value=2, variable=quest27)
    r23 = ttk.Radiobutton(new_root_27, text="3000-4000МЛ В НЕДЕЛЮ", value=4, variable=quest27)
    r24 = ttk.Radiobutton(new_root_27, text="5000МЛ И БОЛЕЕ В НЕДЕЛЮ", value=8, variable=quest27)
    r21.place(x=650, y=290)
    r22.place(x=650, y=310)
    r23.place(x=650, y=330)
    r24.place(x=650, y=350)

    label = Label(new_root_27, text = "СКОЛЬКО мл ВОДЫ ВЫ ВЫПИВАЕТЕ В ДЕНЬ?", font = 16)
    label.place(x=650, y=380)
    r21 = ttk.Radiobutton(new_root_27, text="0-500 ЕЖЕДНЕВНО", value=7, variable=quest28)
    r22 = ttk.Radiobutton(new_root_27, text="501-1250 ЕЖЕДНЕВНО", value=3, variable=quest28)
    r23 = ttk.Radiobutton(new_root_27, text="БОЛЕЕ 1250 ЕЖЕДНЕВНО", value=0, variable=quest28)
    r21.place(x=650, y=410)
    r22.place(x=650, y=430)
    r23.place(x=650, y=450)

    btn = Button(new_root_27, text = "ВВЕСТИ", font=35, command = itogi_anketa)
    btn.place(x=400, y=670) 
### ОКНО2.7 (АНКЕТИРОВАНИЕ_ПИТАНИЕ) ###



def itogi_anketa():
    total7_1=int(quest19.get())+int(quest20.get())+int(quest21.get())+int(quest22.get())+int(quest23.get())+int(quest24.get())+int(quest25.get())+int(quest26.get())+int(quest27.get())+int(quest28.get())
    anketa.append(total7_1) 

    if sum(anketa) <= 120:
        new_root_4 = Toplevel(root, bg = "green")
        new_root_4.title("АНКЕТИРОВАНИЕ_ИТОГИ")
        new_root_4.geometry("935x170")
        
        my_label_1 = Label(new_root_4, text = "ПО РЕЗУЛЬТАТАМ АНКЕТИРОВАНИЯ РИСКА РАЗВИТИЯ ЗАБОЛЕВАНИЙ ССС НЕ ВЫЯВЛЕНО", fg = "#FFF", font = 16, bg = "green") 
        my_label_1.place(x=20, y=20)
        my_label_4 = Label(new_root_4, text = "СОХРАНЯЙТЕ ЗДОРОВЫЙ ОБРАЗ ЖИЗНИ!", font = 16, fg = "#FFF", bg = "green") 
        my_label_4.place(x=260, y=55)
        my_label_5 = Label(new_root_4, text = "ВАМ НЕОБХОДИМО СНОВА ПРОЙТИ АНКЕТИРОВАНИЕ ЧЕРЕЗ 1 ГОД", fg = "#FFF", font = 16, bg = "green") 
        my_label_5.place(x=160, y=90)
        

        btn = Button(new_root_4, text = "ПОДРОБНЕЕ", font=35, command = grafik)
        btn.place(x=400, y=125)
        
    else: 
        new_root_4 = Toplevel(root, bg = "red")
        new_root_4.title("АНКЕТИРОВАНИЕ_ИТОГИ")
        new_root_4.geometry("935x250")
        
        my_label_1 = Label(new_root_4, text = "ПО РЕЗУЛЬТАТАМ АНКЕТИРОВАНИЯ ВЫЯВЛЕН РИСК РАЗВИТИЯ ЗАБОЛЕВАНИЙ ССС", fg = "#FFF", font = 16, bg = "red") 
        my_label_1.place(x=45, y=20)
        my_label_2 = Label(new_root_4, text = "ДЛЯ ПОСЛЕДУЮЩЕГО ОБСЛЕДОВАНИЯ ВАМ НЕОБХОДИМО СДАТЬ АНАЛИЗЫ:", font = 16, fg = "#FFF", bg = "red") 
        my_label_2.place(x=70, y=55)
        my_label_3 = Label(new_root_4, text = "АНАЛИЗ КРОВИ НА ЛПНП, ЛПВП, ТРИГЛИЦЕРИДЫ, САХАР, КОРТИЗОЛ", font = 16, fg = "#FFF", bg = "red") 
        my_label_3.place(x=135, y=90)
        my_label_4 = Label(new_root_4, text = "ГОМОЦИСТЕИН, C-РЕАКТИВНЫ БЕЛОК, ФИБРИНОГЕН", font = 16, fg = "#FFF", bg = "red") 
        my_label_4.place(x=180, y=125)
        my_label_5 = Label(new_root_4, text = "ПОКАЗАНИЯ АРТЕРИАЛЬНОГО ДАВЛЕНИЯ", font = 16, fg = "#FFF", bg = "red") 
        my_label_5.place(x=195, y=160)

        btn = Button(new_root_4, text = "ПОДРОБНЕЕ", font=35, command = grafik)
        btn.place(x=400, y=200)

def grafik():
    colour = []
    if anketa[0] <= 30:
        colour.append("green")
    elif anketa[0] > 30 and anketa[0] <= 50:
        colour.append("yellow")
    else:
        colour.append("red")
    if anketa[1] <= 25:
        colour.append("green")
    elif anketa[1] > 25 and anketa[1] <= 110:
        colour.append("yellow")
    else:
        colour.append("red")
    if anketa[2] <= 15:
        colour.append("green")
    elif anketa[2] > 15 and anketa[2] <= 40:
        colour.append("yellow")
    else:
        colour.append("red")
    if anketa[3] <= 5:
        colour.append("green")
    elif anketa[3] > 5 and anketa[3] <= 11:
        colour.append("yellow")
    else:
        colour.append("red")
    if anketa[4] <= 19:
        colour.append("green")
    elif anketa[4] > 19 and anketa[4] <= 49:
        colour.append("yellow")
    else:
        colour.append("red")
    if anketa[5] <= 9:
        colour.append("green")
    elif anketa[5] > 9 and anketa[5] <= 19:
        colour.append("yellow")
    else:
        colour.append("red")
    if anketa[6] <= 6:
        colour.append("green")
    elif anketa[6] > 6 and anketa[6] <= 13:
        colour.append("yellow")
    else:
        colour.append("red")
    plt.bar(kategorii, anketa, label='БАЛЛЫ', color = colour) 
    width = 1.5
    plt.legend()
    plt.show()        
### ОКНО3 (АНАЛИЗЫ) ###
def anketa_3():
    new_root_3 = Toplevel(root)
    new_root_3.title("АНАЛИЗЫ")
    new_root_3.geometry("700x500")

    my_label = Label(new_root_3, text = "ЛИПОПРОТЕИДЫ ВЫСОКОЙ ПЛОСКОСТИ", font = 16)
    my_label.place(x=20, y=20)
    l1 = ttk.Entry(new_root_3, font = 18, textvariable = lpvp)
    l1.place(x=450, y=20)

    my_label = Label(new_root_3, text = "ЛИПОПРОТЕИДЫ НИЗКОЙ ПЛОСКОСТИ", font = 16)
    my_label.place(x=20, y=60)
    l1 = ttk.Entry(new_root_3, font = 18, textvariable = lpnp)
    l1.place(x=450, y=60)

    my_label = Label(new_root_3, text = "ТРИГЛИЦЕРИДЫ", font = 16)
    my_label.place(x=20, y=100)
    l1 = ttk.Entry(new_root_3, font = 18, textvariable = trgl)
    l1.place(x=450, y=100)

    my_label = Label(new_root_3, text = "АРТЕРИАЛЬНОЕ ДАВЛЕНИЕ", font = 16)
    my_label.place(x=20, y=140)
    l1 = ttk.Entry(new_root_3, font = 18, textvariable = artdav)
    l1.place(x=450, y=140)

    my_label = Label(new_root_3, text = "C-РЕАКТИВНЫЙ БЕЛОК", font = 16)
    my_label.place(x=20, y=180)
    l1 = ttk.Entry(new_root_3, font = 18, textvariable = cbelok)
    l1.place(x=450, y=180)

    my_label = Label(new_root_3, text = "ГОМОЦИСТЕИН", font = 16)
    my_label.place(x=20, y=220)
    l1 = ttk.Entry(new_root_3, font = 18, textvariable = gmtsst)
    l1.place(x=450, y=220)

    my_label = Label(new_root_3, text = "ФИБРИНОГЕН", font = 16)
    my_label.place(x=20, y=260)
    l1 = ttk.Entry(new_root_3, font = 18, textvariable = fbrn)
    l1.place(x=450, y=260)

    my_label = Label(new_root_3, text = "ТИРЕОТРОПНЫЙ ГОРМОН", font = 16)
    my_label.place(x=20, y=300)
    l1 = ttk.Entry(new_root_3, font = 18, textvariable = ttg)
    l1.place(x=450, y=300)

    my_label = Label(new_root_3, text = "ГЛЮКОЗА", font = 16)
    my_label.place(x=20, y=340)
    l1 = ttk.Entry(new_root_3, font = 18, textvariable = glkz)
    l1.place(x=450, y=340)

    my_label = Label(new_root_3, text = "КОРТИЗОЛ", font = 16)
    my_label.place(x=20, y=380)
    l1 = ttk.Entry(new_root_3, font = 18, textvariable = krtzl)
    l1.place(x=450, y=380)

    btnanketa0 = Button(new_root_3, text="ВВЕСТИ", font=35, command = analizi_3)
    btnanketa0.place(x=305, y=430)
### ОКНО3 (АНАЛИЗЫ) ###

def analizi_3():
    analizi.append(float(lpvp.get()))
    analizi.append(float(lpnp.get()))
    analizi.append(float(trgl.get()))
    analizi.append(float(artdav.get()))
    analizi.append(float(cbelok.get()))
    analizi.append(float(gmtsst.get()))
    analizi.append(float(fbrn.get()))
    analizi.append(float(ttg.get()))
    analizi.append(float(glkz.get()))
    analizi.append(float(krtzl.get()))

##работа с excel##
def lpvp_1():
    if (baza[0] == 0 and (baza[1] >= 18 and baza[1] <= 20)):
        if analizi[0] >= 0.78 and analizi[0] <= 1.63:
            a = "ЛПВП В НОРМЕ"
            itogi.append(a)
        elif analizi[0] > 1.63:
            a = "ЛПВП ПОВЫШЕН"
            itogi.append(a)
        elif analizi[0] < 0.78:
            a = "ЛПВП ПОНИЖЕН"
            itogi.append(a)
    elif baza[0] == 0 and (baza[1] >= 21 and baza[1] <= 25):
        if analizi[0] >= 0.78 and analizi[0] <= 1.63:
            a = "ЛПВП В НОРМЕ"
            itogi.append(a)
        elif analizi[0] > 1.63:
            a = "ЛПВП ПОВЫШЕН"
            itogi.append(a) 
        elif analizi[0] < 0.78:
            a = "ЛПВП ПОНИЖЕН"
            itogi.append(a)
    elif baza[0] == 0 and (baza[1] >= 26 and baza[1] <= 30):
        if analizi[0] >= 0.8 and analizi[0] <= 1.63:
            a = "ЛПВП В НОРМЕ"
            itogi.append(a)
        elif analizi[0] > 1.63:
            a = "ЛПВП ПОВЫШЕН"
            itogi.append(a)
        elif analizi[0] < 0.8:
            a = "ЛПВП ПОНИЖЕН"
            itogi.append(a)
    elif baza[0] == 0 and (baza[1] >= 31 and baza[1] <= 35):
        if analizi[0] >= 0.72 and analizi[0] <= 1.63:
            a = "ЛПВП В НОРМЕ"
            itogi.append(a)
        elif analizi[0] > 1.63:
            a = "ЛПВП ПОВЫШЕН"
            itogi.append(a)
        elif analizi[0] < 0.72:
            a = "ЛПВП ПОНИЖЕН"
            itogi.append(a)
    elif baza[0] == 0 and (baza[1] >= 36 and baza[1] <= 40):
        if analizi[0] >= 0.75 and analizi[0] <= 1.6:
            a = "ЛПВП В НОРМЕ"
            itogi.append(a)
        elif analizi[0] > 1.6:
            a = "ЛПВП ПОВЫШЕН"
            itogi.append(a)
        elif analizi[0] < 0.75:
            a = "ЛПВП ПОНИЖЕН"
            itogi.append(a)
    elif baza[0] == 0 and (baza[1] >= 41 and baza[1] <= 45):
        if analizi[0] >= 0.7 and analizi[0] <= 1.73:
            a = "ЛПВП В НОРМЕ"
            itogi.append(a) 
        elif analizi[0] > 1.73:
            a = "ЛПВП ПОВЫШЕН"
            itogi.append(a)
        elif analizi[0] < 0.7:
            a = "ЛПВП ПОНИЖЕН"
            itogi.append(a)
    elif baza[0] == 0 and (baza[1] >= 46 and baza[1] <= 50):
        if analizi[0] >= 0.78 and analizi[0] <= 1.66:
            a = "ЛПВП В НОРМЕ"
            itogi.append(a)
        elif analizi[0] > 1.66:
            a = "ЛПВП ПОВЫШЕН"
            itogi.append(a) 
        elif analizi[0] < 0.78:
            a = "ЛПВП ПОНИЖЕН"
            itogi.append(a)
    elif baza[0] == 0 and (baza[1] >= 51 and baza[1] <= 55):
        if analizi[0] >= 0.72 and analizi[0] <= 1.63:
            a = "ЛПВП В НОРМЕ"
            itogi.append(a)
        elif analizi[0] > 1.63:
            a = "ЛПВП ПОВЫШЕН"
            itogi.append(a)
        elif analizi[0] < 0.72:
            a = "ЛПВП ПОНИЖЕН"
            itogi.append(a)
    elif (baza[0] == 0 and (baza[1] >= 56 and baza[1] <= 60)):
        if analizi[0] >= 0.72 and analizi[0] <= 1.84:
            a = "ЛПВП В НОРМЕ"
            itogi.append(a) 
        elif analizi[0] > 1.84:
            a = "ЛПВП ПОВЫШЕН"
            itogi.append(a)
        elif analizi[0] < 0.72:
            a = "ЛПВП ПОНИЖЕН"
            itogi.append(a)
    elif baza[0] == 0 and (baza[1] >= 61 and baza[1] <= 65):
        if analizi[0] >= 0.78 and analizi[0] <= 1.91:
            a = "ЛПВП В НОРМЕ"
            itogi.append(a)
        elif analizi[0] > 1.91:
            a = "ЛПВП ПОВЫШЕН"
            itogi.append(a) 
        elif analizi[0] < 0.78:
            a = "ЛПВП ПОНИЖЕН"
            itogi.append(a)
    elif baza[0] == 0 and baza[1]>=66:
        if analizi[0] >= 0.78 and analizi[0] <= 1.94:
            a = "ЛПВП В НОРМЕ"
            itogi.append(a) 
        elif analizi[0] > 1.94:
            a = "ЛПВП ПОВЫШЕН"
            itogi.append(a)
        elif analizi[0] < 0.78:
            a = "ЛПВП ПОНИЖЕН"
            itogi.append(a)
    ##ЛПВП ЖЕНЩИНЫ###
    elif (baza[0] == 1 and (baza[1] >= 18 and baza[1] <= 20)):
        if analizi[0] >= 1.53 and analizi[0] <= 3.55:
            a = "ЛПВП В НОРМЕ"
            itogi.append(a)
        elif analizi[0] > 1.53:
            a = "ЛПВП ПОВЫШЕН"
            itogi.append(a)
        elif analizi[0] < 3.55:
            a = "ЛПВП ПОНИЖЕН"
            itogi.append(a)
    elif baza[0] == 1 and (baza[1] >= 21 and baza[1] <= 25):
        if analizi[0] >= 1.48 and analizi[0] <= 4.12:
            a = "ЛПВП В НОРМЕ"
            itogi.append(a)
        elif analizi[0] > 4.12:
            a = "ЛПВП ПОВЫШЕН"
            itogi.append(a)
        elif analizi[0] < 1.48:
            a = "ЛПВП ПОНИЖЕН"
            itogi.append(a)
    elif baza[0] == 1 and (baza[1] >= 26 and baza[1] <= 30):
        if analizi[0] >= 1.84 and analizi[0] <= 4.25:
            a = "ЛПВП В НОРМЕ"
            itogi.append(a)
        elif analizi[0] > 4.25:
            a = "ЛПВП ПОВЫШЕН"
            itogi.append(a)
        elif analizi[0] < 1.84:
            a = "ЛПВП ПОНИЖЕН"
            itogi.append(a)
    elif baza[0] == 1 and (baza[1] >= 31 and baza[1] <= 35):
        if analizi[0] >= 1.81 and analizi[0] <= 4.04:
            a = "ЛПВП В НОРМЕ"
            itogi.append(a)
        elif analizi[0] > 4.04:
            a = "ЛПВП ПОВЫШЕН"
            itogi.append(a)
        elif analizi[0] < 1.81:
            a = "ЛПВП ПОНИЖЕН"
            itogi.append(a)
    elif baza[0] == 1 and (baza[1] >= 36 and baza[1] <= 40):
        if analizi[0] >= 1.94 and analizi[0] <= 4.45:
            a = "ЛПВП В НОРМЕ"
            itogi.append(a)
        elif analizi[0] > 4.45:
            a = "ЛПВП ПОВЫШЕН"
            itogi.append(a)
        elif analizi[0] < 1.94:
            a = "ЛПВП ПОНИЖЕН"
            itogi.append(a)
    elif baza[0] == 1 and (baza[1] >= 41 and baza[1] <= 45):
        if analizi[0] >= 1.92 and analizi[0] <= 4.51:
            a = "ЛПВП В НОРМЕ"
            itogi.append(a)
        elif analizi[0] > 1.73:
            a = "ЛПВП ПОВЫШЕН"
            itogi.append(a) 
        elif analizi[0] < 0.7:
            a = "ЛПВП ПОНИЖЕН"
            itogi.append(a)
    elif baza[0] == 1 and (baza[1] >= 46 and baza[1] <= 50):
        if analizi[0] >= 2.05 and analizi[0] <= 4.82:
            a = "ЛПВП В НОРМЕ"
            itogi.append(a)
        elif analizi[0] > 4.82:
            a = "ЛПВП ПОВЫШЕН"
            itogi.append(a)
        elif analizi[0] < 2.05:
            a = "ЛПВП ПОНИЖЕН"
            itogi.append(a)
    elif baza[0] == 1 and (baza[1] >= 51 and baza[1] <= 55):
        if analizi[0] >= 2.28 and analizi[0] <= 5.21:
            a = "ЛПВП В НОРМЕ"
            itogi.append(a)
        elif analizi[0] > 5.21:
            a = "ЛПВП ПОВЫШЕН"
            itogi.append(a)
        elif analizi[0] < 2.28:
            a = "ЛПВП ПОНИЖЕН"
            itogi.append(a)
    elif (baza[0] == 1 and (baza[1] >= 56 and baza[1] <= 60)):
        if analizi[0] >= 2.31 and analizi[0] <= 5.44:
            a = "ЛПВП В НОРМЕ"
            itogi.append(a)
        elif analizi[0] > 5.44:
            a = "ЛПВП ПОВЫШЕН"
            itogi.append(a)
        elif analizi[0] < 2.31:
            a = "ЛПВП ПОНИЖЕН"
            itogi.append(a)
    elif baza[0] == 1 and (baza[1] >= 61 and baza[1] <= 65):
        if analizi[0] >= 2.59 and analizi[0] <= 5.80:
            a = "ЛПВП В НОРМЕ"
            itogi.append(a) 
        elif analizi[0] > 5.80:
            a = "ЛПВП ПОВЫШЕН"
            itogi.append(a)
        elif analizi[0] < 2.59:
            a = "ЛПВП ПОНИЖЕН"
            itogi.append(a)
    elif baza[0] == 0 and baza[1]>=66:
        if analizi[0] >= 2.38 and analizi[0] <= 5.72:
            a = "ЛПВП В НОРМЕ"
            itogi.append(a)
        elif analizi[0] > 5.72:
            a = "ЛПВП ПОВЫШЕН"
            itogi.append(a)
        elif analizi[0] < 2.38:
            a = "ЛПВП ПОНИЖЕН"
            itogi.append(a)
def lpnp_1():
    if (baza[0] == 0 and (baza[1] >= 18 and baza[1] <= 20)):
        if analizi[1] >= 1.61 and analizi[1] <= 3.37:
            b = "ЛПНП В НОРМЕ"
            itogi.append(b)
        elif analizi[1] > 3.37:
            b = "ЛПНП ПОВЫШЕН"
            itogi.append(b)
        elif analizi[1] < 1.61:
            b = "ЛПНП ПОНИЖЕН"
            itogi.append(b)
    elif baza[0] == 0 and (baza[1] >= 21 and baza[1] <= 25):
        if analizi[1] >= 1.71 and analizi[1] <= 3.81:
            b = "ЛПНП В НОРМЕ"
            itogi.append(b)
        elif analizi[1] > 3.81:
            b = "ЛПНП ПОВЫШЕН"
            itogi.append(b)
        elif analizi[1] < 1.71:
            b = "ЛПНП ПОНИЖЕН"
            itogi.append(b)
    elif baza[0] == 0 and (baza[1] >= 26 and baza[1] <= 30):
        if analizi[1] >= 1.81 and analizi[1] <= 4.27:
            b = "ЛПНП В НОРМЕ"
            itogi.append(b)
        elif analizi[1] > 4.27:
            b = "ЛПНП ПОВЫШЕН"
            itogi.append(b)
        elif analizi[1] < 1.81:
            b = "ЛПНП ПОНИЖЕН"
            itogi.append(b)
    elif baza[0] == 0 and (baza[1] >= 31 and baza[1] <= 35):
        if analizi[1] >= 2.02 and analizi[1] <= 4.79:
            b = "ЛПНП В НОРМЕ"
            itogi.append(b)
        elif analizi[1] > 4.79:
            b = "ЛПНП ПОВЫШЕН"
            itogi.append(b)
        elif analizi[1] < 2.02:
            b = "ЛПНП ПОНИЖЕН"
            itogi.append(b)
    elif baza[0] == 0 and (baza[1] >= 36 and baza[1] <= 40):
        if analizi[1] >= 2.10 and analizi[1] <= 4.90:
            b = "ЛПНП В НОРМЕ"
            itogi.append(b)
        elif analizi[1] > 4.90:
            b = "ЛПНП ПОВЫШЕН"
            itogi.append(b)
        elif analizi[1] < 2.10:
            b = "ЛПНП ПОНИЖЕН"
            itogi.append(b)
    elif baza[0] == 0 and (baza[1] >= 41 and baza[1] <= 45):
        if analizi[1] >= 2.25 and analizi[1] <= 4.82:
            b = "ЛПНП В НОРМЕ"
            itogi.append(b)
        elif analizi[1] > 4.82:
            b = "ЛПНП ПОВЫШЕН"
            itogi.append(b)
        elif analizi[1] < 2.25:
            b = "ЛПНП ПОНИЖЕН"
            itogi.append(b)
    elif baza[0] == 0 and (baza[1] >= 46 and baza[1] <= 50):
        if analizi[1] >= 2.51 and analizi[1] <= 5.23:
            b = "ЛПНП В НОРМЕ"
            itogi.append(b)
        elif analizi[1] > 5.23:
            b = "ЛПНП ПОВЫШЕН"
            itogi.append(b)
        elif analizi[1] < 2.51:
            b = "ЛПНП ПОНИЖЕН"
            itogi.append(b)
    elif baza[0] == 0 and (baza[1] >= 51 and baza[1] <= 55):
        if analizi[1] >= 2.31 and analizi[1] <= 5.10:
            b = "ЛПНП В НОРМЕ"
            itogi.append(b)
        elif analizi[1] > 5.10:
            b = "ЛПНП ПОВЫШЕН"
            itogi.append(b)
        elif analizi[1] < 2.31:
            b = "ЛПНП ПОНИЖЕН"
            itogi.append(b) 
    elif (baza[0] == 0 and (baza[1] >= 56 and baza[1] <= 60)):
        if analizi[1] >= 2.28 and analizi[1] <= 5.26:
            b = "ЛПНП В НОРМЕ"
            itogi.append(b)
        elif analizi[1] > 5.26:
            b = "ЛПНП ПОВЫШЕН"
            itogi.append(b)
        elif analizi[1] < 2.28:
            b = "ЛПНП ПОНИЖЕН"
            itogi.append(b)
    elif baza[0] == 0 and (baza[1] >= 61 and baza[1] <= 65):
        if analizi[1] >= 2.15 and analizi[1] <= 5.44:
            b = "ЛПНП В НОРМЕ"
            itogi.append(b)
        elif analizi[1] > 5.44:
            b = "ЛПНП ПОВЫШЕН"
            itogi.append(b)
        elif analizi[1] < 2.15:
            b = "ЛПНП ПОНИЖЕН"
            itogi.append(b)
    elif baza[0] == 0 and baza[1]>=66:
        if analizi[1] >= 2.54 and analizi[1] <= 5.44:
            b = "ЛПНП В НОРМЕ"
            itogi.append(b)
        elif analizi[1] > 5.44:
            b = "ЛПНП ПОВЫШЕН"
            itogi.append(b) 
        elif analizi[1] < 2.54:
            b = "ЛПНП ПОНИЖЕН"
            itogi.append(b)
    ##ЛПНП ЖЕНЩИНЫ###
    if (baza[0] == 1 and (baza[1] >= 18 and baza[1] <= 20)):
        if analizi[1] >= 1.53 and analizi[1] <= 3.55:
            b = "ЛПНП В НОРМЕ"
            itogi.append(b)
        elif analizi[1] > 3.55:
            b = "ЛПНП ПОВЫШЕН"
            itogi.append(b)
        elif analizi[1] < 1.53:
            b = "ЛПНП ПОНИЖЕН"
            itogi.append(b)
    elif baza[0] == 1 and (baza[1] >= 21 and baza[1] <= 25):
        if analizi[1] >= 1.48 and analizi[1] <= 4.12:
            b = "ЛПНП В НОРМЕ"
            itogi.append(b)
        elif analizi[1] > 4.12:
            b = "ЛПНП ПОВЫШЕН"
            itogi.append(b)
        elif analizi[1] < 1.48:
            b = "ЛПНП ПОНИЖЕН"
            itogi.append(b)
    elif baza[0] == 1 and (baza[1] >= 26 and baza[1] <= 30):
        if analizi[1] >= 1.84 and analizi[1] <= 4.25:
            b = "ЛПНП В НОРМЕ"
            itogi.append(b)
        elif analizi[1] > 4.25:
            b = "ЛПНП ПОВЫШЕН"
            itogi.append(b)
        elif analizi[1] < 1.84:
            b = "ЛПНП ПОНИЖЕН"
            itogi.append(b)
    elif baza[0] == 1 and (baza[1] >= 31 and baza[1] <= 35):
        if analizi[1] >= 1.81 and analizi[1] <= 4.04:
            b = "ЛПНП В НОРМЕ"
            itogi.append(b)
        elif analizi[1] > 4.04:
            b = "ЛПНП ПОВЫШЕН"
            itogi.append(b)
        elif analizi[1] < 1.81:
            b = "ЛПНП ПОНИЖЕН"
            itogi.append(b)
    elif baza[0] == 1 and (baza[1] >= 36 and baza[1] <= 40):
        if analizi[1] >= 1.94 and analizi[1] <= 4.45:
            b = "ЛПНП В НОРМЕ"
            itogi.append(b)
        elif analizi[1] > 4.45:
            b = "ЛПНП ПОВЫШЕН"
            itogi.append(b)
        elif analizi[1] < 1.94:
            b = "ЛПНП ПОВЫШЕН"
            itogi.append(b)
    elif baza[0] == 1 and (baza[1] >= 41 and baza[1] <= 45):
        if analizi[1] >= 1.92 and analizi[1] <= 4.51:
            b = "ЛПНП В НОРМЕ"
            itogi.append(b)
        elif analizi[1] > 4.51:
            b = "ЛПНП ПОВЫШЕН"
            itogi.append(b)
        elif analizi[1] < 1.92:
            b = "ЛПНП ПОНИЖЕН"
            itogi.append(b)
    elif baza[0] == 1 and (baza[1] >= 46 and baza[1] <= 50):
        if analizi[1] >= 2.05 and analizi[1] <= 4.82:
            b = "ЛПНП В НОРМЕ"
            itogi.append(b)
        elif analizi[1] > 4.82:
            b = "ЛПНП ПОВЫШЕН"
            itogi.append(b)
        elif analizi[1] < 2.05:
            b = "ЛПНП ПОНИЖЕН"
            itogi.append(b)
    elif baza[0] == 1 and (baza[1] >= 51 and baza[1] <= 55):
        if analizi[1] >= 2.28 and analizi[1] <= 5.21:
            b = "ЛПНП В НОРМЕ"
            itogi.append(b)
        elif analizi[1] > 5.21:
            b = "ЛПНП ПОВЫШЕН"
            itogi.append(b)
        elif analizi[1] < 2.28:
            b = "ЛПНП ПОНИЖЕН"
            itogi.append(b)
    elif (baza[0] == 1 and (baza[1] >= 56 and baza[1] <= 60)):
        if analizi[1] >= 2.31 and analizi[1] <= 5.44:
            b = "ЛПНП В НОРМЕ"
            itogi.append(b)
        elif analizi[1] > 5.44:
            b = "ЛПНП ПОВЫШЕН"
            itogi.append(b)
        elif analizi[1] < 2.31:
            b = "ЛПНП ПОНИЖЕН"
            itogi.append(b)
    elif baza[0] == 1 and (baza[1] >= 61 and baza[1] <= 65):
        if analizi[1] >= 2.59 and analizi[1] <= 5.80:
            b = "ЛПНП В НОРМЕ"
            itogi.append(b)
        elif analizi[1] > 5.80:
            b = "ЛПНП ПОВЫШЕН"
            itogi.append(b)
        elif analizi[1] < 2.59:
            b = "ЛПНП ПОНИЖЕН"
            itogi.append(b)
    elif baza[0] == 1 and baza[1]>=66:
        if analizi[1] >= 2.38 and analizi[1] <= 5.72:
            b = "ЛПНП В НОРМЕ"
            itogi.append(b)
        elif analizi[1] > 5.72:
            b = "ЛПНП ПОВЫШЕН"
            itogi.append(b)
        elif analizi[1] < 2.38:
            b = "ЛПНП ПОНИЖЕН"
            itogi.append(b)

def trgl_1():
    if (baza[0] == 0 and (baza[1] >= 18 and baza[1] <= 20)):
        if analizi[2] >= 0.45 and analizi[2] <= 1.81:
            с = "ТРИГЛИЦЕРИДЫ В НОРМЕ"
            itogi.append(с)
        elif analizi[2] > 1.81:
            с = "ТРИГЛИЦЕРИДЫ ПОВЫШЕНЫ"
            itogi.append(с)
        elif analizi[2] < 0.45:
            с = "ТРИГЛИЦЕРИДЫ ПОНИЖЕНЫ"
            itogi.append(с)
    elif baza[0] == 0 and (baza[1] >= 21 and baza[1] <= 25):
        if analizi[2] >= 0.5 and analizi[2] <= 2.27:
            с = "ТРИГЛИЦЕРИДЫ В НОРМЕ"
            itogi.append(с)
        elif analizi[2] > 2.27:
            с = "ТРИГЛИЦЕРИДЫ ПОВЫШЕНЫ"
            itogi.append(с)
        elif analizi[2] < 0.5:
            с = "ТРИГЛИЦЕРИДЫ ПОНИЖЕНЫ"
            itogi.append(с)
    elif baza[0] == 0 and (baza[1] >= 26 and baza[1] <= 30):
        if analizi[2] >= 0.52 and analizi[2] <= 2.81:
            с = "ТРИГЛИЦЕРИДЫ В НОРМЕ"
            itogi.append(с)
        elif analizi[2] > 2.81:
            с = "ТРИГЛИЦЕРИДЫ ПОВЫШЕНЫ"
            itogi.append(с)
        elif analizi[2] < 0.52:
            с = "ТРИГЛИЦЕРИДЫ ПОНИЖЕНЫ"
            itogi.append(с)
    elif baza[0] == 0 and (baza[1] >= 31 and baza[1] <= 35):
        if analizi[2] >= 0.56 and analizi[2] <= 3.01:
            с = "ТРИГЛИЦЕРИДЫ В НОРМЕ"
            itogi.append(с)
        elif analizi[2] > 3.01:
            с = "ТРИГЛИЦЕРИДЫ ПОВЫШЕНЫ"
            itogi.append(с)
        elif analizi[2] < 0.56:
            с = "ТРИГЛИЦЕРИДЫ ПОНИЖЕНЫ"
            itogi.append(с)
    elif baza[0] == 0 and (baza[1] >= 36 and baza[1] <= 40):
        if analizi[2] >= 0.61 and analizi[2] <= 3.62:
            с = "ТРИГЛИЦЕРИДЫ В НОРМЕ"
            itogi.append(с)
        elif analizi[2] > 3.62:
            с = "ТРИГЛИЦЕРИДЫ ПОВЫШЕНЫ"
            itogi.append(с)
        elif analizi[2] < 0.61:
            с = "ТРИГЛИЦЕРИДЫ ПОНИЖЕНЫ"
            itogi.append(с)
    elif baza[0] == 0 and (baza[1] >= 41 and baza[1] <= 45):
        if analizi[2] >= 0.62 and analizi[2] <= 3.61:
            с = "ТРИГЛИЦЕРИДЫ В НОРМЕ"
            itogi.append(с)
        elif analizi[2] > 3.61:
            с = "ТРИГЛИЦЕРИДЫ ПОВЫШЕНЫ"
            itogi.append(с)
        elif analizi[2] < 0.62:
            с = "ТРИГЛИЦЕРИДЫ ПОНИЖЕНЫ"
            itogi.append(с) 
    elif baza[0] == 0 and (baza[1] >= 46 and baza[1] <= 50):
        if analizi[2] >= 0.65 and analizi[2] <= 3.70:
            с = "ТРИГЛИЦЕРИДЫ В НОРМЕ"
            itogi.append(с)
        elif analizi[2] > 3.70:
            с = "ТРИГЛИЦЕРИДЫ ПОВЫШЕНЫ"
            itogi.append(с)
        elif analizi[2] < 0.65:
            с = "ТРИГЛИЦЕРИДЫ ПОНИЖЕНЫ"
            itogi.append(с)
    elif baza[0] == 0 and (baza[1] >= 51 and baza[1] <= 55):
        if analizi[2] >= 0.65 and analizi[2] <= 3.61:
            с = "ТРИГЛИЦЕРИДЫ В НОРМЕ"
            itogi.append(с)
        elif analizi[2] > 3.61:
            с = "ТРИГЛИЦЕРИДЫ ПОВЫШЕНЫ"
            itogi.append(с)
        elif analizi[2] < 0.65:
            с = "ТРИГЛИЦЕРИДЫ ПОНИЖЕНЫ"
            itogi.append(с) 
    elif (baza[0] == 0 and (baza[1] >= 56 and baza[1] <= 60)):
        if analizi[2] >= 0.65 and analizi[2] <= 3.23:
            с = "ТРИГЛИЦЕРИДЫ В НОРМЕ"
            itogi.append(с)
        elif analizi[2] > 3.23:
            с = "ТРИГЛИЦЕРИДЫ ПОВЫШЕНЫ"
            itogi.append(с)
        elif analizi[2] < 0.65:
            с = "ТРИГЛИЦЕРИДЫ ПОНИЖЕНЫ"
            itogi.append(с)
    elif baza[0] == 0 and (baza[1] >= 61 and baza[1] <= 65):
        if analizi[2] >= 0.65 and analizi[2] <= 3.29:
            с = "ТРИГЛИЦЕРИДЫ В НОРМЕ"
            itogi.append(с)
        elif analizi[2] > 3.29:
            с = "ТРИГЛИЦЕРИДЫ ПОВЫШЕНЫ"
            itogi.append(с)
        elif analizi[2] < 0.65:
            с = "ТРИГЛИЦЕРИДЫ ПОНИЖЕНЫ"
            itogi.append(с)
    elif baza[0] == 0 and baza[1]>=66:
        if analizi[2] >= 0.62 and analizi[2] <= 2.94:
            с = "ТРИГЛИЦЕРИДЫ В НОРМЕ"
            itogi.append(с)
        elif analizi[2] > 2.94:
            с = "ТРИГЛИЦЕРИДЫ ПОВЫШЕНЫ"
            itogi.append(с)
        elif analizi[2] < 0.62:
            с = "ТРИГЛИЦЕРИДЫ ПОНИЖЕНЫ"
            itogi.append(с)
    ##ТРИГЛИЦЕРИДЫ ЖЕНЩИНЫ###
    if (baza[0] == 1 and (baza[1] >= 18 and baza[1] <= 20)):
        if analizi[2] >= 0.4 and analizi[2] <= 1.53:
            с = "ТРИГЛИЦЕРИДЫ В НОРМЕ"
            itogi.append(с)
        elif analizi[2] > 1.53:
            с = "ТРИГЛИЦЕРИДЫ ПОВЫШЕНЫ"
            itogi.append(с)
        elif analizi[2] < 0.4:
            с = "ТРИГЛИЦЕРИДЫ ПОНИЖЕНЫ"
            itogi.append(с)
    elif baza[0] == 1 and (baza[1] >= 21 and baza[1] <= 25):
        if analizi[2] >= 0.41 and analizi[2] <= 1.48:
            с = "ТРИГЛИЦЕРИДЫ В НОРМЕ"
            itogi.append(с)
        elif analizi[2] > 1.48:
            с = "ТРИГЛИЦЕРИДЫ ПОВЫШЕНЫ"
            itogi.append(с)
        elif analizi[2] < 0.41:
            с = "ТРИГЛИЦЕРИДЫ ПОНИЖЕНЫ"
            itogi.append(с)
    elif baza[0] == 1 and (baza[1] >= 26 and baza[1] <= 30):
        if analizi[2] >= 0.42 and analizi[2] <= 1.63:
            с = "ТРИГЛИЦЕРИДЫ В НОРМЕ"
            itogi.append(с)
        elif analizi[2] > 1.63:
            с = "ТРИГЛИЦЕРИДЫ ПОВЫШЕНЫ"
            itogi.append(с)
        elif analizi[2] < 0.42:
            с = "ТРИГЛИЦЕРИДЫ ПОНИЖЕНЫ"
            itogi.append(с)
    elif baza[0] == 1 and (baza[1] >= 31 and baza[1] <= 35):
        if analizi[2] >= 0.44 and analizi[2] <= 1.7:
            с = "ТРИГЛИЦЕРИДЫ В НОРМЕ"
            itogi.append(с)
        elif analizi[2] > 1.7:
            с = "ТРИГЛИЦЕРИДЫ ПОВЫШЕНЫ"
            itogi.append(с)
        elif analizi[2] < 0.44:
            с = "ТРИГЛИЦЕРИДЫ ПОНИЖЕНЫ"
            itogi.append(с)
    elif baza[0] == 1 and (baza[1] >= 36 and baza[1] <= 40):
        if analizi[2] >= 0.45 and analizi[2] <= 1.99:
            с = "ТРИГЛИЦЕРИДЫ В НОРМЕ"
            itogi.append(с)
        elif analizi[2] > 1.99:
            с = "ТРИГЛИЦЕРИДЫ ПОВЫШЕНЫ"
            itogi.append(с)
        elif analizi[2] < 0.45:
            с = "ТРИГЛИЦЕРИДЫ ПОНИЖЕНЫ"
            itogi.append(с)
    elif baza[0] == 1 and (baza[1] >= 41 and baza[1] <= 45):
        if analizi[2] >= 0.51 and analizi[2] <= 2.16:
            с = "ТРИГЛИЦЕРИДЫ В НОРМЕ"
            itogi.append(с) 
        elif analizi[2] > 2.16:
            с = "ТРИГЛИЦЕРИДЫ ПОВЫШЕНЫ"
            itogi.append(с)
        elif analizi[2] < 0.51:
            с = "ТРИГЛИЦЕРИДЫ ПОНИЖЕНЫ"
            itogi.append(с)
    elif baza[0] == 1 and (baza[1] >= 46 and baza[1] <= 50):
        if analizi[2] >= 0.52 and analizi[2] <= 2.42:
            с = "ТРИГЛИЦЕРИДЫ В НОРМЕ"
            itogi.append(с)
        elif analizi[2] > 2.42:
            с = "ТРИГЛИЦЕРИДЫ ПОВЫШЕНЫ"
            itogi.append(с)
        elif analizi[2] < 0.52:
            с = "ТРИГЛИЦЕРИДЫ ПОНИЖЕНЫ"
            itogi.append(с)
    elif baza[0] == 1 and (baza[1] >= 51 and baza[1] <= 55):
        if analizi[2] >= 0.59 and analizi[2] <= 2.63:
            с = "ТРИГЛИЦЕРИДЫ В НОРМЕ"
            itogi.append(с)
        elif analizi[2] > 2.63:
            с = "ТРИГЛИЦЕРИДЫ ПОВЫШЕНЫ"
            itogi.append(с)
        elif analizi[2] < 0.59:
            с = "ТРИГЛИЦЕРИДЫ ПОНИЖЕНЫ"
            itogi.append(с)
    elif (baza[0] == 1 and (baza[1] >= 56 and baza[1] <= 60)):
        if analizi[2] >= 0.62 and analizi[2] <= 2.96:
            с = "ТРИГЛИЦЕРИДЫ В НОРМЕ"
            itogi.append(с)
        elif analizi[2] > 2.96:
            с = "ТРИГЛИЦЕРИДЫ ПОВЫШЕНЫ"
            itogi.append(с)
        elif analizi[2] < 0.62:
            с = "ТРИГЛИЦЕРИДЫ ПОНИЖЕНЫ"
            itogi.append(с)
    elif baza[0] == 1 and (baza[1] >= 61 and baza[1] <= 65):
        if analizi[2] >= 0.63 and analizi[2] <= 2.7:
            с = "ТРИГЛИЦЕРИДЫ В НОРМЕ"
            itogi.append(с)
        elif analizi[2] > 2.7:
            с = "ТРИГЛИЦЕРИДЫ ПОВЫШЕНЫ"
            itogi.append(с)
        elif analizi[2] < 0.63:
            с = "ТРИГЛИЦЕРИДЫ ПОНИЖЕНЫ"
            itogi.append(с)
    elif baza[0] == 1 and baza[1]>=66:
        if analizi[2] >= 0.68 and analizi[2] <= 2.71:
            с = "ТРИГЛИЦЕРИДЫ В НОРМЕ"
            itogi.append(с)
        elif analizi[2] > 2.71:
            с = "ТРИГЛИЦЕРИДЫ ПОВЫШЕНЫ"
            itogi.append(с)
        elif analizi[2] < 0.68:
            с = "ТРИГЛИЦЕРИДЫ ПОНИЖЕНЫ"
            itogi.append(с)
def artdav_1():
    if baza[1] < 60:
        if analizi[3] >= 35 and analizi[3] <= 45:
            d = "АРТЕРИАЛЬНОЕ ДАВЛЕНИЕ В НОРМЕ"
            itogi.append(d)
        elif analizi[3] > 45 or analizi[3] < 35:
            d = "АРТЕРИАЛЬНОЕ ДАВЛЕНИЕ НЕ В НОРМЕ"
            itogi.append(d)
    if baza[1] >= 60:
        if analizi[3] >= 35 and analizi[3] <= 50:
            d =  "АРТЕРИАЛЬНОЕ ДАВЛЕНИЕ В НОРМЕ"
            itogi.append(d)
        else:
            d = "АРТЕРИАЛЬНОЕ ДАВЛЕНИЕ НЕ В НОРМЕ"
            itogi.append(d)
            
def cbelok_1():
    if analizi[4] >= 0 and analizi[4] <= 1:
        e = "С-РЕАКТИВНЫЙ БЕЛОК В НОРМЕ"
        itogi.append(e)
    elif analizi[4] > 1 and analizi[4] <= 3:
        e = "С-РЕАКТИВНЫЙ БЕЛОК СЛЕГКА ПРЕВЫШАЕТ НОРМУ"
        itogi.append(e)
    elif analizi[4] > 3:
        e = "С-РЕАКТИВНЫЙ ЗНАЧИТЕЛЬНО ПРЕВЫШАЕТ НОРМУ"
        itogi.append(e)
def gmst_1():
    if baza[0] == 0:
        if analizi[5] >= 5.46 and analizi[5] <= 16.20:
            f = "ГОМОЦИСТЕИН В НОРМЕ"
            itogi.append(f)
        elif analizi[5] > 16.2:
            f = "ГОМОЦИСТЕИН ПОВЫШЕН"
            itogi.append(f)
        elif analizi[5] < 5.46:
            f = "ГОМОЦИСТЕИН ПОНИЖЕН"
            itogi.append(f)
    elif baza[0] == 1:
        if analizi[5] >= 4.44 and analizi[5] <= 13.56:
            f = "ГОМОЦИСТЕИН В НОРМЕ"
            itogi.append(f)
        elif analizi[5] > 13.56:
            f = "ГОМОЦИСТЕИН ПОВЫШЕН"
            itogi.append(f)
        elif analizi[5] < 4.44:
            f = "ГОМОЦИСТЕИН ПОНИЖЕН"
            itogi.append(f)
def fbrn_1():
    if analizi[6] >= 2 and analizi[6] < 4: 
            l = "ФИБРИНОГЕН В НОРМЕ"
            itogi.append(l)
    elif analizi[6] > 4:
        l = "ФИБРИНОГЕН ПОВЫШЕН"
        itogi.append(l)
    elif analizi[6] < 2:
        l = "ФИБРИНОГЕН ПОНИЖЕН"
        itogi.append(l)
    
def ttg_1():
    if baza[0] == 0 and (baza[1] >= 18 and baza[1] <= 50):
        if analizi[7] >= 2.2 and analizi[7] <= 15.2:
            g = "ТТГ В НОРМЕ"
            itogi.append(g)
        elif analizi[7] > 15.2:
            g = "ТТГ ПОВЫШЕН"
            itogi.append(g)
        elif analizi[7] < 2.2:
            g = "ТТГ ПОНИЖЕН"
            itogi.append(g)
    elif baza[0] == 0 and (baza[1] >= 51 and baza[1] <= 60):
        if analizi[7] >= 1.9 and analizi[7] <= 8.4:
            g = "ТТГ В НОРМЕ"
            itogi.append(g)
        elif analizi[7] > 8.4:
            g = "ТТГ ПОВЫШЕН"
            itogi.append(g)
        elif analizi[7] < 1.9:
            g = "ТТГ ПОНИЖЕН"
            itogi.append(g)
    elif baza[0] == 0 and (baza[1] >= 61 and baza[1] <= 70):
        if analizi[7] >= 1.1 and analizi[7] <= 7.9:
            g = "ТТГ В НОРМЕ"
            itogi.append(g)
        elif analizi[7] > 7.9:
            g = "ТТГ ПОВЫШЕН"
            itogi.append(g)
        elif analizi[7] < 1.1:
            g = "ТТГ ПОНИЖЕН"
            itogi.append(g)
    elif baza[0] == 0 and baza[1] >= 71:
        if analizi[7] >= 0.8 and analizi[7] <= 4.7:
            g = "ТТГ В НОРМЕ"
            itogi.append(g)
        elif analizi[7] > 4.7:
            g = "ТТГ ПОВЫШЕН"
            itogi.append(g)
        elif analizi[7] < 0.8:
            g = "ТТГ ПОНИЖЕН"
            itogi.append(g)
    elif baza[0] == 1 and (baza[1] >= 18 and baza[1] <= 50):
        if analizi[7] >= 0.9 and analizi[7] <= 11.7:
            g = "ТТГ В НОРМЕ"
            itogi.append(g)
        elif analizi[7] > 11.7:
            g = "ТТГ ПОВЫШЕН"
            itogi.append(g)
        elif analizi[7] < 0.9:
            g = "ТТГ ПОНИЖЕН"
            itogi.append(g)
    elif baza[0] == 1 and (baza[1] >= 51 and baza[1] <= 60):
        if analizi[7] >= 0.7 and analizi[7] <= 5.4:
            g = "ТТГ В НОРМЕ"
            itogi.append(g)
        elif analizi[7] > 5.4:
            g = "ТТГ ПОВЫШЕН"
            itogi.append(g)
        elif analizi[7] < 0.7:
            g = "ТТГ ПОНИЖЕН"
            itogi.append(g) 
    elif baza[0] == 1 and (baza[1] >= 61 and baza[1] <= 70):
        if analizi[7] >= 0.4 and analizi[7] <= 3.5:
            g = "ТТГ В НОРМЕ"
            itogi.append(g)
        elif analizi[7] > 3.50:
            g = "ТТГ ПОВЫШЕН"
            itogi.append(g)
        elif analizi[7] < 0.4:
            g = "ТТГ ПОНИЖЕН"
            itogi.append(g)
    elif baza[0] == 1 and baza[1] >= 71:
        if analizi[7] >= 0.5 and analizi[7] <= 2.4:
            g = "ТТГ В НОРМЕ"
            itogi.append(g)
        elif analizi[7] > 2.4:
            g = "ТТГ ПОВЫШЕН"
            itogi.append(g)
        elif analizi[7] < 0.5:
            g = "ТТГ ПОНИЖЕН"
            itogi.append(g)
def krtzl_1():
    if analizi[8] > 101.2 and analizi[8] < 535.7: ##в нмоль/л ##
            j = "КОРТИЗОЛ В НОРМЕ"
            itogi.append(j)
    elif analizi[8] > 535.7:
        j = "КОРТИЗОЛ ПОВЫШЕН"
        itogi.append(j)
    elif analizi[8] < 101.2:
        j = "КОРТИЗОЛ ПОНИЖЕН"
        itogi.append(j)
def glkz_1():
    if analizi[9] >= 3.3 and analizi[9] <= 5.5: 
        k = "УРОВЕНЬ САХАРА В НОРМЕ"
        itogi.append(k)
    elif analizi[9] < 3.3:
        k = "УРОВЕНЬ САХАРА ПОНИЖЕН"
        itogi.append(k)
    elif analizi[9] > 5.5 and analizi[9] <= 8.3: 
        k = "УРОВЕНЬ САХАРА В НОРМЕ"
        itogi.append(k)
    elif analizi[9] > 8.3:
        k = "УРОВЕНЬ САХАРА СИЛЬНО ПОВЫШЕН"
        itogi.append(k)
def imt_1():
    if (baza[3]/((baza[2]/100)**2)) < 18.5:
        m = "НЕДОСТАТОК МАССЫ ТЕЛА"
        itogi.append(m)
    elif (baza[3]/((baza[2]/100)**2)) >= 18.5 and (baza[3]/((baza[2]/100)**2)) < 24.9:
        m = "МАССА ТЕЛА В НОРМЕ"
        itogi.append(m)
    elif (baza[3]/((baza[2]/100)**2)) >= 24.9 and (baza[3]/((baza[2]/100)**2)) < 29.9:
        m = "ИЗБЫТОЧНАЯ МАССА ТЕЛА"
        itogi.append(m)
    elif (baza[3]/((baza[2]/100)**2)) >= 29.9 and (baza[3]/((baza[2]/100)**2)) < 34.9:
        m = "ОЖИРЕНИЕ 1 СТЕПЕНИ"
        itogi.append(m)
    elif (baza[3]/((baza[2]/100)**2)) >= 34.9 and (baza[3]/((baza[2]/100)**2)) < 39.9:
        m = "ОЖИРЕНИЕ 2 СТЕПЕНИ"
        itogi.append(m)
    else:
        m = "ОЖИРЕНИЕ 3 СТЕПЕНИ"
        itogi.append(m)







def okno():
    new_root_5 = Toplevel(root)
    new_root_5.title("АНАЛИЗЫ")
    new_root_5.geometry("500x500")

    my_label0 = Label(new_root_5, text = itogi[0], font = 16)
    my_label0.place(x=20, y=20)

    my_label1 = Label(new_root_5, text = itogi[1], font = 16)
    my_label1.place(x=20, y=50)

    my_label2 = Label(new_root_5, text = itogi[2], font = 16)
    my_label2.place(x=20, y=80)

    my_label3 = Label(new_root_5, text = itogi[3], font = 16) 
    my_label3.place(x=20, y=110)

    my_label4 = Label(new_root_5, text = itogi[4], font = 16) 
    my_label4.place(x=20, y=140)

    my_label5 = Label(new_root_5, text = itogi[5], font = 16) 
    my_label5.place(x=20, y=170)

    my_label6 = Label(new_root_5, text = itogi[6], font = 16) 
    my_label6.place(x=20, y=200)

    my_label7 = Label(new_root_5, text = itogi[7], font = 16) 
    my_label7.place(x=20, y=230)

    my_label8 = Label(new_root_5, text = itogi[8], font = 16) 
    my_label8.place(x=20, y=260)

    my_label9 = Label(new_root_5, text = itogi[9], font = 16) 
    my_label9.place(x=20, y=290)

    my_label10 = Label(new_root_5, text = itogi[10], font = 16) 
    my_label10.place(x=20, y=320)

##для главного окна###
btn1 = Button(root, text = "НАЧАТЬ", font=35, command = anketa_1)
btn1.place(x=400, y=35)

btn2_1 = Button(root, text = "НАЧАТЬ", font=35, command = anketa_2_1)
btn2_1.place(x=400, y=95)

btn2_2 = Button(root, text = "НАЧАТЬ", font=35, command = anketa_2_2)
btn2_2.place(x=400, y=155)

btn2_3 = Button(root, text = "НАЧАТЬ", font=35, command = anketa_2_3)
btn2_3.place(x=400, y=215)

btn2_4 = Button(root, text = "НАЧАТЬ", font=35, command = anketa_2_4)
btn2_4.place(x=400, y=275)

btn2_5 = Button(root, text = "НАЧАТЬ", font=35, command = anketa_2_5)
btn2_5.place(x=400, y=335)

btn2_6 = Button(root, text = "НАЧАТЬ", font=35, command = anketa_2_6)
btn2_6.place(x=400, y=395)

btn2_7 = Button(root, text = "НАЧАТЬ", font=35, command = anketa_2_7)
btn2_7.place(x=400, y=455)

btn3 = Button(root, text = "НАЧАТЬ", font=35, command = anketa_3)
btn3.place(x=400, y=515)

text1 = Label(root, text = "ОСНОВНЫЕ ДАННЫЕ", font = 35)
text1.place(x=30, y=40)

text2_1 = Label(root, text = "АНКЕТИРОВАНИЕ_ИСТОРИЯССС", font = 35)
text2_1.place(x=30, y=100)

text2_2 = Label(root, text = "АНКЕТИРОВАНИЕ_ОБРАЗЖИЗНИ", font = 35)
text2_2.place(x=30, y=160)

text2_3 = Label(root, text = "АНКЕТИРОВАНИЕ_СТРЕСС", font = 35)
text2_3.place(x=30, y=220)

text2_4 = Label(root, text = "АНКЕТИРОВАНИИЕ_СОН", font = 35)
text2_4.place(x=30, y=280)

text2_5 = Label(root, text = "АНКЕТИРОВАНИЕ_САХАР", font = 35)
text2_5.place(x=30, y=340)

text2_6 = Label(root, text = "АНКЕТИРОВАНИЕ_БОЛИ", font = 35)
text2_6.place(x=30, y=400)

text2_7 = Label(root, text = "АНКЕТИРОВАНИЕ_ПИТАНИЕ", font = 35)
text2_7.place(x=30, y=460)

text3 = Label(root, text = "АНАЛИЗЫ", font = 35)
text3.place(x=30, y=520)

btn4_1 = Button(root, text = "ИТОГ", font=35, command=lambda:[lpvp_1(),lpnp_1(),trgl_1(), artdav_1(), cbelok_1(), gmst_1(), fbrn_1(), ttg_1(), krtzl_1(), glkz_1(), imt_1(), okno()])
btn4_1.place(x=420, y=600)
##для главного окна###

root.mainloop()
