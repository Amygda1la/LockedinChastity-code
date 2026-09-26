init python:
    gallery_page = 0
    characters_index = 0
    characters = ["All", "Kim", "Diane", "Jamie", "Yelena", "Others"]
    kim_gallery = [2,3,4,6,7,10,12,16,17,20,25,27,28,31,32,33,34,35,36,37,38,39,46,47,48,51,57,60,64,67,68,69,70,73,74,76,77,78,79,81,82,83,84,85,87,94,98,100,101,109,110,111,116,118,119,120,121,125,128,130,134,135,136,144,145,146,149,164,165,167,168,169,170,171,177,178]
    diane_gallery = [9,13,18,19,23,24,29,30,41,42,44,45,52,53,54,58,62,63,66,68,69,71,88,89,91,92,99,104,105,106,111,114,116,118,119,126,132,134,135,136,148,150,151,170,172,173,174,176,177]
    jamie_gallery = [5,8,14,15,21,22,26,40,43,50,55,59,61,65,70,73,75,86,90,94,95,96,107,108,112,113,115,117,120,124,127,131,133,137,138,142,147,149,152,153,156,157,158,159,160,161,162,163,166,167,168,169,172]
    yelena_gallery = [56,86,97,102,103,122,123,128,129,139,149,175]
    others_gallery = [1,11,72,80,93,140,141,143,154,155]
    characters_colors_dict = {"All": ("#000000","#FFFFFF"), "Kim": ("#FDFFE3","#40D1FF"), "Diane": ("#2B2B2B","#96391A"), "Jamie": ("#525252", "#854325"), "Yelena": ("#B39800", "#00D66F"), "Others": ("#B500FF", "#FC0D95")}



    def get_characters_gallery(character):
     if character == "All":
      return list(range(1, len(gallery_items)+1))
     match character:
      case "Kim":
       return kim_gallery
      case "Diane":
       return diane_gallery
      case "Jamie":
       return jamie_gallery
      case "Yelena":
       return yelena_gallery
      case "Others":
       return others_gallery
     return []



    def get_number_of_unlocked_scenes (scenes_list):
     return len([scene for scene in scenes_list if scene in persistent.unlocked_gallery_scenes])



screen gallery_B():
    tag menu
    $ scenes_list = get_characters_gallery(characters[characters_index])
    $ start = gallery_page * maxperpage
    $ end = min(start + maxperpage, len(scenes_list))
    $ max_pages = (len(scenes_list)+8) // 9
    use game_menu(_("Gallery"), scroll="viewport"):
        style_prefix "about"
    use page_list_bar(gallery_page, max_pages, menu_name = "gallery_page")
    use menu_manager("gallery_page",gallery_manager_switch,scenes_list)
    #grid for images
    grid maxnumx maxnumy:
        at gallery_open
        pos (gx1, gy1)
        yfill True
        xspacing 100
        yspacing - 160
        for scene_index, scene_number in enumerate(scenes_list[start:end]):
            $i = scene_number - 1
            $hover_image = get_gallery_hover(gallery_items[i].images[0])
            $is_locked = gallery_items[i].image_number not in persistent.unlocked_gallery_scenes
            if is_locked:
             $gallery_idle = At(gallery_items[i].thumbnail_image, locked_blur)
            else:
             $gallery_idle = gallery_items[i].thumbnail_image
            imagebutton:
             idle gallery_idle
             hover_foreground  At(hover_image, hover_blur)
             xalign 0.5
             yalign 0.5
             action ( Show("unlock_confirmation", None, gallery_items[i].image_number,menu_name = "gallery_page") if is_locked else Show("gallery_closeup", dissolve, gallery_items[i].images))
             hovered Show("thumbnail_info", None, gallery_items[i].name, gallery_items[i].image_number, scene_index)
             unhovered Hide("thumbnail_info")
             at imageThumb


    frame:
     xalign 0.5
     yalign 0.98
     textbutton "⇄":
      action ToggleVariable("gallery_manager_switch")


    frame:
     xalign 0.99
     ysize 85
     padding (9, 0)
     text "[get_number_of_unlocked_scenes(scenes_list)]/[len(scenes_list)] unlocked":
        size 35
        color "#ffffff"
        xalign 0.5
        yalign 0.5


    frame:
     yalign 0.98
     xalign 0.6
     background Frame(Solid(characters_colors_dict[characters[characters_index]][0]), 4, 4)
     textbutton "{color=[characters_colors_dict[characters[characters_index]][1]]}[characters[characters_index]]{/color}":
      background "#000000"
      action [CycleVariable("characters_index", [0,1,2,3,4,5]), SetVariable("gallery_page", 0)]
