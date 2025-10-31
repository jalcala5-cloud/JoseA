import tkinter as tk
from tkinter import ttk
from datetime import datetime, date
import calendar
import time
from PIL import Image, ImageTk

# === CONFIGURATION ===
BACKGROUND_IMAGE_PATH = "A_2D_digital_rendering_showcases_a_computer_applic.png"  # your skull image
BG_COLOR = "#000000"
FG_COLOR = "#00FF77"
HIGHLIGHT_COLOR = "#FF00AA"

# === APP CLASS ===
class NeonDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Neon macOS Dashboard")
        self.root.geometry("1200x800")
        self.root.configure(bg=BG_COLOR)

        # Load background image
        try:
            bg_image = Image.open(BACKGROUND_IMAGE_PATH)
            bg_image = bg_image.resize((1200, 800))
            self.bg_photo = ImageTk.PhotoImage(bg_image)
            bg_label = tk.Label(root, image=self.bg_photo)
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            print("Background not loaded:", e)

        # === CLOCK ===
        self.clock_label = tk.Label(root, font=("Courier", 36, "bold"),
                                    fg=FG_COLOR, bg=BG_COLOR)
        self.clock_label.pack(pady=20)
        self.update_clock()

        # === CALENDAR ===
        self.calendar_frame = tk.Frame(root, bg=BG_COLOR)
        self.calendar_frame.pack(pady=20)
        self.draw_calendar()

        # === BUTTONS ===
        self.button_frame = tk.Frame(root, bg=BG_COLOR)
        self.button_frame.pack(pady=20)

        buttons = [
            ("Google Docs", "https://docs.google.com/"),
            ("ChatGPT", "https://chat.openai.com/"),
            ("YouTube", "https://youtube.com/"),
        ]

        for text, _ in buttons:
            btn = tk.Button(self.button_frame, text=text,
                            fg=FG_COLOR, bg="#111111",
                            font=("Courier", 18, "bold"),
                            relief="flat", width=20, height=2,
                            activebackground="#00FF77",
                            activeforeground="#000000")
            btn.pack(pady=8)
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#00FF77", fg="#000000"))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg="#111111", fg=FG_COLOR))

        # === SEARCH BAR ===
        self.search_var = tk.StringVar()
        tk.Entry(root, textvariable=self.search_var, font=("Courier", 14),
                 fg=FG_COLOR, bg="#111111", insertbackground=FG_COLOR,
                 relief="flat", width=40).pack(pady=10)
        tk.Button(root, text="Search", font=("Courier", 14, "bold"),
                  fg=FG_COLOR, bg="#222222", activebackground="#00FF77",
                  command=self.search_action).pack(pady=5)

    def update_clock(self):
        now = datetime.now().strftime("%I:%M:%S %p")
        self.clock_label.config(text=now)
        self.root.after(1000, self.update_clock)

    def draw_calendar(self):
        today = date.today()
        cal = calendar.monthcalendar(today.year, today.month)
        month_name = calendar.month_name[today.month]

        tk.Label(self.calendar_frame, text=f"{month_name} {today.year}",
                 font=("Courier", 20, "bold"), fg=FG_COLOR, bg=BG_COLOR).grid(row=0, column=0, columnspan=7, pady=5)

        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for i, day in enumerate(days):
            tk.Label(self.calendar_frame, text=day, font=("Courier", 12, "bold"),
                     fg=FG_COLOR, bg=BG_COLOR, width=6).grid(row=1, column=i)

        for r, week in enumerate(cal, start=2):
            for c, d in enumerate(week):
                if d == 0:
                    tk.Label(self.calendar_frame, text="", bg=BG_COLOR, width=6).grid(row=r, column=c)
                elif d == today.day:
                    tk.Label(self.calendar_frame, text=str(d),
                             bg=HIGHLIGHT_COLOR, fg="#FFFFFF", width=6).grid(row=r, column=c)
                else:
                    tk.Label(self.calendar_frame, text=str(d),
                             bg=BG_COLOR, fg=FG_COLOR, width=6).grid(row=r, column=c)

    def search_action(self):
        query = self.search_var.get()
        if query:
            print(f"Searching for: {query}")  # placeholder for webbrowser.open()

# === RUN APP ===
if __name__ == "__main__":
    root = tk.Tk()
    app = NeonDashboard(root)
    root.mainloop()