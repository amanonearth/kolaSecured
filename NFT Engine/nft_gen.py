from os import path, mkdir
from PIL import Image, ImageDraw, ImageFont
import requests # to get image from the web
import shutil # to save it locally
import cv2
import numpy as np


def generate_image(background, favicon, ratings):
  background_image = Image.open(background)
  image_url = favicon
  filename = image_url.split("/")[-1]

  r = requests.get(image_url, stream = True)

  if r.status_code == 200:
      r.raw.decode_content = True
      
      with open(filename,'wb') as f:
          shutil.copyfileobj(r.raw, f)
          
      print('Image sucessfully Downloaded: ',filename)
  else:
      print('Image Couldn\'t be retreived')

  character_image = Image.open(filename)
  coordinates = (int(1920/2-character_image.width/2), int(1000-character_image.height)) #x, y
  background_image.paste(character_image, coordinates, mask=character_image)

  img = Image.new('RGB', (60, 30), color = (73, 109, 137))
 
  fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
  d = ImageDraw.Draw(img)
  d.text((10,10), str(ratings), font=fnt, fill=(255, 255, 0))
  
  img.save('ratings.png')
  layer1 = Image.open("background.png")
  layer2 = Image.open("ratings.png")
  layer1.paste(layer2,(0,125))
  layer1.save('output.png')
  layer1 = Image.open('output.png')
  
  layer3 = Image.open("favicon.ico")
  layer1.paste(layer3,(0,0))
  layer1.save('output.png')


    
generate_image("background.png", "https://google.com/favicon.ico", 5)

