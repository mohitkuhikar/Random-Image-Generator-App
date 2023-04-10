#import os
import matplotlib
from randimage import get_random_image

num = 0
while True:
  #Generates Random Images and Saves them
  img_size = (100,100)
  print("Size (Completed!)")
  img = get_random_image(img_size)
  print("Image Generation (Completed!)")

  #Saves our generated Image File
  image = f"randimage{num}.png"
  matplotlib.image.imsave(image, img)
  print("Saving Image (Completed!")

  #Uploads to Instagram
  #media = cl.photo_upload(path=image, caption=f"Random Image {num}!!", extra_data= {"custom_accessibility_caption": "alt text example", "like_and_view_counts_disabled": False, "disable_comments": False,})
    
  #Deletes the Image once after Uploading!
  #os.remove(image)
  num += 1
