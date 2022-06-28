import pywhatkit
import pyautogui as pg

results = None
def getDetails():
    target_phone = input("Enter target phone number: ")
    message = input("Enter a message to send: ")
    time_hour = input("Enter time in 24 hour system: ")
    time_minute = input("Enter time in minute: ")
    results = [target_phone, message, time_hour, time_minute]
    return results

def sendMessage():
    results = getDetails()
    if(len(results[0]) < 10) :
        print("Enter a valid phone number")
        sendMessage()
    else:
        pywhatkit.sendwhatmsg(results[0], results[1], int(results[2]), int(results[3]))
        pg.press("enter")

sendMessage()