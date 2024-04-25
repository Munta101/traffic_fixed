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

# esp32 as a webserver

import network
import uasyncio as asyncio
import usocket as socket

# Function to handle incoming client connections
async def handle_client(reader, writer):
    request = await reader.read()
    response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nHello, World!"
    await writer.awrite(response.encode("utf-8"))
    await writer.aclose()

# Function to start the web server
async def start_webserver():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 80))
    server_socket.listen(5)
    print("Web server started")

    while True:
        client_socket, _ = server_socket.accept()
        reader = asyncio.StreamReader(client_socket)
        writer = asyncio.StreamWriter(client_socket, {})
        asyncio.create_task(handle_client(reader, writer))

# Connect to Wi-Fi
def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        pass
    print("Connected to Wi-Fi")

# Replace 'your_wifi_ssid' and 'your_wifi_password' with your actual Wi-Fi credentials
wifi_ssid = "Wokwi-GUEST"
wifi_password = ""

# Start the web server
connect_to_wifi(wifi_ssid, wifi_password)
asyncio.run(start_webserver())


# connect to wifi ...display ip address

import network
import time

# Connect to Wi-Fi
def connect_to_wifi(ssid, password):
    station = network.WLAN(network.STA_IF)
    if station.isconnected():
        print("Already connected to Wi-Fi:", station.ifconfig()[0])
        return

    station.active(True)
    station.connect(ssid, password)

    print("Connecting to Wi-Fi...")
    while not station.isconnected():
        pass

    print("Connected to Wi-Fi:", station.ifconfig()[0])
    print("IP address:", station.ifconfig()[0])

# Replace with your Wi-Fi network credentials
wifi_ssid = "Wokwi-GUEST"
wifi_password = ""

# Connect to Wi-Fi
connect_to_wifi(wifi_ssid, wifi_password)


# connect to wifi..ip address...led

import network
import machine
import time

# LED pin configuration
led_pin = 2  # Assuming the LED is connected to GPIO pin 2

# Initialize the LED pin
led = machine.Pin(led_pin, machine.Pin.OUT)

# Connect to Wi-Fi
def connect_to_wifi(ssid, password):
    station = network.WLAN(network.STA_IF)
    if station.isconnected():
        print("Already connected to Wi-Fi:", station.ifconfig()[0])
        led.value(1)  # Turn on the LED
        return

    station.active(True)
    station.connect(ssid, password)

    print("Connecting to Wi-Fi...")
    while not station.isconnected():
        pass

    print("Connected to Wi-Fi:", station.ifconfig()[0])
    led.value(1)  # Turn on the LED
    print("IP address:", station.ifconfig()[0])

# Replace with your Wi-Fi network credentials
wifi_ssid = "Wokwi-GUEST"
wifi_password = ""

# Connect to Wi-Fi
connect_to_wifi(wifi_ssid, wifi_password)
