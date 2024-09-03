#import RPi.GPIO as GPIO
import time
import cv2
import time
import imghdr
sensor = 12
global count
count = 0
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor,GPIO.IN)

print("IR Sensor Ready.....")
print(" ")

try: 
   while True:
       if count >=10:
           break
       
       elif GPIO.input(sensor):
              
            
              print("Object Detected")
              time.sleep(0.2)
              count +=1
              print(count)
              cv2.namedWindow("preview")
              vc = cv2.VideoCapture(0)

              if vc.isOpened(): # try to get the first frame
                 rval, frame = vc.read()
               
              else:
                 rval = False

              while rval:
                  cv2.imshow("preview", frame)
                  rval, frame = vc.read()
                  cv2.imwrite('abc.jpg',frame)
                  time.sleep(3)
                  rval = False
                  vc.release()
                  cv2.destroyWindow("preview")
                  breakpoint
    

                  import smtplib
                  from email.message import EmailMessage
                  import imghdr

                  Sender_Email = "pragati.code@gmail.com"
                  Reciever_Email = "akshata.sct@gmail.com"

                  Password ='grqheqzoutabdfzd'
                  newMessage = EmailMessage()    #creating an object of EmailMessage class
                  newMessage['Subject'] = "object detected" #Defining email subject
                  newMessage['From'] = Sender_Email  #Defining sender email
                  newMessage['To'] = Reciever_Email  #Defining reciever email


                 # newMessage.set_content('Object detect... \n Here I attached mylocation: \n Latitude is:'+str(latitude)+'\n Langitude is:'+str(longitude)) #Defining email body
                  with open('abc.jpg', 'rb') as f:
                       image_data = f.read()
                       image_type = imghdr.what(f.name)
                       image_name = f.name
                  newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
                  with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                       
                       smtp.login(Sender_Email, Password)              
                       smtp.send_message(newMessage)
                             


except KeyboardInterrupt:
    GPIO.cleanup()
