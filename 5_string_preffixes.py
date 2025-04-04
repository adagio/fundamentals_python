# String preffixes

# raw strings
raw_string = r'\n'
print(raw_string)

# f-string
world_name = 'Earth'
f_string = f'hello {world_name}'
print(f_string)

# bytes string
bytes_string = b'hello'
print(bytes_string)
print(type(bytes_string))

# unicode string, defauilt in Python 3
unicode_string = u'¡Arriba! ¡Perú!'
print(unicode_string)
print(type(unicode_string))

# Step 1: Define a binary header using a bytes string
# Imagine this is a simple image file header:
# - b'IMG' (3 bytes: magic number to identify the format)
# - b'\x01\x00' (2 bytes: version number, little-endian)
# - b'\x80\x02' (2 bytes: width = 640 pixels, little-endian)
# - b'\xe0\x01' (2 bytes: height = 480 pixels, little-endian)

header = b'IMG' + b'\x01\x00' + b'\x80\x02' + b'\xe0\x01'
print("Binary header:", header)  # Output: b'IMG\x01\x00\x80\x02\xe0\x01'

# Step 2: Write the binary data to a file
with open("image.bin", "wb") as file:  # 'wb' = write binary mode
    file.write(header)
    # Add some dummy "pixel data" (just random bytes for this example)
    pixel_data = bytes([255, 128, 64, 32])  # 4 bytes of "pixel" data
    file.write(pixel_data)

# Step 3: Read the binary data back and interpret it
with open("image.bin", "rb") as file:  # 'rb' = read binary mode
    data = file.read()
    print("Full binary data:", data)

    # Parse the header
    magic = data[0:3]          # First 3 bytes
    version = int.from_bytes(data[3:5], "little")  # Next 2 bytes
    width = int.from_bytes(data[5:7], "little")    # Next 2 bytes
    height = int.from_bytes(data[7:9], "little")   # Next 2 bytes
    pixel_data = data[9:]      # Remaining bytes

    print(f"Magic: {magic}")          # Output: Magic: b'IMG'
    print(f"Version: {version}")      # Output: Version: 1
    print(f"Width: {width}")          # Output: Width: 640
    print(f"Height: {height}")        # Output: Height: 480
    print(f"Pixel data: {pixel_data}") # Output: Pixel data: b'\xff\x80@ '

# Step 4: Verify the data makes sense
if magic == b'IMG' and version == 1:
    print(f"Image size: {width}x{height} pixels")