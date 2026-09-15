init python:
    maxnumx = 3
    maxnumy = 3
    maxthumbx = config.screen_width / (maxnumx + 1)
    maxthumby = config.screen_height / (maxnumy + 1)
    maxperpage = maxnumx * maxnumy
    gallery_page = 0
    #changed. This function just adds image number of scene to set that was
    #created in gallery file
    def unlock_gallery_scene(image_number):
     persistent.unlocked_gallery_items.add(image_number)
    #changed. this function is used  to decide which hover we need to use when player hovers over a thumbnail
    #it first checks whether the thumbnail exists in the gallery thumbnails folderm if the thumbnail is not found, it uses the 2560 hover image instead
    def get_gallery_hover(image):
     thumbnail = "images/gallery thumbnails/" + image + ".png"
     if not renpy.loadable(thumbnail):
        return "images/hover_2560.png"
     return "images/hover_550.png"



#here are the styles and transforms used in both the replay and gallery screens

# 1280x720 gallery A
#define sx = 384
#define sy = 216

# # 1280x720 gallery B
define sx = 550
define sy = 310
# 1920x1080 gallery A
#define sx = 600
#define sy = 338

# 1920x1080 gallery B
#define sx = 450
#define sy = 253
# changed. Added these two variables. They are arrays containing
# the predefined positions for the thumbnail text.
#
# These are the formulas I used to calculate the text positions.
#
# info_xspacing and info_yspacing are the spacing values that you used
# when creating the info text grid in the gallery code.
#
# info_xspacing = 100
# info_yspacing = 160
#
# gx2 + (sx + info_xspacing) * column - for info_pos_x
# gy2 + (sy + info_yspacing) * row - for info_pos_y
#
# I slightly adjusted the final positions manually because
# the positions calculated by the formulas didn't look quite right.
#
# The column and row variables are created in the screen definition.
define info_pos_y = [150, 580, 1000]
define info_pos_x = [640, 1290, 1940]
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

# style gallery_button: # hover overlay it must be 4 pixels bigger then the images
    #hover_foreground "images/gallery/hover 1924x1084.png"

style name_text: #text color and outlines please change
     color "#FFFFFF"
     outlines [(3, "#000000", 2, 2)]
     size 44 # 1280x720
    #size 30 #1920x1080

transform imageThumb: #images to thumbnail re-sizer
    size (sx, sy) #for 1920x1080 and 1280x720 DO NOT CHANGE

#the locked image for the galleries
image locked = "images/lock.jpg"
#changed this is just quick transform for the action on cg in gallery
transform gallery_fade:
    alpha 0.0
    linear 0.3 alpha 1.0
style gallery_vertical_bar:
    bar_vertical True
    bar_invert True
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
    #changed.  Mobile slider frame
    if renpy.variant("touch"):
     frame:
      xalign 0.97
      yalign 0.5
      xsize 90
      ysize 500
      background "#0008"
      padding (25, 25)
      vbox:
       spacing 15
       xalign 0.5
       yalign 0.5
       text "[image_index + 1] / [len(images)]":
        xalign 0.5
        size 24
        color "#ffffff"
       bar:
        value ScreenVariableValue("image_index", range=max(0, len(images) - 1) )
        xsize 35
        ysize 400
        style "gallery_vertical_bar"
#changed. This screen displays the name of the GalleryItem object as text
# when the player hovers over a thumbnail.
#
# The second argument is used to determine the position of the hovered thumbnail
# and place the text correctly.
screen gallery_thumbnail_info(name, image_number):
#changed. image_number - 1 is needed because it allows us to correctly calculate
#the row and column values for the grid system.
 $remainder = (image_number-1) % 9
 $row = remainder // 3
 $column = remainder % 3
 text "[name]":
  style_prefix "name"
  #changed.  Instead of calculating the text position,
  #we pick one of the predefined positions using the row and column values.
  #with the rown and column variables
  pos(info_pos_x[column], info_pos_y[row])
 # сhanged. Limit the text size so that it wraps to a new line
 # if it doesn't fit within the thumbnail.
  xmaximum 550
  ymaximum 310
#changed. this screen is used to ask the player if he wants to
# unlock locked scene he clicked on
screen unlock_confirmation(image_number):
 modal True
 frame:
  xalign 0.5
  yalign 0.5
  padding (60, 40)
  vbox:
   spacing 40
   text "Unlock this scene?":
    xalign 0.5
   fixed:
    xsize 500
    ysize 60
    textbutton "Yes":
     xalign 0.0
     yalign 0.5
     action [Function(unlock_gallery_scene, image_number),Hide("unlock_confirmation")]
    textbutton "No":
     xalign 1.0
     yalign 0.5
     action Hide("unlock_confirmation")



screen page_list_bar(page_index):
 frame:
  xalign 0.6
  has hbox spacing 50
  $start_page = max(0, page_index - 4)
  for i in range(10):
   $page = start_page + i
   if page < 17:
    textbutton str(page + 1):
     action SetVariable("gallery_page", page)

