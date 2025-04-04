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
root. geometry("400x150")
root.title("Blink LED Setup")

frame = ttk. Frame(root, padding=3)
frame. pack()

def BlinkLight(Colour):
	GPIO.output(LED_PIN1, GPIO.LOW)
	GPIO.output(LED_PIN2, GPIO.LOW)
	GPIO.output(LED_PIN3, GPIO.LOW)

	if(Colour == "red"):
		GPIO.output(LED_PIN1, GPIO.HIGH)

	elif(Colour == "green"):
		GPIO.output(LED_PIN2, GPIO.HIGH)

	elif(Colour == "blue"):
		GPIO.output(LED_PIN3, GPIO.HIGH)

ttk. Button(frame, text="Red", width="20", command=lambda: BlinkLight("red")).grid(column=1, row=0)
ttk. Button(frame, text="Green", width="20", command=lambda: BlinkLight("green")).grid(column=1, row=1)
ttk. Button(frame, text="Blue", width="20", command=lambda: BlinkLight("blue")).grid(column=1, row=2)

ttk. Button(frame, text="Close", width="5", command=root.destroy).grid(column=1, row=4)

try:
    root.mainloop()
finally:
    GPIO.cleanup()


