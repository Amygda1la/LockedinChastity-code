# changed. "default persistent.unlock_gallery" is used to create the "Unlock All CGs" button
# it is made using two things:
# 1) persistent. Persistent object saves its data to a file, so technically,
# unlock_gallery is just an attribute of the persistent object that RenPy saves.
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



screen gallery_B():
    tag menu
    $ start = gallery_page * maxperpage
    $ end = min(start + maxperpage - 1, len(gallery_items) - 1)
    use game_menu(_("Gallery"), scroll="viewport"):
        style_prefix "about"
#changed this frame generates button for the quick switch between pages in the 10 buttons format
#has one problem (the page, when the loop ends is coded manually the max_pages variable, in this [if page < max_pages] condition)
    use page_list_bar(gallery_page, 20, menu_name = "gallery_page")
    #grid for images
    grid maxnumx maxnumy:
        pos (gx1, gy1)
        yfill True
        xspacing 100
        yspacing - 160
        for i in range(start, end + 1):
            $gallery_items[i].image_number = i + 1
            $gallery_items[i].refresh_lock()
            $hover_image = get_gallery_hover(gallery_items[i].images[0])
            $is_locked = gallery_items[i].is_locked and not persistent.unlock_gallery
            if is_locked:
             $gallery_idle = At(gallery_items[i].thumbnail_image, locked_blur)
            else:
             $gallery_idle = gallery_items[i].thumbnail_image
            imagebutton:
             idle gallery_idle
             # style "gallery_button" #delete this line to remove hover
             hover_foreground hover_image
             xalign 0.5
             yalign 0.5
             action ( Show("unlock_confirmation", None, gallery_items[i].image_number) if is_locked else Show("gallery_closeup", dissolve, gallery_items[i].images))
             #changed. I Deleted the grid for the text, bc it is no longer needed and
             #now thumbnail_info screen show the text for player
             hovered Show("thumbnail_info", None, gallery_items[i].name, gallery_items[i].image_number)
             unhovered Hide("thumbnail_info")
             at imageThumb



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
    #changed this is new button that unlocks all cgs,
    textbutton "{color=#000}[('Lock all CGs' if persistent.unlock_gallery else 'Unlock all CGs')]{/color}":
     action ToggleField(persistent, "unlock_gallery")
     xalign 0.6
     yalign 0.98
     background "#fff8"