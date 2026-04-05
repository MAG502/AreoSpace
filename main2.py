import customtkinter as ctk

ctk.set_appearance_mode("dark")

root = ctk.CTk()
root.geometry("500x300")
root.title("Test")

label = ctk.CTkLabel(root, text="Drone Info", font=("Arial", 24))
label.pack(pady=50)

root.mainloop()