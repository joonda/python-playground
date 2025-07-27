from PIL import Image
import numpy as np
import easyocr

image_path = "./img/test_clean.png"
pil_img = Image.open(image_path)

img_array = np.array(pil_img)

reader = easyocr.Reader(['ko'])
results = reader.readtext(img_array)

for _, text, _ in results:
    print(text)