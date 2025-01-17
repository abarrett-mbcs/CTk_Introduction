import customtkinter
import sys
from pathlib import Path
from PIL import Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x700")
root.title("GUI Demonstration")
root.resizable(False, False)

def home():
    print("Test")
    label3.configure(bg_color="Red")

def exit_app():
    print("App exit")
    root.quit()


if getattr(sys, "frozen", False):
    OUTPUT_PATH = Path.cwd()
    ASSETS_PATH = Path(sys._MEIPASS) / "assets"
else:
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / "assets"
filename = str(ASSETS_PATH) + "/abjourney.jpg"
print(filename)
image = Image.open(filename)
background_image = customtkinter.CTkImage(image, size=(200, 300))
bg_lbl = customtkinter.CTkLabel(root, text="")
bg_lbl.place(x=0, y=0)

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True, )

label2 = customtkinter.CTkLabel(master=frame, text="Anthony Barrett presents")
label2.pack(pady=12, padx=10)

frame2 = customtkinter.CTkFrame(master=frame)
frame2.pack(pady=20, padx=60)

label3 = customtkinter.CTkLabel(master=frame2, text="Another label", width=200, height=100, )
label3.pack(pady=12, padx=10)

label = customtkinter.CTkLabel(master=frame, text="", image=background_image, height=50, width=30)
label.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="TEST BUTTON", command=home)
button.pack(pady=12, padx=10)

buttonx = customtkinter.CTkButton(master=frame, text="Exit App", command=exit_app, fg_color="Green")
buttonx.pack(pady=12, padx=10)

root.mainloop()