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
