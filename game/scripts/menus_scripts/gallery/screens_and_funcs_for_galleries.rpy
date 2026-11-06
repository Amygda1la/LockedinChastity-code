init python:
    maxnumx = 3
    maxnumy = 3
    maxthumbx = config.screen_width / (maxnumx + 1)
    maxthumby = config.screen_height / (maxnumy + 1)
    maxperpage = maxnumx * maxnumy



    def unlock_page_scenes_not_clickable(scenes_list, page, menu_name):
     first_elem = page * 9
     last_elem = first_elem + 9
     page_scenes = scenes_list[first_elem:last_elem]
     if menu_name == "gallery_page":
      for scene in page_scenes:
       if scene not in persistent.unlocked_gallery_scenes:
        return False
      return True
     else:
      for number in page_scenes:
       if 1 <= number <= len(Replay_items):
        if not renpy.seen_label(Replay_items[number - 1].replay):
         return False
      return True



    def lock_page_scenes_not_clickable(scenes_list, page, menu_name):
     first_elem = page * 9
     last_elem = first_elem + 9
     page_scenes = scenes_list[first_elem:last_elem]
     if menu_name == "gallery_page":
      for scene in page_scenes:
       if scene in persistent.unlocked_gallery_scenes:
        return False
      return True
     else:
      for number in page_scenes:
       if 1 <= number <= len(Replay_items):
        if renpy.seen_label(Replay_items[number - 1].replay):
         return False
      return True



    def lock_all_scenes_not_clickable(scenes_list, menu_name):
     if menu_name == "replay_page":
      for number in scenes_list:
       if 1 <= number <= len(Replay_items):
        if renpy.seen_label(Replay_items[number - 1].replay):
         return False
      return True
     else:
      for scene in scenes_list:
       if scene in (persistent.unlocked_gallery_scenes):
        return False
      return True



    def unlock_all_scenes_not_clickable(scenes_list,menu_name):
     if menu_name == "replay_page":
      for number in scenes_list:
       if 1 <= number <= len(Replay_items):
        if not renpy.seen_label(Replay_items[number - 1].replay):
         return False
      return True
     else:
      for scene in scenes_list:
       if scene not in (persistent.unlocked_gallery_scenes):
        return False
      return True



    def get_list_of_character_properties(character_index,is_replay = False):
     ## helper that explains meaning of every index of list this function returns:
     ##  0 - gallery list
     ##  1 - hover image
     ##  2 - text color
      if not is_replay:
       match characters[character_index]:
        case "All":
         return [list(range(1, len(gallery_items)+1)), "gui/characters_hovers/hover_550.webp", "#FFFFFF"]
        case "Kim":
         return [kim_gallery, "gui/characters_hovers/kim_hover.webp", "#40D1FF"]
        case "Diane":
         return [diane_gallery, "gui/characters_hovers/diane_hover.webp", "#96391A"]
        case "Jamie":
         return [jamie_gallery, "gui/characters_hovers/jamie_hover.webp", "#854325"]
        case "Yelena":
         return [yelena_gallery, "gui/characters_hovers/yelena_hover.webp", "#00D66F"]
        case "Others":
         return [others_gallery, "gui/characters_hovers/others_hover.webp", "#FC0D95"]
      else:
       match characters_replay[character_index_replay]:
        case "All":
         return [list(range(1, len(Replay_items)+1)), "gui/characters_hovers/hover_550.webp", "#FFFFFF"]
        case "Kim":
         return [kim_replays, "gui/characters_hovers/kim_hover.webp", "#40D1FF"]
        case "Diane":
         return [diane_replays, "gui/characters_hovers/diane_hover.webp", "#96391A"]
        case "Jamie":
         return [jamie_replays, "gui/characters_hovers/jamie_hover.webp", "#854325"]
        case "Yelena":
         return [yelena_replays, "gui/characters_hovers/yelena_hover.webp", "#00D66F"]



    replay_manager_switch = False
    gallery_manager_switch = False



    def get_number_of_unlocked_scenes (scenes_list,menu_name):
     if menu_name == "gallery_page":
      return len([scene for scene in scenes_list if scene in persistent.unlocked_gallery_scenes])
     else:
      return len([replay for replay in scenes_list if renpy.seen_label(Replay_items[replay -1].replay)])



    def unlock_all_scenes(menu_name, scenes_list):
     if menu_name == "replay_page":
      for i in scenes_list:
       replay_item = Replay_items[i - 1]
       renpy.mark_label_seen(replay_item.replay)
     else:
      for scene in scenes_list:
       persistent.unlocked_gallery_scenes.add(scene)



    def lock_all_scenes(menu_name,scenes_list):
     if menu_name == "replay_page":
      for i in scenes_list:
       replay_item = Replay_items[i - 1]
       renpy.mark_label_unseen(replay_item.replay)
     else:
      for scene in scenes_list:
       persistent.unlocked_gallery_scenes.discard(scene)



    def lock_page(page,menu_name, scenes_list):
     first_elem = page * 9
     last_elem = min(first_elem + 9, len(scenes_list))
     if menu_name == "replay_page":
      for i in scenes_list[first_elem:last_elem]:
       replay_item = Replay_items[i - 1]
       renpy.mark_label_unseen(replay_item.replay)
     else:
      for scene_number in scenes_list[first_elem:last_elem]:
       persistent.unlocked_gallery_scenes.discard(scene_number)



    def unlock_page(page,menu_name, scenes_list):
     first_elem = page * 9
     last_elem = min(first_elem + 9, len(scenes_list))
     if menu_name == "replay_page":
      for i in scenes_list[first_elem:last_elem]:
       replay_item = Replay_items[i - 1]
       renpy.mark_label_seen(replay_item.replay)
     else:
      for scene_number in scenes_list[first_elem:last_elem]:
       persistent.unlocked_gallery_scenes.add(scene_number)



    def unlock_scene(scene_number,menu_name):
     if menu_name == "gallery_page":
      persistent.unlocked_gallery_scenes.add(scene_number)
     else:
      renpy.mark_label_seen(Replay_items[scene_number -1].replay)



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



