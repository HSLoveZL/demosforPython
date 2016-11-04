import Image
import ImageDraw
import ImageFilter
import ImageFont
import random


# random'A~Z'
def rndChar():
    return chr(random.randint(65, 90))

# randomColor1
def rndColor1():
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)

# randomColor2
def rndColor2():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)

width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# establishfontstyle
font = ImageFont.truetype('/usr/lib/jvm/java-8-oracle/jre/lib/oblique-fonts/LucidaTypewriterBoldOblique.ttf', 28)
# establishdraw
draw = ImageDraw.Draw(image)
# filleveryimagepoint
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor1())
# outputchar
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# mohuPicture
# image = image.Filter(ImageFilter.BLUR)
