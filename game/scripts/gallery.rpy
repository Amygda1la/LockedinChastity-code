
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





#changed this transform is being used as censor for locked images instead of lock image
#so now it just blures thumbnail image and not replaces it with lock image
transform gallery_blur:
 blur 150
screen gallery_B():

    tag menu
    $ start = gallery_page * maxperpage
    $ end = min(start + maxperpage - 1, len(gallery_items) - 1)
    use game_menu(_("Gallery"), scroll="viewport"):
        style_prefix "about"
#changed this frame generates button for the quick switch between pages in the 5 buttons format
#has one problem (the page, when the lopp ends is coded manually, in this if page < 30 condition)
#the code is a bit complicated (chat gpt wrote it for me), but it is understandable
    frame:
     xalign 0.6
     has hbox spacing 50
     $start_page = max(0, gallery_page - 4)
     for i in range(10):
      $page = start_page + i
      if page < 17:
       textbutton str(page + 1):
        action SetVariable("gallery_page", page)
    #grid for images
    grid maxnumx maxnumy:
        pos (gx1, gy1)
        yfill True
        #changed xspacing from 25 to 100
        xspacing 100
        yspacing - 160
        for i in range(start, end + 1):
            # changed. I just moved the refresh_lock() call,
            # so now it is called regardless of the condition.
            #
            # The second line is needed for the gallery_thumbnail_info screen.
            # It changes the value of the GalleryItem object,
            # so the screen can show the text for the image.
            $gallery_items[i].image_number = i + 1
            $gallery_items[i].refresh_lock()
            #changed. unlockes the cg if unlock_gallery is true and locks if player havent seen
            #them yet.
            if gallery_items[i].is_locked and not persistent.unlock_gallery:
                # changed. Now the locked image is an imagebutton.
                # It is needed because the hover state works only with imagebuttons,
                # when player clicks, the unlock confirmation screen appears, so
                # no player can unlock each scene manually
                imagebutton:
                 idle gallery_items[i].images
                 style "gallery_button"
                 xalign 0.5
                 yalign 0.5
                 action Show("unlock_confirmation", dissolve, gallery_items[i].image_number)
                 #changed. I Deleted the grid for the text, bc it is no longer needed and
                 #now gallery_thumbnail_info screen show the text for player
                 hovered Show("gallery_thumbnail_info", dissolve, gallery_items[i].name, gallery_items[i].image_number)
                 unhovered Hide("gallery_thumbnail_info")
                 #applying the gallery_blur to hide the thumbnail from player
                 at imageThumb, gallery_blur
            else:
                imagebutton:
                    idle gallery_items[i].images
                    style "gallery_button" #delete this line to remove hover
                    action Show("gallery_closeup", dissolve, gallery_items[i].images)
                    hovered Show("gallery_thumbnail_info", dissolve, gallery_items[i].name, gallery_items[i].image_number)
                    unhovered Hide("gallery_thumbnail_info")
                    xalign 0.5
                    yalign 0.5
                    at imageThumb


    #previous and next buttons
    #changed. slightly adjusted the position of next and previous buttons
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
    #changed this is new button that unlocks all cgs,
    textbutton "{color=#000}[('Lock all CGs' if persistent.unlock_gallery else 'Unlock all CGs')]{/color}":
     action ToggleField(persistent, "unlock_gallery")
     xalign 0.6
     yalign 0.98
     background "#fff8"
# changed. "default persistent.unlock_gallery" is used to create the "Unlock All CGs" button
# it is made using two things:
# 1) persistent. Persistent object saves its data to a file, so technically,
# unlock_gallery is just an attribute of the persistent object that Ren'Py saves.
# (its an attribute like GalleryItem.name is an attribute to the GalleryItem object)
#
# 2) default. (I think you know how it works because you used it)
# default tells Ren'Py to create the variable if it hasn't been created yet,
# and not overwrite it if it already exists.
default persistent.unlock_gallery = False
#changed. This varible stores the image numbers of scenes manually unlocked by the player
#A set is use to prevent duplicate scene numbers
default persistent.unlocked_gallery_items = set()
init python:
    maxnumx = 3
    maxnumy = 3
    maxthumbx = config.screen_width / (maxnumx + 1)
    maxthumby = config.screen_height / (maxnumy + 1)
    maxperpage = maxnumx * maxnumy
    gallery_page = 0
