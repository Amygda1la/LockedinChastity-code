
screen gallery_A():

    tag menu

    add "gray"

    $ start = gallery_page * maxperpage
    $ end = min(start + maxperpage - 1, len(gallery_items) - 1)

    #grid for images
    grid maxnumx maxnumy:
        xfill True
        yfill True

        for i in range(start, end + 1):
            $gallery_items[i].refresh_lock()
            if gallery_items[i].is_locked:
                add gallery_items[i].locked:
                    xalign 0.5
                    yalign 0.5
                    at imageThumb
            else:
                imagebutton:
                    idle gallery_items[i].images
                    style "gallery_button" #delete this line to remove hover
                    action Show("gallery_closeup", dissolve, gallery_items[i].images)
                    xalign 0.5
                    yalign 0.5
                    at imageThumb

        #required to fill in empty grid items
        for i in range(end - start + 1, maxperpage):
            null

    #grid for info
    grid maxnumx maxnumy:
        pos (gx2, gy2)
        xfill True
        yfill True
        xspacing 25
        yspacing - 190
        for i in range(start, end + 1):
            hbox:
                style_prefix "name"
                spacing maxthumbx - 20
                xalign 0.0
                yalign 0.1
                text gallery_items[i].name
                xysize(sx, sy)
        #required to fill in empty grid items
        for i in range(end - start + 1, maxperpage):
            null

    #previous, next, and return buttons
    if gallery_page > 0:
        textbutton "{color=#000}Previous{/color}":
            action SetVariable("gallery_page", gallery_page - 1)
            xalign 0.1
            yalign 0.98
            background "#fff8"
    if (gallery_page + 1) * maxperpage < len(gallery_items):
        textbutton "{color=#000}Next{/color}":
            action SetVariable("gallery_page", gallery_page + 1)
            xalign 0.9
            yalign 0.98
            background "#fff8"
    textbutton "{color=#000}Return{/color}":
        action Return()
        xalign 0.5
        yalign 0.98
        background "#fff8"
#changed this is transform that you can replace the lock image with the blur like on value 80 it can work like an option
# transform gallery_blur:
#  blur 10
screen gallery_B():

    tag menu
    $ start = gallery_page * maxperpage
    $ end = min(start + maxperpage - 1, len(gallery_items) - 1)
    use game_menu(_("Gallery"), scroll="viewport"):
        style_prefix "about"
#changed it is just temp gallery page buttons that are coded manually cause i got bored
# (will be replaced with the normal one)
    frame:
     xalign 0.6
     has hbox spacing 30
     textbutton "1":
       action SetVariable("gallery_page", 0)
     textbutton "2":
       action SetVariable("gallery_page", 1)
     textbutton "3":
       action SetVariable("gallery_page", 2)
     textbutton "4":
       action SetVariable("gallery_page", 3)
     textbutton "5":
       action SetVariable("gallery_page", 4)
    #grid for images
    grid maxnumx maxnumy:
        pos (gx1, gy1)
        yfill True
        #changed xspacing from 25 to 100
        xspacing 100
        yspacing - 160
        for i in range(start, end + 1):
            #changed to lock the images if unlock_gallery is false and it works with prev unlocked images
            #(the code below doesnt close them)
            #also deleted the  if gallery_items[i].is_locked: before add because it works without it
            if gallery_items[i].is_locked and not persistent.unlock_gallery:
                $gallery_items[i].refresh_lock()
                add gallery_items[i].locked:
                    xalign 0.5
                    yalign 0.5
                    at imageThumb
            else:
                imagebutton:
                    idle gallery_items[i].images
                    #changed added hover image so this line make sense now
                    style "gallery_button" #delete this line to remove hover
                    action Show("gallery_closeup", dissolve, gallery_items[i].images)
                    xalign 0.5
                    yalign 0.5
                    at imageThumb

        #required to fill in empty grid items
        for i in range(end - start + 1, maxperpage):
            null
    #grid for info
    grid maxnumx maxnumy:
        pos (gx2, gy2)
        yfill True
        #changed to adjust the info with previously displaced thumbs xspcing changed fromm 25 to 100
        xspacing 100
        yspacing - 160

        for i in range(start, end + 1):
        ## changed it so it unlocks info with images if unlock all cgs is clicked
        #the if statement is just reversed version of if statement in grid for images code
         if not (gallery_items[i].is_locked) or persistent.unlock_gallery:
            hbox:
                style_prefix "name"
                spacing maxthumbx - 20
                xalign 0.0
                yalign 0.1
                text gallery_items[i].name
                xysize(sx, sy)
         else:
          null

        #required to fill in empty grid items
        for i in range(end - start + 1, maxperpage):
            null

    #previous and next buttons
    if gallery_page > 0:
        textbutton "{color=#000}Previous{/color}":
            action SetVariable("gallery_page", gallery_page - 1)
            xalign 0.3
            yalign 0.98
            background "#fff8"
    if (gallery_page + 1) * maxperpage < len(gallery_items):
        textbutton "{color=#000}Next{/color}":
            action SetVariable("gallery_page", gallery_page + 1)
            xalign 0.9
            yalign 0.98
            background "#fff8"
    #changed this is new button that unlocks all cgs, and it works like toggle
    textbutton "{color=#000}[('Lock all CGs' if persistent.unlock_gallery else 'Unlock all CGs')]{/color}":
     action ToggleField(persistent, "unlock_gallery")
     xalign 0.6
     yalign 0.98
     background "#fff8"
#changed What it does: 1)persistent thing saves the state in some file and technically unlock_gallery
#is just a field of persistent object that renpy somehow saves
# default (i think you know how it works but bc you used it)(im sorry i dont know a thing)
# default just tells renpy to create variable if it was not created and not eveerwrite it if it was created already
#this variable is created to make the unlock all cgs button
default persistent.unlock_gallery = False
init python:
    maxnumx = 3
    maxnumy = 3
    maxthumbx = config.screen_width / (maxnumx + 1)
    maxthumby = config.screen_height / (maxnumy + 1)
    maxperpage = maxnumx * maxnumy
    gallery_page = 0
