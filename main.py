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
barcode = Code128(barcode_data, writer=ImageWriter())
barcode.save("barcode")

# Crear un PDF con ReportLab
pdf_file = "output.pdf"
pdf = canvas.Canvas(pdf_file, pagesize=letter)
width, height = letter

# Agregar el código QR al PDF
pdf.drawImage("qr_code.png", 50, height - 150, width=100, height=100)

# Agregar el código de barras al PDF
pdf.drawImage("barcode.png", 200, height - 150, width=200, height=100)

# Agregar texto al PDF
pdf.setFont("Helvetica", 12)
pdf.drawString(50, height - 170, "Código QR para: " + qr_data)
pdf.drawString(200, height - 170, "Código de barras para: " + barcode_data)

# Guardar el PDF
pdf.save()

print(f"PDF generado: {pdf_file}")
