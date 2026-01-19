import customtkinter as ctk #importing customtkinter lib

#--------------------WINDOWS LAYOUT----------------
app = ctk.CTk()
app.title("Talib--CALCULATOR")
app.geometry("500x710")
app.resizable(False,False)

#--------------------FUNCTION FOR CALCULATING AND DISPLAYING THE INPUT------------------
num_data = ""
def calcu_fun(value):
    global num_data
    if value=="=":
        num_data+=""
    else:
        num_data+=value
    if value == "":  
        num_data = ""
        main_box.configure(text="")
    elif value == "=":
        try:
            if "(" and ")" in num_data:
                brk_st = num_data.index("(")
                brk_end = num_data.index(")")
                cal_brk = eval(num_data[brk_st+1:brk_end])
                new_num = num_data[0:brk_st] +"*"+ str(cal_brk) + num_data[brk_end+1:]
                main_box.configure(text=eval(new_num))
            else:    
                cal = eval(num_data[:])
                main_box.configure(text=cal)
                num_data = str(cal)
        except Exception as e:
            main_box.configure(text="ERROR")
    else:
        main_box.configure(text=num_data)
            
#---------------------CREATING FRAME FOR BG COLOR-------------------------
main_frame = ctk.CTkFrame(app,fg_color="#15523F")
main_frame.pack(fill="both",expand=True)

#CREATOR NAME
title_txt = ctk.CTkLabel(
    main_frame,
    text="MADE BY TALIB",
    font = ("Verdana",30,"bold"),
    text_color="#0a0909"
)
title_txt.place(x=125,y=0)

# THE LABEL BOX FOR INPUT AND ANSWER 
main_box = ctk.CTkLabel(
    main_frame,
    text="",
    text_color="#ffffff",
    font=("Arial",60),
    anchor="e",
    fg_color="transparent",
    height=60,
    width=480
)
main_box.place(x=10,y=120)

#MAKING FRAME FOR BUTTONS
button_frame = ctk.CTkFrame(
    main_frame,
    fg_color="transparent",
    height=400,
    width=480
)
button_frame.place(x=10,y=200)

#CLEAR BUTTON TO CLEAR THE SCREEN
clear_btn= ctk.CTkButton(
    button_frame,
    text="AC",
    command = lambda: calcu_fun(""),
    text_color="#FFFDFD",
    fg_color="#6E706F",
    font=("Arial",40),
    corner_radius=30,
    height= 90,
    width=110
)
clear_btn.grid(row=0,column=0)

#START BRACKET BUTTON
start_bracket_btn= ctk.CTkButton(
    button_frame,
    text="(",
    command = lambda: calcu_fun("("),
    text_color="#FFFDFD",
    fg_color="#6E706F",
    font=("Arial",40),
    corner_radius=30,
    height= 90,
    width=110
)
start_bracket_btn.grid(row=0,column=1,padx=10)

#END BRACKET BUTTON
end_bracket_btn= ctk.CTkButton(
    button_frame,
    text=")",
    command = lambda: calcu_fun(")"),
    text_color="#FFFDFD",
    fg_color="#6E706F",
    font=("Arial",40),
    corner_radius=30,
    height= 90,
    width=110
)
end_bracket_btn.grid(row=0,column=2)

#DIVIDE OPERATOR BUTTON
divide_btn= ctk.CTkButton(
    button_frame,
    text="÷",
    command = lambda: calcu_fun("/"),
    text_color="#FFFDFD",
    fg_color="#09251D",
    font=("Arial",40),
    corner_radius=30,
    height= 90,
    width=110
)
divide_btn.grid(row=0,column=3,padx=10)

# NUM 7 BUTTON
seven_btn= ctk.CTkButton(
    button_frame,
    text="7",
    command = lambda: calcu_fun("7"),
    text_color="#FFFDFD",
    fg_color="#000000",
    font=("Arial",40),
    corner_radius=30,
    height= 90,
    width=110
)
seven_btn.grid(row=1,column=0,pady=10)

#NUM 8 BUTTON
eight_btn= ctk.CTkButton(
    button_frame,
    text="8",
    command = lambda: calcu_fun("8"),
    text_color="#FFFDFD",
    fg_color="#000000",
    font=("Arial",40),
    corner_radius=30,
    height= 90,
    width=110
)
eight_btn.grid(row=1,column=1,padx=10,pady=10)

#NUM 9 BUTTON
nine_btn= ctk.CTkButton(
    button_frame,
    text="9",
    command = lambda: calcu_fun("9"),
    text_color="#FFFDFD",
    fg_color="#000000",
    font=("Arial",40),
    corner_radius=30,
    height= 90,
    width=110
)
nine_btn.grid(row=1,column=2,pady=10)

