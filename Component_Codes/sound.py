import RPi.GPIO as GPIO
import time
import RPi.GPIO as GPIO
import time
import cv2
import time
import imghdr
#GPIO SETUP
channel = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
        if GPIO.input(channel):
                print ("Sound Detected!")
                time.sleep(0.2)
                cv2.namedWindow("preview")
                vc = cv2.VideoCapture(0)
               
                if vc.isOpened(): # try to get the first frame
                   rval, frame = vc.read()
                   print(rval)
               
                else:
                   rval = False
                   print(rval)

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


                    import requests 
                    api_address = "http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q="
                           
                    import json
                    location_req_url='http://api.ipstack.com/103.51.95.183?access_key=3e3v9eb64f09d7e376e1b7af28b91933'
                    r = requests.get(location_req_url)
                    location_obj = json.loads(r.text)
                           
                    #lat = location_obj['latitude']
                    #lon = location_obj['longitude']
                    #latitude = lat
                    #longitude = lon
                    #print(str(latitude))
                    #print(str(longitude))


                    #newMessage.set_content('Object detect... \n Here I attached mylocation: \n Latitude is:'+str(latitude)+'\n Langitude is:'+str(longitude)) #Defining email body
                    with open('abc.jpg', 'rb') as f:
                         image_data = f.read()
                         image_type = imghdr.what(f.name)
                         image_name = f.name
                         newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                            smtp.login(Sender_Email, Password)              
        
        else:
                  print("Sound not Detected")
    

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

# infinite loop
while True:
        time.sleep(1)
