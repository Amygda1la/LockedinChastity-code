## req for images: 

webp format

thumbnails must end with _t and they must be placed inside gallery thumbnails folder. Also they also must be .webp

Size for the thumbnails images: 550/310

## How to work with it
### For gallery:
Add GalleryItem to the gallery_items list in file gallery_setup.rpy

> helper for gallery:
> 
> gallery_items.append(GalleryItem("thumbnail_text", [list of images name]))

gallery uses first element of [list of images name] and searchess the thumbnail for it in images/gallery thumbnails/ folder. So for each scene you have to add thumbnail version of the first image inside gallery thumbnails folder.

#### Character gallery:

 each character has his own gallery and to update it you need place a scene number inside the character list (they are at the first lines of the gallery.rpy file).
 
 It's easier to Update the character lists after you  already added all the scenes in the gallery_items list
 
 To look for each scene number you need to uncomment line 315 in screens_and_funcs_for_galleries.rpy and hover on the scene number of which you are searching for. The number will appear at the top left corner, so just Add the scene number to the character list this scene is appropriate.
 
### For Replay:
 > helper for replay:
>
 > Replay_items.append(ReplayItem(["the thumbnail_image"], "the_label_from_code", "brief description"))
 
 same thing with character lists. They are in  at the first line of replay.rpy file
 
 Replay menu also searches for the thumbnail in the gallery thumbnails folder, so you can just use the same thumbnail you are using in the gallery menu for the replay
 

### Folder with webp images for the 0.57 version

https://drive.google.com/drive/folders/1DcdzzEKdvd-6Tb8BRdW_6_U2rkKnwUvf?usp=sharing

just replace your images folder with this one. It has all photos converted to webp format and also thumbnails for gallery and replay menus

also replays gui images folder with the one inside repo

P.S I haven't commented anything (im sorry)
