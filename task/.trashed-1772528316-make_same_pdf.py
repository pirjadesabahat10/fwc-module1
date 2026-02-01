from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from PIL import Image
import os

PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 50

files = sorted(
    [f for f in os.listdir('.') if f.startswith('fig') and f.endswith('.jpg')],
    key=lambda x: float(x.replace('fig', '').replace('.jpg', ''))
)

c = canvas.Canvas("final_task.pdf", pagesize=A4)

for f in files:
    img = Image.open(f)
    img_width, img_height = img.size

    scale = min(
        (PAGE_WIDTH - 2*MARGIN) / img_width,
        (PAGE_HEIGHT - 2*MARGIN) / img_height
    )

    new_w = img_width * scale
    new_h = img_height * scale

    x = (PAGE_WIDTH - new_w) / 2
    y = (PAGE_HEIGHT - new_h) / 2

    c.drawImage(f, x, y, new_w, new_h)
    c.showPage()

c.save()

