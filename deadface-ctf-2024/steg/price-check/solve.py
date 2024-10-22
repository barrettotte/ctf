import numpy as np
import pandas as pd
from PIL import Image

csv_file = 'STEG05.csv'
pixel_data = pd.read_csv(csv_file, header=None)

pixel_values = pixel_data.values.flatten().astype(np.uint8)
height, width = pixel_data.shape

image_array = pixel_values.reshape((height, width))
image = Image.fromarray(image_array, mode='L')
image.save('qrcode.png')
image.show()
