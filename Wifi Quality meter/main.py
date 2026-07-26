import pywifi
import time 
wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]
iface.scan()
time.sleep(2)
for network in iface.scan_results():
    if network.signal > -50:
        print("Strong WiFi Network Found:")
    elif network.signal > -70:
        print("Moderate WiFi Network Found:")
    else:
        print("Weak WiFi Network Found:")
        
    print(network.ssid, network.signal) 
