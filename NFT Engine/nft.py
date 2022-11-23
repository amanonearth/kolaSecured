import requests
from requests.structures import CaseInsensitiveDict
import sys
sys.path.insert(0, '/Users/a-manonearth/Sites/ST/Scanning Engine')
from PIL import Image, ImageDraw, ImageFont
import requests # to get image from the web
import shutil # to save it locally
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


    


def host_nft(image):
    url = "https://api.nft.storage/upload"

    headers = CaseInsensitiveDict()
    headers["accept"] = "application/json"
    headers["x-agent-did"] = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweGI4QUVCYTg4RWU3RTE1QjA1NzZFMEFDQTRlMDNjRWE1MTE4NzIwNEMiLCJpc3MiOiJuZnQtc3RvcmFnZSIsImlhdCI6MTY2OTIyOTE2NzUyOSwibmFtZSI6ImJwaXQifQ.OMrrbQ8vuC4goFaRDhB_TTkj_B-X0crsI0JppBoSyHc"
    headers["Content-Type"] = "image/*"
    headers["Authorization"] = "Bearer WyIweGJlYzJiOTk0YTE2MjZlMmE4YWFhMmU0NTAwNjE1Nzk3YWQyMzNiOWRmYTUzZmRkNTJiMzFkOTE3ZmUwMjQ2MTgxYzlkOTJkZmUwYWE4Mzk0YWZiMDgyNzVjYjNmYmFhMWJhOTA5YTQxMmRiMmIzODA4YTY0NjU5MjJkYjQ3ZTFhMWMiLCJ7XCJpYXRcIjoxNjY5MjI5MDY0LFwiZXh0XCI6MTY2OTIzNjI2NCxcImlzc1wiOlwiZGlkOmV0aHI6MHhiOEFFQmE4OEVlN0UxNUIwNTc2RTBBQ0E0ZTAzY0VhNTExODcyMDRDXCIsXCJzdWJcIjpcIjB4S2FYamtMWTBINktfamV5OEVRTUU5RHdfempQNF8wSlVHS1NuTjcxaUk9XCIsXCJhdWRcIjpcIlpvYmw1QzJHRWVvT1dudXdpb0RURDRBSnd1NlhFTW5WSEttWjZWOFZZLUU9XCIsXCJuYmZcIjoxNjY5MjI5MDY0LFwidGlkXCI6XCI0ODZjYWZjNy0xMzUwLTQ1ZTEtYTZkYS04YTE2YWIwOWY5ZDBcIixcImFkZFwiOlwiMHhjY2U1YmNlNTdlZmJkMzM5Y2ZiMTM3YWIwNWY5ZTU3ODU2ZTk4MDcwMDcyNWQ5MTliYjQ4NTMyZTczZmI2Zjk2NWE2MzI1NDJiOTYwYjkyYzU0MTlkODQ5YjczMDhlZWNkMmRkYWIzNDFhZjcxZjQ3Mjc4NmJjMTY0MzExZDJiMTFiXCJ9Il0="

    data = f"@{image}"


    resp = requests.post(url, headers=headers, data=data)
    return resp.text