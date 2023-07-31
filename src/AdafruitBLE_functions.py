from adafruit_ble import BLERadio
from adafruit_ble import BLEConnection
from adafruit_ble.advertising import Advertisement
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService
import sys

# given device name, return object of type connection
def connect_to_device(device_name, my_timeout):
    ble = BLERadio()
    print("scanning")
    devices = ble.start_scan(timeout=my_timeout)
    
    for i in devices:
        if(i.complete_name == device_name):
            print("device found\n", i)
            print("connecting to device")
            break
    my_connection = ble.connect(i, timeout=my_timeout)
    if(my_connection != None):
        print("connection successful")
    return my_connection
    # if we made it here, the device is not found \n",
    print("device not found")
    sys.exit(1)

# write to UART by passing object of type connection 
def write_UART_conn(my_connection: BLEConnection, my_message):
    if not(my_connection.connected):
        sys.exit("connection not active")
    service = my_connection[UARTService]
    service.write(my_message.encode('utf-8'))

def write_UART_int(my_connection: BLEConnection, my_message):
    if not(my_connection.connected):
        sys.exit("connection not active")
    service = my_connection[UARTService]
    service.write(str(my_message).encode('utf-8'))
    
# write to UART by passing device name 
def write_UART_name(device_name, my_message, my_timeout = 10, disconnect=True):
    my_connection = connect_to_device(device_name, my_timeout)
    if not(my_connection.connected):
        sys.exit("connection not active")
    write_UART_conn(my_connection, my_message)
    if disconnect:
        my_connection.disconnect()

# taken from adafruit example 
def print_ad():
    ble = BLERadio()
    print("scanning")
    found = set()
    scan_responses = set()
    # By providing Advertisement as well we include everything, not just specific advertisements.
    for advertisement in ble.start_scan(ProvideServicesAdvertisement, Advertisement):
        addr = advertisement.address
        if advertisement.scan_response and addr not in scan_responses:
            scan_responses.add(addr)
        elif not advertisement.scan_response and addr not in found:
            found.add(addr)
        else:
            continue
        print(addr, advertisement)
        print("\t" + repr(advertisement))
        print()

    print("scan done")
    