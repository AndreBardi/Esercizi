# Apri un file JPEG e leggilo in modalità binaria
with open("pitone.jpg", "rb") as file:
    byte_data = file.read()

# Converti i byte in stringa binaria
binary_data = ''.join(f'{byte:08b}' for byte in byte_data)

print(binary_data[:128])  

byte_data = bytearray(int(binary_data[i:i+8], 2) for i in range(0, len(binary_data), 8))

# Salva i byte in un file JPEG
with open("nuovo_pitone.jpg", "wb") as file:
    file.write(byte_data)
