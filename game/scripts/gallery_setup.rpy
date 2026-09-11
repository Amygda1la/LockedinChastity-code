#a very simple gallery
#"kim and alex chat 2" in the kim rides a dildo gallery
#diane and will first house sex diane and will video
# wiliam kim doggy 3
# william kim mating press kiss 1
init python:


    class GalleryItem:
        def __init__(self, name, images, locked="locked",image_number = None):
            self.name = name
            self.images = images
            self.locked = locked
            self.refresh_lock()
            # changed. Added this field to the GalleryItem object because it is being used
            # in the gallery_thumbnail_info screen.
            # Every CG in the gallery now has a unique number.
            # The number is basically the i iterator in the for loop
            # that creates the layout for the gallery menu.
            self.image_number = image_number
        # changed. The refresh_lock() function has been changed, so now the gallery
        # will unlock a scene if the player has seen the first image of that scene.
        #
        # This can cause errors if the first images of two scenes are the same.
        # However, if you make a copy of the same image and give it a different name,
        # the problem will be fixed.
        #
        # Also deleted the unlocked counter(im sorry).
        def refresh_lock(self):
            lockme = True
            if renpy.seen_image(self.images[0]):
             lockme = False
            self.is_locked = lockme
    #changed just added all cgs from the first script to the massive in order they are shown in the game, including the animation
    gallery_items = []
    gallery_items.append(GalleryItem("Alex doggy", ["alex doggy1", "alex doggy2", "alex doggy3", "alex doggy4"]))
    gallery_items.append(GalleryItem("Kim selfie", ["kim selfie"] ))
    gallery_items.append(GalleryItem("Kim in Wil's home", ["kim fondle 1", "kim fondle 2", "kim fondle 3", "kim condom1", "kim condom2", "kim masturbating 1", "kim masturbating 2", "kim masturbating 3", "kim and will bathroom up", "kim and will bathroom down"] ))
    gallery_items.append(GalleryItem("Kim window", ["kim window","kim window"] ))
    gallery_items.append(GalleryItem("Kim and Jamie handjob", ["kim and jamie handjob 1", "kim and jamie handjob 2"] ))
    gallery_items.append(GalleryItem("Kim and Alex chat", ["kim and alex chat 1", "kim and alex chat 2", "kim and alex chat 3", "kim and alex chat 31", "kim and alex chat 4", "kim and alex chat 5"] ))
    gallery_items.append(GalleryItem("Kim spies on Alex and Will", ["kim spies on alex and will 1", "kim spies on alex and will 2", "kim spies on alex and will 3", "kim tumbles"] ))
    gallery_items.append(GalleryItem("Jamie and Will sharing a bed", ["jamieandwill cuddlenight","jamieandwill cuddlemorning","will morningwood","will dickreveal","will bulge"] ))
    gallery_items.append(GalleryItem("Will and Diane chat 1", ["will bulgeselfie", "diane lewd1"] ))
    gallery_items.append(GalleryItem("Kim masturbates", ["kim houseselfie","kim text1","kim text0","kim text2","kim text25","kim text3","kim text4","kim text5"] ))
    gallery_items.append(GalleryItem("Alex texts Jamie", ["alex text1", "alex text2"] ))
    gallery_items.append(GalleryItem("Kim sucks a dildo", ["kim dildo1","kim dildo2","kim startsuck1","kim startsuck2", "kim sucking1", "kim sucking2","kim sucking","kim sucking3","kim sucking4","kim imagine","kim imaginarycum", "kim aftermath"] ))
    gallery_items.append(GalleryItem("Will and Diane chat 2", ["diane lewd2","will dickpic","will masturbating"] ))
    gallery_items.append(GalleryItem("Jamie and Kim missionary sex (Jamie's pov)", ["kim and jamie standing","kim and jamie kiss 1","kim and jamie kiss 2","kim and jamie missionary 1","kim and jamie missionary 2","kim and jamie missionary 3","kim and jamie missionary 4","kim and jamie missionary a1","kim and jamie missionary 5","kim and jamie missionary 6","kim and jamie missionary a2","kim and jamie missionary 7"] ))
    gallery_items.append(GalleryItem("Jamie and Kim cowgirl (Jamie's pov)", ["kim and jamie ride 1","kim and jamie ride 2","kim and jamie ride 3","kim and jamie cowgirl 1","kim and jamie cowgirl 2","kim and jamie ride 4"] ))
    gallery_items.append(GalleryItem("Jamie and Kim missionary sex (Kim's pov)", ["kim and jamie standing","kim and jamie kiss 1","kim and jamie kiss 2","kim and jamie missionary 1","kim and jamie missionary 2","kim and jamie missionary kimpov 3","kim and jamie missionary kimpov 4","kim and jamie missionary b1","kim and jamie missionary kimpov 5","kim and jamie missionary kimpov 6","kim and jamie missionary b2","kim and jamie missionary 7"] ))
    gallery_items.append(GalleryItem("Jamie and Kim cowgirl (Kim's pov)", ["kim and jamie ride 1","kim and jamie ride kimpov 2","kim and jamie ride kimpov 3","kim and jamie cowgirl kimpov 1","kim and jamie cowgirl kimpov 2","kim and jamie ride 4"]))
    gallery_items.append(GalleryItem("Will and Diane sexting", ["diane nude text","will dickpic"] ))
    gallery_items.append(GalleryItem("Will and Diane app date", ["diane and will side 1","diane and will side 2","diane and will side 3","diane and will sidefuck 1","diane and will sidefuck 2","diane and will side 4","diane and will side 5","diane and will side 6","diane and will side 7"] ))
    gallery_items.append(GalleryItem("Kim rides a dildo", ["kim and alex chat 2","kim dildo1","kim dildo ride 1","kim dildo ride 2","kim dildo ride 3","kim dildo ride 4","kim cowgirl dildo 1","kim cowgirl dildo 2","kim dildo ride 5","kim dildo ride 6",] ))
    gallery_items.append(GalleryItem("Will and Diane aftermath (Jamie's pov) ", ["dianesextape", "diane and will frontdoor 2", "diane and will frontdoor 1"] ))
    gallery_items.append(GalleryItem("Diane and Will first house sex (Jamie's pov)", ["diane and will roomdoor 6","diane and will roomdoor 1","diane and will roomdoor 2","diane and will roomdoor 3","diane and will roomdoor 4","diane and will roomdoor 5","diane and will roomdoor 6", "diane and will video", "diane and will secret delusion"] ))
    gallery_items.append(GalleryItem("Diane and Will first house sex", ["will and diane doggy 1", "will and diane doggy 2","will and diane doggy 3","will and diane doggy 4","diane and will doggyfuck 1","will and diane doggy 5","will and diane doggy 6","diane and will doggyfuck 2 ","will and diane doggy 5","will and diane doggy 7","will and diane doggy 8","will and diane doggy 9"]))
    gallery_items.append(GalleryItem("Diane and Will doorfuck",["diane and will secret 1","diane and will secret 2","diane and will doorfuck 1","diane and will doorfuck 2","diane and will doorfuck 3","diane and will doorfuck 4","diane and will secret 11","diane and will secret 12","will and diane doggy 1"] ))
    gallery_items.append(GalleryItem("Kim and Jamie doggy (Kim's pov)", ["kim and jamie doggy 1","kim and jamie doggykimpov 2","kim and jamie doggy kim pov 2","kim and jamie doggykimpov 4","kim and jamie doggy kim pov 2","kim and jamie doggy kim pov 3","kim and jamie doggykimpov 7",] ))
    gallery_items.append(GalleryItem("Kim and Jamie doggy (Jamie's pov)", ["kim and jamie doggy 1","kim and jamie doggy 2","kim and jamie doggy jamie pov 1","kim and jamie doggy jamie pov 2","kim and jamie doggy 4","kim and jamie doggy jamie pov 2","kim and jamie doggy jamie pov 3","kim and jamie doggy 7"] ))
    gallery_items.append(GalleryItem("Kim and Will after party", ["kim and will bj bulge","kim and will bj 6",] ))
    gallery_items.append(GalleryItem("Kim gives Will a blowjob", ["kim and will bj bulge", "kim and will bj 6","kim and will bj 1","kim and will bj 2","kim and will bj 3","kim and will bj 4","kim and will bj 2","kim and will blowjob 1","kim and will blowjob 2","kim and will bj 4","kim and will bj 5",] ))
    gallery_items.append(GalleryItem("Will carries Diane", ["diane will carry 0","diane will carry 1","diane will carry 2","diane will carry 1","diane will carry 2","diane and will carry 1","diane will carry 2","diane and will carry 2","diane will carry 1","diane will carry 3","diane will carry 4","diane will carry 5","diane will carry 6",]))
    gallery_items.append(GalleryItem("Diane gives a handjob ", ["diane handjob 1","diane and will handjob 1","diane and will handjob 2","diane handjob 4","diane handjob 5",]))
    gallery_items.append(GalleryItem("Kim masturbating to bbc", ["kim bbc masturbating","kim bbc masturbating cum","kim stalking 1","kim stalking 2","kim stalking 3","kim stalking 4"]))
    gallery_items.append(GalleryItem("Kim and Will dancing", ["william kim dance 1","william kim dance 2"]))
    gallery_items.append(GalleryItem("Will and Kim after party drunk", ["william kim body kiss","william kim body","william kim body kiss","william kim kiss 1","william kim kiss 2"]))
    gallery_items.append(GalleryItem("Will and Kim after party missionary", ["william kim missionary 1","william kim missionary 2","william kim missionary 3","william kim missionary 4","william kim missionary 5","william kim missionary 4","kim and will missionary 1","kim and will missionary 2","william kim missionary cum","william kim missionary 6","william kim missionary 7","william kim missionary 8","william kim missionary 9","william kim missionary 10"]))
    gallery_items.append(GalleryItem("Will and Kim after party doggy", ["william kim doggy 1", "william kim doggy 2", "kim and will doggy 1"]))
    gallery_items.append(GalleryItem("Will and kim after party blowjob", ["william kim bj 1","william kim bj 2","kim and will bed bj 1"]))
    gallery_items.append(GalleryItem("Will and Kim after party mating press", ["william kim mating press 1","william kim mating press 2","kim and will mating press 1", "william muscle","kim and will mating press 2", "william kim mating press 3"]))
    gallery_items.append(GalleryItem("Will and kim after sex", ["william kim aftersex", "william kim kiss 2"]))
    gallery_items.append(GalleryItem("William Kim shower sex", ["william kim shower sex 1", "william kim shower sex 2","kim and will shower 1","william kim shower sex 1","william kim shower sex 3"]))
    gallery_items.append(GalleryItem("Jamie cleaning service", ["william kim room","william kim shower sex peek 1"]))
    gallery_items.append(GalleryItem("Will and Diane boobjob", ["diane boobjob 1","diane boobjob 2","diane boobjob 3","diane and will boobjob 1","diane and will boobjob 2","diane boobjob 2","diane and will boobjob 2","diane boobjob 2","diane and will boobjob 2","diane boobjob 4","diane boobjob 5"]))
    gallery_items.append(GalleryItem("Diane reverse cowgirl", ["diane reverse cowgirl 1","diane reverse cowgirl 2","diane reverse cowgirl 3","diane and will reverse cowgirl 1","diane and will reverse cowgirl 2","diane reverse cowgirl 6","diane and will reverse cowgirl 2","diane reverse cowgirl 7","diane reverse cowgirl 8","diane reverse cowgirl 9"]))
    gallery_items.append(GalleryItem("Kim and Jamie makeup sex", ["kim and jamie makeup sex 0","kim and jamie makeup sex 1","kim and jamie makeup sex 2","kim jamie makeup sex 1","kim jamie makeup sex 2", "kim and jamie makeup sex 2"]))
    # gallery_items.append(GalleryItem("", []))
    # gallery_items.append(GalleryItem("", []))
    # gallery_items.append(GalleryItem("", []))
    # gallery_items.append(GalleryItem("", []))
    # gallery_items.append(GalleryItem("", []))
    # gallery_items.append(GalleryItem("", []))
    # gallery_items.append(GalleryItem("", []))
    # gallery_items.append(GalleryItem("", []))
    # gallery_items.append(GalleryItem("", []))
    # gallery_items.append(GalleryItem("", []))
    # gallery_items.append(GalleryItem("", []))
    # gallery_items.append(GalleryItem("", []))
    # gallery_items.append(GalleryItem("", []))
    # gallery_items.append(GalleryItem("", []))
    # gallery_items.append(GalleryItem("", []))
    # gallery_items.append(GalleryItem("", []))
    # gallery_items.append(GalleryItem("", []))
    # gallery_items.append(GalleryItem("", []))
    # gallery_items.append(GalleryItem("", []))


#gallery background
image gray = "#777"

#gallery images
image img1 = ("images/gallery/gallery1.jpg")
image img2 = ("images/gallery/gallery2.jpg")
