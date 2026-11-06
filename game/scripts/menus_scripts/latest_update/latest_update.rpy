label new_content:
 scene black
 "heya"
 menu:

  "Sissy route":
   $sissy = True
   jump catselfie

  "NTR route":
   $netorare = True
   jump kim_touch

  "NTS route":
   $netorase = True
   jump gaming_time

  "Yelena route":
   $yelena = True
   jump yelena_island

  "Branch Select":
   jump branching
  "Return":
   return

transform bubble_size:
 size (550,310)
 zoom 1
transform bubble_hover:
 zoom 1.2
 ease 0.2 zoom 1
 size (550,310)
transform bubble_anim(x,y,start_wait,alive_wait):
 align (x,y)
 alpha 0
 block:
  pause start_wait
  ease 0.7 alpha 1
  pause alive_wait
  ease 0.7 alpha 0
  pause 2
  repeat
# screen latest_updates:
#  default show_jamie = False
#  tag menu
#  add "images/menus/latest_chapters/latest_chapters_layout.webp"
#  add "thought_circle_small" at bubble_anim(0.42,0.81,1,3.4)
#  add "thought_circle_medium" at bubble_anim(0.40,0.78,1.7,2.7)
#  add "thought_circle_big" at bubble_anim(0.375,0.73, 2.4, 2)
#  if show_jamie:
#   add "jamie_test" pos (1135, 1225) xysize (90, 60)
#  imagebutton:
#   idle At("images/menus/latest_chapters/ntr_route.webp",bubble_size)
#   align(0.4,0.3)
#   action [SetVariable("netorare", True), Start("kim_touch")]
#   hover At("images/menus/latest_chapters/ntr_route_hover.webp",bubble_hover)
#   hovered SetScreenVariable("show_jamie", True)
#   unhovered SetScreenVariable("show_jamie", False)
#  use return_latest_update_button







# screen return_latest_update_button:
#  button:
#   action Return()
#   align (0.03,0.98)
#   xysize (257, 150)
#   add "images/menus/ui_assets/return.webp" at transform:
#    fit "contain"
#    on idle:
#     alpha 1
#    on hover:
#     alpha 0
#   add "images/menus/ui_assets/return_hovered.webp" at transform:
#    fit "contain"
#    on idle:
#     alpha 0
#     zoom 1.2
#    on hover:
#     alpha 1
#     ease 0.2 alpha 1 zoom 1
#     # pause 1
#     # block:
#     #  ease 0.1 zoom 1.2
#     #  ease 0.1 zoom 1
#     #  pause 1
#     #  repeat

#   add "images/menus/ui_assets/ex_right.webp" at transform:
#    offset (170,-10)
#    fit "contain"
#    rotate -17
#    pause 5
#    block:
#     easein 0.1 yoffset -70
#     easeout 0.1 yoffset -10
#     pause 5
#     repeat

# transform route_box_button(x,y):
#  pos (x,y)
#  xysize (1300,700)
#  fit "contain"
#  on idle:
#   alpha 1
#  on hover:
#   alpha 0
# transform route_box_button_hovered(x,y):
#  pos (x,y)
#  xysize (1300,700)
#  fit "contain"
#  on idle:
#   alpha 0
#  on hover:
#   alpha 1


# transform route_size:
#   xysize (1300,700)


# transform route_zoom:
#     on idle:
#         ease 0.2 zoom 0.8
#     on hover:
#         ease 0.2 zoom 1


# screen latest_updates:
#  default gelato_ride = True
#  default ntr_ride = False
#  default nts_ride = False
#  default sissy_ride = False
#  default yelena_ride = False
#  tag menu
#  add"images/menus/ui_assets/backs_latest/back_lay1.webp"
#  add"images/menus/ideas_photos/jamie_overlay.webp" xysize (2560, 1440)
#  # add"images/menus/ui_assets/ntr.webp" at route_box_button(0,0)
 # add"images/menus/ui_assets/ntr_hovered.webp" at route_box_button_hovered(0,0)
 # add"images/menus/ui_assets/nts.webp" at route_box_button(1300,0)
 # add"images/menus/ui_assets/nts_hovered.webp" at route_box_button_hovered(1300,0)
 # add"images/menus/ui_assets/sissy.webp" at route_box_button(0,700)
 # add"images/menus/ui_assets/sissy_hovered.webp" at route_box_button_hovered(0,700)
 # add"images/menus/ui_assets/yelena.webp" at route_box_button(1300,700)
 # add"images/menus/ui_assets/yelena_hovered.webp" at route_box_button_hovered(1300,700)
 # imagebutton:
 #  idle At("images/menus/ui_assets/ntr.webp", route_size)
 #  pos(0,0)
 #  at route_zoom

 #  action [SetVariable("netorare", True), Start("kim_touch")]
 #  hover At("images/menus/ui_assets/ntr_hovered.webp",route_size)
 #  hovered [SetScreenVariable("ntr_ride", True),SetScreenVariable("gelato_ride",False)]
 #  unhovered [SetScreenVariable("ntr_ride", False),SetScreenVariable("gelato_ride",True)]
 # imagebutton:
 #  idle At("images/menus/ui_assets/nts.webp", route_size)
 #  pos(1325,0)
 #  at route_zoom

 #  action [SetVariable("netorase", True), Start("gaming_time")]
 #  hover At("images/menus/ui_assets/nts_hovered.webp",route_size)
 #  hovered [SetScreenVariable("nts_ride", True), SetScreenVariable("gelato_ride",False)]
 #  unhovered [SetScreenVariable("nts_ride", False), SetScreenVariable("gelato_ride",True)]
 # imagebutton:
 #  idle At("images/menus/ui_assets/sissy.webp", route_size)
 #  pos(0,800)
 #  at route_zoom

 #  action [SetVariable("sissy", True), Start("catselfie")]
 #  hover At("images/menus/ui_assets/sissy_hovered.webp",route_size)
 #  hovered [SetScreenVariable("sissy_ride", True),SetScreenVariable("gelato_ride",False)]
 #  unhovered [SetScreenVariable("sissy_ride", False), SetScreenVariable("gelato_ride",True)]
 # imagebutton:
 #  idle At("images/menus/ui_assets/yelena.webp", route_size)
 #  pos(1325,800)
 #  at route_zoom

 #  action [SetVariable("yelena", True), Start("yelena_island")]
 #  hover At("images/menus/ui_assets/yelena_hovered.webp",route_size)
 #  hovered [SetScreenVariable("yelena_ride", True), SetScreenVariable("gelato_ride",False)]
 #  unhovered [SetScreenVariable("yelena_ride", False), SetScreenVariable("gelato_ride",True)]
 # if gelato_ride:
  # add "images/menus/ui_assets/01_G.webp" at ride_anim()
  # add "images/menus/ui_assets/02_E.webp"
  # add "images/menus/ui_assets/03_L.webp"
  # add "images/menus/ui_assets/04_A.webp"
  # add "images/menus/ui_assets/05_T.webp"
  # add "images/menus/ui_assets/06_O.webp"
 # use return_latest_update_button