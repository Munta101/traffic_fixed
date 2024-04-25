import network

# Function to scan for available Wi-Fi networks
def scan_wifi_networks():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)  # Activate the interface
    
    # Scan for available networks
    available_networks = wlan.scan()
    
    # Print available networks
    print("Available Wi-Fi Networks:")
    for net in available_networks:
        ssid = net[0].decode("utf-8")
        print("SSID: {}, RSSI: {}".format(ssid, net[3]))

# Call the function to scan for Wi-Fi networks
scan_wifi_networks()

# Wokwi SSID
# Wokwi-GUEST

# CODE TO CONNECT TO WIFI NETWORK
import network
import time

# Connect to Wi-Fi
def connect_to_wifi(ssid, password):
    station = network.WLAN(network.STA_IF)
    if station.isconnected():
        print("Already connected to Wi-Fi:", station.ifconfig())
        return

    station.active(True)
    station.connect(ssid, password)

    print("Connecting to Wi-Fi...")
    while not station.isconnected():
        pass

    print("Connected to Wi-Fi:", station.ifconfig())


# Replace with your Wi-Fi network credentials
wifi_ssid = "Wokwi-GUEST"
wifi_password = ""

# Connect to Wi-Fi
connect_to_wifi(wifi_ssid, wifi_password)