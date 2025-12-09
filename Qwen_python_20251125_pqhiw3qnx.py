# Name: Jose Alcala
# Date: 11/6/2025
# Class: CIS188
# Final Project: Swiss Army Python Automate with Neon Launcher

import tkinter as tk
from tkinter import ttk, messagebox, colorchooser, filedialog, simpledialog
from PIL import Image, ImageTk
import calendar
from datetime import datetime, date
import time
import threading
import webbrowser
import os
import itertools
import json
import subprocess  # <<< ADDED IMPORT

# ----------------------------
# Global Configuration
# ----------------------------
CONFIG_FILE = "swiss_config.json"
DEFAULT_CONFIG = {
    "background_color": "#000000",
    "label_color": "#ffffff",  # <<< FIXED: was #000000 (invisible)
    "font_size": 20,
    "marquee_text": "Pima Community College - Swiss Army Automate Dashboard",
    "marquee_speed": 50,  # ms
    "urls": ["https://docs.google.com", "https://chatgpt.com", "https://youtube.com"],
    "wallpaper_path": None,
    "dark_mode": True,
    "time_24h": True,
    "layout": "Two-Column"
}

# Load or create config
if os.path.exists(CONFIG_FILE):
    with open(CONFIG_FILE, "r") as f:
        config = json.load(f)
else:
    config = DEFAULT_CONFIG.copy()
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)

# ----------------------------
# Helper Functions
# ----------------------------
def save_config():
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)

def run_terminal():
    """Launch Terminal on macOS"""
    subprocess.run(["open", "-a", "Terminal"])

def open_url(url):
    webbrowser.open_new(url)

def add_custom_url():
    url = simpledialog.askstring("Add URL", "Enter full URL (e.g., https://example.com):")
    if url:
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
        config["urls"].append(url)
        save_config()
        # Rebuild will be called by main app instance
        if hasattr(add_custom_url, 'app_ref'):
            add_custom_url.app_ref.rebuild_url_buttons()

