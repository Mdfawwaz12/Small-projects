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

    '''
    ye program terminal mein run holakoch ranga, uska vaste pythonw ./desktop_notify karko run
    karre katho terminal time ka hisaab se run holakoch ranga, isse stop karna katho taskbar mein 
    jako end task dedalnaso
    '''