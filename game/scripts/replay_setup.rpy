## Replay Gallery screen ######################################
##
## This is a simple screen that shows buttons that replay a scene from the game.
init python:

    maxthumbx = config.screen_width / (3 + 1)
    maxthumby = config.screen_height / (3 + 1)

    replay_page = 0

    class ReplayItem:
        def __init__(self, thumbs, replay, name, locked="locked"):
            self.thumbs = thumbs
            self.replay = replay
            self.name = name
            self.locked=locked

    #add replay items here format below
    #Replay_items.append(ReplayItem(["the thumbnail"], "the_label_from_code", "brief description"))
    Replay_items = []
    Replay_items.append(ReplayItem("alex sex 1", "party_alex_invite_ntr", "Alex and Kim's island party"))
    Replay_items.append(ReplayItem("trio party 1", "party_alex_invite_nts", "Kim missing out on the party"))
    Replay_items.append(ReplayItem("jamie ponder 1", "foreign_date", "Jamie's Date with the foreigner"))
    Replay_items.append(ReplayItem("ky plane 1", "kim_vs_yelena_plane", "Kim and Yelena's battle of wits")) 
    Replay_items.append(ReplayItem("diane plane bj 1", "diane_plane_bj", "Diane airplane BJ"))
    Replay_items.append(ReplayItem("diane door mad", "missing_william_jamie", "Diane misses William (Jamie POV)"))
    Replay_items.append(ReplayItem("diane door mad", "missing_william", "Diane misses William (Diane POV)"))
    Replay_items.append(ReplayItem("kim jamie mirror 1", "caging_up", "Jamie wears a cage"))
    Replay_items.append(ReplayItem("push down 1", "catselfie", "Will Takes Jamie's Picture"))
    Replay_items.append(ReplayItem("jamie will diner 1", "tcg_cont", "Will takes \"Jenny\" on a Date"))
    Replay_items.append(ReplayItem("jamie plap 1", "wplaps", "Kim punishes Jamie for ignoring her"))
    Replay_items.append(ReplayItem("jamie frott 1", "rocknstone", "Will and Jamie Sword Fight"))
    Replay_items.append(ReplayItem("jamie mirror lingerie", "kim_punishment", "Kim takes \"Jenny\" on a Date"))
    Replay_items.append(ReplayItem("raven pic 1", "axe", "The group goes to a convention while cosplaying"))
    Replay_items.append(ReplayItem("kim succumb 1", "kim_touch", "Kim's First Creampie"))
    Replay_items.append(ReplayItem("kim succumb 1", "jamie_delivery", "Kim's First Creampie (Jamie POV)"))




# a black background screen for the selection
image black = "#000000"

#replay thumbnails images setup defined here
image alexpussy = ("images/cg/alex doggy1.png")
image Rthumb1 = ("images/replay/replay_unlock.jpg")
#image Rthumb2 = ("images/replay/anotherimage.jpg")