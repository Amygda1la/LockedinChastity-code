#a very simple gallery
init python:


    class GalleryItem:
        def __init__(self, name, images, image_number = None):
            self.name = name
            self.images = images
            # changed. Added this field to the GalleryItem object because it is being used
            # in the gallery_thumbnail_info screen.
            # Every CG in the gallery now has a unique number.
            # The number is basically the i+1 iterator in the for loop
            # that creates the layout for the gallery menu.
            self.image_number = image_number
        # changed. The refresh_lock() function has been changed, so now the gallery
        # will unlock a scene if the player has seen the first image of that scene.
        #
        # This can cause errors if the first images of two scenes are the same.
        # However, if you make a copy of the same image and give it a different name,
        # the problem will be fixed.
        def refresh_lock(self):
            lockme = True
            #changed. Added a check for manually unlocked gallery scenes
            # if this scene was manually unlocked by the player, it will remain unlocked.
            if self.image_number in persistent.unlocked_gallery_items:
             lockme = False
            elif renpy.seen_image(self.images[0]):
             persistent.unlocked_gallery_items.add(self.image_number)
             lockme = False
            self.is_locked = lockme
        @property
        def thumbnail_image(self):
         thumbnail = "images/gallery thumbnails/" + self.images[0] + ".png"
         if renpy.loadable(thumbnail):
          return thumbnail
         return self.images[0]
    #changed just added all cgs from the first and second scripts to the massive in order they are shown in the game, including the animation
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
    gallery_items.append(GalleryItem("Diane sleeps with Will", ["diane blanket"]))
    gallery_items.append(GalleryItem("Diane Will missionary", ["diane will missionary 0","diane will missionary 1","diane will missionary 2","diane and will missionary 1","diane and will missionary 2","diane will missionary 4","diane will missionary 5",]))
    gallery_items.append(GalleryItem("Kim and Will mating press dream", ["william kim mating press dream 1","kim and will mating press dream 1"]))
    gallery_items.append(GalleryItem("morning Kim", ["morning kim 3","morning kim 4","morning kim 5","morning kim 1","morning kim 2"]))
    gallery_items.append(GalleryItem("Kim with ice cream", ["ice cream 1", "ice cream 2"]))
    gallery_items.append(GalleryItem("Kim and Jamie handjob", ["kim jamie handjob 1", "kim and jamie edging 1", "kim and jamie edging 2", "kim jamie handjob 3"]))
    gallery_items.append(GalleryItem("Jamie bench", ["jamie bench 1","jamie bench 2","jamie bench 3", "jamie bench 2", "jamie bench 3","jamie bench 5","jamie bench 4","jamie bench 6",]))
    gallery_items.append(GalleryItem("Kim squat", ["kim squat 1","kim squat 2","kim squat 3","kim squat 2","kim squat 3","kim squat 2","kim squat 3","kim squat 2"]))
    gallery_items.append(GalleryItem("Will and Diane date 2", ["diane mirror selfie"]))
    gallery_items.append(GalleryItem("Diane and Will handjob", ["diane hj1","diane and will handjob 4","diane and will handjob 5","diane hj4","diane hj5"]))
    gallery_items.append(GalleryItem("Diane and Will mating press", ["diane mating press 1","diane mating press 3","diane mating press 2a","diane mating press 2","diane mating press 2a","diane mating press 3","diane and will mating press 1","diane and will mating press 2","diane mating press 3b","diane mating press 3a","diane mating press 4","diane mating press 5","diane mating press 6"]))
    gallery_items.append(GalleryItem("Will and Diane date 2 (Jamie's pov)", ["diane mirror selfie 2", "diane and will handjob alt 1","diane and will handjob alt 2","diane hj9","diane hj10","diane mating press 7","diane mating press 9","diane mating press 8","diane mating press 9","diane and will mating press alt 1","diane and will mating press alt 2","diane mating press 9","diane mating press 8","diane mating press 10","diane mating press 11","diane mating press 12"]))
    gallery_items.append(GalleryItem("Yelena kabedon", ["yelena kabedon 1","yelena kabedon 2"]))
    gallery_items.append(GalleryItem("Kim cow", ["kim cow 1", "kim cow 2","kim cowkini send"]))
    gallery_items.append(GalleryItem("Diane in crowd", ["diane sweat"]))
    gallery_items.append(GalleryItem("Will and Jamie in park", ["will and jamie park"]))
    gallery_items.append(GalleryItem("Kim kabedon", ["kim kabedon 2","kim kabedon 1","kim kabedon 3","kim kabedon 1","kim kabedon 2"]))
    gallery_items.append(GalleryItem("Kim and Jamie degrade", ["kim jamie degrade 1", "kim and diane demean 1","kim jamie degrade 3"]))
    gallery_items.append(GalleryItem("Diane cock kiss", ["diane cock kiss 1","diane cock kiss 2","diane cock kiss 1","diane cock kiss 2"]))
    gallery_items.append(GalleryItem("Diane and Will reverse", ["diane anal spread 1", "diane and will reverse 1", "diane and will reverse 2","diane and will reverse 3","diane anal spread 9","diane anal spread 10"]))
    gallery_items.append(GalleryItem("Kim is getting harassed", ["kim harass"]))
    gallery_items.append(GalleryItem("Maid Jamie", ["maid jamie"]))
    gallery_items.append(GalleryItem("Diane and Will tent", ["diane will tent 1","diane will tent 2","dianewill tent 1","dianewill tent 2","diane will tent 5","diane will tent 6"]))
    gallery_items.append(GalleryItem("Scared Kim and Will", ["scared woods"]))
    gallery_items.append(GalleryItem("Massage", ["massage","diane massage", "kim massage", "massage"]))
    gallery_items.append(GalleryItem("Nice view", ["nice view"]))
    gallery_items.append(GalleryItem("Potential", ["potential"]))
    gallery_items.append(GalleryItem("Diane forest doggy", ["diane forest seggs 1","diane forest doggy 1","diane forest doggy 2","diane forest seggs 4","diane forest seggs 5"]))
    gallery_items.append(GalleryItem("Couple peek", ["couple peek"]))
    gallery_items.append(GalleryItem("Scared cave", ["scared cave"]))
    gallery_items.append(GalleryItem("Kim and Will fishing", ["kim and will fishing"]))
    gallery_items.append(GalleryItem("Kim and Will cabin (Jamie's pov)", ["shadow doggy", "shadow mating press"]))
    gallery_items.append(GalleryItem("Kim cabin sleep", ["kim cabin sleep 1","kim cabin sleep 2","kim cabin sleep 3"]))
    gallery_items.append(GalleryItem("Kim is getting eaten", ["kim eating out 1","kim eating out 2"]))
    gallery_items.append(GalleryItem("Cabin missionary", ["cabin missionary 1","cabin missionary 2","cabin missionary 4","cabin missionary 3","kim and will cabin missionary 1","kim and will cabin missionary 2","cabin missionary 3"]))
    gallery_items.append(GalleryItem("Cabin doggy", ["cabin doggy 2","kim and will cabin doggy 1","cabin doggy 4","kim and will cabin doggy 2", "cabin doggy 4","cabin doggy 5","cabin doggy 6"]))
    gallery_items.append(GalleryItem("Cabin art", ["cabin art", "cabin art night", "cabin art fire"]))
    gallery_items.append(GalleryItem("Cabin timelapse", ["d2 1","d2 2","d3 1", "d3 2", "d3 3","cabin bath 1","d3 4", "d4 1", "d4 2", "d4 bj", "d4 3", "d5 1", "d5 2", "d5 9", "d5 3", "d5 4","d5 5","d5 6","d5 7","d5 8"]))
    gallery_items.append(GalleryItem("Kim cabin cowgirl", ["kim cabin cowgirl 1","kim cabin cowgirl 2","kim cabin yeehaw 1","kim cabin cowgirl 3","kim cabin yeehaw 3","kim cabin cowgirl 5"]))
    gallery_items.append(GalleryItem("Car seggs", ["car seggs 1","car seggs 2","car seggs 3"]))
    gallery_items.append(GalleryItem("Kim bathroom blowjob", ["kim bathroom bj1","kim toilet bj 2","kim bathroom bj3","kim bathroom bj4","kim toilet bj 2","kim toilet bj 3","kim bathroom bj7","kim bathroom bj4", "kim toilet bj 2","kim bathroom bj5","kim toilet bj 3","kim bathroom bj8","kim bathroom bj6"]))
    gallery_items.append(GalleryItem("Kim storage seggs", ["kim storage sex 1","kim storage seggs 4","kim storage seggs 1","kim storage seggs 3","kim storage seggs 1","kim storage seggs 2", "kim storage sex 11"]))
    gallery_items.append(GalleryItem("Yelena and Jamie balcony", ["yelena kiss 1", "yelena kiss 2", "yelena kiss 3"]))
    gallery_items.append(GalleryItem("Kim love hotel", ["kim love ho 1","kim love ho 2","kim love ho 3","kim love hotel missionary 1","kim love ho 7","kim love hotel missionary 2","kim love ho 7"]))
    gallery_items.append(GalleryItem("Diane first blowjob", ["diane first bj1","diane first bj2","diane first bj3","diane first bj2","diane fbj 1", "diane fbj 2","diane first bj4","diane first bj5"]))
    gallery_items.append(GalleryItem("Diane and Will backshots", ["diane will lingerie ride 3","diane will lingerie ride 4","diane and will backshots 1","diane and will backshots 1","diane lingerie peek"]))
    gallery_items.append(GalleryItem("Jamie fingering", ["jamie finger 4","jamie finger 2","jamie finger 1","jamie finger 6","jamie fingering 1","jamie finger 7","jamie finger 8"]))
    gallery_items.append(GalleryItem("Will and Diane kiss", ["will diane kiss 2", "will diane kiss 1"]))
    gallery_items.append(GalleryItem("Diane afterparty", ["diane afterparty 2","diane afterparty 1","diane will balloons 1","diane will balloons 2","diane afterparty 3"]))
    gallery_items.append(GalleryItem("gelatomoosoomay", ["gelatomoosoomay"]))
    gallery_items.append(GalleryItem("Jamie wears dildo", ["kim jamie dildo 1","kim jamie dildo 2","kim jamie dildo 3","jamie dildo 1","jamie dildo 2","kim jamie dildo 4"]))
    gallery_items.append(GalleryItem("Kim and Jamie makeup sex (ntr route)", ["kim and jamie makeup sex 0", "kim and jamie makeup sex 2"]))
    gallery_items.append(GalleryItem("Jamie suck's dildo", ["jamie succ 1","jamie succ 2","jamie succ 4","jamie succ 5","jamie sucking 1", "jamie sucking 2","jamie succ 3"]))
    gallery_items.append(GalleryItem("Yelena bear costume", ["yelena costume"]))
    gallery_items.append(GalleryItem("Kim and Will christmas fuck", ["kim will christmas 1","kim will christmasfuck 1","kim will christmasfuck 2","kim will christmas 3", "william kim kiss 2"]))
    gallery_items.append(GalleryItem("Will and Diane christmas seggs", ["diane christmas sex 1","wd christmas 1","wd christmas 2","wd christmas 3", "diane christmas sex 7"]))
    gallery_items.append(GalleryItem("Kim and Jamie skating", ["kim skates smile"]))
    gallery_items.append(GalleryItem("Kim and jamie at the restaraunt", ["kim dinner grin"]))
    gallery_items.append(GalleryItem("Yelena and Jamie at the restaraunt", ["yelena dinner smile","yelena dinner grin","yelena dinner neutral"]))
    gallery_items.append(GalleryItem("Yelena skates with Jamie", ["yelena skates smile"]))
    gallery_items.append(GalleryItem("Diane dinner with Will", ["diane dinner smile","diane dinner grin","diane dinner shy"]))
    gallery_items.append(GalleryItem("Diane dog suck", ["diane dog bj 2","diane dog suck 1","diane dog suck 2","diane dog bj 4","diane dog bj 3","diane dog bj 2","diane dog bj 5"]))
    gallery_items.append(GalleryItem("Diane degrade", ["diane degrade 1","diane degrade 2","diane degrade 3","diane reverse doggy 1","diane reverse doggy 2","diane reverse doggy 3","diane degrade 10"]))
    gallery_items.append(GalleryItem("Jamie cheer", ["jamie cheer shy"]))
    gallery_items.append(GalleryItem("Jamie pegging", ["jamie pegging 1","jamie pegging 2","jamie pegging 3", "jamie first peg 1","jamie first peg 2", "jamie pegging 4"]))
    gallery_items.append(GalleryItem("Kim cow blowjob", ["kim cow bj 1","kim cow bj 2","kim cow bj 3","kim cow bj 4","kim raw bj 1","kim raw bj 2","kim cow bj 5","kim cow bj 6"]))
    gallery_items.append(GalleryItem("Kim cow carried", ["kim cow sex 1","kimcow carry 1","kimcow carry 2","kimcow 1","kimcow 2","kim cow mate 3","kim cow mate 4"]))
    gallery_items.append(GalleryItem("Threesome cosplay", ["threesome cosplay"]))
    gallery_items.append(GalleryItem("Jamie jerk's of to cosplay NTS", ["nts jamie 1","jamie nts pov 1","nts jamie 3"]))
    gallery_items.append(GalleryItem("Jamie jerk's of to cosplay SISSY", ["threesome cosplay","jamie nts pov 1", "sissy jamie 1", "sissy jamie 2", "jamie sissy pov 1", "sissy jamie 2"]))
    gallery_items.append(GalleryItem("Diane finds out", ["diane peek","will diane smooch 1","will diane smooch 2", "diane stare 1", "diane disc 5", "diane disc 4", "diane kim threesome 1", "diane disc 4", "diane disc 1", "diane kim threesome 2", "diane disc 6"]))
    gallery_items.append(GalleryItem("Jamie cowgirl", ["jamie cowgirl 1","jamie cowgirl 2","jamie yeehaw 1","jamie yeehaw 2","jamie cowgirl 3"]))
    gallery_items.append(GalleryItem("Kim and Diane bikinis", ["kimdiane fit"]))
    gallery_items.append(GalleryItem("Dinner (Jamie's pov)", ["kim diane kiss", "drunk jamie 1", "morning kim hicky 1","morning kim hicky 2"]))
    gallery_items.append(GalleryItem("Dinner blowjob NTR", ["kim diane bj 1", "diane kim blowjob 1", "kim diane bj 4","kim diane bj 5","kim diane bj 6","diane kim blowjob 2", "kim diane bj 8"]))
    gallery_items.append(GalleryItem("Dinner missionary NTR", ["kim diane t1", "diane kim missionary 1","diane kim missionary 2","diane kim missionary 3", "kim diane t7", "kim diane t8", "kim diane t9", "diane kim missionary 4", "diane kim missionary 5", "kim diane t13", "kim diane t14"]))
    gallery_items.append(GalleryItem("restaurant NTS (Jamie's pov)", ["nts restaurant","drunk jamie 2","drunk jamie 3","drunk jamie 4"]))
    gallery_items.append(GalleryItem("restaurant NTS (Kim's pov)", ["william kim kiss 2","william kim kiss 1","kim netorase 1", "kim nts cg 1", "kim netorase 2", "kim netorase 1", "kim nts cg 5", "kim nts cg 4", "kim nts cg 3", "kim netorase 3","kim netorase 4", "kim nts cg 6", "kim nts cg 7","kim nts cg 8", "kim nts cg 9"]))
    gallery_items.append(GalleryItem("Yelena in the fitting room", ["yelena fit"]))
    gallery_items.append(GalleryItem("Yelena in the bed", ["yelena bed"]))
    gallery_items.append(GalleryItem("Will lifts Jamie", ["jamie lift 2","jamie lift"]))
    gallery_items.append(GalleryItem("Kim quickie on the plane", ["kim quickie 1", "kim plane bj 1", "kim quickie 7","kim quickie 6","kim quickie 5","kim plane bj 2","kim quickie 8","kim quickie 5","kim quickie 9"]))
    gallery_items.append(GalleryItem("Diane and Will island night", ["diane afterparty 1","diane will balloons 1", "diane afterparty 1", "diane island peek 2", "diane blinds 1","diane blinds 2","diane island peek 8","diane island peek 1","diane blinds 4","diane island peek 12"]))
    gallery_items.append(GalleryItem("Diane and Will island night (Jamie's pov)", ["diane island peek 2","diane blinds 1","diane blinds 2","diane island peek 8","diane island peek 1"]))
    gallery_items.append(GalleryItem("Jamie applies lotion", ["yelena lotion 0","yelena lotion 1","yelena lotion 2",]))
    gallery_items.append(GalleryItem("Volleyball match", ["volleyball yk"]))
    gallery_items.append(GalleryItem("Kim bathroom sex", ["isle bathroom sex 1","kim orange 1", "isle bathroom sex 3","kim orange 2","kim orange 3","isle bathroom sex 2","kim orange 4","isle bathroom sex 9","isle bathroom sex 10"]))
    gallery_items.append(GalleryItem("Kim bathroom sex (Jamie's pov)", ["isle bathroom jamie 2","isle bathroom jamie 3","isle bathroom jamie 4","isle bathroom jamie 2","isle bathroom jamie 1"]))
    gallery_items.append(GalleryItem("Diane's first MMF", ["french sex 1","french sex 2","french pan 1","french pan 2","french g3","french sex 6",]))
    gallery_items.append(GalleryItem("Jamie skydive", ["skydive"]))
    gallery_items.append(GalleryItem("Kim island threesome", ["island stack","island stack 1","island stack 2","island stack 3", "island stack 4"," pussy stack 2","pussy stack 3", "island stack 8","island stack 9","island stack 0","island stack 10","island stack 15","pussy stack 4","pussy stack 5","island stack 16","island stack 17"]))
    gallery_items.append(GalleryItem("Divided NTS", ["divided 1","divided 2","divided 3","divided 4","divided 5"]))
    gallery_items.append(GalleryItem("Divided NTR", ["divided ntr 1","divided ntr 2","divided 3","divided 4","divided 5"]))
    gallery_items.append(GalleryItem("Divided NTS (Jamie's pov)", ["divided jamie 1","divided jamie 2","divided jamie 3","divided jamie 4","divided jamie 5", "morning kim hicky 1"]))
    gallery_items.append(GalleryItem("Divided NTR (Jamie's pov)", ["divided jamie ntr 1","divided jamie ntr 2","divided jamie ntr 3","divided jamie ntr 4","divided jamie 5"]))
    gallery_items.append(GalleryItem("Yelena sleeps with Jamie", ["yelena davui 3", "yelena davui 2"]))
    gallery_items.append(GalleryItem("Intimidation", ["intimidation"]))
    gallery_items.append(GalleryItem("Yana secret", ["yana secret 1", "yana secret 2"]))
    gallery_items.append(GalleryItem("Jamie in bikini", ["green jamie 1","green jamie 2","green jamie 3"]))
    gallery_items.append(GalleryItem("Party Alex invite NTS", ["trio party 1", "trio party 2"]))
    gallery_items.append(GalleryItem("Kim Alex threesome", ["alex sex 1","kim alex threesome 1","kim alex threesome 2","alex sex 7"]))
    gallery_items.append(GalleryItem("Alex kisses Kim", ["kimalex kiss"]))
    gallery_items.append(GalleryItem("Kim's First anal", ["couch sex 1","couch sex 2","couch sex 3","couch sex 4","kim couch 1","kim couch 2","kim couch 3", "couch sex 7","couch sex 8"]))
    gallery_items.append(GalleryItem("Jamie ponder", ["jamie ponder 2","jamie ponder 4", "jamie ponder 3","jamie ponder 2","jamie ponder 3","jamie ponder 1","jamie ponder 4"]))
    gallery_items.append(GalleryItem("Diane plane blowjob", ["diane plane bj 1","diane plane b1","diane plane b2","diane plane bj 8","diane plane bj 9",]))
    gallery_items.append(GalleryItem("Kim vs Yelena in plane", ["ky plane 1","ky plane 2","ky plane 3","ky plane 2","ky plane 4","ky plane 5","ky plane 6","ky plane 7","ky plane 8",]))
    gallery_items.append(GalleryItem("Diane misses Will", ["diane door mad", "diane and will roomdoor 6", "diane miss 2", "diane miss 3", "diane miss 4", "diane dong 1", "diane dong 2"]))
    gallery_items.append(GalleryItem("Diane comes to will's place", ["diane cook 1", "diane cook 2","diane cook 3","diane cook 4","diane cook 5","diane cook 4","counter sex 1","counter sex 2","diane counter 5"]))
    gallery_items.append(GalleryItem("Jamie locked in chastity", ["kim jamie mirror 1","cage finger 1","cage finger 2", "kim whisper 3"]))
    # gallery_items.append(GalleryItem("", []))
#gallery background
image gray = "#777"
