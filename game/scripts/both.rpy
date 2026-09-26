init python:
    maxnumx = 3
    maxnumy = 3
    maxthumbx = config.screen_width / (maxnumx + 1)
    maxthumby = config.screen_height / (maxnumy + 1)
    maxperpage = maxnumx * maxnumy


    
    def get_gallery_hover(image):
     thumbnail = "images/gallery thumbnails/" + image + "_t" + ".webp"
     if not renpy.loadable(thumbnail):
      return "images/hover_2560.webp"
     match characters[characters_index]:
      case "Kim":
       return "images/kim_hover.webp"
      case "Diane":
       return "images/diane_hover.webp"
      case "Jamie":
       return "images/jamie_hover.webp"
      case "Yelena":
       return "images/yelena_hover.webp"
      case "Others":
       return "images/others_hover.webp"
     return "images/hover_550.webp"


    # replay_manager_switch = False
    gallery_manager_switch = False



    def unlock_all_scenes(menu_name, scenes_list):
     if menu_name == "replay_page":
      for i in range(len(Replay_items)):
       persistent.unlocked_replay_scenes.add(Replay_items[i].replay_number)
     else:
      for scene in scenes_list:
       persistent.unlocked_gallery_scenes.add(scene)



    def lock_all_scenes(menu_name,scenes_list):
     if menu_name == "replay_page":
      persistent.unlocked_replay_scenes = set()
     else:
      for scene in scenes_list:
       persistent.unlocked_gallery_scenes.discard(scene)



    def lock_page(page,menu_name):
     first_elem = page * 9
     if menu_name == "replay_page":
      last_elem = min(first_elem + 9, len(Replay_items))
      for i in range(first_elem, last_elem):
       persistent.unlocked_replay_scenes.discard(Replay_items[i].replay_number)
     else:
      scenes_list = get_characters_gallery(characters[characters_index])
      last_elem = min(first_elem + 9, len(scenes_list))
      for scene_number in scenes_list[first_elem:last_elem]:
       persistent.unlocked_gallery_scenes.discard(scene_number)



    def unlock_page(page,menu_name):
     first_elem = page * 9
     if menu_name == "replay_page":
      last_elem = min(first_elem + 9, len(Replay_items))
      for i in range(first_elem, last_elem):
       persistent.unlocked_replay_scenes.add(Replay_items[i].replay_number)
     else:
      scenes_list = get_characters_gallery(characters[characters_index])
      last_elem = min(first_elem + 9, len(scenes_list))
      for scene_number in scenes_list[first_elem:last_elem]:
       persistent.unlocked_gallery_scenes.add(scene_number)



    def unlock_scene(scene_number,menu_name):
     if menu_name == "replay_page":
      persistent.unlocked_replay_scenes.add(scene_number)
     else:
      persistent.unlocked_gallery_scenes.add(scene_number)



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



transform locked_blur:
 blur 150



transform hover_blur:
    alpha 0.0
    size (550,310)
    blur 110
    linear 0.15 alpha 1.0



transform gallery_open:
    alpha 0.0
    blur 20
    ease 0.4 alpha 1.0 blur 0



 transform gallery_fade:
    alpha 0.0
    linear 0.3 alpha 1.0



style gallery_vertical_bar:
    bar_vertical True
    bar_invert True



transform imageThumb: #images to thumbnail re-sizer
    size (sx, sy) #for 1920x1080 and 1280x720 DO NOT CHANGE



#the locked image for the galleries
image locked = "images/lock.jpg"



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



screen thumbnail_info(name, image_number,scene_index):
 $row = scene_index // 3
 $column = scene_index % 3
 text "[name]":
  style_prefix "name"
  pos(info_pos_x[column], info_pos_y[row])
  xmaximum 550
  ymaximum 310



screen unlock_confirmation(image_number,menu_name):
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
     action [Function(unlock_scene, image_number,menu_name),Hide("unlock_confirmation")]
    textbutton "No":
     xalign 1.0
     yalign 0.5
     action Hide("unlock_confirmation")



screen manager_confirmation(function, *args):
 modal True
 frame:
  xalign 0.5
  yalign 0.5
  padding (60, 40)
  vbox:
   spacing 40
   text "Sure?":
    xalign 0.5
   fixed:
    xsize 500
    ysize 60
    textbutton "Yes":
     xalign 0.0
     yalign 0.5
     action [Function(function, *args),Hide("manager_confirmation")]
    textbutton "No":
     xalign 1.0
     yalign 0.5
     action Hide("manager_confirmation")



screen page_list_bar(page_index, max_pages, menu_name):
 frame:
  xalign 0.265
  has hbox spacing 50
  if page_index > 0:
   textbutton "{color=#fff}<<{/color}":
    action SetVariable(menu_name, 0)
   textbutton "{color=#fff}<{/color}":
    action SetVariable(menu_name, page_index - 1)
  else:
   textbutton "{color=#a8aaad}<<{/color}":
    action NullAction()
   textbutton "{color=#a8aaad}<{/color}":
    action NullAction()
 frame:
  xalign 0.6
  has hbox spacing 50
  $start_page = max(0, page_index - 4)
  for i in range(10):
   $page = start_page + i
   if page < max_pages:
    textbutton str(page + 1):
     action SetVariable(menu_name, page)
 frame:
  xalign 0.85
  has hbox spacing 50
  if page_index != max_pages - 1:
   textbutton "{color=#fff}>{/color}":
    action SetVariable(menu_name, page_index + 1)
   textbutton "{color=#fff}>>{/color}":
    action SetVariable(menu_name, max_pages -1)
  else:
   textbutton "{color=#a8aaad}>{/color}":
    action NullAction()
   textbutton "{color=#a8aaad}>>{/color}":
    action NullAction()



screen menu_manager(menu_name, switched, scenes_list):
  if not switched:
   frame:
    xalign 0.97
    yalign 0.98
    textbutton ("Unlock all CGs" if menu_name == "gallery_page" else "Unlock all Replays"):
    # action Function(unlock_all_scenes,menu_name)
     if len(persistent.unlocked_gallery_scenes) == len(gallery_items):
      action NullAction()
      text_color "#6d6e6e"
     else:
      action Show("manager_confirmation",None, unlock_all_scenes, menu_name, scenes_list)
      text_color"#FFFFFF"
   frame:
    xalign 0.29
    yalign 0.98
    textbutton ("Refresh All Gallery" if menu_name == "gallery_page" else "Refresh all Replays"):
    # action Function(lock_all_scenes,menu_name)
     if len(persistent.unlocked_gallery_scenes) == 0:
      action NullAction()
      text_color "#6d6e6e"
     else:
      action Show("manager_confirmation", None, lock_all_scenes, menu_name, scenes_list)
      text_color"#FFFFFF"

  else:
   if menu_name == "gallery_page":
    $page = gallery_page
   else:
    $page = replay_page
   frame:
    xalign 0.97
    yalign 0.98
    background Frame(Solid("#D10073"), 6, 6)
    textbutton "{color=#000000}Unlock page{/color}":
    # action Function(unlock_page, page, menu_name)
     background "#FFFFFF"
     action Show("manager_confirmation", None, unlock_page, page, menu_name)
   frame:
    xalign 0.29
    yalign 0.98
    background Frame(Solid("#D10073"), 6, 6)
    textbutton "{color=#000000}Refresh Page{/color}":
        background "#FFFFFF"
        action Show("manager_confirmation", None, lock_page, page, menu_name)


