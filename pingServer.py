import urllib.request
import time
from gi.repository import Notify
Notify.init("WTMC Robotics site status")

url = "http://www.wtmcrobotics.com/"
while(True):
    try:
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        print("Success!")
        Notify.Notification.new("Site is live!").show()
        quit()
    except:
        time.sleep(1)
        pass
