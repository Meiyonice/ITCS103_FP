from customtkinter import *
import tkinter as tk
from PIL import Image

# ==========================================================
# ===================== FUNCTIONS ==========================
# ==========================================================

# ========== Login Function =========
def attempt_login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "1234":
        login_window.destroy()
        main_app.deiconify()  # To show the main app after successful login
    else:
        error_label.configure(text="Invalid credentials", text_color="red")


# ==========================================================
# ===================== UI SETUP ===========================
# ==========================================================

# ========== CustomTkinter Color Configuration =========
# set_appearance_mode("system")
# set_default_color_theme("blue")

# ========== Main App Window =========
main_app = CTk()
main_app.withdraw() # To hide the main app temporarily

# ========= Window Dimensions =========
screen_width = main_app.winfo_screenwidth()
screen_height = main_app.winfo_screenheight()

window_width = 850
window_height = 600

x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

# ========== Login Window ==========
login_window = tk.Toplevel()
login_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
login_window.title("Sales Tracker")
login_window.wm_iconbitmap("sts_icon.ico")
login_window.config(bg="#242424")
login_window.resizable(0, 0)

side_img = Image.open("side-img.png")
side_img = CTkImage(dark_image=side_img, light_image=side_img, size=(425, 600))

# CTkLabel(login_window, image=side_img, text="SALES TRACKER", text_color="#f55247", anchor="center", font=("Times New Roman", 30)).pack(expand=True, side="left")
CTkLabel(login_window, image=side_img, text="").pack(expand=True, side="left")

login_frame = CTkFrame(login_window,  width=425, height=600, fg_color="#272d3c", border_color="#0b121e", border_width=2)
login_frame.pack_propagate(0)
login_frame.pack(expand=True, side="right")

CTkLabel(login_frame, text="Login", text_color="#f55247", font=("Arial", 50, "bold")).pack(pady=(115, 70))

CTkLabel(login_frame, text="Username").pack()
username_entry = CTkEntry(login_frame)
username_entry.pack(pady=5)

CTkLabel(login_frame, text="Password").pack(pady=(15, 0))
password_entry = CTkEntry(login_frame, show="*")
password_entry.pack(pady=5)

CTkButton(login_frame, text="Login", command=attempt_login, fg_color="#f55247").pack(pady=(20, 5))
error_label = CTkLabel(login_frame, text="")
error_label.pack()

# ========= Main App Window UI =========
main_app.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
main_app.title("Sales Tracker")
main_app.wm_iconbitmap("sts_icon.ico")

CTkLabel(main_app, text="Welcome to Sales Tracker!", font=("Arial", 20)).pack(pady=40)

# ========= Main Loop =========
main_app.mainloop()