# ----------------------------
# Main Application Class
# ----------------------------
class SwissAutomateDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Swiss")
        self.root.geometry("1200x800")
        self.root.configure(bg=config["background_color"])
        self.fullscreen = False

        # Allow add_custom_url to trigger UI update
        add_custom_url.app_ref = self

        # State
        self.selected_date = date.today()
        self.today_cycle = itertools.cycle(["#ff00ff", "#ff00aa", "#ff0055"])
        self.current_today_color = next(self.today_cycle)

        self.setup_ui()
        self.update_clock()
        self.refresh_calendar()
        self.start_marquee()

    def setup_ui(self):
        # === Top Bar: Time & Date ===
        self.time_label = tk.Label(self.root, font=("Courier", config["font_size"], "bold"),
                                   fg=config["label_color"], bg=config["background_color"])
        self.time_label.pack(side="top", pady=5)

        # === Marquee ===
        self.marquee_frame = tk.Frame(self.root, bg=config["background_color"])
        self.marquee_frame.pack(side="top", fill="x")
        self.marquee_text = config["marquee_text"]
        self.marquee_label = tk.Label(self.marquee_frame, text=self.marquee_text,
                                      fg=config["label_color"], bg=config["background_color"],
                                      font=("Arial", 14, "bold"))
        self.marquee_label.pack()

        # === Main Content: Two Columns ===
        main_pane = tk.PanedWindow(self.root, orient=tk.HORIZONTAL, bg=config["background_color"])
        main_pane.pack(fill="both", expand=True, padx=10, pady=10)

        # --- LEFT: Calendar + Reminder ---
        left_frame = tk.Frame(main_pane, bg=config["background_color"])
        main_pane.add(left_frame)

        # Title
        tk.Label(left_frame, text="CALENDAR", font=("Courier", 18, "bold"),
                 fg="#00ffcc", bg=config["background_color"]).pack(pady=5)

        # Calendar Grid
        self.cal_frame = tk.Frame(left_frame, bg=config["background_color"])
        self.cal_frame.pack(pady=10)

        # Reminder Box
        self.reminder_var = tk.StringVar(value="No events for this day.")
        self.reminder_box = tk.Label(left_frame, textvariable=self.reminder_var,
                                     bg="#222222", fg="#e70505", width=30, height=4,
                                     relief="sunken", font=("Arial", 10))
        self.reminder_box.pack(pady=10)

        # Calendar Control Buttons
        btn_frame = tk.Frame(left_frame, bg=config["background_color"])
        btn_frame.pack()
        tk.Button(btn_frame, text="Refresh", command=self.refresh_calendar).pack(side="left", padx=2)
        tk.Button(btn_frame, text="Reset", command=self.reset_calendar).pack(side="left", padx=2)
        tk.Button(btn_frame, text="Save", command=self.save_reminder).pack(side="left", padx=2)
        tk.Button(btn_frame, text="Exit", command=self.root.quit).pack(side="left", padx=2)

        # --- RIGHT: URL + Apps + AI Terminal ---
        right_frame = tk.Frame(main_pane, bg=config["background_color"])
        main_pane.add(right_frame)

        # Screen Toggle Button (Top Right)
        self.toggle_btn = tk.Button(right_frame, text=".Toggle Screen", command=self.toggle_fullscreen,
                                    bg="#ff3366", fg="white", font=("Courier", 10))
        self.toggle_btn.pack(anchor="ne", padx=5, pady=5)

        # URL Section
        tk.Label(right_frame, text="Quick Web Apps", font=("Courier", 16, "bold"),
                 fg="#00ffcc", bg=config["background_color"]).pack(pady=5)
        self.url_frame = tk.Frame(right_frame, bg=config["background_color"])
        self.url_frame.pack(pady=5)
        self.rebuild_url_buttons()

        tk.Button(right_frame, text="+ Add URL", command=add_custom_url,
                  bg="#3333ff", fg="white").pack(pady=5)

        # Mac Apps
        tk.Label(right_frame, text="Mac Apps", font=("Courier", 16, "bold"),
                 fg="#00ffcc", bg=config["background_color"]).pack(pady=10)
        app_frame = tk.Frame(right_frame, bg=config["background_color"])
        app_frame.pack()
        tk.Button(app_frame, text="Terminal", command=run_terminal).pack(side="left", padx=5)
        tk.Button(app_frame, text="Documents", command=lambda: subprocess.run(["open", os.path.expanduser("~/Documents")])).pack(side="left", padx=5)

        # AI Terminal Simulation
        tk.Label(right_frame, text="AI Agent Terminal", font=("Courier", 14, "bold"),
                 fg="#ffcc00", bg=config["background_color"]).pack(pady=10)
        self.ai_text = tk.Text(right_frame, height=6, bg="#111111", fg="#00ff00", state="disabled")
        self.ai_text.pack(fill="x", padx=10)
        self.simulate_ai_loop()

        # Settings Button
        tk.Button(right_frame, text="⚙ Settings", command=self.open_settings,
                  bg="#555555", fg="white").pack(pady=10, side="bottom")

    def rebuild_url_buttons(self):
        for widget in self.url_frame.winfo_children():
            widget.destroy()
        for url in config["urls"]:
            name = url.split("//")[-1].split("/")[0]
            btn = tk.Button(self.url_frame, text=name, command=lambda u=url: open_url(u),
                            bg="#224466", fg="white")
            btn.pack(pady=2, fill="x")

    def update_clock(self):
        now = datetime.now()
        fmt = "%H:%M:%S" if config["time_24h"] else "%I:%M:%S %p"
        time_str = now.strftime(fmt) + " • " + now.strftime("%A, %B %d, %Y")
        self.time_label.config(text=time_str)
        self.root.after(1000, self.update_clock)

    def refresh_calendar(self):
        for widget in self.cal_frame.winfo_children():
            widget.destroy()

        cal = calendar.monthcalendar(self.selected_date.year, self.selected_date.month)
        month_name = self.selected_date.strftime("%B %Y")
        tk.Label(self.cal_frame, text=month_name, font=("Courier", 14, "bold"),
                 fg="#ff66cc", bg=config["background_color"]).grid(row=0, column=0, columnspan=7)

        # Days of week
        days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        for i, day in enumerate(days):
            tk.Label(self.cal_frame, text=day, font=("Arial", 10, "bold"),
                     fg="#e40b0b", bg=config["background_color"]).grid(row=1, column=i, padx=2, pady=2)

        # Calendar grid
        today = date.today()
        for week_idx, week in enumerate(cal):
            for day_idx, day in enumerate(week):
                if day == 0:
                    tk.Label(self.cal_frame, text="", bg=config["background_color"]).grid(row=week_idx+2, column=day_idx)
                else:
                    d = date(self.selected_date.year, self.selected_date.month, day)
                    bg_color = config["background_color"]
                    fg_color = "#ffffff"
                    if d == self.selected_date:
                        bg_color = "#ff69b4"  # Pink for selected
                    if d == today:
                        self.current_today_color = next(self.today_cycle)
                        bg_color = self.current_today_color
                        fg_color = "#000000"
                    btn = tk.Button(self.cal_frame, text=str(day), width=3,
                                    bg=bg_color, fg=fg_color,
                                    command=lambda d=d: self.select_date(d))
                    btn.grid(row=week_idx+2, column=day_idx, padx=1, pady=1)

        self.update_reminder()

    def select_date(self, d):
        self.selected_date = d
        self.refresh_calendar()

    def update_reminder(self):
        events = {
            date.today(): "Final Project Due!",
            date(2025, 12, 25): "Christmas Day"
        }
        self.reminder_var.set(events.get(self.selected_date, "No events for this day."))

    def save_reminder(self):
        new_rem = simpledialog.askstring("Save Reminder", "Enter reminder for selected date:")
        if new_rem:
            messagebox.showinfo("Saved", f"Reminder saved for {self.selected_date}")

    def reset_calendar(self):
        self.selected_date = date.today()
        self.refresh_calendar()

    def start_marquee(self):
        def scroll():
            text = self.marquee_label.cget("text")
            self.marquee_label.config(text=text[1:] + text[0])
            self.root.after(config["marquee_speed"], scroll)
        scroll()

    def simulate_ai_loop(self):
        def ai():
            responses = [
                "Swiss AI active... scanning systems.",
                "Neon protocol engaged.",
                "Automation sequence: RUNNING.",
                "Realtime sync: 100%.",
                "Jose, your dashboard is optimized."
            ]
            i = 0
            while True:
                self.ai_text.config(state="normal")
                self.ai_text.delete(1.0, tk.END)
                self.ai_text.insert(tk.END, responses[i % len(responses)])
                self.ai_text.config(state="disabled")
                i += 1
                time.sleep(2)
        threading.Thread(target=ai, daemon=True).start()

    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen
        self.root.attributes("-fullscreen", self.fullscreen)
        if not self.fullscreen:
            self.root.geometry("1200x800")

    def open_settings(self):
        SettingsWindow(self.root, self)

