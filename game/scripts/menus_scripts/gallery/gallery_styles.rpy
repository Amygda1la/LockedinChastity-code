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



transform imageThumb(delay = 0): #images to thumbnail re-sizer
    size (sx, sy) #for 1920x1080 and 1280x720 DO NOT CHANGE