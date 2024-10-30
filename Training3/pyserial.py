"""
import serial

# Reemplaza 'COM3' con el puerto serial correcto en tu sistema
# En Linux podría ser '/dev/ttyUSB0' o similar
port = 'COM3'
baudrate = 9600  # La tasa de baudios debe coincidir con la configuración del dispositivo

try:
    # Abre el puerto serial
    ser = serial.Serial(port, baudrate, timeout=1)
    
    # Lee y muestra los datos del UPS
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
except serial.SerialException as e:
    print(f"No se puede abrir el puerto serial: {e}")
except KeyboardInterrupt:
    print("Lectura interrumpida por el usuario.")
finally:
    if ser.is_open:
        ser.close()
"""
