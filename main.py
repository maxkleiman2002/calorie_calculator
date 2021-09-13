from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from database_calorie import *

def exit():
    root.destroy()




root = Tk()
root.title("Калькулятор калорий")
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w//2
h = h//2
w = w-960
h = h-540
root.geometry('1920x1080+{}+{}'.format(w,h))

tabControl  = ttk.Notebook(root)




def calorie_rate_calculation():
    for id in tabControl.tabs():
        tabControl.forget(id)
    style = ttk.Style()
    tabb = ttk.Frame(tabControl)
    tabControl.add(tabb, text = "Расчет нормы калорий")
    tabControl.pack(expand=1, fill="both")
    style.configure('TFrame',background ="#DBEFF9")

    lab_title = Label(tabb, bg ="#447E9B",fg = "#F7F9FA",text="Калькулятор потребления калорий", width=130,height=2, font=("Roboto",
                                                          18, "bold")).place(x = 0, y = 0)
    def radio_men():
        if varV.get() == 0:
            men['bg'] = '#DBEFF9'
            men['activebackground'] = '#DBEFF9'
            men['fg'] = 'black'
            men['activeforeground'] = 'black'

    def radio_women():
        if varV.get() == 1:
            women['bg'] = '#DBEFF9'
            women['activebackground'] = '#DBEFF9'

    lbl_sex = Label(tabb, text = "Пол: ", bg ="#DBEFF9", fg ="#373B3C", font=("Roboto",14)).place(x = 765, y = 100)
    varV = IntVar()
    varV.set(-1)
    men = Radiobutton(tabb, text="Мужской", bg ="#DBEFF9",fg ="#373B3C",variable=varV, value=0, font=("Roboto",14), command = radio_men).place(x = 900, y = 100,width = 100)

    image_men = Image.open("menn.png")
    image_men = image_men.resize((25, 25), Image.ANTIALIAS)
    image_men = ImageTk.PhotoImage( image_men)
    image_lable1 = Label(tabb, image = image_men,bg = "#DBEFF9")
    image_lable1.image = image_men
    image_lable1.place(x = 1002, y = 100)

    women = Radiobutton(tabb, text="Женский", bg ="#DBEFF9", fg ="#373B3C",variable=varV, value=1, font=("Roboto",14), command = radio_women).place(x = 1050, y = 100,width = 100)

    image_women = Image.open("women.png")
    image_women = image_women.resize((25, 25),Image.ANTIALIAS)
    image_women = ImageTk.PhotoImage(image_women)
    image_lable2 = Label(tabb,image = image_women, bg = "#DBEFF9")
    image_lable2.image = image_women
    image_lable2.place(x = 1152, y =  100)



    lbl_weight = Label(tabb, text = "Вес: ",bg ="#DBEFF9",fg ="#373B3C",font=("Roboto",14)).place(x = 770, y = 170,width = 40)
    entry_weight = Entry(tabb,bg ="#fff",fg ="#373B3C",width = 10, font=("Roboto",14))
    entry_weight.place(x = 950, y = 170)

    lbl_height = Label(tabb, text = "Рост: ", bg ="#DBEFF9",fg ="#373B3C",font=("Roboto",14)).place(x = 770, y = 240, width = 50)
    entry_height = Entry(tabb, bg="#fff", fg="#373B3C", width=10, font=("Roboto", 14))
    entry_height.place(x = 950, y = 240)

    lbl_age = Label(tabb, text = "Возраст: ", bg ="#DBEFF9",fg ="#373B3C",font=("Roboto",14)).place(x = 770, y = 310, width = 80)
    entry_age = Entry(tabb, bg="#fff", fg="#373B3C", width=10, font=("Roboto", 14))
    entry_age.place(x = 950, y =  310)

    def sedentary_button():
        if varV2.get() == 0:
            sedentary_lifestyle['bg'] = '#DBEFF9'
            sedentary_lifestyle['activebackground'] = '#DBEFF9'
            sedentary_lifestyle['fg'] = 'black'
            sedentary_lifestyle['activeforeground'] = 'black'

            normal_physical_activity['bg'] = '#0D936D'
            normal_physical_activity['activebackground'] = '#0D936D'
            normal_physical_activity['fg'] = '#fff'
            normal_physical_activity['activeforeground'] = '#fff'

            intense_physical_activity['bg'] = '#F26C0D'
            intense_physical_activity['activebackground'] = '#F26C0D'
            intense_physical_activity['fg'] = '#fff'
            intense_physical_activity['activeforeground'] = '#fff'

            extremely_physical_activity['bg'] = '#891209'
            extremely_physical_activity['activebackground'] = '#891209'
            extremely_physical_activity['fg'] = 'white'
            extremely_physical_activity['activeforeground'] = 'white'




    def normal_physically_button():
        if varV2.get() == 1:
            sedentary_lifestyle['bg'] = '#016A9F'
            sedentary_lifestyle['activebackground'] = '#016A9F'
            sedentary_lifestyle['fg'] = '#fff'
            sedentary_lifestyle['activeforeground'] = '#fff'

            normal_physical_activity['bg'] = '#DBEFF9'
            normal_physical_activity['activebackground'] = '#DBEFF9'
            normal_physical_activity['fg'] = 'black'
            normal_physical_activity['activeforeground'] = 'black'

            intense_physical_activity['bg'] = '#F26C0D'
            intense_physical_activity['activebackground'] = '#F26C0D'
            intense_physical_activity['fg'] = '#fff'
            intense_physical_activity['activeforeground'] = '#fff'

            extremely_physical_activity['bg'] = '#AA150A'
            extremely_physical_activity['activebackground'] = '#AA150A'
            extremely_physical_activity['fg'] = 'white'
            extremely_physical_activity['activeforeground'] = 'white'


    def intensive_physically_button():
        if varV2.get() == 2:
            sedentary_lifestyle['bg'] = '#016A9F'
            sedentary_lifestyle['activebackground'] = '#016A9F'
            sedentary_lifestyle['fg'] = '#fff'
            sedentary_lifestyle['activeforeground'] = '#fff'

            normal_physical_activity['bg'] = '#0D936D'
            normal_physical_activity['activebackground'] = '#0D936D'
            normal_physical_activity['fg'] = '#fff'
            normal_physical_activity['activeforeground'] = '#fff'



            intense_physical_activity['bg'] = '#DBEFF9'
            intense_physical_activity['activebackground'] = '#DBEFF9'
            intense_physical_activity['fg'] = 'black'
            intense_physical_activity['activeforeground'] = 'black'

            extremely_physical_activity['bg'] = '#AA150A'
            extremely_physical_activity['activebackground'] = '#AA150A'
            extremely_physical_activity['fg'] = 'white'
            extremely_physical_activity['activeforeground'] = 'white'

    def extremely_physical_button():
        if varV2.get() == 3:
            sedentary_lifestyle['bg'] = '#016A9F'
            sedentary_lifestyle['activebackground'] = '#016A9F'
            sedentary_lifestyle['fg'] = '#fff'
            sedentary_lifestyle['activeforeground'] = '#fff'

            normal_physical_activity['bg'] = '#0D936D'
            normal_physical_activity['activebackground'] = '#0D936D'
            normal_physical_activity['fg'] = '#fff'
            normal_physical_activity['activeforeground'] = '#fff'

            intense_physical_activity['bg'] = '#F26C0D'
            intense_physical_activity['activebackground'] = '#F26C0D'
            intense_physical_activity['fg'] = '#fff'
            intense_physical_activity['activeforeground'] = '#fff'

            extremely_physical_activity['bg'] = '#DBEFF9'
            extremely_physical_activity['activebackground'] = '#DBEFF9'
            extremely_physical_activity['fg'] = 'black'
            extremely_physical_activity['activeforeground'] = 'black'



    lbl_activity = Label(tabb, text = "Уровень активности: ", bg ="#DBEFF9",fg ="#373B3C",font=("Roboto",14)).place(x = 770, y = 380, width = 185)
    varV2 = IntVar()
    varV2.set(-1)
    sedentary_lifestyle = Radiobutton(tabb, text ="Малоподвижный образ жизни", width = 25, height = 3,bg ="#016A9F", fg ="#fff", variable =  varV2, value = 0, indicatoron = 0, font=("Roboto",14), command = sedentary_button )
    sedentary_lifestyle.place(x = 770, y = 450, width = 300)
    normal_physical_activity = Radiobutton(tabb,text = "Нормальная физнагрузка",width = 25, height = 3, bg ="#0D936D", fg ="#fff", variable = varV2, value = 1,indicatoron = 0, font=("Roboto",14), command = normal_physically_button)
    normal_physical_activity.place(x = 770,y = 550, width = 300)
    intense_physical_activity = Radiobutton(tabb,text = "Интенсивная физнагрузка",width = 25, height = 3, bg ="#F26C0D", fg ="#fff", variable = varV2, value = 2,indicatoron = 0, font=("Roboto",14), command = intensive_physically_button)
    intense_physical_activity.place(x = 770,y = 650, width =300)
    extremely_physical_activity = Radiobutton(tabb, text = "Экстримальная физнагрузка", width = 25, height = 3, bg ="#AA150A", fg ="#fff", variable = varV2, value = 3,indicatoron = 0, font=("Roboto",14), command = extremely_physical_button)
    extremely_physical_activity.place(x = 770, y = 750, width = 300)
    #lbl_desired_weight = Label(tabb, text = "Желаемый вес: ", bg ="#DBEFF9",fg ="#373B3C",font=("Roboto",14)).place(x = 770, y = 770, width = 150)
    #entry_desired_weight = Entry(tabb, bg="#fff", fg="#373B3C", width=10, font=("Roboto", 14))
    #entry_desired_weight.place(x = 950, y = 770)

    def lose_weight():
        a = Toplevel()
        w = a.winfo_screenwidth()
        h = a.winfo_screenheight()
        w = w // 2
        h = h // 2
        w = w - 960
        h = h - 540
        a.geometry('1920x1080+{}+{}'.format(w, h))
        a.config(bg = "#DBEFF9")
        weight = entry_weight.get()
        height = entry_height.get()
        age = entry_age.get()
        if varV.get() == 0:
            if varV2.get() == 0:
                result = (10 * float(weight) + 6.25 * float(height) - 5 * float(age) + 5) * 1.375
            elif varV2.get() == 1:
                result = (10 * float(weight) + 6.25 * float(height) - 5 * float(age) + 5) * 1.55
            elif varV2.get() == 2 :
                result = (10 * float(weight) + 6.25 * float(height) - 5 * float(age) + 5) * 1.725
            else:
                result = (10 * float(weight) + 6.25 * float(height) - 5 * float(age) + 5) * 1.9
        else:
            if varV2.get() == 0:
                result = (10 * float(weight) + 6.25 * float(height) - 5 * float(age) - 161) * 1.375
            elif varV2.get() == 1:
                result = (10 * float(weight) + 6.25 * float(height) - 5 * float(age) - 161) * 1.55
            elif varV2.get() == 2:
                result = (10 * float(weight) + 6.25 * float(height) - 5 * float(age) - 161) * 1.725
            else:
                result = (10 * float(weight) + 6.25 * float(height) - 5 * float(age) - 161) * 1.9

        safe = result - 250
        extremely = result - 500

        lose_weight_safe = Label(a, text=f"Безопасный сценарий - {int(safe)} Ккал", bg="#DBEFF9", fg="#373B3C",
                                    font=("Roboto", 40)).place(x=500, y=100)
        protein_safe = Label(a, text=f"Белки - {int((safe * 0.25) / 4)} Грамм", bg="#DBEFF9", fg="#373B3C",
                             font=("Roboto", 40)).place(x=700, y=200)
        fats_safe = Label(a, text=f"Жиры - {int((safe * 0.15) / 9)} Грамм", bg="#DBEFF9", fg="#373B3C",
                          font=("Roboto", 40)).place(x=700, y=300)
        carbohydrates_safe = Label(a, text=f"Углеводы - {int((safe * 0.6) / 4)} Грамм", bg="#DBEFF9", fg="#373B3C",
                                   font=("Roboto", 40)).place(x=650, y=400)

        lose_weight_extremely = Label(a, text=f"Экстремальный сценарий - {int(extremely)} Ккал", bg="#DBEFF9",
                                         fg="#373B3C", font=("Roboto", 40)).place(x=450, y=600)
        protein_extremely = Label(a, text=f"Белки - {int((extremely * 0.25) / 4)} Грамм", bg="#DBEFF9", fg="#373B3C",
                                  font=("Roboto", 40)).place(x=700, y=700)
        fats_extremely = Label(a, text=f"Жиры - {int((extremely * 0.15) / 9)} Грамм", bg="#DBEFF9", fg="#373B3C",
                               font=("Roboto", 40)).place(x=700, y=800)
        carbohydrates_extremely = Label(a, text=f"Углеводы - {int((extremely * 0.6) / 4)} Грамм", bg="#DBEFF9",
                                        fg="#373B3C",
                                        font=("Roboto", 40)).place(x=650, y=900)

    def maintain_weight():
        a = Toplevel()
        w = a.winfo_screenwidth()
        h = a.winfo_screenheight()
        w = w // 2
        h = h // 2
        w = w - 960
        h = h - 540
        a.geometry('1920x1080+{}+{}'.format(w, h))
        a.config(bg="#DBEFF9")
        weight = entry_weight.get()
        height = entry_height.get()
        age = entry_age.get()
        result = 0
        if varV.get() == 0:
            if varV2.get() == 0:
                result = (10 * float(weight) + 6.25 * float(height) - 5 * float(age) + 5) * 1.375
            elif varV2.get() == 1:
                result = (10 * float(weight) + 6.25 * float(height) - 5 * float(age) + 5) * 1.55
            elif varV2.get() == 2:
                result = (10 * float(weight) + 6.25 * float(height) - 5 * float(age) + 5) * 1.725
            else:
                result = (10 * float(weight) + 6.25 * float(height) - 5 * float(age) + 5) * 1.9

        elif varV.get() == 1:
            if varV2.get() == 0:
                result = (10 * float(weight) + 6.25 * float(height) - 5 * float(age) - 161) * 1.375
            elif varV2.get() == 1:
                result = (10 * float(weight) + 6.25 * float(height) - 5 * float(age) - 161) * 1.55
            elif varV2.get() == 2:
                result = (10 * float(weight) + 6.25 * float(height) - 5 * float(age) - 161) * 1.725
            else:
                result = (10 * float(weight) + 6.25 * float(height) - 5 * float(age) - 161) * 1.9


        maintain_weight = Label(a, text=f"Результат - {int(result)} Ккал", bg="#DBEFF9", fg="#373B3C",
                                     font=("Roboto", 40)).place(x = 650, y = 200)
        protein = Label(a, text=f"Белки - {int((result * 0.25) / 4)} Грамм", bg="#DBEFF9", fg="#373B3C",
                             font=("Roboto", 40)).place(x=700, y=300)
        fats = Label(a, text=f"Жиры - {int((result * 0.15) / 9)} Грамм", bg="#DBEFF9", fg="#373B3C",
                          font=("Roboto", 40)).place(x=700, y=400)
        carbohydrates = Label(a, text=f"Углеводы - {int((result * 0.6) / 4)} Грамм", bg="#DBEFF9", fg="#373B3C",
                                   font=("Roboto", 40)).place(x=650, y=500)




    def to_gain_weight():
        a = Toplevel()
        w = a.winfo_screenwidth()
        h = a.winfo_screenheight()
        w = w // 2
        h = h // 2
        w = w - 960
        h = h - 540
        a.geometry('1920x1080+{}+{}'.format(w, h))
        a.config(bg="#DBEFF9")
        result = 0
        weight = entry_weight.get()
        height = entry_height.get()
        age = entry_age.get()
        if varV.get() == 0:
            if varV2.get() == 0:
                result = (10 * float(weight) + 6.25 * float(height) - 5 * float(age) + 5) * 1.375
            elif varV2.get() == 1:
                result = (10 * float(weight) + 6.25 * float(height) - 5 * float(age) + 5) * 1.55
            elif varV2.get() == 2:
                result = (10 * float(weight) + 6.25 * float(height) - 5 * float(age) + 5) * 1.725
            else:
                result = (10 * float(weight) + 6.25 * float(height) - 5 * float(age) + 5) * 1.9
        elif varV.get() == 1:
            if varV2.get() == 0:
                result = (10 * float(weight) + 6.25 * float(height) - 5 * float(age) - 161) * 1.375
            elif varV2.get() == 1:
                result = (10 * float(weight) + 6.25 * float(height) - 5 * float(age) - 161) * 1.55
            elif varV2.get() == 2:
                result = (10 * float(weight) + 6.25 * float(height) - 5 * float(age) - 161) * 1.725
            else:
                result = (10 * float(weight) + 6.25 * float(height) - 5 * float(age) - 161) * 1.9

        safe = result + 250
        extremely = result + 500

        to_gain_weight_safe = Label(a, text=f"Безопасный сценарий - {int(safe)} Ккал", bg="#DBEFF9", fg="#373B3C",
                                     font=("Roboto", 40)).place(x = 500, y = 100)
        protein_safe = Label(a, text=f"Белки - {int((safe*0.25)/4)} Грамм", bg="#DBEFF9", fg="#373B3C",
                                     font=("Roboto", 40)).place(x = 700, y = 200)
        fats_safe = Label(a, text=f"Жиры - {int((safe*0.15)/9)} Грамм", bg="#DBEFF9", fg="#373B3C",
                                     font=("Roboto", 40)).place(x = 700, y = 300)
        carbohydrates_safe = Label(a, text=f"Углеводы - {int((safe*0.6)/4)} Грамм", bg="#DBEFF9", fg="#373B3C",
                                     font=("Roboto", 40)).place(x = 650, y = 400)

        to_gain_weight_extremely = Label(a, text=f"Экстремальный сценарий - {int(extremely)} Ккал", bg="#DBEFF9",
                                          fg="#373B3C", font=("Roboto", 40)).place(x = 450, y = 600)
        protein_extremely = Label(a, text=f"Белки - {int((extremely * 0.25) / 4)} Грамм", bg="#DBEFF9", fg="#373B3C",
                             font=("Roboto", 40)).place(x=700, y=700)
        fats_extremely = Label(a, text=f"Жиры - {int((extremely * 0.15) / 9)} Грамм", bg="#DBEFF9", fg="#373B3C",
                          font=("Roboto", 40)).place(x=700, y=800)
        carbohydrates_extremely = Label(a, text=f"Углеводы - {int((extremely * 0.6) / 4)} Грамм", bg="#DBEFF9", fg="#373B3C",
                                   font=("Roboto", 40)).place(x=650, y=900)




    lose_weight_button = Button(tabb, bg ="#F7BF31", text = "Похудеть", width = 20, height = 2,fg = "#fff",font=("Roboto",14), command = lose_weight).place(x = 520, y = 870, width = 250)
    to_gain_weight_button = Button(tabb, bg="#F7BF31", text="Набрать вес", width=20, height=2, fg="#fff",font=("Roboto", 14), command = to_gain_weight).place(x = 850, y = 870, width = 250)
    maintain_weight_button = Button(tabb, bg="#F7BF31", text="Поддерживать вес", width=20, height=2, fg="#fff",font=("Roboto", 14), command = maintain_weight).place(x = 1180, y = 870, width = 250)

    def next_screen(names):
        for widget in names:
            widget.place_forget()

