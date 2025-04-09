from tkinter import *
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk
from tkinter.ttk import Progressbar
 
i = 0
timer = 20
frame = []
def open():
    global frame, i, window
    i = 0  
    frame = [] 
    window = Toplevel()
    window.title("Quiz Game - Python Quiz")
    window.geometry("800x800+300+0")
    window.resizable(False, False)
    window.config(bg="orange")    
    progress = Progressbar(window, orient=HORIZONTAL, length=400, mode='determinate')
    progress.pack(pady=20)
    timer_label = Label(window, text=f"Time left: {timer} seconds", font=("Arial", 16), bg="orange")
    timer_label.pack(pady=10)
    font_style = ("Rockwell Extra Bold", 20)
    
    var1 = IntVar()
    q1 = Frame(window, bg="gray", padx=10, pady=10)
    Label(q1, text="Q1- What is Python named after?",  font=font_style, fg="gold", bg="black").pack(pady=20)
    Radiobutton(q1, text="A snake", value=3, variable=var1, font=font_style, bg="gray").pack(anchor="w")
    Radiobutton(q1, text="A comedy show", value=4, variable=var1,   font=font_style, bg="gray").pack(anchor="w")
    Radiobutton(q1, text="A fruit", value=1, variable=var1,  font=font_style, bg="gray").pack(anchor="w")
    Radiobutton(q1, text="A programming book", value=2, variable=var1,  font=font_style, bg="gray").pack(anchor="w")
    

    var2 = IntVar()
    q2 = Frame(window, bg="gray", padx=10, pady=10)
    Label(q2, text="Q2- What does `print('Python\n'[::-1])`output?", font=font_style, fg="gold", bg="black").pack(pady=20)
    Radiobutton(q2, text="Python", value=2, variable=var2, font=font_style, bg="gray").pack(anchor="w")
    Radiobutton(q2, text="nothyP", value=4, variable=var2,  font=font_style, bg="gray").pack(anchor="w")
    Radiobutton(q2, text="Error", value=1, variable=var2,  font=font_style, bg="gray").pack(anchor="w")
    Radiobutton(q2, text="Nothing", value=3, variable=var2,  font=font_style, bg="gray").pack(anchor="w")
    
    var3 = IntVar()
    q3 = Frame(window, bg="gray", padx=10, pady=10)
    Label(q3, text="Q3-What's a set in Python used for?",font=font_style, fg="gold", bg="black").pack(pady=20)
    Radiobutton(q3, text="Storing duplicates", value=1, variable=var3,  font=font_style, bg="gray").pack(anchor="w")
    Radiobutton(q3, text="Storing unique items", value=5, variable=var3, font=font_style, bg="gray").pack(anchor="w")
    Radiobutton(q3, text="Sorting elements", value=2, variable=var3,  font=font_style, bg="gray").pack(anchor="w")
    Radiobutton(q3, text="Creating tables", value=3, variable=var3,  font=font_style, bg="gray").pack(anchor="w")
    
    var4 = IntVar()
    q4 = Frame(window, bg="gray", padx=10, pady=10)
    Label(q4, text="Q4- Which of these is the \n`Zen of Python` about?",font=font_style, fg="gold", bg="black").pack(pady=20)
    Radiobutton(q4, text="Simplicity", value=4, variable=var4,  font=font_style, bg="gray").pack(anchor="w")
    Radiobutton(q4, text="Complexity", value=1, variable=var4,  font=font_style, bg="gray").pack(anchor="w")
    Radiobutton(q4, text="Speed", value=2, variable=var4,  font=font_style, bg="gray").pack(anchor="w")
    Radiobutton(q4, text="Mystery", value=3, variable=var4, font=font_style, bg="gray").pack(anchor="w")
   
    var5 = IntVar()
    q5 = Frame(window, bg="gray", padx=10, pady=10)
    Label(q5, text="Q5- What is the most commonly used \nkeyword to define a function?", font=font_style, fg="gold", bg="black").pack(pady=20)
    Radiobutton(q5, text="create", value=1, variable=var5,  font=font_style, bg="gray").pack(anchor="w")
    Radiobutton(q5, text="def", value=5, variable=var5,  font=font_style, bg="gray").pack(anchor="w")
    Radiobutton(q5, text="func", value=2, variable=var5,  font=font_style, bg="gray").pack(anchor="w")
    Radiobutton(q5, text="define", value=3, variable=var5,  font=font_style, bg="gray").pack(anchor="w")

    var6 = IntVar()
    q6 =Frame(window, bg="gray", padx=10, pady=10)
    Label(q6, text="Q6- What's Python's philosophy \ntowards programming?",font=font_style, fg="gold", bg="black").pack(pady=20)
    Radiobutton(q6, text="Complexity is better than clarity.", value=1, variable=var6,  font=font_style, bg="gray").pack(anchor="w")
    Radiobutton(q6, text="Explicit is better than implicit.", value=6, variable=var6, font=font_style, bg="gray").pack(anchor="w")
    Radiobutton(q6, text="Errors should never be caught.", value=2, variable=var6,  font=font_style, bg="gray").pack(anchor="w")
    Radiobutton(q6, text="Speed is always the priority.", value=3, variable=var6,  font=font_style, bg="gray").pack(anchor="w")

    var7 = IntVar()
    q7 = Frame(window, bg="gray", padx=10, pady=10)
    Label(q7, text="Q7- What is the output of 3 * 1 ** 3?", font=font_style, fg="gold", bg="black").pack(pady=20)
    Radiobutton(q7, text="3", value=10, variable=var7,  font=font_style, bg="gray").pack(anchor="w")
    Radiobutton(q7, text="9", value=2, variable=var7,  font=font_style, bg="gray").pack(anchor="w")
    Radiobutton(q7, text="1", value=3, variable=var7, font=font_style, bg="gray").pack(anchor="w")
    Radiobutton(q7, text="Syntax Error", value=1, variable=var7,  font=font_style, bg="gray").pack(anchor="w")

    var8 = IntVar()
    q8 = Frame(window, bg="gray", padx=10, pady=10)
    Label(q8, text="Q8- Which is used to define \na block of code in Python?",font=font_style, fg="gold", bg="black").pack(pady=20)
    Radiobutton(q8, text="Parentheses", value=1, variable=var8, font=font_style, bg="gray").pack(anchor="w")
    Radiobutton(q8, text="Brackets", value=2, variable=var8,  font=font_style, bg="gray").pack(anchor="w")
    Radiobutton(q8, text="Indentation", value=5, variable=var8,  font=font_style, bg="gray").pack(anchor="w")
    Radiobutton(q8, text="Quotation", value=3, variable=var8,  font=font_style, bg="gray").pack(anchor="w")
    
    var9 = IntVar()
    q9 = Frame(window, bg="gray", padx=10, pady=10)
    Label(q9, text="Q9- Which method is used to\n add an element to a set?", font=font_style, fg="gold", bg="black").pack(pady=20)
    Radiobutton(q9, text=".add()", value=4, variable=var9, font=font_style, bg="gray").pack(anchor="w")
    Radiobutton(q9, text=".append()", value=3, variable=var9,  font=font_style, bg="gray").pack(anchor="w")
    Radiobutton(q9, text=".insert()", value=1, variable=var9, font=font_style, bg="gray").pack(anchor="w")
    Radiobutton(q9,text=".update()", value=2, variable=var9,  font=font_style, bg="gray").pack(anchor="w")
   
    var10 = IntVar()
    q10 = Frame(window, bg="gray", padx=10, pady=10)
    Label(q10, text="Q10- Which of the following is immutable?", font=font_style, fg="gold", bg="black").pack(pady=20)
    Radiobutton(q10, text="List", value=2, variable=var10, font=font_style, bg="gray").pack(anchor="w")
    Radiobutton(q10, text="Set", value=3, variable=var10,  font=font_style, bg="gray").pack(anchor="w")
    Radiobutton(q10, text="Dictionary", value=1, variable=var10,  font=font_style, bg="gray").pack(anchor="w")
    Radiobutton(q10, text="Tuple", value=4, variable=var10,  font=font_style, bg="gray").pack(anchor="w")

    var11 = IntVar()
    q11 = Frame(window, bg="gray", padx=10, pady=10)
    Label(q11, text="Q11- What is the purpose of the \n'pass' statement?",font=font_style, fg="gold", bg="black").pack(pady=20)
    Radiobutton(q11, text="Pause execution", value=1, variable=var11, font=font_style, bg="gray").pack(anchor="w")
    Radiobutton(q11, text="Do nothing", value=4, variable=var11,  font=font_style, bg="gray").pack(anchor="w")
    Radiobutton(q11, text="Break a loop", value=2, variable=var11, font=font_style, bg="gray").pack(anchor="w")
    Radiobutton(q11, text="End a function", value=3, variable=var11,  font=font_style, bg="gray").pack(anchor="w")

    var12 = IntVar()
    q12 = Frame(window, bg="gray", padx=10, pady=10)
    Label(q12, text="Q12- Which keyword is used to create a\n function in Python?",font=font_style, fg="gold", bg="black").pack(pady=20)
    Radiobutton(q12, text="def", value=4, variable=var12,  font=font_style, bg="gray").pack(anchor="w")
    Radiobutton(q12, text="function", value=1, variable=var12,  font=font_style, bg="gray").pack(anchor="w")
    Radiobutton(q12, text="func", value=2, variable=var12,  font=font_style, bg="gray").pack(anchor="w")
    Radiobutton(q12, text="method", value=3, variable=var12,  font=font_style, bg="gray").pack(anchor="w")

    frame = [q1, q2, q3, q4,q5, q6,q7,q8,q9,q10,q11,q12]
    def update_timer():
        global timer
        if timer > 0:
            timer -= 1
            timer_label.config(text=f"Time left: {timer} seconds")
            window.after(1000, update_timer)
        else:
            next_frame()


    def next_frame():
        global i, timer
        timer = 20
        if i < len(frame) - 1:
            frame[i].pack_forget()
            i += 1
            frame[i].pack()
            progress['value'] = (i + 1) * (100 // len(frame))
            update_timer()
        
        if i == len(frame) - 1:
            b2.pack_forget()
            b3.pack(fill="x", side="right", expand=True)



    
    def submit():
        total_score = sum([var1.get(), var2.get(), var3.get(), var4.get(),var5.get(), var6.get(), var7.get(), var8.get(),var9.get(), var10.get(), var11.get(), var12.get()])
        if total_score <= 15:
            level = "Beginner"
        elif 15 < total_score <= 28:
            level = "Intermediate"
        else:
            level = "Advanced"
        showinfo("Result", f"Your total score is: {total_score}\nPython Knowledge Level: {level}", parent=window)
        window.destroy()
        

    btn = Frame(window) 
    b2 = Button(btn, text="Next",bg="green",fg="black" ,font=("Rockwell Extra Bold", 20), command=next_frame)
    b2.pack(side="right", padx=10, pady=10) 
    b3 = Button(btn, text="Submit",bg="red",fg="black" ,font=("Rockwell Extra Bold", 20), command=submit)
    b3.pack(side="right", padx=10, pady=10)
    b3.pack_forget()  
    btn.pack(side="top", fill="x",pady=10) 

    frame[i].pack()

root = Tk()
root.title("Quiz Game")
root.geometry("800x800+300+0")
root.config(bg="black")
root.resizable(False, False)

Label(root, text="⭐💫\n⭐💫\n⭐💫\n⭐💫\n⭐💫\n⭐💫\n  ", font=("Rockwell Extra Bold", 70), fg="gold", bg="navy").place(x=0, y=0)
Label(root, text="💫⭐\n💫⭐\n💫⭐\n💫⭐\n💫⭐\n💫⭐\n   ", font=("Rockwell Extra Bold", 70), fg="gold", bg="navy").place(x=550, y=0)
Label(root, text='"Python  \nKnowledge \nConstrictor "', font=("Rockwell Extra Bold", 30), fg="gold", bg="teal").place(x=240, y=200)
Button(root, text="👉 Start", bd=15, command=open, width=15, font=("Arial", 20), relief="sunken", bg="silver", fg="red").place(x=260, y=600)
root.mainloop()
