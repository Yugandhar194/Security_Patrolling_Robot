import RPi.GPIO as GPIO
import time
import cv2
import smtplib
from email.message import EmailMessage

sensor_pin = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor_pin, GPIO.IN)

def capture_image():
    camera = cv2.VideoCapture(0)  # 0 is the default camera index, adjust if needed
    print("camera on")
    if camera.isOpened():
        ret, frame = camera.read()
        if ret:
            print("capture image")
            cv2.imwrite("captured_image.jpg", frame)
    
    camera.release()

def send_email():
    import smtplib
    from email.message import EmailMessage
    import imghdr

    Sender_Email = "yugandhardeshmukh1945@gmail.com"
    Reciever_Email = "yugsjdeshmukh194.sct@gmail.com"

    Password ='nclaterbplrgfqswj'
    newMessage = EmailMessage()    #creating an object of EmailMessage class
    newMessage['Subject'] = "object detected" #Defining email subject
    newMessage['From'] = Sender_Email  #Defining sender email
    newMessage['To'] = Reciever_Email  #Defining reciever email
    
    with open('captured_image.jpg', 'rb') as f:
                       image_data = f.read()
                       image_type = imghdr.what(f.name)
                       image_name = f.name
    newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                       
                       smtp.login(Sender_Email, Password)              
                       smtp.send_message(newMessage)

try:
    print("IR Sensor Ready...")
    print(" ")

    while True:
        if GPIO.input(sensor_pin):
            print("Object Detected")
            capture_image()
            print("1")
            send_email()
            print("2")
            time.sleep(1)  # Adjust the sleep time to avoid rapid detection changes
        else:
            print("Object Not Detected")

        time.sleep(1)  # Adjust the sleep time as needed

except KeyboardInterrupt:
    print("Program terminated by user.")
finally:
    GPIO.cleanup()