def food_calorie_calculator():
    for id in tabControl.tabs():
        tabControl.forget(id)
    style = ttk.Style()
    tab_vegetables = ttk.Frame(tabControl)
    #tab_fruits = ttk.Frame(tabControl)
    #tab_bread = ttk.Frame(tabControl)
    #tab_fish = ttk.Frame(tabControl)
    #tab_sweets = ttk.Frame(tabControl)
    #tab_meat = ttk.Frame(tabControl)
    tab_result = ttk.Frame(tabControl)
    tabControl.add(tab_vegetables, text = "Овощи,зелень,грибы")
    #tabControl.add(tab_fruits, text="Фрукты, сухофрукты, ягоды")
    #tabControl.add(tab_bread,text = "Хлеб, крупы, макароны")
    #tabControl.add(tab_fish, text="Рыба и морепродукты")
    #tabControl.add(tab_sweets, text ="Сладости, орехи")
    #tabControl.add(tab_meat, text = "Мясо, птица, мясопродукты")
    tabControl.add(tab_result, text = "Результат")
    tabControl.pack(expand=1, fill="both")
    style.configure('TFrame',background ="#DBEFF9")

    lab_title = Label(tab_vegetables, bg="#447E9B", fg="#F7F9FA", text="Калькулятор калорийности продуктов", width=130, height=2,
                      font=("Roboto",
                            18, "bold")).place(x=0, y=0)
    lab_vegetables = Label(tab_vegetables,bg ="#DBEFF9", fg = "#447E9B", text = "Овощи,зелень,грибы",font=("Roboto",
                            24, "bold")).place(x=800, y=100)

    def read_value(product_name):
        try:
            cursor = connection.cursor()
            print("Подключен к SQLite")

            sql_select_query = """SELECT * FROM product WHERE name == ?"""
            cursor.execute(sql_select_query, (product_name,))
            print("Продукт - ", product_name)
            date = []
            Lab_info = {}
            lab_sum = {}
            lab_pr = {}
            count1 = 0
            count2 = 0
            count3 = 0
            count4 = 0
            date.append(product_name)

            for product in date:
                 for row in cursor:
                    print(row)
                    print(f"Название - {row[1]}")
                    print("Калорийность - ", row[2])
                    print("Белки - ", row[3])
                    print("Жиры - ", row[4])
                    print("Углеводы - ", row[5])
                    Lab_info[product] = Label(tab_result,text = f"Продукт - {row[1]} / Ккал - {row[2]} / Белки -  {row[3]} / Жиры - {row[4]} / Углеводы - {row[5]} ",bg="#DBEFF9",fg="#373B3C", font=("Roboto", 20))
                    #Lab_name[product].place(x = 300, y = 100)
                    Lab_info[product].pack(pady = 20)


                    #count1 += row[2]
                    #count2 += row[3]
                    #count3 += row[4]
                    #count4 += row[5]
            #lab_sum = Label(tab_result,text=f" Итого на 100 грамм ------ Калорийность - {count1} /  Белки - {count2:.2f}  / Жиры -  {count3:.2f}  / Углеводы - {count4:.2f}",bg="#DBEFF9", fg="#373B3C", font=("Roboto", 20))
            #lab_sum.pack(pady=30)






        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)











    image_beet = Image.open("beet_.png")
    image_beet = image_beet.resize((150, 150), Image.ANTIALIAS)
    image_beet = ImageTk.PhotoImage(image_beet)
    image_button_beet = Button(tab_vegetables,image=image_beet, bg="#DBEFF9",highlightthickness = 0, bd = 0)
    image_button_beet.image = image_beet
    image_button_beet.place(x=100, y=200)
    image_button_beet.bind('<Button-1>',lambda e:read_value('Свекла'))
    lab_beet = Label(tab_vegetables, text ="Свекла",bg ="#DBEFF9",fg="#373B3C",font=("Roboto",16))
    lab_beet.place(x = 130, y = 360)

    image_onion = Image.open("onion.png")
    image_onion = image_onion.resize((150, 150),Image.ANTIALIAS)
    image_onion = ImageTk.PhotoImage(image_onion)
    image_button_onion = Button(tab_vegetables,image=image_onion, bg="#DBEFF9",highlightthickness = 0, bd = 0)
    image_button_onion.image = image_onion
    image_button_onion.place(x=350, y=200)
    image_button_onion.bind('<Button-1>',lambda e:read_value('Лук репчатый'))
    lab_onion = Label(tab_vegetables, text="Лук репчатый", bg="#DBEFF9", fg="#373B3C", font=("Roboto", 16))
    lab_onion.place(x=360, y=360)

    image_tomato = Image.open("tomato.png")
    image_tomato = image_tomato.resize((150,150), Image.ANTIALIAS)
    image_tomato = ImageTk.PhotoImage(image_tomato)
    image_tomato_button = Button(tab_vegetables, image = image_tomato, bg="#DBEFF9",highlightthickness = 0, bd = 0)
    image_tomato_button.image = image_tomato
    image_tomato_button.place(x = 600, y = 200)
    image_tomato_button.bind('<Button-1>',lambda e:read_value('Помидоры'))
    lab_tomato = Label(tab_vegetables, text="Помидоры", bg="#DBEFF9", fg="#373B3C", font=("Roboto", 16))
    lab_tomato.place(x=620, y=360)

    image_boiled_potatoes = Image.open("potato_otv.png")
    image_boiled_potatoes = image_boiled_potatoes.resize((150, 150),Image.ANTIALIAS)
    image_boiled_potatoes = ImageTk.PhotoImage(image_boiled_potatoes)
    image_boiled_potatoes_button = Button(tab_vegetables, image = image_boiled_potatoes, bg="#DBEFF9",highlightthickness = 0, bd = 0)
    image_boiled_potatoes_button.image = image_boiled_potatoes
    image_boiled_potatoes_button.place(x=850, y=200)
    image_boiled_potatoes_button.bind('<Button-1>', lambda e:read_value('Картофель отварной'))
    lab_boiled_potatoes1 = Label(tab_vegetables, text="Картофель", bg="#DBEFF9", fg="#373B3C", font=("Roboto", 16))
    lab_boiled_potatoes2 = Label(tab_vegetables, text="отварной", bg="#DBEFF9", fg="#373B3C",font=("Roboto", 16))
    lab_boiled_potatoes1.place(x=870, y=360)
    lab_boiled_potatoes2.place(x=875, y=385)

    image_fried_potatoes = Image.open("fried_potatoes.png")
    image_fried_potatoes = image_fried_potatoes.resize((150, 150),Image.ANTIALIAS)
    image_fried_potatoes = ImageTk.PhotoImage(image_fried_potatoes)
    image_fried_potatoes_button = Button(tab_vegetables, image=image_fried_potatoes, bg="#DBEFF9",highlightthickness=0, bd=0)
    image_fried_potatoes_button.image = image_fried_potatoes
    image_fried_potatoes_button.place(x=1100, y=200)
    image_fried_potatoes_button.bind('<Button-1>', lambda e:read_value('Картофель жареный'))
    lab_fried_potatoes1 = Label(tab_vegetables, text="Картофель", bg="#DBEFF9", fg="#373B3C", font=("Roboto", 16))
    lab_fried_potatoes2 = Label(tab_vegetables, text="жареный", bg="#DBEFF9", fg="#373B3C", font=("Roboto", 16))
    lab_fried_potatoes1.place(x=1120, y=360)
    lab_fried_potatoes2.place(x=1130, y=385)

    image_jacket_potatoes = Image.open("jacket_potatoes.png")
    image_jacket_potatoes = image_jacket_potatoes.resize((150, 150),Image.ANTIALIAS)
    image_jacket_potatoes = ImageTk.PhotoImage(image_jacket_potatoes)
    image_jacket_potatoes_button = Button(tab_vegetables, image=image_jacket_potatoes, bg="#DBEFF9", highlightthickness=0,bd=0)
    image_jacket_potatoes_button.image = image_jacket_potatoes
    image_jacket_potatoes_button.place(x=1350, y=200)
    image_jacket_potatoes_button.bind('<Button-1>', lambda e:read_value('Картофель в мундире'))
    lab_jacket_potatoes1 = Label(tab_vegetables, text="Картофель", bg="#DBEFF9", fg="#373B3C", font=("Roboto", 16))
    lab_jacket_potatoes2 = Label(tab_vegetables, text="в мундире", bg="#DBEFF9", fg="#373B3C", font=("Roboto", 16))
    lab_jacket_potatoes1.place(x=1370, y=360)
    lab_jacket_potatoes2.place(x=1373, y=385)

    image_carrot = Image.open("carrot.png")
    image_carrot = image_carrot.resize((150, 150), Image.ANTIALIAS)
    image_carrot = ImageTk.PhotoImage(image_carrot)
    image_carrot_button = Button(tab_vegetables, image=image_carrot, bg="#DBEFF9", highlightthickness=0, bd=0)
    image_carrot_button.image = image_carrot
    image_carrot_button.place(x=1600, y=200)
    image_carrot_button.bind('<Button-1>',lambda e: read_value('Морковь'))
    lab_carrot = Label(tab_vegetables, text="Морковь", bg="#DBEFF9", fg="#373B3C", font=("Roboto", 16))
    lab_carrot.place(x=1625, y=360)

    image_cucumber = Image.open("cucumber.png")
    image_cucumber = image_cucumber.resize((150, 150), Image.ANTIALIAS)
    image_cucumber = ImageTk.PhotoImage(image_cucumber)
    image_cucumber_button = Button(tab_vegetables, image=image_cucumber, bg="#DBEFF9", highlightthickness=0, bd=0)
    image_cucumber_button.image = image_cucumber
    image_cucumber_button.place(x=100, y=440)
    image_cucumber_button.bind('<Button-1>', lambda e:read_value('Огурец'))
    lab_cucumber = Label(tab_vegetables, text="Огурец", bg="#DBEFF9", fg="#373B3C", font=("Roboto", 16))
    lab_cucumber.place(x=130, y=600)

    image_white_cabbage = Image.open("white_cabbage.png")
    image_white_cabbage = image_white_cabbage.resize((150, 150), Image.ANTIALIAS)
    image_white_cabbage = ImageTk.PhotoImage(image_white_cabbage)
    image_white_cabbage_button = Button(tab_vegetables, image=image_white_cabbage, bg="#DBEFF9",highlightthickness=0, bd=0)
    image_white_cabbage_button.image = image_white_cabbage
    image_white_cabbage_button.place(x=350, y=440)
    image_white_cabbage_button.bind('<Button-1>', lambda e:read_value('Белокачанная капуста'))
    lab_white_cabbage1 = Label(tab_vegetables, text="Белокачанная", bg="#DBEFF9", fg="#373B3C", font=("Roboto", 16))
    lab_white_cabbage2 = Label(tab_vegetables, text="капуста", bg="#DBEFF9", fg="#373B3C", font=("Roboto", 16))
    lab_white_cabbage1.place(x=355, y=600)
    lab_white_cabbage2.place(x=385, y=625)

    image_cauliflower = Image.open("cauliflower.png")
    image_cauliflower = image_cauliflower.resize((150, 150), Image.ANTIALIAS)
    image_cauliflower = ImageTk.PhotoImage(image_cauliflower)
    image_cauliflower_button = Button(tab_vegetables, image=image_cauliflower, bg="#DBEFF9", highlightthickness=0,bd=0)
    image_cauliflower_button.image = image_cauliflower
    image_cauliflower_button.place(x=600, y=440)
    image_cauliflower_button.bind('<Button-1>', lambda e:read_value('Цветная капуста'))
    lab_cauliflower1 = Label(tab_vegetables, text="Цветная", bg="#DBEFF9", fg="#373B3C", font=("Roboto", 16))
    lab_cauliflower2 = Label(tab_vegetables, text="капуста", bg="#DBEFF9", fg="#373B3C", font=("Roboto", 16))
    lab_cauliflower1.place(x=625, y=600)
    lab_cauliflower2.place(x=630, y=625)

    image_green_pea = Image.open("green_pea.png")
    image_green_pea = image_green_pea.resize((150, 150), Image.ANTIALIAS)
    image_green_pea = ImageTk.PhotoImage(image_green_pea)
    image_green_pea_button = Button(tab_vegetables, image=image_green_pea, bg="#DBEFF9", highlightthickness=0, bd=0)
    image_green_pea_button.image = image_green_pea
    image_green_pea_button.place(x=850, y=440)
    image_green_pea_button.bind('<Button-1>', lambda e: read_value('Зеленый горошок'))
    lab_green_pea1 = Label(tab_vegetables, text="Зеленый", bg="#DBEFF9", fg="#373B3C", font=("Roboto", 16))
    lab_green_pea2 = Label(tab_vegetables, text="горошок", bg="#DBEFF9", fg="#373B3C", font=("Roboto", 16))
    lab_green_pea1.place(x=875, y=600)
    lab_green_pea2.place(x=875, y=625)

    image_eggplant = Image.open("eggplant.png")
    image_eggplant = image_eggplant.resize((150, 150), Image.ANTIALIAS)
    image_eggplant = ImageTk.PhotoImage(image_eggplant)
    image_eggplant_button = Button(tab_vegetables, image=image_eggplant, bg="#DBEFF9", highlightthickness=0, bd=0)
    image_eggplant_button.image = image_eggplant
    image_eggplant_button.place(x=1100, y=440)
    image_eggplant_button.bind('<Button-1>', lambda e: read_value('Баклажан'))
    lab_eggplant = Label(tab_vegetables, text="Баклажан", bg="#DBEFF9", fg="#373B3C", font=("Roboto", 16))
    lab_eggplant.place(x=1120, y=600)

    image_squash = Image.open("squash.png")
    image_squash = image_squash.resize((150, 150), Image.ANTIALIAS)
    image_squash = ImageTk.PhotoImage(image_squash)
    image_squash_button = Button(tab_vegetables, image=image_squash, bg="#DBEFF9", highlightthickness=0, bd=0)
    image_squash_button.image = image_squash
    image_squash_button.place(x=1350, y=440)
    image_squash_button.bind('<Button-1>', lambda e:read_value('Кабачок'))
    lab_squash = Label(tab_vegetables, text="Кабачок", bg="#DBEFF9", fg="#373B3C", font=("Roboto", 16))
    lab_squash.place(x=1380, y=600)

    image_pumpkin = Image.open("pumpkin.png")
    image_pumpkin = image_pumpkin.resize((150, 150), Image.ANTIALIAS)
    image_pumpkin = ImageTk.PhotoImage(image_pumpkin)
    image_pumpkin_button = Button(tab_vegetables, image=image_pumpkin, bg="#DBEFF9", highlightthickness=0, bd=0)
    image_pumpkin_button.image = image_pumpkin
    image_pumpkin_button.place(x=1600, y=440)
    image_pumpkin_button.bind('<Button-1>', lambda e: read_value('Тыква'))
    lab_pumpkin = Label(tab_vegetables, text="Тыква", bg="#DBEFF9", fg="#373B3C", font=("Roboto", 16))
    lab_pumpkin.place(x=1645, y=600)

    image_sweet_pepper = Image.open("sweet_pepper.png")
    image_sweet_pepper = image_sweet_pepper.resize((150, 150), Image.ANTIALIAS)
    image_sweet_pepper = ImageTk.PhotoImage(image_sweet_pepper)
    image_sweet_pepper_button = Button(tab_vegetables, image=image_sweet_pepper, bg="#DBEFF9", highlightthickness=0, bd=0)
    image_sweet_pepper_button.image = image_sweet_pepper
    image_sweet_pepper_button.place(x=100, y=680)
    image_sweet_pepper_button.bind('<Button-1>', lambda e:read_value('Перец сладкий'))
    lab_sweet_pepper1 = Label(tab_vegetables, text="Болгарский", bg="#DBEFF9", fg="#373B3C", font=("Roboto", 16))
    lab_sweet_pepper2 = Label(tab_vegetables, text="перец", bg="#DBEFF9", fg="#373B3C", font=("Roboto", 16))
    lab_sweet_pepper1.place(x=120, y=840)
    lab_sweet_pepper2.place(x=140, y=865)

    image_radish= Image.open("radish.png")
    image_radish = image_radish.resize((150, 150), Image.ANTIALIAS)
    image_radish = ImageTk.PhotoImage(image_radish)
    image_radish_button = Button(tab_vegetables, image=image_radish, bg="#DBEFF9", highlightthickness=0, bd=0)
    image_radish_button.image = image_radish
    image_radish_button.place(x=350, y=680)
    image_radish_button.bind('<Button-1>', lambda e:read_value('Редис'))
    lab_radish = Label(tab_vegetables, text="Редис", bg="#DBEFF9", fg="#373B3C", font=("Roboto", 16))
    lab_radish.place(x=390, y=840)

    #image_turnip = Image.open("repa.png")
    #image_turnip = image_turnip.resize((150, 150), Image.ANTIALIAS)
    #image_turnip = ImageTk.PhotoImage(image_turnip)
    #image_turnip_button = Button(tab_vegetables, image=image_turnip, bg="#DBEFF9", highlightthickness=0, bd=0)
    #image_turnip_button.image = image_turnip
    #image_turnip_button.place(x=600, y=580)
    #image_turnip_button.bind('<Button-1>', lambda e: read_value('Репа'))
    #lab_turnip = Label(tab_vegetables, text="Репа", bg="#DBEFF9", fg="#373B3C", font=("Roboto", 16))
    #lab_turnip.place(x=645, y=740)

    image_celery = Image.open("selery.png")
    image_celery = image_celery.resize((150, 150), Image.ANTIALIAS)
    image_celery = ImageTk.PhotoImage(image_celery)
    image_celery_button = Button(tab_vegetables, text="Сельдерей",image=image_celery, bg="#DBEFF9", highlightthickness=0, bd=0, command = read_value)
    image_celery_button.image = image_celery
    image_celery_button.place(x=600, y=680)
    image_celery_button.bind('<Button-1>', lambda e: read_value('Сельдерей'))
    lab_celery = Label(tab_vegetables, text="Сельдерей", bg="#DBEFF9", fg="#373B3C", font=("Roboto", 16))
    lab_celery.place(x=620, y=840)

    image_corn = Image.open("corn.png")
    image_corn = image_corn.resize((150, 150), Image.ANTIALIAS)
    image_corn = ImageTk.PhotoImage(image_corn)
    image_corn_button = Button(tab_vegetables,text="Кукуруза вареная", image=image_corn, bg="#DBEFF9", highlightthickness=0, bd=0,command = read_value)
    image_corn_button.image = image_corn
    image_corn_button.place(x=850, y=680)
    image_corn_button.bind('<Button-1>', lambda e:read_value('Кукуруза вареная'))
    lab_corn1 = Label(tab_vegetables, text="Кукуруза", bg="#DBEFF9", fg="#373B3C", font=("Roboto", 16))
    lab_corn2 = Label(tab_vegetables, text="вареная", bg="#DBEFF9", fg="#373B3C", font=("Roboto", 16))
    lab_corn1.place(x=870, y=840)
    lab_corn2.place(x=875, y=865)

    image_fried_champignons = Image.open("champignons .png")
    image_fried_champignons = image_fried_champignons.resize((150, 150), Image.ANTIALIAS)
    image_fried_champignons = ImageTk.PhotoImage(image_fried_champignons)
    image_fried_champignons_button = Button(tab_vegetables,text = "Шампиньоны жаренные", image=image_fried_champignons, bg="#DBEFF9", highlightthickness=0, bd=0, command = read_value)
    image_fried_champignons_button.image = image_fried_champignons
    image_fried_champignons_button.place(x=1100, y=680)
    image_fried_champignons_button.bind('<Button-1>', lambda e:read_value('Шампиньоны жаренные'))
    lab_fried_champignons1 = Label(tab_vegetables, text="Шампиньоны", bg="#DBEFF9", fg="#373B3C", font=("Roboto", 16))
    lab_fried_champignons2 = Label(tab_vegetables, text="жаренные", bg="#DBEFF9", fg="#373B3C", font=("Roboto", 16))
    lab_fried_champignons1.place(x=1115, y=840)
    lab_fried_champignons2.place(x=1133, y=865)

    def command_basket():
        b = Toplevel()
        w = b.winfo_screenwidth()
        h = b.winfo_screenheight()
        w = w // 2
        h = h // 2
        w = w - 400
        h = h - 300
        b.geometry('800x600+{}+{}'.format(w, h))
        b.config(bg="#DBEFF9")
        lab_info = Label(b, text="Информация про калорийность и органические вещества", bg="#DBEFF9", fg="#373B3C",
                         font=("Roboto", 20))
        lab_info.place(x=20, y=20)
        lab_cal = Label(b, text = f"{read_value()}",bg="#DBEFF9", fg="#373B3C", font=("Roboto", 20))
        lab_cal.place(x=250, y=100)

    image_braised_porcini_mushrooms = Image.open("funghi_porcini.png")
    image_braised_porcini_mushrooms = image_braised_porcini_mushrooms.resize((150, 150), Image.ANTIALIAS)
    image_braised_porcini_mushrooms = ImageTk.PhotoImage(image_braised_porcini_mushrooms)
    image_braised_porcini_mushrooms_button = Button(tab_vegetables,text="Белые грибы тушеные", image=image_braised_porcini_mushrooms, bg="#DBEFF9",highlightthickness=0, bd=0, command = read_value)
    image_braised_porcini_mushrooms.image = image_braised_porcini_mushrooms
    image_braised_porcini_mushrooms_button.place(x=1350, y=680)
    image_braised_porcini_mushrooms_button.bind('<Button-1>', lambda e:read_value('Белые грибы тушеные'))
    lab_braised_porcini_mushrooms1 = Label(tab_vegetables, text="Белые грибы", bg="#DBEFF9", fg="#373B3C", font=("Roboto", 16))
    lab_braised_porcini_mushrooms2 = Label(tab_vegetables, text="тушеные", bg="#DBEFF9", fg="#373B3C", font=("Roboto", 16))
    lab_braised_porcini_mushrooms1.place(x=1360, y=840)
    lab_braised_porcini_mushrooms2.place(x=1375, y=865)

    image_butterlets = Image.open("butterlets.png")
    image_butterlets = image_butterlets.resize((150, 150), Image.ANTIALIAS)
    image_butterlets = ImageTk.PhotoImage(image_butterlets)
    image_butterlets_button = Button(tab_vegetables,text="Маслята маринованные", image=image_butterlets, bg="#DBEFF9",highlightthickness=0, bd=0, command = read_value)
    image_butterlets.image = image_butterlets
    image_butterlets_button.place(x=1600, y=680)
    image_butterlets_button.bind('<Button-1>', lambda e:read_value('Маслята маринованные'))
    lab_butterlets1 = Label(tab_vegetables, text="Маслята", bg="#DBEFF9", fg="#373B3C",
                                           font=("Roboto", 16))
    lab_butterlets2 = Label(tab_vegetables, text="маринованные", bg="#DBEFF9", fg="#373B3C",
                                           font=("Roboto", 16))
    lab_butterlets1.place(x=1635, y=840)
    lab_butterlets2.place(x=1615, y=865)



    basket = Image.open("basket.png")
    basket = basket.resize((50, 50), Image.ANTIALIAS)
    basket = ImageTk.PhotoImage(basket)
    basket_button = Button(tab_vegetables, text="Корзина",image=basket, bg="#DBEFF9", highlightthickness=0, bd=0, command = command_basket)
    basket_button.image = basket
    basket_button.place(x= 1815, y=90)
    lab_basket = Label(tab_vegetables, text="Корзина", bg="#DBEFF9", fg="#373B3C", font=("Roboto", 16))
    lab_basket.place(x=1800, y=150)

    lab_info = Label(tab_result, text="Информация про калорийность и органические вещества", bg="#DBEFF9",
                     fg="#373B3C", font=("Roboto", 20, "bold"))
    lab_info.pack(pady=10)





mainmenu = Menu(root)
root.config(menu = mainmenu)

taskmenu =  Menu(mainmenu,tearoff = 0)
taskmenu.add_command(label = "Расчет нормы калорий", command = calorie_rate_calculation)
taskmenu.add_command(label = "Калькулятор калорийности продуктов", command = food_calorie_calculator)
taskmenu.add_separator()
taskmenu.add_command(label = "Выход",command = exit)

helpmenu = Menu(mainmenu,tearoff = 0)
helpmenu.add_command(label = "Помощь")
helpmenu.add_command(label = "О программе")

mainmenu.add_cascade(label = "Задания", menu = taskmenu)
mainmenu.add_cascade(label = "Справка", menu = helpmenu)

root.mainloop()