# ----------------------------
# Settings Window
# ----------------------------
class SettingsWindow:
    def __init__(self, parent, main_app):
        self.main_app = main_app
        self.win = tk.Toplevel(parent)
        self.win.title("Settings")
        self.win.geometry("600x700")
        self.win.configure(bg="#111111")
        self.create_widgets()

    def create_widgets(self):
        notebook = ttk.Notebook(self.win)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # General Tab
        general = tk.Frame(notebook, bg="#111111")
        notebook.add(general, text="General")

        tk.Label(general, text="Label Color", bg="#111111", fg="white").pack(pady=5)
        tk.Button(general, text="Pick Color", command=self.pick_label_color).pack()

        tk.Label(general, text="Font Size", bg="#111111", fg="white").pack(pady=5)
        self.font_size_var = tk.IntVar(value=config["font_size"])
        tk.Spinbox(general, from_=8, to=40, textvariable=self.font_size_var).pack()

        # Store reference to time format var
        self.time_24h_var = tk.BooleanVar(value=config["time_24h"])
        tk.Checkbutton(general, text="24-Hour Time", variable=self.time_24h_var,
                       bg="#111111", fg="white").pack(pady=5)

        # Web Tab
        web = tk.Frame(notebook, bg="#111111")
        notebook.add(web, text="Web")
        tk.Button(web, text="Add URL", command=add_custom_url).pack(pady=10)

        # AI Tab
        ai = tk.Frame(notebook, bg="#111111")
        notebook.add(ai, text="AI")
        tk.Label(ai, text="AI is simulated in terminal", bg="#111111", fg="white").pack(pady=20)

        # Background Tab
        bg = tk.Frame(notebook, bg="#111111")
        notebook.add(bg, text="Background")
        tk.Button(bg, text="Change Background Color", command=self.pick_bg_color).pack(pady=5)
        tk.Button(bg, text="Upload Wallpaper", command=self.upload_wallpaper).pack(pady=5)

        # Save Button
        tk.Button(self.win, text="SAVE & APPLY", command=self.save_settings,
                  bg="#00ffcc", font=("Courier", 12, "bold")).pack(pady=10)

    def pick_label_color(self):
        color = colorchooser.askcolor(title="Label Color")[1]
        if color:
            config["label_color"] = color

    def pick_bg_color(self):
        color = colorchooser.askcolor(title="Background Color")[1]
        if color:
            config["background_color"] = color

    def upload_wallpaper(self):
        path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
        if path:
            config["wallpaper_path"] = path

    def save_settings(self):
        config["font_size"] = self.font_size_var.get()
        config["time_24h"] = self.time_24h_var.get()  # <<< FIXED: now saves correctly
        save_config()
        messagebox.showinfo("Saved", "Settings saved! Restart to apply some changes.")

# ----------------------------
# Main Execution
# ----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = SwissAutomateDashboard(root)
    root.mainloop()