# pip install qrcode
import qrcode

def Generate_qr_code(text,filename):
   qr = qrcode.QRCode(
      version=1,
      error_correction=qrcode.constants.ERROR_CORRECT_L,
      box_size=10,
      border=4,
   )
   qr.add_data(text)
   qr.make(fit=True)

   img = qr.make_image(fill_color="black", back_color="white")
   img.save(filename)

# the link you want to turn into QR
link = input("Enter/Paste the intented link:")

# filename of your QR code image
filename = 'QRcode.png'

Generate_qr_code(link,filename)