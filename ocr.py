from PIL import Image
import pytesseract


imag = Image.open('imag.png').convert('RGBA')
mask = Image.open('mask.png').convert('RGBA')

data = Image.alpha_composite(imag, mask)

config_str = '--oem 3 --psm 6 -c tessedit_char_whitelist=|ABCDEFGHIJKLMNOPQRSTUVWXYZ'

try:
    res = pytesseract.image_to_string(data, config=config_str)
except:
    print('error')

res = res.replace('|', 'I')
res = res.replace('\x0c', '')
res = res.split('\n')

print(res)
