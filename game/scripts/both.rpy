#here are the styles and transforms used in both the replay and gallery screens

# 1280x720 gallery A
#define sx = 384
#define sy = 216

# 1280x720 gallery B
define sx = 550
define sy = 310

# 1920x1080 gallery A
#define sx = 600
#define sy = 338

# 1920x1080 gallery B
#define sx = 450
#define sy = 253

#pos positions pixel close enough!
default gx1 = 640 #1280x720
#changed to lift all thumbs a bit app to make place for buttons
default gy1 = 10 #1280x720
#default gx1 = 460 #1920x1080
#default gy1 = 30 #1920x1080

#text
#default gx2 = 25 # gallery_A 1280x720 and 1920x1080
#default gy2 = 10 # gallery_A

default gx2 = 640 # 322 #1280x720 gallery_B
#changed i dont remember why(
default gy2 = 110 #75  #1280x720 gallery_B

#default gx2 = 460 #1920x1080 gallery_B
#default gy2 = 83 #1920x1080 gallery_B

style gallery_button: # hover overlay it must be 4 pixels bigger then the images
#changed because i place my placeholder hover to test how it works
    hover_foreground "images/hover.png"
    #hover_foreground "images/gallery/hover 1924x1084.png"

style name_text: #text color and outlines please change
    color "#fc0390"
    outlines [ (1, "#000000", 0, 0) ]
    size 44 # 1280x720
    #size 30 #1920x1080

transform imageThumb: #images to thumbnail re-sizer
    size (sx, sy) #for 1920x1080 and 1280x720 DO NOT CHANGE

#the locked image for the galleries
image locked = "images/lock.jpg"
#changed this is just quick transform that happens when idle images[image_index] happens
transform gallery_fade:
    alpha 0.0
    linear 0.3 alpha 1.0
#changed this screen now can switch images and it response to click and mousewheel up and down
screen gallery_closeup(images): #shows full sized image as a button on top of everything!
    zorder 10
    default image_index = 0
    key "mousedown_4" action If(
     image_index != 0,
     SetScreenVariable("image_index", image_index -1),
     Hide("gallery_closeup", transition = dissolve))
    key "mousedown_5" action If(
     image_index < len(images) -1,
     SetScreenVariable("image_index", image_index + 1),
     Hide("gallery_closeup", transition = dissolve))
    imagebutton:
     idle images[image_index]
     at gallery_fade
     action If(
      image_index < len(images) - 1,
      SetScreenVariable("image_index", image_index + 1),
      Hide("gallery_closeup", dissolve))
     xalign 0.5
     yalign 0.98
     background "#fff8"

init python:
    maxnumx = 3
    maxnumy = 3
    maxthumbx = config.screen_width / (maxnumx + 1)
    maxthumby = config.screen_height / (maxnumy + 1)
    maxperpage = maxnumx * maxnumy
    gallery_page = 0