#MULTIPLAY OPERATOR BUTTON
multiply_btn= ctk.CTkButton(
    button_frame,
    text="x",
    command = lambda: calcu_fun("*"),
    text_color="#FFFDFD",
    fg_color="#09251D",
    font=("Arial",40),
    corner_radius=30,
    height= 90,
    width=110
)
multiply_btn.grid(row=1,column=3,padx=10,pady=10)

#NUM 4 BUTTON
four_btn= ctk.CTkButton(
    button_frame,
    text="4",
    command = lambda: calcu_fun("4"),
    text_color="#FFFDFD",
    fg_color="#000000",
    font=("Arial",40),
    corner_radius=30,
    height= 90,
    width=110
)
four_btn.grid(row=2,column=0)

#NUM 5 BUTTON
five_btn= ctk.CTkButton(
    button_frame,
    text="5",
    command = lambda: calcu_fun("5"),
    text_color="#FFFDFD",
    fg_color="#000000",
    font=("Arial",40),
    corner_radius=30,
    height= 90,
    width=110
)
five_btn.grid(row=2,column=1,padx=10)

#NUM SIX BUTTON
six_btn= ctk.CTkButton(
    button_frame,
    text="6",
    command = lambda: calcu_fun("6"),
    text_color="#FFFDFD",
    fg_color="#000000",
    font=("Arial",40),
    corner_radius=30,
    height= 90,
    width=110
)
six_btn.grid(row=2,column=2)

#SUBSTRACT OPERATOR BUTTON
subs_btn= ctk.CTkButton(
    button_frame,
    text="-",
    command = lambda: calcu_fun("-"),
    text_color="#FFFDFD",
    fg_color="#09251D",
    font=("Arial",40),
    corner_radius=30,
    height= 90,
    width=110
)
subs_btn.grid(row=2,column=3,padx=10)

#NUM 1 BUTTON
one_btn= ctk.CTkButton(
    button_frame,
    text="1",
    command = lambda: calcu_fun("1"),
    text_color="#FFFDFD",
    fg_color="#000000",
    font=("Arial",40),
    corner_radius=30,
    height= 90,
    width=110
)
one_btn.grid(row=3,column=0,pady=10)

#NUM 2 BUTTON
two_btn= ctk.CTkButton(
    button_frame,
    text="2",
    command = lambda: calcu_fun("2"),
    text_color="#FFFDFD",
    fg_color="#000000",
    font=("Arial",40),
    corner_radius=30,
    height= 90,
    width=110
)
two_btn.grid(row=3,column=1,padx=10,pady=10)

#NUM 3 BUTTON
three_btn= ctk.CTkButton(
    button_frame,
    text="3",
    command = lambda: calcu_fun("3"),
    text_color="#FFFDFD",
    fg_color="#000000",
    font=("Arial",40),
    corner_radius=30,
    height= 90,
    width=110
)
three_btn.grid(row=3,column=2,pady=10)

#ADDITION OPERATOR BUTTON
add_btn= ctk.CTkButton(
    button_frame,
    text="+",
    command = lambda: calcu_fun("+"),
    text_color="#FFFDFD",
    fg_color="#09251D",
    font=("Arial",40),
    corner_radius=30,
    height= 90,
    width=110
)
add_btn.grid(row=3,column=3,padx=10,pady=10)

#2ND FRAME FOR THE LAST BUTTONS
last_button_frame = ctk.CTkFrame(
    main_frame,
    fg_color="transparent",
    height=100,
    width=480
)
last_button_frame.place(x=10,y=600)

#NUM 0 BUTTON
zero_btn= ctk.CTkButton(
    last_button_frame,
    text="0",
    command = lambda: calcu_fun("0"),
    text_color="#FFFDFD",
    fg_color="#000000",
    font=("Arial",40),
    corner_radius=30,
    height= 90,
    width=229
)
zero_btn.grid(row=4,column=0,padx=10)

#DECIMAL BUTTON
deci_btn= ctk.CTkButton(
    last_button_frame,
    text=".",
    command = lambda: calcu_fun("."),
    text_color="#FFFDFD",
    fg_color="#000000",
    font=("Arial",40),
    corner_radius=30,
    height= 90,
    width=110
)
deci_btn.grid(row=4,column=2)

#EQUAL TO BUTTON
equal_btn= ctk.CTkButton(
    last_button_frame,
    text="=",
    command = lambda: calcu_fun("="),
    text_color="#FFFDFD",
    fg_color="#09251D",
    font=("Arial",40),
    corner_radius=30,
    height= 90,
    width=110
)
equal_btn.grid(row=4,column=3,padx=10)
app.mainloop()