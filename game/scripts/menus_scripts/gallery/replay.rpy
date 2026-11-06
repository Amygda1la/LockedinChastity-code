init python:
 replay_page = 0
 character_index_replay = 0
 characters_replay = ["All", "Kim", "Diane", "Jamie", "Yelena"]
 kim_replays = [2,3,4,5,8,10,13,15,16,18,19,20,24,25,28,31,33,34,36,37,38,39,40,42,44,45,46,47,48,50,51,52,54,57,58,59,60,61,63,64,66,67,68,70,71,72,73,75,76,77,78,80,81,83,87,90,92,93,94,96,100]
 diane_replays = [7,9,11,12,14,17,22,23,26,27,29,32,33,34,35,37,41,43,48,49,51,57,60,61,66,68,69,70,71,73,74,76,84,86,98,100]
 jamie_replays = [1,3,6,10,15,20,21,24,25,29,30,31,33,34,35,37,42,44,45,48,50,52,55,56,58,59,60,62,65,66,68,70,71,72,73,75,77,78,82,83,85,87,88,89,90,91,92,93,95,96,97]
 yelena_replays = [101,102,103,104,105,106,107,108,109,110,111,68,70,72,73,75,79,83,99]

screen replay_gallery_B():
    tag menu
    $start = replay_page * maxperpage
    $character_properties = get_list_of_character_properties(character_index_replay, True)
    # $scenes_list = get_characters_replay(characters_replay[character_index_replay])
    $scenes_list = character_properties[0]
    $end = min(start + maxperpage, len(Replay_items))
    $max_pages =  (len(scenes_list)+8) // 9
    use game_menu(_("{size=-20}Replays{/size}"), scroll="viewport"):
     style_prefix "about"
    use page_list_bar(replay_page, max_pages, menu_name = "replay_page")
    use menu_manager("replay_page",replay_manager_switch,scenes_list)

    # use menu_manager("replay_page",replay_manager_switch,Replay_items)

    grid maxnumx maxnumy:
        at gallery_open
        pos (gx1, gy1)
        yfill True
        xspacing 100
        yspacing - 160
        for scene_index, scene_number  in enumerate(scenes_list[start:end]):
            $i = scene_number -1
            $hover_image = character_properties[1]
            if renpy.seen_label(Replay_items[i].replay):
             imagebutton:
              idle Replay_items[i].thumbnail_image
              hover_foreground  At(hover_image, hover_blur)
              xalign 0.5
              yalign 0.5
              action Replay(Replay_items[i].replay)
              hovered Show("thumbnail_info", None, Replay_items[i].name, Replay_items[i].replay_number, scene_index)
              unhovered Hide("thumbnail_info")
              at imageThumb
            else:
             imagebutton:
              idle Replay_items[i].thumbnail_image
              hover_foreground  At(hover_image, hover_blur)
              xalign 0.5
              yalign 0.5
              action ( Show("unlock_confirmation", None, Replay_items[i].replay_number,menu_name = "replay_page"))
              hovered Show("thumbnail_info", None, Replay_items[i].name, Replay_items[i].replay_number, scene_index)
              unhovered Hide("thumbnail_info")
              at imageThumb, locked_blur


    frame:
     xalign 0.99
     ysize 85
     padding (9, 0)
     text "[get_number_of_unlocked_scenes(scenes_list,'replay_page')]/[len(scenes_list)] unlocked":
        size 35
        color "#ffffff"
        xalign 0.5
        yalign 0.5


    frame:
     yalign 0.98
     xalign 0.6
     # background Frame(Solid(characters_colors_dict_replay[characters_replay[character_index_replay]][0]), 4, 4)
     background Frame(character_properties[1], 10,10)
     textbutton "{color=[character_properties[2]]}[characters[character_index_replay]]{/color}":
      background "#000000"
      action [CycleVariable("character_index_replay", [0,1,2,3,4]), SetVariable("replay_page", 0)]


    frame:
     xalign 0.5
     yalign 0.98
     textbutton "⇄":
      action ToggleVariable("replay_manager_switch")
