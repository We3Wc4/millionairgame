import tkinter as tk
import random
import time

mainwindow = tk.Tk()
mainwindow.geometry("1200x800")
mainwindow.config(bg="dark gray")
round = 0
money = 0

questions = [
    "Какая планета самая большая в нашей солнечной системе?",
    "Что такое 2 + 2?",
    "Какая страна является самой большой по территории?",
    "Кто написал роман 'Война и мир'?",
    "Что такое 'Python'?",
    "Какая часть тела человека отвечает за зрение?",
    "Кто является первым президентом США?",
    "Сколько континентов на Земле?",
    "Какая самая длинная река в мире?",
    "Как называется столица Франции?",
    "Какое химическое соединение является основным компонентом воды?",
    "Какая валюта используется в Японии?",
    "Какой элемент таблицы Менделеева имеет символ 'O'?",
    "Кто открыл закон всемирного тяготения?",
    "Какой город является столицей России?",
    "Какая река протекает через Египет?",
    "Сколько океанов на Земле?",
    "Какое государство является самым маленьким по площади?",
    "Какой элемент является самым легким в таблице Менделеева?",
    "Какая планета в нашей солнечной системе ближе всего к Солнцу?",
    "Сколько материков на Земле?",
    "Какая страна известна как 'Страна восходящего солнца'?",
    "Какой космический объект является карликовой планетой?",
    "Кто изобрел телефон?",
    "Какой элемент в таблице Менделеева обозначается как 'Na'?"
]

answers = [
    ["Юпитер", "Сатурн", "Земля", "Марс"],
    ["4", "5", "3", "6"],
    ["Россия", "Канада", "США", "Китай"],
    ["Лев Толстой", "Федор Достоевский", "Александр Пушкин", "Николай Гоголь"],
    ["Язык программирования", "Мифическое существо", "Тип змеи", "Робот"],
    ["Глаза", "Уши", "Нос", "Рот"],
    ["Джордж Вашингтон", "Авраам Линкольн", "Томас Джефферсон", "Рональд Рейган"],
    ["7", "6", "5", "8"],
    ["Нил", "Амазонка", "Миссисипи", "Янцзы"],
    ["Париж", "Берлин", "Лондон", "Мадрид"],
    ["H2O", "CO2", "O2", "N2"],
    ["Йена", "Доллар", "Евро", "Фунт стерлингов"],
    ["Кислород", "Азот", "Углерод", "Водород"],
    ["Исаак Ньютон", "Галилео Галилей", "Альберт Эйнштейн", "Никола Тесла"],
    ["Москва", "Санкт-Петербург", "Казань", "Екатеринбург"],
    ["Нил", "Амазонка", "Миссисипи", "Дунай"],
    ["5", "4", "3", "6"],
    ["Ватикан", "Монако", "Сингапур", "Лихтенштейн"],
    ["Водород", "Гелий", "Литий", "Бериллий"],
    ["Меркурий", "Венера", "Земля", "Марс"],
    ["6", "7", "5", "8"],
    ["Япония", "Китай", "Индия", "Южная Корея"],
    ["Плутон", "Марс", "Юпитер", "Венера"],
    ["Александр Белл", "Никола Тесла", "Томас Эдисон", "Грэм Белл"],
    ["Натрий", "Никель", "Азот", "Калий"]
]
def changeround():
    time.sleep(0.1)
    rnumber = random.randint(0, len(questions) - 1)
    rquestion = questions[rnumber]
    ranswer = answers[rnumber]
    print(rquestion, ranswer)
    canswer = ranswer[0]
    print(canswer)
    random.shuffle(ranswer)
    question.config(text=f"{rquestion}")
    a1.config(text=f"{ranswer[0]}",bg="dark gray")
    a2.config(text=f"{ranswer[1]}",bg="dark gray")
    a3.config(text=f"{ranswer[2]}",bg="dark gray")
    a4.config(text=f"{ranswer[3]}",bg="dark gray")
    mainwindow.update()

def b1():
    print(a1["text"])
    if a1["text"] == canswer:
        print("correct")
        a1.config(bg="light green")
        changeround()
    else:
        print("incorrect")
        a1.config(bg="red")
        mainwindow.update()
        time.sleep(0.5)
        mainwindow.destroy()
def b2():
    print(a2["text"])
    if a2["text"] == canswer:
        print("correct")
        a2.config(bg="light green")
        changeround()
    else:
        print("incorrect")
        a2.config(bg="red")
        mainwindow.update()
        time.sleep(0.5)
        mainwindow.destroy()
def b3():
    print(a3["text"])
    if a3["text"] == canswer:
        print("correct")
        a3.config(bg="light green")
        changeround()
    else:
        print("incorrect")
        a3.config(bg="red")
        mainwindow.update()
        time.sleep(0.5)
        mainwindow.destroy()
def b4():
    print(a4["text"])
    if a4["text"] == canswer:
        print("correct")
        a4.config(bg="light green")
        changeround()
    else:
        print("incorrect")
        a4.config(bg="red")
        mainwindow.update()
        time.sleep(0.5)
        mainwindow.destroy()


rnumber = random.randint(0,len(questions)-1)
rquestion = questions[rnumber]
ranswer = answers[rnumber]
print(rquestion,ranswer)
canswer = ranswer[0]
print(canswer)
random.shuffle(ranswer)

question = tk.Label(text=f"{rquestion}",font=("Arial", 25),bg="dark gray")
question.pack(pady=30)
a1 = tk.Button(text=ranswer[0],font=("Impact",30),bg="dark gray",width=23,command=b1)
a1.place(x=75,y=325)
a2 = tk.Button(text=ranswer[1],font=("Impact",30),bg="dark gray",width=23,command=b2)
a2.place(x=700,y=325)
a3 = tk.Button(text=ranswer[2],font=("Impact",30),bg="dark gray",width=23,command=b3)
a3.place(x=75,y=450)
a4 = tk.Button(text=ranswer[3],font=("Impact",30),bg="dark gray",width=23,command=b4)
a4.place(x=700,y=450)
lvl = tk.Label(text=f"round:{round}",font=("Impact",25),bg="dark gray")
lvl.place(x=1000,y=100)
mony = tk.Label(text=f"$:{money}",font=("Impact",25),bg="dark gray")
mony.place(x=980,y=175)







mainwindow.mainloop()