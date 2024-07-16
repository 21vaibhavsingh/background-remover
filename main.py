from rembg import remove
import easygui as eg 

from PIL import Image

input_path = eg.fileopenbox(title='select image file')
output_path = eg.filesavebox(title='save file to..')
#output_path ='images/output.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)

image = Image.open(output_path)
image.show()