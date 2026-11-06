transform return_hover_bubble:
 alpha 0
 xysize (350, 125)
 on hover:
  alpha 0
  offset (-30, -200)
  ease 0.2 alpha 1 yoffset -20
  block:
   ease 0.1 zoom 1.2 xoffset -60
   ease 2 zoom 1 xoffset -30
   repeat
 on idle:
  ease 0.15 alpha 0 xoffset -200
  # block:
  #   choice:
  #    ease 0.2 xoffset (-20) zoom 0.9
  #   choice:
  #    ease 0.2 xoffset (-40) zoom 1.1
  #   choice:
  #    ease 0.2 yoffset(-30) zoom 0.9
  #   choice:
  #    ease 0.2 yoffset(-10) zoom 1.1
  #   repeat
# transform spike_hover_left:
#  alpha 0
#  offset(-30,-50)
#  on idle:
#   linear 0.15 alpha 0
#  on hover:
#   linear 0.15 alpha 1
#   block:
#    ease 0.3 zoom 1.1
#    easein 0.3 zoom 0.9
#    repeat

# transform spike_hover_right:
#  alpha 0
#  offset(270,-85)
#  rotate 25
#  on idle:
#   linear 0.15 alpha 0
#  on hover:
#   linear 0.15 alpha 1
#   block:
#    easein 0.3 zoom 1.1
#    ease 0.3 zoom 0.9
#    repeat

# screen return_menu_button(x_align = 0.1, y_align = 0.1):
#  button:
#   action Return()
#   align (x_align, y_align)
#   xysize (300, 100)
#   add "images/menus/ui_assets/return_hover.webp" at return_hover_bubble
#   add Transform("images/menus/ui_assets/return.webp", xysize=(300, 100))
        # add "images/menus/ui_assets/spike_left_1.webp" at spike_hover_left
        # add "images/menus/ui_assets/spike_right_1.webp" at spike_hover_right



