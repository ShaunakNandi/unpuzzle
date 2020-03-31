from PIL import Image
import os

def crop():
  root = 'PATH_TO_STORE_INPUT_IMG_AND_TILES'
  imgP = root+'inputImg.jpg'

  img = Image.open(imgP)
  index = 1
  # For NxN cropping, n = N
  n = 3
  w,h = img.size
  
  for y in range(0,h,h//n):
    for x in range(0,w,w//n):
      box = (x, y, x+w//n, y+h//n)
      grid = img.crop(box)
      try:    grid.save(os.path.join(root,'IMG-%s.jpg' %index))
      except: pass
      index += 1
        
  return

def main():
  crop()
  return

if __name__ == '__main__':
  main()