# # #pos positions pixel close enough!
default gx1 = 640 #1280x720
# # #changed to lift all thumbs a bit app to make place for buttons
default gy1 = 10 #1280x720
# #default gx1 = 460 #1920x1080
#default gy1 = 30 #1920x1080

#text
#default gx2 = 25 # gallery_A 1280x720 and 1920x1080
#default gy2 = 10 # gallery_A

# default gx2 = 640 # 322 #1280x720 gallery_B
# #changed i dont remember why(
# default gy2 = 110 #75  #1280x720 gallery_B

#default gx2 = 460 #1920x1080 gallery_B
#default gy2 = 83 #1920x1080 gallery_B

# style gallery_button: # hover overlay it must be 4 pixels bigger then the images
    #hover_foreground "images/gallery/hover 1924x1084.png"


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
 # text "[image_number]"
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
    if menu_name == "gallery_page":
     textbutton ("Unlock all CGs"):
      if unlock_all_scenes_not_clickable(scenes_list, menu_name):
       action NullAction()
       text_color "#6d6e6e"
      else:
       action Show("manager_confirmation",None, unlock_all_scenes, menu_name, scenes_list)
       text_color"#FFFFFF"
    else:
     textbutton ("Unlock all Replays"):
      if unlock_all_scenes_not_clickable(scenes_list, menu_name):
       action NullAction()
       text_color "#6d6e6e"
      else:
       action Show("manager_confirmation", None, unlock_all_scenes, menu_name, scenes_list)
       text_color "#FFFFFF"


    # textbutton ("Unlock all CGs" if menu_name == "gallery_page" else "Unlock all Replays"):
    # action Function(unlock_all_scenes,menu_name)
     # if len(persistent.unlocked_gallery_scenes) == len(gallery_items):
     #  action NullAction()
     #  text_color "#6d6e6e"
     # else:
     #  action Show("manager_confirmation",None, unlock_all_scenes, menu_name, scenes_list)
     #  text_color"#FFFFFF"
   frame:
    xalign 0.29
    yalign 0.98
    if menu_name == "gallery_page":
     textbutton ("Refresh All Gallery"):
      if lock_all_scenes_not_clickable(scenes_list, menu_name):
       action NullAction()
       text_color "#6d6e6e"
      else:
       action Show("manager_confirmation", None, lock_all_scenes, menu_name, scenes_list)
       text_color"#FFFFFF"
    else:
     textbutton ("Refresh all Replays"):
      if lock_all_scenes_not_clickable(scenes_list,menu_name):
       action NullAction()
       text_color "#6d6e6e"
      else:
       action Show("manager_confirmation", None, lock_all_scenes, menu_name, scenes_list)
       text_color "#FFFFFF"
    # textbutton ("Refresh All Gallery" if menu_name == "gallery_page" else "Refresh all Replays"):
    # # action Function(lock_all_scenes,menu_name)
    #  if len(persistent.unlocked_gallery_scenes) == 0:
    #   action NullAction()
    #   text_color "#6d6e6e"
    #  else:
    #   action Show("manager_confirmation", None, lock_all_scenes, menu_name, scenes_list)
    #   text_color"#FFFFFF"

  else:
   if menu_name == "gallery_page":
    $page = gallery_page
   else:
    $page = replay_page
   frame:
    xalign 0.97
    yalign 0.98
    background Frame(Solid("#D10073"), 6, 6)
    textbutton "Unlock page":
     background "#FFFFFF"
     if unlock_page_scenes_not_clickable(scenes_list, page, menu_name):
      text_color "#d4006a"
      action NullAction()
     else:
      action Show("manager_confirmation", None, unlock_page, page, menu_name, scenes_list)
      text_color "#000000"
   frame:
    xalign 0.29
    yalign 0.98
    background Frame(Solid("#D10073"), 6, 6)
    textbutton "Refresh Page":
     background "#FFFFFF"
     if lock_page_scenes_not_clickable(scenes_list, page, menu_name):
      text_color "#d4006a"
      action NullAction()
     else:
      action Show("manager_confirmation", None, lock_page, page, menu_name, scenes_list)
      text_color "#000000"
