import tkinter as tk
from tkinter import messagebox

class BMI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("BMI Calculator")
        
        self.label = tk.Label(self.root, text= "BMI Calculator")
        self.label.pack()

        self.label_name = tk.Label(self.root, text = "Name")
        self.label_name.pack()
        self.input_name = tk.Entry(self.root)
        self.input_name.pack()

        self.label_age = tk.Label(self.root, text = "Age")
        self.label_age.pack()
        self.input_age = tk.Entry(self.root)
        self.input_age.pack()

        self.label_Height = tk.Label(self.root, text = "Height")
        self.label_Height.pack()
        self.input_Height = tk.Entry(self.root)
        self.input_Height.pack()

        self.label_Weight = tk.Label(self.root, text = "Weight")
        self.label_Weight.pack()
        self.input_Weight = tk.Entry(self.root)
        self.input_Weight.pack()

        self.button = tk.Button(self.root, text ="calculate", command = self.calculator)
        self.button.pack()


    def calculator(self):
        Name = str(self.input_name.get())
        Age = float(self.input_age.get())
        Height = float(self.input_Height.get())
        Weight = float(self.input_Weight.get())


        Height_in_meter = Height / 100

        Body_mass_index = Weight / (Height_in_meter ** 2)

        if Body_mass_index <= 16:
            messagebox.showinfo("BMI" , "Lean")
        elif 16 < Body_mass_index <=25:
            messagebox.showinfo("BMI", "Normal")
        elif 25 < Body_mass_index <=45:
            messagebox.showinfo("BMI", "Obese")

    def run(self):
        self.root.mainloop()
    
calculators = BMI()
calculators.run()