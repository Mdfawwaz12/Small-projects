import time
from plyer import notification
while True:
    notification.notify(
        title =  "water drinking remainder",
        message = "water is efficient to drink and good for healthy skin to drink 3litres a day",
        timeout = 3,
        app_icon = "D:\python\water.ico"
    )
    
    time.sleep(5)

   
