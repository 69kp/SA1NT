import tkinter as tk
from tkinter import font
from datetime import datetime, timedelta

# --------------------
# Einstellungen
# --------------------
DEMO_TEXT = "SA1NT OWNS YOU"
COUNTDOWN_HOURS = 0.0056

# --------------------
# Fenster
# --------------------
root = tk.Tk()
root.title("CONTROLS ARE LOCKED")
root.configure(bg="black")


# Vollbild
root.attributes("-fullscreen", True)

# ESC beendet die Demo
root.bind("<Escape>", lambda e: root.destroy())

# --------------------
# Fonts
# --------------------
title_font = font.Font(family="Consolas", size=52, weight="bold")
header_font = font.Font(family="Consolas", size=28, weight="bold")
text_font = font.Font(family="Consolas", size=23)
count_font = font.Font(family="Consolas", size=43, weight="bold")

RED = "#ff0000"
BG = "black"

# --------------------
# Countdown
# --------------------
end_time = datetime.now() + timedelta(hours=COUNTDOWN_HOURS)

def update_timer():
    remaining = end_time - datetime.now()

    if remaining.total_seconds() <= 0:
        timer_label.config(text="GOODBYE :)")
    else:
        total = int(remaining.total_seconds())
        s = total % 60

        timer_label.config(text= s)

    root.after(1000, update_timer)

# --------------------
# Oberer Banner
# --------------------
banner = tk.Label(
    root,
    text=DEMO_TEXT,
    fg=RED,
    bg=BG,
    font=title_font
)
banner.pack(pady=40)

# Linker Schädel mit Glow
for offset in [(0,0),(2,2),(-2,-2),(1,-1),(-1,1)]:
    tk.Label(
        root,
        text="☠☠",
        fg="#660000",
        bg="black",
        font=("Segoe UI Symbol", 110, "bold")
    ).place(x=30+offset[0], y=10+offset[1])

tk.Label(
    root,
    text="☠☠",
    fg="#ff0000",
    bg="black",
    font=("Segoe UI Symbol", 110, "bold")
).place(x=30, y=10)


# Rechter Schädel
for offset in [(0,0),(2,2),(-2,-2),(1,-1),(-1,1)]:
    tk.Label(
        root,
        text="☠☠",
        fg="#660000",
        bg="black",
        font=("Segoe UI Symbol", 110, "bold")
    ).place(relx=1.0, x=-330+offset[0], y=10+offset[1])

tk.Label(
    root,
    text="☠☠",
    fg="#ff0000",
    bg="black",
    font=("Segoe UI Symbol", 110, "bold")
).place(relx=1.0, x=-330, y=10)

# --------------------
# Haupttitel
# --------------------
title = tk.Label(
    root,
    text="YOUR FILES HAVE BEEN ENCRYPTED",
    fg=RED,
    bg=BG,
    font=header_font
)
title.pack()

subtitle = tk.Label(
    root,
    text="CONTROLS ARE LOCKED",
    fg=RED,
    bg=BG,
    font=text_font
)
subtitle.pack(pady=(0, 20))

# --------------------
# Inhalt
# --------------------
content = tk.Frame(root, bg=BG)
content.pack(fill="both", expand=True, padx=30)

# Linke Seite
left = tk.Frame(content, bg=BG, highlightbackground=RED, highlightthickness=1)
left.pack(side="left", fill="both", expand=True, padx=10)

left_text = """
WHAT HAPPENED?

All important files are getting encypted right now :(

Once the timer is up your pc is fucked.

Scan completed:         [✓]
Data modified:          [✓]
Encryption in process:  [✓]

status: succesful

------------------------------------

HOW TO RECOVER FILES?

There is nothing to recover.

All files will be encrypted, even the Boot files.

Sit back and enjoy :)
"""

tk.Label(
    left,
    text=left_text,
    justify="left",
    anchor="nw",
    fg=RED,
    bg=BG,
    font=text_font
).pack(fill="both", expand=True, padx=15, pady=15)

# Rechte Seite
right = tk.Frame(content, bg=BG, highlightbackground=RED, highlightthickness=1)
right.pack(side="right", fill="both", expand=True, padx=10)

tk.Label(
    right,
    text="TIME REMAINING",
    fg=RED,
    bg=BG,
    font=header_font
).pack(pady=20)

timer_label = tk.Label(
    right,
    text="72:00:00",
    fg=RED,
    bg=BG,
    font=count_font
)
timer_label.pack()

tk.Label(
    right,
    text="""

INFORMATION

• encryption performed
• network activity blocked
• file access granted

Lesson learned?

Dont fw SA1NT :)


""",
    fg=RED,
    bg=BG,
    justify="left",
    font=text_font
).pack(pady=20)

# --------------------
# Fußzeile
# --------------------
footer = tk.Label(
    root,
    text="DEMONSTRATION ONLY - NOT REAL MALWARE",
    fg=RED,
    bg=BG,
    font=text_font
)
footer.pack(pady=15)

update_timer()
root.mainloop()
