import os
import qrcode
from pathvalidate import is_valid_filename

# img = qrcode.make("https://pypi.org/project/qrcode/")
# type(img)
# img.save("qr_code.png")

def generate_qr_code(data, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name + ".png")

def main():
    print("#~ ALL QR CODES WILL BE SAVED AS A .PNG FILE! ~#")    
    print("Type 'quit' at any stage to cancel.")

    while True:
        text = input("Input desired text to be converted to QR code: ")
        
        if not text.strip():
            print("text cannot be empty.")
            continue

        if text.strip().lower() == 'quit':
            return

        while True:
            file_name = input("Input file name for QR code: ")

            if file_name.strip().lower() == 'quit':
                return

            if not file_name.strip():
                print("file name cannot be empty.")
                continue

            if not is_valid_filename(file_name):
                print("invalid file name, please use correct characters.")
                continue

            if os.path.exists(file_name + ".png"):
                confirm = input("File exists. Overwrite? (y/n): ")
                if confirm.lower() != 'y':
                    continue
            break

        try:
            generate_qr_code(text, file_name)
            print(f"QR code saved as '{file_name}.png'")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()