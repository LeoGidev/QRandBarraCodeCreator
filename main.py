import qrcode
from barcode import Code128
from barcode.writer import ImageWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Crear un código QR
qr_data = "https://www.example.com"
qr = qrcode.make(qr_data)
qr.save("qr_code.png")

# Crear un código de barras
barcode_data = "123456789012"