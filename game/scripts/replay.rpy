init python:
 replay_page = 0



screen replay_gallery_B():
    tag menu
    $start = replay_page * maxperpage
    $end = min(start + maxperpage, len(Replay_items))
    $max_pages =  (len(Replay_items)+8) // 9
    use game_menu(_("{size=-20}Replay Gallery{/size}"), scroll="viewport"):
        style_prefix "about"
    use page_list_bar(replay_page, max_pages, menu_name = "replay_page")
    # use menu_manager("replay_page",replay_manager_switch,Replay_items)
    #grid for images
    grid maxnumx maxnumy:
        at gallery_open
        pos (gx1, gy1)
        yfill True
        xspacing 100
        yspacing - 160
        for scene_index, i  in enumerate(range(start,end)):
            if renpy.seen_label(Replay_items[i].replay):
             imagebutton:
              idle Replay_items[i].thumbnail_image
              hover_foreground  At("images/hover_550.webp", hover_blur)
              xalign 0.5
              yalign 0.5
              action Replay(Replay_items[i].replay)
              hovered Show("thumbnail_info", None, Replay_items[i].name, Replay_items[i].replay_number,scene_index)
              unhovered Hide("thumbnail_info")
              at imageThumb
            else:
             imagebutton:
              idle Replay_items[i].thumbnail_image
              hover_foreground  At("images/hover_550.webp", hover_blur)
              xalign 0.5
              yalign 0.5
              action NullAction()
              hovered Show("thumbnail_info", None, Replay_items[i].name, Replay_items[i].replay_number, scene_index)
              unhovered Hide("thumbnail_info")
              at imageThumb, locked_blur

    # frame:
    #  xalign 0.5
    #  yalign 0.98
    #  textbutton "⇄":
    #   action ToggleVariable("replay_manager_switch")
