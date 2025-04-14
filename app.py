from tkinter import *
from tkinter import ttk
import RPi.GPIO as GPIO

LED_PIN1 = 11
LED_PIN2 = 12
LED_PIN3 = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)
GPIO.setup(LED_PIN3, GPIO.OUT)

GPIO.output(LED_PIN1, GPIO.LOW)
GPIO.output(LED_PIN2, GPIO.LOW)
GPIO.output(LED_PIN3, GPIO.LOW)

root = Tk()
root.geometry("480x320")
root.title("LED Control Panel")
root.resizable(False, False)

style = ttk.Style()
style.configure('TRadiobutton', font=('Arial', 12), padding=10)
style.configure('Title.TLabel', font=('Arial', 16, 'bold'))
style.configure('Close.TButton', font=('Arial', 10), padding=5, foreground='red')

mainFrame = ttk.Frame(root, padding=20)
mainFrame.pack(fill=BOTH, expand=True)

ttk.Label(mainFrame, text="LED Control Panel", style='Title.TLabel').grid(column=0, row=0, columnspan=3, pady=10)

statusFrame = ttk.Frame(mainFrame)
statusFrame.grid(column=0, row=1, columnspan=3, pady=10)

led_indicators = {
    "red": Canvas(statusFrame, width=60, height=60, bg='white', highlightthickness=1, highlightbackground='black'),
    "green": Canvas(statusFrame, width=60, height=60, bg='white', highlightthickness=1, highlightbackground='black'),
    "blue": Canvas(statusFrame, width=60, height=60, bg='white', highlightthickness=1, highlightbackground='black')
}

# Create LED indicators on the canvases
for color, canvas in led_indicators.items():
    canvas.grid(row=0, column=list(led_indicators.keys()).index(color), padx=10)
    canvas.create_oval(10, 10, 50, 50, fill='gray', tags="led")

def updateLED(active_color=None):
    for color, canvas in led_indicators.items():
        if color == active_color:
            canvas.itemconfig("led", fill=color)
        else:
            canvas.itemconfig("led", fill='gray')

def BlinkLight():
    GPIO.output(LED_PIN1, GPIO.LOW)
    GPIO.output(LED_PIN2, GPIO.LOW)
    GPIO.output(LED_PIN3, GPIO.LOW)
    
    color = led_color.get()
    if color == "red":
        GPIO.output(LED_PIN1, GPIO.HIGH)
    elif color == "green":
        GPIO.output(LED_PIN2, GPIO.HIGH)
    elif color == "blue":
        GPIO.output(LED_PIN3, GPIO.HIGH)
    
    updateLED(color)

# Variable to hold the selected radio button value
led_color = StringVar(value="")  # Start with no selection

radioFrame = ttk.Frame(mainFrame)
radioFrame.grid(column=0, row=2, columnspan=3, pady=20)

# Create radio buttons
ttk.Radiobutton(radioFrame, text="Red", variable=led_color, value="red", command=BlinkLight).pack(side=LEFT, padx=10)
ttk.Radiobutton(radioFrame, text="Green", variable=led_color, value="green", command=BlinkLight).pack(side=LEFT, padx=10)
ttk.Radiobutton(radioFrame, text="Blue", variable=led_color, value="blue", command=BlinkLight).pack(side=LEFT, padx=10)

# Different style close button
close_button = ttk.Button(mainFrame, text="Close", style='Close.TButton', command=root.destroy)
close_button.grid(column=0, row=3, columnspan=3, pady=6, sticky='e', padx=10)

updateLED()

try:
    root.mainloop()
finally:
    GPIO.cleanup()
