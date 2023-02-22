import pyqrcode
import png
from pyqrcode import QRCode

r = "https://Priyanka484.github.io/Portfolio/"
# r = "I am priyanka sen"
url = pyqrcode.create(r)
url.png("linkQRCode.png",scale = 6)
