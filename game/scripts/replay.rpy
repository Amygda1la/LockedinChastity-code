## Replay Gallery screen ######################################
## Take care when making changes to this file #################
screen Replayexit():
    zorder 100
    imagebutton:
        auto "images/replay/exit_%s.png"
        action EndReplay()
        yalign .99
        xalign .99
            #yes AUTO create 2 images titled exit_hover.png and exit_idle.png
            #if you want to change the images for this screen

#add these 2 line below if you want an exit button during the replay(optional)
#this must be added after every label used for replay
# label replayOne
#     if _in_replay:
#         show screen Replayexit


screen replay_gallery_B():

    tag menu
    $start = replay_page * 9
    $end = min(start + 9 - 1, len(Replay_items) - 1)
    use game_menu(_("{size=-20}Replay Gallery{/size}"), scroll="viewport"):
        style_prefix "about"
    use page_list_bar(replay_page, 7, menu_name = "replay_page")
    #grid for images
    grid maxnumx maxnumy:
        pos (gx1, gy1)
        yfill True
        xspacing 100
        yspacing - 160
        for i in range(start, end + 1):
            $Replay_items[i].replay_number = i + 1
            if renpy.seen_label(Replay_items[i].replay):
             imagebutton:
              idle Replay_items[i].thumbs
              hover_foreground "images/hover_2560.png"
              xalign 0.5
              yalign 0.5
              action Replay(Replay_items[i].replay)
              hovered Show("thumbnail_info", None, Replay_items[i].name, Replay_items[i].replay_number)
              unhovered Hide("thumbnail_info")
              at imageThumb
            else:
             imagebutton:
              idle Replay_items[i].thumbs
              hover_foreground "images/hover_2560.png"
              xalign 0.5
              yalign 0.5
              action NullAction()
              hovered Show("thumbnail_info", None, Replay_items[i].name, Replay_items[i].replay_number)
              unhovered Hide("thumbnail_info")
              at imageThumb, locked_blur



    #previous/next buttons
    if replay_page > 0:
        textbutton "{color=#fff}Previous{/color}":
            action SetVariable("replay_page", replay_page - 1)
            xalign 0.3
            yalign 0.98
            background "#000"
    if (replay_page + 1) * 9 < len(Replay_items):
        textbutton "{color=#fff}Next{/color}":
            action SetVariable("replay_page", replay_page + 1)
            xalign 0.9
            yalign 0.98
            background "#000"

