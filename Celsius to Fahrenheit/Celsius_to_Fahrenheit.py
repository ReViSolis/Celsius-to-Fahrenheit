import tkinter as tk

def reset():
    entry1.delete(0, tk.END)
    entry1.insert(0, "0.0")
    entry2.delete(0, tk.END)
    entry2.insert(0, "0.0")

def to_fahr():
    celcios = float(entry2.get())
    fahr = (celcios * 9/5) +32
    entry1.delete(0, tk.END)
    entry1.insert(0, f"{fahr:.2f}")

def to_celcios():
    fahr = float(entry1.get())
    celcios = (fahr - 32) * 5.0/9.0
    entry2.delete(0, tk.END)
    entry2.insert(0, f"{celcios:.2f}")

app = tk.Tk()
app.title("Conversor de temperaturas")

label1 = tk.Label(app, text="Fahrenheit:")
label1.grid(row=0, column=0)

entry1 = tk.Entry(app)
entry1.grid(row=0, column=1)

button1 = tk.Button(app, text="Convertir a Celcios", command=to_celcios)
button1.grid(row=0, column=2)

label2 = tk.Label(app, text="Celcios:")
label2.grid(row=1, column=0)

entry2 = tk.Entry(app)
entry2.grid(row=1, column=1)

button2 = tk.Button(app, text="Convertir a Fahrenhait", command=to_fahr)
button2.grid(row=1, column=2)

button3 = tk.Button(app, text="Restablecer", command=reset)
button3.grid(row=2, column=1)

app.mainloop()