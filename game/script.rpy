define nissa = Character("Nissa", image = "nissa")
define chandra = Character("Chandra", image = "chandra")
define ulamog = Character("Ulamog", image = "ulamog")
define kozilek = Character("Kozilek", image = "kozilek")
define emrakul = Character("Emrakul", image = "emrakul")
define yargle = Character("Yargle", image = "yargle")

image affinity = "hornythopter.png"
image credits_image = "credits.png"
image eyeOfUgin = "eyeOfUgin.png"
image magicRD = "magicR&D.png"
image rainbow = "rainbow.png"
image rhinos = "rhinos.png"
image saffronOlive = "saffronOlive.png"
image squirrelMob = "squirrelMob.png"
image thoughtKnotSeer = "thoughtKnotSeer.png"

python:
    name_1 = "mc1"
    name_2 = "mc2"
    gender = "non-binary"

    # flags
    date_1 = ""
    date_2 = ""

    emrakul_date_1 = ""

init -1 python:
    def char_callback(event, **kwargs):
        showing_tags = renpy.get_showing_tags()
        current_tag = renpy.get_say_image_tag()
        character_tags = [
            t for t in
            ['nissa', 'chandra', 'ulamog', 'kozilek', 'emrakul', 'yargle',
            'eyeOfUgin', 'thoughtKnotSeer', 'affinity', 'rhinos',
            'saffronOlive', 'magicRD']
            if t in showing_tags
            and t != current_tag ]
        if current_tag and event == "begin":
            for tag in character_tags:
                renpy.show( tag, zorder = 0 )
            if renpy.showing(current_tag):
                renpy.show( current_tag, zorder = 100 )
        return (), kwargs
    config.all_character_callbacks.append( char_callback )

    far_left = Position(xalign = -0.3)
    far_right = Position(xalign = 1.2)

label main_menu:
    with None
    $ renpy.transition(dissolve)
    play music "audio/menu.ogg" fadein 4.0
    jump main_menu_screen

label start:

    stop music fadeout 4.0

    python:
        name_1 = renpy.input("first name:")
        name_2 = renpy.input("last name:")
        if not name_1:
            name_1 = "Foo"
        if not name_2:
            name_2 = "Bar"
        name_1 = name_1.strip()
        name_2 = name_2.strip()

        mc = Character(name_1)

    menu:

        "gender \nnote: this won't affect any romance options, only
        what honorifics characters use"

        "male":
            $ gender = "male"
        "female":
            $ gender = "female"
        "lovecraftian eldritch abomination":
            $ gender = "non-binary"
        "nb/gnc":
            $ gender = "non-binary"

    jump day1_scene1

    return

label day1_scene1:

    stop music fadeout 2.0
    play music home_intro noloop fadein 1.0
    queue music home

    scene bg bedroom with dissolve

    "Wednesday."

    "Wednesdays are the worst."

    "Yes, even worse than Mondays."

    "Because Wednesdays reside right in the middle of the week."

    "The day when all your energy from the weekend has been depleted."

    "And unlike Thursdays when you can tell yourself \"There's only one day
    left to go\"."

    "Wednesdays are only halfway through the week. Which means there's still a
    whole other half of a week left to endure."

    mc "*sigh*"

    "You woke up early today."

    "Not by choice you grumble to yourself."

    "The birds outside have reached the concerted decision that today is the
    perfect day to screech louder than a harpy clawing its way up from the
    ninth circle of hell."

    "And at 6:00 in the morning no less."

    "A rather unfortunate situation, you think to yourself."

    "And although this would be a problem on any day of the week, today is a
    Wednesday."

    "And as has been established: Wednesdays suck."

    "Well, since you're up this early you might as well try getting some
    homework done."

    mc "Hehe.."

    "That was a funny joke."

    "Well, okay. It wasn't that funny."

    "You mostly laughed to be facetious, hiding your problems under a thin
    veneer of light-hearted charm."

    "To avoid the mountain of stress that would come crashing down were you
    to actually acknowledge your problems as being legitimate sources of
    stress in your life."

    "It's not a very effective coping mechanism considering you've already
    started trying to meta-cognitively justify why you can't avoid problems
    in this manner."

    "Whatever, the point is you're not doing any homework this morning."

    "You've already exhausted all you mental energy explaining to yourself
    why you're not doing homework. Leaving no energy remaining to actually
    do said homework."

    "Oh well. After a feat of mental gymnastics that would leave an olympic
    judge with their jaw on the floor, it's almost already 6:30."

    "You suppose it's time to start getting ready for school."

    "You grab your backpack off the floor and and stuff a +1/+1 counter in your
    mouth, which will need to suffice as your breakfast for the day."

    "You grab your keys and stare at the front door, preparing to mentally
    disassociate yourself from reality for the next eight or so hours."

    play music walking fadeout 2.0 fadein 1.0

    scene bg street with dissolve

    show nissa wave at left with dissolve

    if gender == "male":
        nissa "[name_1]-kun!!"
    elif gender == "female":
        nissa "[name_1]-chan!!"
    else:
        nissa "[name_1]-san!!"

    nissa neutral @ smile "You're early today! Eheheh."

    "Oh... Right. You almost forgot."

    "Well, actually..{w} You did forget.{w} But you'd feel bad admitting that,
    so to keep your fragile moral conscious intact you'll leave it at
    'almost forgot'."

    "That's Nissa. She's your neighbor and childhood friend."

    "You've known each other basically since you were born due to the
    inherently entropic nature of early developmental friendships predicated
    almost entirely on geography and familial connections."

    "It's hard to imagine you becoming friends in any other situation.{w}
    Y'know, the kind of person you seem to associate with purely out of
    circumstance."

    "Not that you're complaining, she's super nice and always finds ways to
    make your life..."

    "Well...{w} Interesting, to say the least."

    "Normally she's the one to wake you up. But as both of you noticed, that
    didn't happen today."

    show nissa excited:
        linear 1.0 offscreenright

    "Without waiting for your response, Nissa grabs your arm and starts
    dragging you down the steps of your porch."

    "She never did harbor any patience for your internal monologues."

    nissa "C'mon! Let's go~"

    "It's only 6:45, at this rate you'll arrive at school way too early."

    scene bg park with dissolve

    show nissa neutral at right with easeinright

    "Nissa's hand begins to swing your arm back and forth as you slow to a
    normal pace."

    "She begins to talk at you, but you're not really paying attention."

    "You free your arm from her {b}binding grasp{/b} and return your hands to
    your pockets."

    "The trees are in {b}lush growth{/b} and the flowers in {b}vernal bloom{/b}
    despite it being late October."

    "And yet it still feels cold and dreary as the {b}autumnal gloom{/b} lurks
    beneath the {b}veil of summer{/b}."

    "Nissa's going on about the Mul Daya and being generally low-key kinda
    racist."

    "But her words pass through your mind as the {b}creeping chill{/b} of
    the upcoming day of school fills you with {b}dread{/b}."

    scene bg schoolgrounds
    show nissa neutral at right
    with dissolve

    "You arrive at school with nearly half and hour to spare."

    hide nissa with moveoutleft

    "Nissa leaves to get to her class, as you should probably be doing too."

    jump day1_scene2

    return

label day1_scene2:

    play music school fadeout 2.0 fadein 1.0

    scene bg classroom backleft with dissolve

    "The abysmal mundanity of school makes its cycle, taking with it eight
    more hours of your fleeting existence."

    "The day seems to have passed by in {b}slow motion{/b}."

    "At the very least you were able to {b}recover{/b} some of your lost
    {b}sleep{/b}."

    "You feel marginally {b}revitalize{/b}d.{w} Well, as much as one can after
    falling unconscious against a $5 IKEA chair with the spinal posture of a
    scoliotic shrimp performing pilates."

    "By the time you acknowledge your situation, the classroom is already
    empty."

    "You curse your internal monologue for keeping you longer than absolutely
    necessary and make your way to the classroom door."

    show nissa wave at center with dissolve

    if gender == "male":
        nissa "[name_1]-kun!!"
    elif gender == "female":
        nissa "[name_1]-chan!!"
    else:
        nissa "[name_1]-san!!"

    nissa neutral "You're late, eheheh. I caught you this time."

    mc "How did you know I'd stay late?"

    nissa smile "I didn't. I do this every day, but this time you're the last
    one here.{w} I guess today's my luck day~"

    "Gee. She does this every day?{w} And you never knew. Now you feel like the
    asshole."

    nissa neutral @ excited "C'mon! C'mon! Let's go."

    "Nissa pulls at your arm with a playful smile on her face."

    mc "Go where?"

    nissa @ smile "We're planning our class' event for the school
    {b}festival{/b}."

    "That's right.. Nissa's the class president this year."

    "Also the school {b}festival{/b} is coming up...{w} Apparently."

    "You probably slept through that part."

    "You were never really one to partake in school events."

    "You vaguely {b}recall{/b} Nissa's {b}relentless assault{/b} of invitations
    to previous school {b}festival{/b}s and events."

    "Well, actually. You remember them quite {b}clear{/b}ly. You've just
    selectively ignored those {b}agonizing memories{/b} to avoid the
    {b}burden of guilt{/b} you'd feel for systematically declining them."

    "And look where that's gotten you. Staring down the exact thing you've
    been trying to avoid while actively feeling guilty about trying to avoid
    it."

    if gender == "male":
        nissa distracted "[name_1]-kun?"
    elif gender == "female":
        nissa distracted "[name_1]-chan?"
    else:
        nissa distracted "[name_1]-san?"

    "{b}Damn{/b}. You really need to keep your internal monologues in check."

    "Well, you're already feeling guilty for avoiding her invitations. So it
    looks like there's no way out of this one."

    mc "Sure, sounds good."

    "You give the most half-assed response despite your heart's best
    intentions."

    nissa smile @ excited "Yay!! C'mon c'mon!"

    "But Nissa's jubilant reaction shows no sign of disappointment."

    "You don't deserve her."

    scene bg hall
    show nissa neutral at center
    with dissolve

    "Nissa drags you out into the hallway."

    mc "So where exactly are we going?"

    nissa @ smile "The library!"

    "The library? Only nerds and blue players hang out at the library."

    "Although that's a bit redundant considering the venn diagram between
    nerds and blue players is literally just a circle."

    "You {b}opt{/b} not to say that out loud however."

    jump day1_scene3

    return

label day1_scene3:

    play music library fadeout 2.0 fadein 1.0

    scene bg library 3 with dissolve

    "You arrive at the library behind Nissa."

    "You can't believe you're wasting your valuable free time at school."

    "Free time,{w} whose entire definition mind you,{w} is predicated on not
    being at school."

    "And yet, here you are.{w} At school."

    "And in the library no less."

    show nissa wave at right with dissolve

    if gender == "male":
        nissa "Over here [name_1]-kun!"
    elif gender == "female":
        nissa "Over here [name_1]-chan!"
    else:
        nissa "Over here [name_1]-san!"

    scene bg library 2
    show nissa wave at right
    with dissolve

    "Nissa waves you over to a corner of the library."

    show nissa neutral with Dissolve(0.25)

    "There are a few others sitting around a table, presumably other class
    presidents."

    "What are you doing here again?"

    show nissa:
        linear 0.6 xalign -0.3

    nissa smile "Hi hi everyone! Sorry I'm late."

    nissa neutral "This is my friend [name_2]-san."

    mc "Uh.. Hi guys."

    show ulamog neutral at Position(xalign = 0.15) with dissolve

    if gender == "male":
        ulamog "Hi [name_2]-kun!!"
    elif gender == "female":
        ulamog "Hi [name_2]-chan!!"
    else:
        ulamog "Hi [name_2]-san!!"

    ulamog @ hands "I'm Ulamog! Nice to meet you."

    "The tall figure greets you with a smile. Its legs are made of tentacles
    and its arms split at the elbows to form two sets of forearms. Thick
    grey {b}carapace{/b} potrudes from exposed muscle and sinew creating
    bone-like patterns along the reddish surface."

    show kozilek cross at Position(xalign = 0.8) with dissolve

    kozilek "...{w} Hey.."

    show ulamog hands:
        xalign 0.15
        linear 0.2 xalign 0.6

    ulamog "Kozi-kun! You have to be nicer than that."

    kozilek "..."

    kozilek neutral "Hi.. I'm Kozilek."

    ulamog "Mmmmm hehehe~"

    hide ulamog
    hide kozilek
    with moveoutright

    "The other Eldrazi, apparently named Kozilek, is more reluctant to greet
    you but does so nonetheless."

    show emrakul wave at center with dissolve

    emrakul "Emrakul.. Fufufu."

    show emrakul neutral with Dissolve(0.25)

    show chandra neutral flip at far_right with dissolve

    chandra "Yo."

    chandra "Chandra Nalaar."

    hide nissa
    hide emrakul
    hide chandra
    with dissolve

    "The remainder of the, presumably, class presidents greet you as you
    take a seat."

    "You feel an {b}uncomfortable chill{/b} as the realization sets in."

    "You are sitting in a room with three--"

    show ulamog neutral at far_left with dissolve

    "Hot."

    show kozilek neutral at Position(xalign = 0.2) with dissolve

    "Sexy."

    show emrakul neutral at right with dissolve

    "Romantically avaliable."

    "Lovecraftian Gothic Horror Eldritch Tentacle {b}Abomination{/b}s."

    "Oh, and there's like a hot red head chick too.. But, like,{w} yea..
    Eldrazi."

    "It's a precarious situation to be in. Will you be able to win the hearts
    of one of these Eldrazi?"

    "It's often cited that the perils of high school romance are much akin to
    piloting Ladies Looking Left tribal at cEDH night."

    "Well, actually.. No, nobody says that.{w} But it certainly seems that
    way."

    "Maybe if you play your cards correctly (pun most definitely intended)
    you'll reach {b}semester's end{/b} one Eldrazi happier than you started."

    hide ulamog
    hide kozilek
    hide emrakul
    with dissolve

    "Nissa begins the meeting, discussing various plans for the upcoming school
    {b}festival{/b}. Her words pass through your mind and {b}leave no
    trace{/b}."

    "You become {b}lost in thought{/b} as your mind wanders off."

    "It's a Herculean task not fantasizing about the three Eldrazi sitting in
    front of you."

    "But this isn't Theros, and your {b}iron will{/b} eventually
    {b}crumble{/b}s as you {b}succumb to temptation{/b}."

    "Maybe you shouldn't've read all those tentacle doujinshi. You're starting
    to recognize them {b}exert influence{/b} over the direction of your
    fantasies."

    "But your erotic daydreaming is cut short by a sudden {b}burning
    inquiry{/b}:{w} Why tentacles of all things?"

    "It's seems quite arbitrary to have gained such footing in popular media."

    "And to only add to your frustration, it's not exactly helping to have
    three very sexually arousing tentacle monsters sitting across the table."

    show emrakul neutral at center with dissolve

    emrakul "Actually tentacles became so ubiquitous in Japanese pornography
    as a way to circumvent {b}censorship{/b} laws at the time."

    "Wait."

    emrakul "During the allied forces occupation of Japan during World War II
    they believed Japan's sexual culture to be the cause of their belligerent
    and aggressive behavior."

    "Huh?"

    emrakul "They thusly implemented a ban on most forms of porn, the strictest
    of which being on male genitalia."

    emrakul @ blush "In response, one animator in particular started using
    tentacles instead for their phallic nature and ability to show angles that
    would normally be obstructed by a human body."

    "What is going on?"

    emrakul "They argued that this did not violate the {b}censorship{/b} laws
    at the time due to it being mostly suggestive in nature."

    emrakul "This form of {b}censorship{/b} evasion became wildly popular. And
    as a result, much of modern hentai still depicts tentacles despite the
    relevant {b}censorship{/b} laws having been {b}repeal{/b}ed years ago."

    "Did you say all that out loud?"

    "You thought you had your monologing problem resolved."

    "You haven't needed to see a therapist in years. Is this a relapse?"

    "No, it couldn't be. You're confident you didn't say all that embarrassing
    tentacle stuff out loud."

    "Then what could have prompted Emrakul's sudden regurgitation of obscure
    hentai knowledge?"

    show nissa uncomfortable at Position(xalign = -0.2) with dissolve

    nissa "Umm..."

    nissa "Emrakul-chan?"

    emrakul scared "Umm... Oh, sorry."

    emrakul neutral "I just thought-- Because [name_2]-san.."

    emrakul scared "Nevermind.. I'm sorry."

    show chandra mischief at far_right with dissolve

    chandra "No, wait. Please, tell me more."

    nissa distracted @ point "Oh, no. It's okay, um..{w} Let's just try to
    focus, okay?"

    "What just happened? You can't seem to wrap your head around it."

    "Possibly because your mind's only fixation for the past half-hour has been
    on the idea of being tied up and groped as Emrakul's slimy appendages
    invade your every orifice in an erotic {b}crush of tentacles{/b}."

    "But also maybe because...{w} Well no, that was probably the reason."

    hide nissa
    hide emrakul
    hide chandra
    with dissolve

    "You emerge from your mind's enclosure of fantasy in an effort to
    pay attention to the conversation happening around you."

    "Or whatever {b}shambling remains{/b} of a conversation there is, as
    any semblence of rational thought appears to have been catastrophically
    derailed hours ago."

    show ulamog hands at left
    show kozilek cross at right
    with dissolve

    ulamog "Nico nico ni!"

    kozilek "..."

    ulamog "Nico nico ni!"

    kozilek "..."

    ulamog "Nico nico--{nw}"

    kozilek cross @ angry "Ulamog! Shut the FUCK up before I NICO NICO break
    your KNEECAPS!!"

    ulamog neutral "..."

    show ulamog hands:
        left
        linear 0.2 center

    ulamog "WAAAAAAAHH!! Kozi-kun, you're so mean!"

    "Despite their previous exclamation, Ulamog takes Kozilek in their arms
    and squeezes them while still wailing."

    kozilek "..."

    kozilek @ neutral "Okay okay.. Sorry."

    ulamog "Awwwww. It's okay Kozi-kun."

    "Maybe it's time you go back to daydreaming."

    show kozilek:
        right
        linear 0.5 xalign 1.2

    "Kozilek frees himself from Ulamog's grip and ever so slightly scoots his
    chair way. Not enough to be outside Ulamog's melee range, but enough to
    signal Kozilek's discomfort."

    "\"Like swinging with a {b}Birds of Paradise{/b}\" you think to yourself.
    It's not about the damage, it's about sending a message."

    show ulamog:
        center
        linear 0.2 xalign 0.7

    "But that message is obviously not received as Ulamog simply latches back
    on to Kozilek."

    kozilek "Ugh. Don't you have homework to do or something?"

    ulamog sheepish "I was doing homework, but I drew all over it, now I can't read
    any of my work."

    "Both you and Kozilek look down, and sure enough Ulamog's notebook is
    covered in doodles of pies, chains, and hospitals."

    "An interesting assortment of drawings, but you don't question it."

    kozilek "Well that's your fault, so don't go asking me for help."

    ulamog neutral "Waaa!? Kozi-kun please, just one question."

    kozilek "Hmph, fine. But you have to stop hugging me."

    ulamog hands "Yay! Okay. What's the derivative of pi?"

    kozilek "Huh?"

    ulamog neutral "What's the derivative of pie?"

    kozilek neutral "But pi's just a constant."

    ulamog "Mmmm. Constantly delicious."

    kozilek cross "..."

    "Yep. Definitely time to go back to daydreaming."

    show nissa neutral at left with dissolve

    nissa "Okay! Umm.. Everyone. I think that wraps up today's meeting."

    nissa "Thank you for sharing your ideas, umm..{w} We'll meet up again
    tomorrow."

    "Nissa's closure isn't exactly the most elegant you've ever heard."

    "If you might so boldly proclaim, it likely wasn't the second most elegant
    either."

    "Now that you're thinking about it...{w} Yes, you're positive.{w} That was
    the least elegant closure you've ever heard."

    "But that wouldn't be a very kind sentiment to audibly express."

    "In fact, considering today's events, you probably shouldn't even be
    thinking it."

    hide ulamog
    hide kozilek
    with dissolve

    "Since Nissa's still in the room."

    "Only Nissa, actually, it seems everybody left during yet another one of
    your seemingly {b}time warp{/b}ing internal monologues."

    if gender == "male":
        nissa "C'mon [name_1]-kun."
    elif gender == "female":
        nissa "C'mon [name_1]-chan."
    else:
        nissa "C'mon [name_1]-san."

    mc "Hm?"

    nissa smile "Let's walk home together."

    mc "Oh, yeah. Sure."

    "The {b}crippling fatigue{/b} of the day washes over you and you're too
    tired to say no. Not that you could've said 'no' to Nissa even if you
    had the energy."

    "Regardless of the reason, you agree to Nissa's proposal and follow her
    out of the library."

    jump day1_scene4

    return

label day1_scene4:

    play music after_school_intro fadeout 2.0 fadein 1.0
    queue music after_school

    scene bg park
    show nissa neutral at left
    with dissolve

    "You and Nissa tread down the {b}homeward path{/b}."

    "While you walk to school every day, Nissa is very involved with
    extra curriculars and after school activites, so you seldom walk back
    from school with her."

    "Maybe it's the break from routine. Maybe it's the guilt for
    ignoring her entire meeting. But you find yourself actually paying
    attention to Nissa for once."

    if gender == "male":
        nissa "So, [name_1]-kun? How do you think the {b}festival{/b} will
        turn out this year?"
    elif gender == "female":
        nissa "So, [name_1]-chan? How do you think the {b}festival{/b} will
        turn out this year?"
    else:
        nissa "So, [name_1]-san? How do you think the {b}festival{/b} will
        turn out this year?"

    "Heck. It is entirely your own fault that you aren't able to genuinely
    engage with this question."

    "It was you and your infinite {b}hubris{/b} that lead you down the path of
    tentacle fantasies rather than responsible social awareness."

    "But an answer you must give, and you wouldn't want to disappoint Nissa
    any further than you surely already have."

    mc "Oh, great. Sounds like it'll be a blast."

    "Not the answer she deserves, but the best you can give."

    nissa @ smile "Oh yay! I'm glad you think so."

    nissa "Who's ideas did you like the most?"

    "Oh boy, okay. Considerably easier.{w} You are an expert when it comes to
    multiple choice."

    "You have a 25 percent success rate.{w} Which is a significant step up from
    your usual 4 percent on short answer questions."

    "But you're getting ahead of yourself. Right now you just need to pick an
    answer."

    menu:
        "Who's ideas did you like the most?"

        "Ulamog":
            mc "I thought Ulamog's ideas were pretty neat."

            nissa @ smile "Ooo! Yeah, Ulamog's a lot of fun."

            nissa "He's quite ambitious, but I think we can make it work."
        "Kozilek":
            mc "I really liked Kozilek's ideas."

            nissa distracted "Ahh. Heh, yeah. He's normally so shy, it's
            surprising to see him suggest something so out of his comfort
            zone."

            nissa smile "It might be difficult, maybe you can help him organize
            it all."

            mc "Um.. Yeah...{w} Maybe."
        "Emrakul":
            mc "I thought Emrakul's ideas were really good."

            nissa distracted "Oh, umm..{w} Yeah.{w} that's..."

            nissa uncomfortable "That's fine I guess.. I just mean, I don't
            really think a hentai curation booth would be very school
            appropriate."

            nissa point "But I mean. If both of you really wanted it,{w} maybe
            we could find a compromise..."

            mc "..."
        "Chandra":
            mc "I thought Chandra's ideas were the best."

            nissa smile "What? Silly, Chandra didn't propose anything. She's
            not even a class president."

            mc "Oh, umm.. Wait, why was she even there then?"

            nissa distracted "Uhh.. She kind of forced herself in."

            nissa point "Well.. I mean,{w} I didn't say no or anything but..."

    scene bg street
    show nissa neutral at left
    with dissolve

    nissa "Oh, well looks like this is our neighborhood."

    nissa wave "I'll see you tomorrow!"

    "You both say your goodbyes as you head toward your separate homes."

    jump day2_scene1

    return

label day2_scene1:

    play music home_intro fadeout 2.0 fadein 1.0
    queue music home

    scene bg bedroom with fade

    "Thursday."

    "Thursdays are fine you suppose."

    "Not a lot of people seem to appreciate Thursdays."

    "They're not great, mind you."

    "But you still maintain that Thursdays are criminally underrated."

    stop music fadeout 2.0

    scene bg street with dissolve

    show nissa wave at center with dissolve

    if gender == "male":
        nissa "C'mon [name_1]-kun, we're gonna be late."
    elif gender == "female":
        nissa "C'mon [name_1]-chan, we're gonna be late."
    else:
        nissa "C'mon [name_1]-san, we're gonna be late."

    mc "Yes yes, I'm coming."

    jump day2_scene2

    return

label day2_scene2:

    play music school fadeout 2.0 fadein 1.0

    scene bg classroom backleft with dissolve

    "You cast a {b}baleful stare{/b} on the clock at the front of the
    classroom."

    "Conveniently located just around eye level of the teacher such that upon
    a cursory glance you appear to be paying attention."

    "The clock ticks towards the final bell. But each tick seems to be longer
    than the last."

    "{b}Time stretch{/b}es out as the gap between you and freedom grows
    exponentially larger."

    "Like watching a storm player pop off, but not being able to concede
    because \"BuT tHeY cOUlD fiZzLe!!1!\"."

    "Like \"No Theo, you just flashbacked {b}past in flames{/b} after milling
    over half your deck with {b}traumatize{/b}. I'm not watching you play
    solitaire in the time it could take me to get a college level education
    in Zimbabwe\"."

    "..."

    "Umm..."

    "It seems the bell has already rung."

    "Students around you are packing up and preparing to leave."

    "You don't have anything to {b}put away{/b} considering you didn't take any
    notes or even remotely engage with the class on any level."

    "So you just take you bag and walk out the door."

    scene bg hall with dissolve

    "You are free."

    "The next sixteen hours are yours to command."

    "You could go to {b}study hall{/b}."

    "Play video games."

    "Join the {b}cult of the waxing moon{/b} and {b}devour flesh{/b} and
    {b}innocent blood{/b} as you {b}descend upon the sinful{/b}."

    "So many options, you buzz with excitement and the {b}thrill of
    possibilities{/b}."

    "As you exit the classroom, you {b}enter the infinite{/b}."

    "But before you can further contemplate your situation, a string of
    {b}nagging thoughts{/b} overtake your mind."

    "Nissa's planning committee is meeting again today. She'd surely be
    disappointed if you didn't come back."

    "You can think of a million reasons to not go to the library right now. And
    you can think of only one reason you should."

    "But the {b}crooked scales{/b} of 'The Big Horny' leave each side
    looking just as enticing as the other."

    jump day2_scene3

    return

label day2_scene3:

    play music library fadeout 2.0 fadein 1.0

    scene bg library 3 with dissolve

    "You end up walking through the library doors. Nissa and the rest are
    already seated at their usual table."

    scene bg library 2 with dissolve

    show nissa neutral at left with dissolve

    "You walk over a take a seat with them."

    if gender == "male":
        nissa distracted "Oh, [name_1]-kun, you actually came."
    elif gender == "female":
        nissa distracted "Oh, [name_1]-chan, you actually came."
    else:
        nissa distracted "Oh, [name_1]-san, you actually came."

    mc "Oh, was I not expected?"

    nissa smile "No! No, that's great. I'm happy you made it."

    nissa neutral "Umm.. I guess let's get started then."

    nissa "We can start working on the projects we came up with yesterday."

    nissa @ distracted "Umm... Yeah, so just start planning I think. If you
    need help umm, just ask I guess."

    "Nissa simply exudes confidence. A {b}radiant fountain{/b} of self-esteem
    for all to behold. She has nearly as much confidence as you have sarcasm,
    and that's saying something."

    show nissa:
        left
        linear 1.0 center

    if gender == "male":
        nissa "Oh, hey [name_1]-kun."
    elif gender == "female":
        nissa "Oh, hey [name_1]-chan."
    else:
        nissa "Oh, hey [name_1]-san."

    nissa distracted "I guess you wouldn't have much to do here huh."

    nissa smile "Sorry I dragged you into this, but I feel better when you're
    around so thanks for coming ehheh."

    nissa neutral "If you'd like, you can help any of the other presidents with
    their class activities. I'm sure they'd love your help, but I don't mean to
    pressure you any further."

    mc "No no, no worries. I'll stick around a while longer.{w}
    Thanks Nissa-chan."

    nissa smile "Okay! Cool."

    hide nissa with dissolve

    "Well, it can't be that bad. Now, who should you help organize?"

    menu:
        "Now, who should you help organize?"

        "Ulamog":
            jump day2_scene4_ulamog
        "Kozilek":
            jump day2_scene4_kozilek
        "Emrakul":
            jump day2_scene4_emrakul
        "Nissa":
            jump day2_scene4_nissa

label day2_scene4_ulamog:

    show ulamog neutral at center with dissolve

    mc "Hey Ulamog."

    if gender == "male":
        ulamog hands "Hi [name_2]-kun!!"
    elif gender == "female":
        ulamog hands "Hi [name_2]-chan!!"
    else:
        ulamog hands "Hi [name_2]-san!!"

    ulamog "Would you like to help with my class' activiy?"

    mc "I'd love to. What is it you're planning?"

    ulamog "Well, I was thinking we could host a cooking competition like you
    see on TV."

    mc "Oh my, that's quite ambitious of you."

    ulamog neutral @ sheepish "Oh? Do you think it's too much?"

    mc "No, no. It's just that, well.. The school {b}festival{/b}s have all
    been pretty.. Uuh.{w} Crappy."

    mc "So it's just surprising to see you doing something so elaborate."

    ulamog hands "Oh. Well I just think it'd be a lot of fun! And I'm willing
    to put in the work to make it happen."

    mc "Wow that's great. So where are you starting?"

    ulamog sheepish "Ummm... Well, that's the thing. I have no idea where to
    start."

    mc "Oh, well. The contestants will need to be cooking, right? So you could
    start with whatever is needed to cook."

    ulamog neutral "Yeah, that's good. Uhhh..{w} Like, ingredients?"

    mc "Ingredients, a kitchen, probably tools."

    ulamog hands "Oh! Maybe we can borrow the school's kitchen."

    mc "I think that might be your only option, but how would you go about
    doing that?"

    ulamog "I'll just go up and ask!"

    mc "Just go up and ask?"

    hide ulamog with moveoutright

    "But Ulamog has already stood up and is dashing out of the library."

    mc "Huh.."

    "You suppose you might as well follow. It could be interesting."

    play music hijinks fadeout 2.0 fadein 1.0

    scene bg hall with dissolve

    show ulamog hands at center with dissolve

    "Ulamog makes an {b}expedite{/b}d pace down the hall with a skip in their
    step."

    "Well, not a literal skip as they have tentacles in place of legs, but a
    metaphorical skip."

    hide ulamog with moveoutright

    "Ulamog turns the corner to the principal's office and you hear the door
    {b}crack open{/b}. What you don't hear is any knock or indication of
    Ulamog's entrance."

    "You round the corner yourself and see Ulamog standing outside the office."

    show ulamog hands at center with dissolve

    ulamog "They said yes!!"

    mc "Wait. Didn't you just enter that door?"

    ulamog "Yes. And I asked, and they said yes!"

    mc "That took like 6 seconds."

    ulamog neutral "Talking is a free action."

    mc "..."

    mc "What?"

    ulamog hands @ sheepish "Uhh.. Wrong game, nevermind. C'mon let's go!"

    hide ulamog with moveoutleft

    "Ulamog runs past you back toward the library."

    "You stand {b}stun{/b}ned, {b}bound in silence{/b}."

    "Maybe it's best not to {b}dwell on the past{/b}, you turn around and
    start walking back as well."

    play music library fadeout 2.0 fadein 1.0

    scene bg library 3 with dissolve

    show nissa neutral at far_left
    show ulamog hands at center
    with dissolve

    nissa "Oh, there you are. Where'd you two go?"

    ulamog "We got a kitchen!!"

    nissa distracted "You got a kitchen?"

    mc "I am just as {b}bewilder{/b}ed as you are."

    mc "No, actually. Probably a bit more."

    ulamog "Now we just need to get knives, and pots, and bowls..."

    "Ulamog starts to ramble off tools as he moves toward his usual spot
    at the back of the library."

    hide ulamog with moveoutright

    nissa neutral "So umm... I see it went well."

    mc "As well as one might expect I suppose."

    ulamog "... And parchment paper and rollers and trays..."

    nissa "Well, I'm glad you two are getting along."

    mc "Yeah, I guess that just--{nw}"

    show ulamog hands:
        offscreenright
        linear 0.25 center

    ulamog "YOINK!!"

    show ulamog hands:
        center
        linear 0.25 offscreenright

    scene bg library 2 with dissolve

    show ulamog hands at center with moveinright

    "And with that, Ulamog grabs your arm and pulls you toward the tables in
    the back."

    "You spend the rest of the time ironing out details with Ulamog as you
    craft your {b}brilliant plan{/b}."

    python:
        date_1 = "ulamog"

    jump day2_scene5

    return

label day2_scene4_kozilek:

    "You spot Kozilek reading in the corner of the library sitting up against a
    bookshelf."

    scene bg library 1 with dissolve

    show kozilek cross at center with dissolve

    "You wander over and take a seat next to him."

    "As you sit down Kozilek glances up at you."

    show kozilek neutral at center with Dissolve(0.25)

    "But when your eyes meet he quickly averts his {b}otherworldly gaze{/b}
    back down to his book."

    show kozilek cross at center with Dissolve(0.25)

    mc "So... \"Kozi-kun\" huh?"

    kozilek "Don't call me that."

    mc "Hmm.. \"Kozilek-tan\" then?"

    kozilek "..."

    show kozilek:
        center
        linear 0.5 xalign 0.6

    "Kozilek moves their body to {b}turn against{/b} you, but in doing so
    pushes himself closer to you."

    mc "Alright alright, message received. \"Kozilek-kun\" then."

    mc "Shouldn't you be preparing your class' event?"

    kozilek neutral "What does it look like I'm doing?"

    "You lean over Kozilek's shoulder to get a better glimpse of what he's
    reading."

    play music hijinks fadeout 2.0 fadein 1.0

    mc "They ran their slimy tentacles across my body, the black {b}void{/b}
    of their eyes looking deeply in--{nw}"

    play sound close_book

    kozilek "NOTHING!!"

    "They slam the book shut before you can read any further."

    kozilek cross @ angry "It's research obviously, ugh. You are such a
    {b}nuisance engine{/b}. Don't you have anything better to do!?"

    mc "Well, I thought I could help you organize and plan..."

    mc "But it looks like you've got everything sorted out."

    "You stand up."

    kozilek angry "Wait no!"

    kozilek cross "I mean.. I do have everything sorted but..{w} You don't need
    to leave."

    mc "You want me to stay?"

    kozilek angry "Yes!"

    kozilek cross "No!"

    kozilek cross @ blush "Umm... I mean you..."

    "Kozilek finishes the rest of their sentence in an incomprehensible
    mumble."

    mc "Pardon me, could you repeat that?"

    kozilek "Ugh, just stay.."

    mc "Apologies, a bit louder this time?"

    kozilek angry "Okay fine!! Just stay idiot!"

    mc "Very well."

    "You find your seat back on the floor and lean up against the bookshelf
    next to Kozilek."

    kozilek cross "I'm not reading this because I like it or anything,{w} just
    saying."

    mc "Hm? I didn't think you were."

    kozilek neutral "Oh.. Yeah, well I'm just letting you know. It really is
    for research."

    mc "I believe you."

    kozilek "I thought our class could perform a short play for the
    {b}festival{/b} based on a historical event."

    mc "Quite a realistic endeavor."

    kozilek "So I needed to do some research to make sure our representation
    was historically accurate."

    mc "That's a very reasonable assessement of the situation."

    kozilek angry "STOP DOING THAT!!"

    mc "Doing what?"

    kozilek cross "That!"

    kozilek angry "You keep agreeing with me!"

    mc "You want me to disagree with you?"

    kozilek "NO!"

    kozilek cross "I mean.. But you don't need to be so nonchalant about it."

    mc "You want me to agree with you enthusiastically?"

    kozilek "Ugh, nevermind! Just stop talking."

    mc "..."

    "You hold out a thumbs-up to signal your understanding."

    kozilek neutral "..."

    "The next several minutes pass in awkward {b}silence{/b}."

    "Well, awkward for Kozilek, you're more just amused."

    show kozilek cross at center with Dissolve(0.25)

    "Kozilek tries pretending to read his book but it's obvious he's just
    uncomfortably ignoring you."

    "His eyes flick back and forth between you and the open book, never
    stopping to scan the words or flip the page."

    "After an {b}hour of eternity{/b}{w}--or well, more like four
    minutes{w}--Kozilek slams the book shut for the second time today and gets
    up."

    play sound close_book

    kozilek @ angry "Ugh! Why do you have to make it so awkward!?"

    mc "Awkward? I'm not doing anything."

    kozilek neutral @ angry "Exactly!"

    "Kozilek aggressively shoves the book into his bag and gets up."

    mc "You're done reading?"

    kozilek cross "Whatever, I don't need more research anyway."

    mc "Alright, good for you."

    kozilek neutral "I'm going to go draft the script now."

    mc "Enjoy."

    show kozilek:
        center
        linear 1.0 offscreenright

    pause 3.0

    show kozilek:
        offscreenright
        linear 1.0 right

    pause 1.0

    kozilek "Aren't you going to come with me?"

    mc "Oh, did you want me to?"

    kozilek cross "Yes.{w} No! I mean..."

    kozilek "I don't really care. You can come if you want to."

    mc "Well that's awfully kind of you."

    play music library fadeout 2.0 fadein 1.0

    scene bg library 3
    show kozilek neutral at center
    with dissolve

    "You follow Kozilek back to the tables as he sits down with blank lined
    paper."

    mc "I should ask, as I never did find out. What is it exactly your play
    is about?"

    kozilek "It's about the Eldrazi Winter, not like you would understand."

    mc "No, I suppose not. After all, it's not like I wasn't living under
    a rock during 2016."

    kozilek "No, you weren't. So just don't bother alright?"

    mc "Mhm."

    "There were too many negative comparatives for you to process in that
    interaction."

    "You could probably figure out what Kozilek meant. But the warranty on your
    braincell has long since expired, so it might be a bad idea to stress it
    any further."

    "You pass the rest of the time in relative comfort as Kozilek makes a crude
    attempt to {b}reconstruct history{/b}."

    "With you correcting him on several key details."

    python:
        date_1 = "kozilek"

    jump day2_scene5

    return

label day2_scene4_emrakul:

    show emrakul neutral at center with dissolve

    mc "Uhhh.. Emrakul, right?"

    show emrakul wave at center with Dissolve(0.25)

    "But Emrakul doesn't reply. Instead, she looks up at you and raises a
    tentacle in greeting."

    "Or, at least, you think she looks at you. The massive eye in the center
    of Emrakul's body seems to pierce your very soul."

    mc "What're you working on?"

    "You take a seat next to Emrakul and look down to see a mildly concerning
    amount of pornographic light novels spread out across the floor."

    "Well, now that you think about it. Any amount of porn would be concerning.
    So the sheer quantity of porn spread out in front of Emrakul isn't really
    done justice by your description."

    "If you were to try again, you think 'ungodly' would paint a much better
    mental image of just how much porn is lying on the library floor of this
    public school."

    mc "Ummm..."

    show emrakul blush at center with Dissolve(0.25)

    "Emrakul doesn't seem to notice your {b}falter{/b}, she just looks down and
    idly moves the hentai comics around with a tentacle."

    mc "Maybe I should leave..?"

    emrakul neutral "I think you'd look good in this one."

    "Emrakul holds up a comic to reveal a suggestively posed human clad
    in what barely qualifies as clothing."

    play music hijinks fadeout 2.0 fadein 1.0

    menu:
        "Compliment her back":
            "Without a second thought to your social setting, or a first regard
            to what card game you're playing, you flick your wrist and down
            your sleeve flies your trusty old UNO reverse card."

            "You twist your fingers to let the metaphorical ace up your sleeve
            face Emrakul."

            "You mutter the {b}magic word{/b}s \"Go fish\" and prepare to banish
            her to The Shadow Realm."

            "Then, with a fervent {b}display of dominance{/b}, you thrust the
            UNO reverse card in Emrakul's face and scream."

            mc "NO U!!"

            mc "You would look far better in that attire than myself."

            python:
                emrakul_date_1 = "compliment"
        "Sit in awkward silence":
            "You look at the near-naked human drawn in the comic, then back at
            Emrakul."

            show emrakul point at center with Dissolve(0.25)

            "Then back at the drawing, all the while maintaining the most
            uncomfortable aura between you and Emrakul."

            "She seems to get the message as she lowers the comic and turns
            away from you."

            python:
                emrakul_date_1 = "silence"
        "Run out of the library screaming":
            "It's a {b}rouse{/b}, you can smell it."

            "Emrakul is trying to seduce you, but you won't fall for it."

            "You will not be tempted by her {b}captivating glance{/b}."

            show emrakul point at center with Dissolve(0.25)

            "Bitches are temporary, the sigma grindset is eternal."

            "You prepare to {b}declare dominance{/b} by sprinting out of the
            library screaming at the top of your lungs."

            "But just as you stand up to T-Pose, Chandra and Nissa walk up
            behind you."

            python:
                emrakul_date_1 = "scream"

    show nissa neutral at far_right
    show chandra neutral at far_left
    show emrakul neutral at center
    with dissolve

    nissa "Hey guys, what's going on over here?"

    chandra mischief "Quite the cultured collection you've got, respect."

    nissa horrified "EEEEEEEEEEEEK!!"

    "It seems Nissa too, fell victim to the classic blunder:{w} looking down."

    nissa uncomfortable "E-Emrakul-chan, I told you yesterday that this isn't
    appropriate for a school event."

    chandra neutral @ shrug "You said nothing of the sort."

    nissa point "I had meant to, b-but I shouldn't need to!"

    nissa uncomfortable "Emrakul-chan, can you please just put these away for
    now?"

    "Nissa looks away and gestures a sweeping motion toward the floor covered
    in disproportionate drawings of naked humans."

    chandra mischief "Now hold on a minute.{w} I think this is exactly what our
    school {b}festival{/b} needs this year."

    "Chandra leans over and takes a comic to {b}select for inspection{/b}."

    show nissa distracted at far_right with Dissolve(0.25)

    "Nissa averts her eyes as Chandra gives the hentai a {b}careful study{/b}."

    "After few too many seconds of {b}silence{/b} Chandra nods in impressed
    approval and tosses the comic back on the floor."

    chandra "Why don't we let these two carry on with their endeavors."

    show chandra:
        linear 1.0 right

    "Chandra turns Nissa around and walks her away from the scene."

    chandra shrug "And we'll worry about your own event."

    play music library fadeout 2.0 fadein 1.0

    hide nissa
    hide chandra
    with moveoutright

    if emrakul_date_1 == "compliment":
        mc "Huh."

        mc "Well."

        "You return the UNO card to your sleeve, having served its purpose."
    elif emrakul_date_1 == "silence":
        mc "Huh."
    elif emrakul_date_1 == "scream":
        mc "Huh."

        mc "Well."

        "You sit back down, the threat to your sigma ways having
        {b}dissipate{/b}d."

    mc "Are you uhh.. Sure you should be doing this?"

    emrakul "I think it's fine."

    mc "Remind me again. What is it you're doing exactly?"

    emrakul blush "Mmmmmm..."

    "Emrakul gestures to the ungodly quantity of porn strewn across the
    floor."

    mc "Ah, I see."

    "You do not see."

    mc "Well then, is there any way I can help?"

    emrakul neutral @ blush "Fufufufufu."

    mc "Oh, {b}wonder{/b}ful."

    "Not {b}wonder{/b}ful."

    show emrakul:
        linear 0.5 offscreenright

    pause 1.5

    show emrakul clothes:
        offscreenright
        linear 0.5 center

    "Emrakul floats over to the tables and returns with a set of..."

    "Technically{w} clothes."

    "In the same way {b}mind rot{/b} is technically draw because it's card
    disadvantage for your opponent and therefore card advantage for you."

    "Which is to say, it's not draw at all."

    "And similarly, what Emrakul's holding in her tentacles aren't really
    clothes at all."

    "You recognize them from the hentai drawing she just showed you."

    mc "Uhhh, wait.. Is that?"

    mc "Why do you have that!?"

    emrakul @ blush "Fufufu. Put it on."

    mc "You brought that to school?"

    emrakul "Just put it on!"

    "She extends a tentacle for you to grab the questionable attire."

    "You reach your hand out and grab the clothes."

    show emrakul neutral at center with Dissolve(0.25)

    mc "I'm not putting this on in a public library."

    emrakul point "B-b-but."

    emrakul "Pleeeeaaase."

    "Emrakul's one eye scrunches up in the most pitiful manner."

    "Gosh, how can you say no to that?"

    "Well, you can think of many ways to say no."

    mc "Fine, I'll do it."

    show emrakul blush at center with Dissolve(0.25)

    "..."

    "Why did you say yes?"

    emrakul "Yay~"

    mc "Uhh..."

    scene bg library 3 with dissolve

    "You wander around the library, the {b}shock{/b} of the entire situation
    still setting in."

    show nissa neutral at far_left with dissolve

    if gender == "male":
        nissa "Oh, uhh.. What're you doin' [name_1]-kun?"
    elif gender == "female":
        nissa "Oh, uhh.. What're you doin' [name_1]-chan?"
    else:
        nissa "Oh, uhh.. What're you doin' [name_1]-san?"

    mc "I.. Uh..."

    "Nissa glances down at your hands."

    nissa uncomfortable "..."

    nissa "Do I umm.."

    nissa "Umm.. Need to end the meeting today?"

    mc "..."

    nissa "So umm...{w} Hey guys!"

    show ulamog neutral at left
    show kozilek neutral at center
    show emrakul neutral at right
    with moveinright

    nissa "I think we should stop here for today, you've all done great
    work."

    ulamog "Awwwww, but it's only been an hour, the library doesn't close until
    18:00."

    nissa uncomfortable "Oh, well uh.. The library was reserved today.{w} By
    another club,{w} so we need to clean up before they get here."

    ulamog "Awww."

    kozilek cross "Hmphf."

    hide ulamog
    hide kozilek
    hide emrakul
    with moveoutright

    "The rest shuffle out of the library leaving you, Nissa, and dubious set of
    clothes in your arms."

    scene bg hall
    show nissa distracted
    with dissolve

    nissa "So I'll uh.. See you tomorrow?"

    mc "Yeah yeah, that uh..{w} Sounds about right, sure."

    python:
        date_1 = "emrakul"

    jump day3_scene1

    return

label day2_scene4_nissa:

    show nissa neutral at Position(xalign = 0.6) with dissolve

    if gender == "male":
        nissa "Oh, [name_1]-kun."
    elif gender == "female":
        nissa "Oh, [name_1]-chan."
    else:
        nissa "Oh, [name_1]-san."

    show chandra neutral at left with dissolve

    chandra "Hey hey."

    nissa "We were just discussing our plans for our class' activity."

    chandra unamused "We absolutely were not. In fact, we were discussing about
    the farthest thing from {b}festival{/b} activities."

    nissa distracted "Well, that's what we should've been discussing."

    chandra "Well it's too late for that. We're not changing the subject
    until we finish this discussion."

    mc "Am I interrupting something?"

    chandra neutral "Yeah, just our conversation about chameleons. Sit down."

    mc "Umm.. Chameleons?"

    chandra shrug "Well I had brought up to her that the fact we know
    chameleons even exist means they suck at their job."

    chandra "But Revane-chan, for some god-forsaken reason, knows that
    chameleons actually change color as a means of communication rather than
    camoflauge."

    chandra unamused "Sexual communication, she made that part quite explicit."

    nissa point "Well, when you put it like that..."

    chandra neutral "Which of course, like any respectable pursuers of science,
    left us {b}wonder{/b}ing which color means \"I want to fuck\"."

    nissa "Only you wanted to know that."

    chandra shrug "I think it's green, she thinks it's red."

    nissa uncomfortable "I didn't say anything about that."

    chandra mischief "You very distinctly and coherently mumbled the words
    \"No, it'd  be red\" into your chest after I said \"Definitely green\"."

    nissa distracted @ point "..."

    play music hijinks fadeout 2.0 fadein 1.0

    if gender == "male":
        chandra mischief "Anyways, [name_2]-kun, this is a question of utmost
        importance. You must be our tie-breaker, you must deliver the
        {b}supreme verdict{/b}."
    elif gender == "female":
        chandra mischief "Anyways, [name_2]-chan, this is a question of utmost
        importance. You must be our tie-breaker, you must deliver the
        {b}supreme verdict{/b}."
    else:
        chandra mischief "Anyways, [name_2]-san, this is a question of utmost
        importance. You must be our tie-breaker, you must deliver the
        {b}supreme verdict{/b}."

    chandra "What color best represents the ever-expanding complexities of
    sexual arousal?"

    menu:

        "Which color means \"I want to bang\"?"

        "White":
            mc "Well, I think white is pretty sexy."

            chandra unamused "..."

            nissa "..."

            mc "What?"

            chandra "Contrary to mainstream media, having an opinion is a
            privilege, not a right."

            chandra "And right now you are very close to losing that
            {b}priveleged position{/b}."

            mc "Uhhh.. Okay?"

            chandra neutral "I'm glad you understand. Now please, take a seat.
            Your mother and I need to have a serious talk with you."

            "Chandra attempts her best Dad-voice and places her hand on top
            of Nissa's."

            "Nissa looks away, but doesn't move her hand."

            "You take take a seat, like a child about to be disciplined."

            mc "Look, if this is about the children in the basement, I already
            said I'm sorry."

            if gender == "male":
                chandra "No [name_2]-kun, I couldn't give a {b}tarmogoyf{/b}'s
                toughness about your \"collection\"."
            elif gender == "female":
                chandra "No [name_2]-chan, I couldn't give a {b}tarmogoyf{/b}'s
                toughness about your \"collection\"."
            else:
                chandra "No [name_2]-san, I couldn't give a {b}tarmogoyf{/b}'s
                toughness about your \"collection\"."

            chandra unamused "We need to address your attitude towards the
            color pie."

            mc "But Dad! All colors are equal."

            chandra "That is NOT how I raised you!"

            chandra "Green must be able to do everything the other colors can,
            but better. That way it's balanced!"

            mc "But what about color diversity!?"

            chandra @ intrigue "After all this time? You're still spouting that
            \"Balanced Design\" {b}conspiracy{/b} nonsense."

            chandra "That's it, go to your room!"

            mc "But--"

            chandra "One more word and I replace your modern deck with seventy
            five {b}colossal dreadmaw{/b}s."

            mc "..."

            nissa uncomfortable "What is  h a p p e n i n g ?"
        "Blue":
            mc "I think it'd probably have to be blue."

            chandra unamused "Blue!? Excuse you! Only incels and legacy players
            get horny at the sight of blue."

            chandra "..."

            chandra mischief "Oh, wait. Unless you play merfolk.."

            chandra intrigue "Do you play merfolk?"

            mc "Uhh...."

            if gender == "male":
                chandra "Answer the question [name_2]-kun."
            elif gender == "female":
                chandra "Answer the question [name_2]-chan."
            else:
                chandra "Answer the question [name_2]-san."

            chandra unamused "Do you play merfolk?"

            mc "I play Mono U Tron, does that count?"

            chandra "..."

            chandra "....."

            "Chandra stares at you with {b}harsh scrutiny{/b}, the weight
            of her judgment pressing down on you."

            chandra "........."

            chandra "Acceptable."

            if gender == "male":
                chandra "But you are {b}on thin ice{/b} [name_2]-kun."
            elif gender == "female":
                chandra "But you are {b}on thin ice{/b} [name_2]-chan."
            else:
                chandra "But you are {b}on thin ice{/b} [name_2]-san."

            nissa uncomfortable "I am so  c o n f u s e d."
        "Black":
            mc "Oh, black for sure. No contest."

            chandra intrigue "You do realize there's more to Magic than
            {b}thoughtseize{/b} and {b}Liliana of the Veil{/b}."

            mc "Like {b}leyline of the void{/b}?"

            chandra unamused "No, that doesn't count."

            mc "What about {b}fatal push{/b}?"

            chandra "One more black card out of your mouth and I'll
            {b}fatal push{/b} you out this window."

            mc "You wouldn't {b}defenestrate{/b} me on the second story now
            would you?"

            chandra shrug "Alright, that's it."

            nissa uncomfortable "What is  h a p p e n i n g ?"
        "Red":
            mc "Well red's pretty sexy I guess."

            chandra intrigue "What!? Who looks at red and thinks \"Yeah, I'd
            fuck that\"?"

            nissa blush "I think red's a very romantic color"

            chandra shrug "Pffft, romantic? Sex isn't romantic."

            chandra "You think chameleons like romance?"

            nissa point "Well I don't know.. I just like the color red."

            chandra mischief "Heh, do you think I'm romantic then?"

            "Chandra gestures to her body clad in various shades of red."

            nissa @ point "Um.. Well, you look very..."

            "Nissa mumbles the rest of her sentence down into her chest."

            "And although her expression is hidden, you wouldn't be surprised
            if she was also turning quite red."
        "Green":
            mc "Well, I think green's pretty sexy."

            chandra neutral "Ahhh, finally!"

            chandra shrug "See! I told you, green is the universal color of
            sex."

            chandra "Even chameleons understand that the power of horny eclipse
            all language barriers."

            chandra unamused "Not like red."

            chandra mischief "Red's for
            {b}burning cinder fury of crimson chaos fire{/b}!! Not sex."

            nissa point "I just thought red looked romantic.."

            chandra "Well you're objectively, scientifically, empirically
            wrong."

            nissa distracted "Uhhh.. Okay."
        "Colorless":
            "Maybe answering \"Colorless\" to a question that expects a color
            as an answer isn't the smartest play."

            "But considering you can count the number of braincells you have
            on one hand, it's possible that logic and reason aren't the most
            effective decision-making tools at your disposal."

            mc "Oh, colorless is definitely the sexiest."

            chandra unamused "..."

            chandra "I bet you're one of those people who think Caw-Blade was
            a {b}Storm Crow{/b} tribal deck with equipment."

            mc "Wait, Caw-Blade wa-"

            chandra intrigue "Yes?"

            mc "...{w} Nevermind."

            chandra neutral "Good."

            chandra "I'm glad I didn't need to bring out the
            {b}ankle shanker{/b}, slash your Achilles tendons."

            mc "Hey, my Achilles tendons have nothing to do with this, you
            leave them out of it!"

            if gender == "male":
                chandra shrug "Sorry [name_2]-kun, that's just business."
            elif gender == "female":
                chandra shrug "Sorry [name_2]-chan, that's just business."
            else:
                chandra shrug "Sorry [name_2]-san, that's just business."

            chandra "It's a {b}cruel reality{/b}."

            nissa uncomfortable "What the  h e c k."

    chandra neutral "So anyways, did you have plan for your class' event
    Revane-chan?"

    nissa distracted "Uhhhh..."

    "You can see the metaphorical whiplash Nissa just got from the sudden
    shift in demeanor."

    "The unexpected change in subject certainly isn't helping her {b}increasing
    confusion{/b}."

    "But she {b}rebound{/b}s surprisingly quickly and moves on."

    nissa smile "Oh, I uhh.. Was thinking of hosting a tea ceremony."

    nissa neutral "There's a classroom with tatami we could borrow and--{nw}"

    chandra mischief "Nah, that's boring, your class should host a {b}death
    match{/b} in the courtyard. {b}Last one standing{/b} gets free college
    admittance."

    nissa distracted @ horrified "Oh my gosh, no! We aren't going to have a
    freaking {b}fight to the death{/b} in the middle of school."

    mc "Oh oh, how about ceremonial human {b}sacrifice{/b} to the {b}Lord of
    Extinction{/b}?"

    chandra "My, well aren't you just a {b}well of ideas{/b}. What a splendid
    suggestion."

    mc "Happy to be of service."

    nissa @ horrified "No! No sacrifices to the extinction lord whoever thing."

    mc "How about the {b}Lord of the Forsaken{/b}?"

    chandra neutral @ intrigue "Or the {b}Lord of the Void{/b}?"

    mc "Or {b}Lord of the Pit{/b}."

    chandra @ shrug "You've got plenty of options."

    nissa uncomfortable "Why are there so many lords?"

    mc "That's not even half of them."

    nissa distracted "Okay okay, stop. I shouldn't've asked."

    chandra "You definitely shouldn't've."

    nissa "We're not doing that. There will be no killing or death during the
    {b}festival{/b}."

    if gender == "male":
        chandra "Well [name_2]-kun, how does it feel to have
        {b}death denied{/b}?"
    elif gender == "female":
        chandra "Well [name_2]-chan, how does it feel to have
        {b}death denied{/b}?"
    else:
        chandra "Well [name_2]-san, how does it feel to have
        {b}death denied{/b}?"

    mc "Not great, I won't lie. It's a bit of a {b}crushing
    disappointment{/b}."

    chandra shrug "Understandable. Oh well, there's always next year right?"

    mc "That's the spirit."

    nissa uncomfortable "Can we please get back on topic?"

    chandra neutral "Right right, of course. Where were we? Tea ceremony,
    no death."

    mc "I can't even {b}poison the cup{/b}s?"

    chandra @ shrug "I would argue that matcha is already poison, but no, no
    poisoning the drinks unfortunately."

    mc "This is a tragedy, I suppose I'll have to settle for spiking them with
    ketamine."

    nissa distracted "No spiking the drinks either."

    mc "Not even Mexican black-tar heroin?"

    "Nissa plants her face in her hands and leans over the table."

    nissa "I just wanted to plan our class' event."

    chandra @ mischief "Ooooo, I think we broke her."

    mc "Okay okay, sorry. I'll stop."

    play music library fadeout 2.0 fadein 1.0

    "You and Chandra try to refrain from any more {b}murder{/b} jokes as Nissa
    starts actually planning her event."

    "The rest of the time passes in relative tedium as productivity often
    scales inversely with fun."

    show nissa neutral with Dissolve(0.25)

    "But by the end Nissa seems to be proud of what she's accomplished, not
    that you really payed attention."

    "It was mostly Chandra helping her while you watched and occasionally
    interjected with meaningless comments."

    scene bg hall with dissolve

    show nissa neutral at center with dissolve

    if gender == "male":
        nissa "Hey [name_1]-kun."
    elif gender == "female":
        nissa "Hey [name_1]-chan."
    else:
        nissa "Hey [name_1]-san."

    nissa "Walk home with me?"

    mc "Certainly."

    play music after_school_intro fadeout 2.0 fadein 1.0
    queue music after_school

    scene bg park
    show nissa neutral at center
    with dissolve

    "You and Nissa make the typical {b}harrowing journey{/b} out of school
    and down the path toward your respective homes."

    "Nissa is unusually quite the entire time, like she's {b}ponder{/b}ing
    something important."

    nissa distracted "..."

    if gender == "male":
        nissa "Hey [name_1]-kun?"
    elif gender == "female":
        nissa "Hey [name_1]-chan?"
    else:
        nissa "Hey [name_1]-san?"

    mc "Yeah?"

    nissa "..."

    nissa point "Do you like Nalaar-san?"

    mc "..."

    mc "You think I like her?"

    nissa distracted "Well, I dunno. That's why I'm asking."

    mc "She likes you."

    nissa uncomfortable "Huh?"

    mc "You seriously haven't noticed?"

    mc "She takes every opportunity to be near you."

    mc "She's not even a class president, why do you think she hangs out at
    the library?"

    nissa point "Because she wants to be involved with school spirit?"

    mc "My lord, how dense can you be?"

    mc "It's because of you."

    mc "There's no reason on Heaven or Earth that somebody would go through
    that except for lust."

    scene bg street
    show nissa distracted at center
    with dissolve

    mc "Well, anyways. I'll let you have your crisis in {b}solitude{/b}, This
    is my house."

    nissa distracted "...{w} Oh uhh..{w} Okay, bye then."

    mc "Bye."

    python:
        date_1 = "nissa"

    jump day3_scene1

    return

label day2_scene5:

    scene bg hall with dissolve

    show nissa neutral at center with dissolve

    if gender == "male":
        nissa "[name_1]-kun!"
    elif gender == "female":
        nissa "[name_1]-chan!"
    else:
        nissa "[name_1]-san!"

    mc "Hey Nissa-chan."

    nissa smile "I saw you helping today, you looked like you were having fun."

    mc "Yeah, I guess you could say that."

    nissa neutral "Anyways, walk home with me?"

    mc "Always."

    scene bg park
    show nissa neutral at center
    with dissolve

    "You and Nissa make the typical {b}harrowing journey{/b} out of school
    and down the path toward your respective homes."

    "Nissa is unusually quite the entire time, like she's {b}ponder{/b}ing
    something important."

    nissa distracted "..."

    if gender == "male":
        nissa "Hey [name_1]-kun?"
    elif gender == "female":
        nissa "Hey [name_1]-chan?"
    else:
        nissa "Hey [name_1]-san?"

    mc "Yeah?"

    nissa "..."

    if date_1 == "ulamog":
        nissa point "Do you like Ulamog-kun?"
    elif date_1 == "kozilek":
        nissa point "Do you like Kozilek-kun?"

    mc "Yeah, I do."

    nissa "No, I meant like, likelike--"

    mc "I know what you meant."

    nissa distracted "Oh."

    if date_1 == "ulamog":
        nissa smile "Hehe, that give me cavities."

        mc "Cavities?"

        nissa "Because it's so sweet~"

        nissa "I think you and Ulamog-kun would be very sweet together."
    elif date_1 == "kozilek":
        nissa smile "Haha, that sounds like fun."

        nissa point "Uhh, I just mean. You two might have a fun time courting
        each other."

        mc "Courting?"

        nissa smile "Well, if he comes off as abrasive at first don't be too
        discouraged."

    mc "Uhh, okay. I will keep it in mind, thank you."

    scene bg street
    show nissa neutral at center
    with dissolve

    nissa "Well, looks like we split here. I'll see you tomorrow!"

    mc "Bye.."

    jump day3_scene1

    return

label day3_scene1:

    play music home_intro fadeout 2.0 fadein 1.0
    queue music home

    scene bg bedroom with fade

    "Fridays are overrated."

    "Yeah, it's true."

    "People don't seem to understand that Fridays are still an entire day of
    work."

    "You still need to go to school for the same amount of time as any other
    weekday."

    "Now, don't get it wrong, Fridays are still great. After all, unlike other
    weekdays, there's no homework because it's all been pushed back to Sunday."

    "But despite this, Fridays are still massively overvalued."

    "If there were a way to short days of the week like a stock market you
    would make so much money shorting Friday that you wouldn't even need to
    work on Fridays."

    "But then that would increase the value of Fridays back to being
    accurately valued."

    "And then you'd need to work of Fridays again..."

    "Which means you could short them again?"

    "Curse you Burton G. Malkiel."

    jump day3_scene2

    return

label day3_scene2:

    play music school fadeout 2.0 fadein 1.0

    scene bg classroom backleft with dissolve

    "The teacher stands up and begins their lesson on some highly empirical
    math concept."

    "Immediately, it feels like a {b}winter orb{/b} hit the battlefield and
    nobody has artifact removal."

    "You're trying to follow along, or at least look like you are, but you
    don't understand a thing."

    "You don't even recognize half the {b}unspeakable symbol{/b}s on the
    whiteboard."

    "And why are there letters? In fact, there are more letters than there are
    numbers. You thought this was math, not English."

    "The {b}journey to eternity{/b} begins as you trudge your way through the
    group slug of public education."

    scene bg hall with dissolve

    "Class ends, leaving you with just enough {b}stamina{/b} to survive a trip
    to the library."

    "And so that's exactly what you end up doing."

    jump day3_scene3

    return

label day3_scene3:

    play music library fadeout 2.0 fadein 1.0

    scene bg library 3 with dissolve

    "You spot the usual suspects just where they're expected and head over to
    them."

    scene bg library 2 with dissolve

    show nissa neutral at far_left
    show ulamog neutral at center
    show kozilek neutral at far_right
    with dissolve

    nissa "Well, the {b}festival{/b} starts on Monday so today's our last day
    to get everything together unless we want to be working over the weekend."

    nissa "I guess we can get started then. Is everybody here?"

    "You look around the library. And count: 1, 2 humanoids; and 1, 2 Eldrazi."

    "Hmmmm.. Upon closer inspection there seems to be a distinct lack of
    Emrakul in the room."

    ulamog "Oh no!! We're missing Emmy-chan!"

    "Yes, keen observation Ulamog."

    nissa distracted "That's strange, she's never late. Where could she be?"

    play music legacy_intro fadeout 2.0 fadein 1.0
    queue music legacy

    scene bg library 2
    show nissa uncomfortable at far_left
    show ulamog neutral at center
    show kozilek neutral at far_right
    with hpunch

    emrakul "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!"

    "Suddenly, a {b}resounding scream{/b} rings out from the hallway outside
    the library."

    nissa "What was that? It sounded like Emrakul-chan."

    show ulamog:
        center
        linear 0.25 offscreenright

    "Ulamog runs over to the windows."

    ulamog "Emmy-chan!!"

    emrakul "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!"

    "Another shrill screech of pure, unadulterated {b}terror{/b} pierces the
    hallways."

    "That's strange."

    "What could possibly scare the most powerful being in all the multiverse?"

    "{b}Emrakul, the Aeons Torn{/b}, master of time and space."

    "Who bends the {b}field of reality{/b} at a whim."

    emrakul "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!"

    "What deeply unfathomable {b}twisted abomination{/b}?"

    "What unspeakable {b}horror of horrors{/b} could elicit such a {b}shriek
    of dread{/b} from {b}Emrakul, the Promised End{/b}?"

    emrakul "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!"

    emrakul "FIFTEEN FLYING SQUIRRELS!!!!"

    stop music fadeout 2.0

    "..."

    "Oh.."

    "..."

    "Yes, you suppose a massive flying {b}squirrel mob{/b} would be
    understandably frightening."

    "But somehow you still feel an inkling of disillusionment."

    hide kozilek with moveoutright

    play music legacy fadein 1.0

    show emrakul scared at center with moveinright

    emrakul "HEELLLLPP!"

    show squirrelMob at right with moveinright

    "Emrakul bursts through the library doors with, indeed, fifteen flying
    squirrels behind her."

    stop music fadeout 2.0

    "Everybody else stares blankly as the squirrels mindlessly flap around the
    room."

    nissa distracted "Ummmm.."

    show chandra neutral at left with dissolve

    chandra "Maybe we should..{w} Deal with that..?"

    hide squirrelMob with dissolve

    "A quick {b}blazing volley{/b} from Chandra {b}incinerate{/b}s the
    squirrels and Emrakul breathes an audible sigh of relief."

    show emrakul neutral with Dissolve(0.25)

    hide chandra with moveoutleft
    hide emrakul with moveoutright
    hide ulamog with moveoutright

    play music library fadeout 2.0 fadein 1.0

    nissa "So..."

    nissa uncomfortable "Everybody's here."

    nissa distracted "I guess we should get started.."

    menu:

        "Help whom?"

        "Ulamog":
            jump day3_scene4_ulamog
        "Kozilek":
            jump day3_scene4_kozilek
        "Emrakul":
            jump day3_scene4_emrakul
        "Nissa":
            jump day3_scene4_nissa

    return

label day3_scene4_ulamog:

    scene bg library 2 with dissolve

    "You wander over to Ulamog who's scribbling down on a sheet of paper."

    show ulamog neutral at center with dissolve

    "Just as you approach him, he stands up."

    if gender == "male":
        ulamog "Oh. Hi [name_2]-kun."
    elif gender == "female":
        ulamog "Oh. Hi [name_2]-chan."
    else:
        ulamog "Oh. Hi [name_2]-san."

    ulamog "I was just about to go {b}hunt down{/b} all the stuff I need."

    ulamog hands "Come with me!"

    mc "Sure."

    scene bg hall
    show ulamog neutral
    with dissolve

    if date_1 == "ulamog":
        mc "So cooking huh. What's it you're looking for then?"

        ulamog "Well, I was gonna check the kitchen we borrowed for all the
        tools and ingredients we need."

        mc "Sounds like a plan."
    else:
        mc "So what're you planning for your event?"

        ulamog "We're going to host a cooking contest."

        ulamog "So I was gonna check the school kitchen for all the tools and
        ingredients we need."

        mc "Oh my, well that sounds ambitious."

        ulamog "It sounds fun!"

    play music jealous fadeout 2.0 fadein 1.0

    scene bg kitchen
    show ulamog neutral at center
    with dissolve

    "You and Ulamog arrive at the kitchen you'll be using."

    "It's significantly more impressive than you expected from this school."

    ulamog "Alright, so we just need to clean it and make sure it has all the
    supplies."

    hide ulamog with moveoutright

    scene bg kitchen with dissolve

    show ulamog hands at center with dissolve

    ulamog "Ooooo! It looks so professional."

    ulamog "I'm so excited! I can't wait to cook in here!"

    show ulamog:
        center
        linear 0.25 left

    "Ulamog scurries around the room, opening every cabinet and drawer like
    a {b}rummaging goblin{/b}."

    show ulamog:
        left
        linear 0.5 right

    ulamog "Woah! So many utensils."

    show ulamog neutral at center with fade

    "After Ulamog is done beholding the kitchen he pulls out a checklist of
    tools and cooking ware."

    "You don't know the names of many them, so you just read them off as Ulamog
    finds them."

    mc "Stainless steel cooking pot."

    ulamog hands "Check."

    mc "Cast iron wok."

    ulamog "Check."

    mc "Knives."

    ulamog "Many."

    mc "Cutting boards."

    ulamog "Check."

    mc "Food processor."

    ulamog neutral "Would a food processor put food tokens from exile into the
    graveyard?"

    mc "I have no clue, do we have one or not?"

    ulamog "No, no. Food tokens, not clue tokens."

    mc "Tokens can't exist outside of the battlefield."

    ulamog "What about {b}bone rattler{/b}?"

    mc "..."

    mc "Do we have a food processor or not?"

    ulamog sheepish "Oh, um.. Yes we do."

    mc "{b}Pulverize{/b}r."

    ulamog hands "Check."

    mc "Meat tenderizer."

    ulamog "Check."

    mc "These are very violent names."

    ulamog "It's fine, don't worry about it."

    mc "Shredder."

    ulamog neutral "Let's see..."

    mc "This can't be real right?"

    ulamog hands "Ah, here it is."

    mc "Geez, okay."

    mc "Guillotine!?"

    ulamog sheepish "Um.. Let me check."

    mc "Why would we possibly need a guillotine in the kitchen?"

    ulamog neutral "You've never used a guillotine before?"

    mc "Can't say I have."

    ulamog "The guillotine is a staple of any kitchen arsenal."

    ulamog hands "It brings the oft lacking {b}gratuitous violence{/b} into
    home gastronomy."

    ulamog "Vive la révolution!"

    mc "Uhh.. So is there actually a guillotine in the school kitchen?"

    ulamog "Oui oui, je viens d'en trouver un dans ce placard."

    mc "Oh, you actually speak French?"

    ulamog "Well of course, it's easy!"

    mc "Really? Will you teach me?"

    ulamog sheepish "Teach you?"

    mc "Yeah, teach me. Since you seem to be quite fluent."

    ulamog hands "Oh, silly. You can't learn French."

    mc "What?"

    ulamog "Didn't you know? You only gain the ability to speak French by
    inserting a baguette into your asshole."

    mc "I'm sorry, what the fuck?"

    ulamog neutral "In fact, most Frenchmen are born with baguettes already in their
    ass."

    mc "No, no. I wasn't being rhetorical, it's a genuine question. What the
    actual fuck?"

    ulamog hands "C'mon, I'll show you!"

    hide ulamog with moveoutleft

    scene bg bathroom with dissolve
    show ulamog hands at center with moveinright

    "Ulamog takes your hand and pulls you into a nearby bathroom."

    "He shoves you into a stall and manifests a 60cm baguette seemingly from
    thin air."

    ulamog baguette "Now pull your pants down and bend over."

    menu:

        mc "Um..."

        "Do as Ulamog says":
            jump baguette_comply
        "Blow the rape whistle":
            jump baguette_whistle

    return

label baguette_comply:

    "You do as Ulamog says."

    "You rest your hands on the toilet seat and {b}brace for impact{/b}."

    "You can see Ulamog preparing the baguette in the reflection of the
    porcelain."

    "Then it starts."

    "One centimeter."

    "Then another."

    mc "Is this really necessary?"

    ulamog "It's this, or take your chances with the Duolingo owl."

    mc "Continue then."

    "You feel the crusty exterior of the bread {b}explore{/b} deeper inside
    you."

    "Suddenly, you feel a {b}rush of knowledge{/b} flowing into you mind."

    "Words fill your head in a {b}swirling torrent{/b} of language."

    "The baguette continues, pushing further into your rectum."

    "And as the doughy enema reaches its climax, a {b}flood of recollection{/b}
    washes over you."

    "Vocabulary, grammar, pronunciation. In a {b}flash of insight{/b} you've
    gained the entirety of the French language without so much as picking up
    a book."

    jump day3_scene4_ulamog_french

    return

label baguette_whistle:

    "You pull the rape whistle from your pocket and blow into it as hard as you
    can."

    play sound whistle

    "The shrill sound {b}reverberate{/b}s around the room."

    mc "RAPE!!!"

    "Then, as if summoned, a blue light tears through the air opening a
    {b}planar portal{/b} in the bathroom stall."

    "From the portal, out step two sharp men in uniforms."

    "And in heavy French accents they start yelling."

    "Man 1" "Arret!"

    "Man 2" "Au sol!"

    "The first man tackles Ulamog to the floor and pins their arms down."

    ulamog sheepish "Wait! Wait! I can explain!"

    if gender == "male":
        "Man 2" "There will be no explanation necessary. How dare you try to
        violate this young man."
    elif gender == "female":
        "Man 2" "There will be no explanation necessary. How dare you try to
        violate this young lady."
    else:
        "Man 2" "There will be no explanation necessary. How dare you try to
        violate this young person."

    ulamog neutral "No, please! I was just trying to teach my friend French."

    "Man 1" "Hm?"

    ulamog baguette "See, I have the baguette in my hand."

    "Man 2" "Well, so he does."

    "Man 1" "Oh my, we are terribly sorry."

    "The man {b}remove{/b}s himself from Ulamog."

    "Man 2" "Please, continue. French is such a beautiful language."

    mc "Wait! What!?"

    "The men step back into the portal and {b}disappear{/b} from reality."

    "Ulamog picks himself up from the bathroom floor and grabs the baguette."

    ulamog neutral "So?"

    menu:

        ulamog "So?"

        "Continue":
            jump baguette_whistle_continue
        "Decline":
            jump baguette_whistle_decline

    return

label baguette_whistle_continue:

    mc "Okay."

    ulamog "Then you'll do it?"

    mc "Sure, I guess."

    ulamog baguette "{b}Wonder{/b}ful!"

    jump baguette_comply

    return

label baguette_whistle_decline:

    mc "Please, I'd rather not do this."

    ulamog @ sheepish "Oh, okay.."

    "Ulamog lowers the baguette looking dejected."

    scene bg hall
    show ulamog neutral at center
    with dissolve

    "You awkwardly leave the bathroom without any more words."

    jump day3_scene4_ulamog_english

    return

label day3_scene4_ulamog_french:

    stop music fadeout 2.0

    scene bg hall
    show ulamog neutral at center
    with dissolve

    mc "C'est vraiment fou, je peux parler français maintenant."

    ulamog hands "Isn't it great!?"

    mc "I don't know if I should be impressed or concerned."

    ulamog "Impressed!"

    mc "Concerned it is then."

    jump day3_scene4_ulamog_english

    return

label day3_scene4_ulamog_english:

    play music library fadeout 2.0 fadein 1.0

    scene bg library 3 with dissolve

    "You return to the library just as the rest of the group is wrapping up."

    scene bg library 2 with dissolve

    show ulamog neutral at center with dissolve

    mc "So did you find everything you needed."

    ulamog "Yep, I think we're ready. Now I just need to show up to school
    early on Monday so I can set up."

    if gender == "male":
        ulamog "Come help me [name_2]-kun!"
    elif gender == "female":
        ulamog "Come help me [name_2]-chan!"
    else:
        ulamog "Come help me [name_2]-san!"

    mc "Uh, and wake up at 6:00am?"

    ulamog "C'mon it'll be fun."

    mc "I'll set my quantum alarm clock. Might happen, might not."

    ulamog sheepish "Hmmm.. Okay. Well, either way I'll see you Monday right?"

    mc "Yeah, I'll be there"

    ulamog hands "Yay!"

    python:
        date_2 = "ulamog"

    jump day3_scene5

    return

label day3_scene4_kozilek:

    hide nissa with dissolve

    "You wander over to Kozilek who's sorting papers on the table."

    scene bg library 2 with dissolve
    show kozilek neutral at center with dissolve

    "As you approach, Kozilek stands up and shoves the papers at you."

    kozilek "Hold these."

    mc "Oh, uhh.."

    "You take the papers before your mouth can formulate a response."

    kozilek "This way."

    hide kozilek with moveoutright

    pause 1.0

    show kozilek cross at far_right with moveinright

    "Kozilek walks out but stops at the library exit and turn to you."

    kozilek cross "Ugh, could you be any slower?"

    "Kozilek stares at you. You suppose you should follow him."

    scene bg hall
    show kozilek cross at center
    with dissolve

    mc "Wait, so what exactly are we doing?"

    kozilek "We're gathering props, okay, just shut up and follow me."

    mc "Fair enough."

    "You look down at the papers in your hands."

    "It looks to be a list, although the chirography balances the fine
    line between 'barely legible' and 'demonic scratchings'."

    if date_1 == "kozilek":
        mc "Forgive me if I ask what this list is of."

        kozilek "Just stuff we need. I already got the rest of my class ready
        with scripts, we just need to get the rest of that list."
    else:
        mc "So what are the props for?"

        kozilek "Our class is doing a play for the {b}festival{/b}."

        kozilek "We need props for a play, so were getting some, it's not that
        difficult."

    kozilek neutral "I'm only asking you to help because you weren't doing
    anything and the rest of our class is busy."

    kozilek "So don't get the wrong idea."

    kozilek cross "It's not like I like you or anything, baka."

    "You suddenly feel a great disturbance in the fabric of reality. As if a
    thousands weebs cried out and were suddenly {b}silence{/b}d."

    mc "Understandable."

    scene bg classroom back
    show kozilek cross at center
    with dissolve

    "Kozilek takes you into an empty classroom with a closet in the back."

    mc "A janitorial closet?"

    kozilek neutral "One of the items we need is a mop, the school said we
    could borrow one from here."

    mc "Huh. Well, it's not my place to question it."

    play sound door_open_close

    show kozilek neutral at center with dissolve

    kozilek "Okay, this is it. Just get in there and find a mop, don't
    make this any more awkward than it needs to be."

    mc "Why? Is this awkward for you?"

    kozilek angry "No!"

    kozilek cross "I mean..{w} Just go!"

    hide kozilek with dissolve

    scene bg closet dark with dissolve

    play sound close_door

    "You and Kozilek enter the closet and hear the door swing close behind
    you."

    play music hijinks fadeout 2.0 fadein 1.0

    "The light from the hallway disperses and you're {b}cast into
    darkness{/b}."

    mc "It's dark in here."

    kozilek "Turn on the light, idiot."

    mc "I can't find it."

    kozilek "Ugh."

    mc "..."

    mc "I don't think there's even a light in here."

    kozilek "Okay! Then just find the mop, you don't need a light!"

    mc "Alright."

    mc "..."

    play sound falling_box_small

    mc "I think I found the mop."

    kozilek "You think?"

    mc "I don't know, it's dark."

    mc "I can't reach it, can you help?"

    kozilek "Ugh, fine. But I'm not doing this for you."

    show kozilek cross at center with dissolve

    mc "Sure."

    kozilek "Shut up!"

    kozilek "Where?"

    "You point."

    kozilek "Ugh."

    "Kozilek grabs the mop and pulls."

    play sound falling_box_small

    hide kozilek with dissolve

    pause 0.5

    play sound falling_box_large

    pause 0.5

    play sound close_door

    kozilek "AAAH!"

    kozilek "What did you do!?!"

    mc "I didn't do anything!"

    play sound falling_box_large

    kozilek "Get it off!"

    mc "I can't see anything."

    play sound falling_box_small

    kozilek "Just AAAAAH!"

    mc "Are you okay?"

    play sound falling_box_large

    "You {b}fumble{/b} your hand through the {b}darkness{/b} until you feel
    Kozilek's bony exterior."

    kozilek "Don't touch me!"

    "Despite what he says, Kozilek grabs your hand."

    play sound falling_box_small

    "You can't see anything in the pitch black closet, but holding Kozilek's
    hand in yours is enough to get your heart racing." # hnnnnngh, the cringe

    "You both sit there in {b}deafening silence{/b} for a bit too long."

    "After a mildly discomforting amount of time a crack of
    {b}blinding light{/b} casts itself into the closet and the door gives way
    behind you."

    play sound door_open_close

    scene bg classroom frontleft with dissolve
    show chandra neutral at left with dissolve

    "You and Kozilek tumble to the cold tiled floor of the classroom. Above you
    stands Chandra with a mixture of disappointment and amusement on her face."

    play music library fadeout 2.0 fadein 1.0

    show kozilek neutral at right with dissolve

    mc "Oh, uhh.. Thanks Nalaar-san."

    chandra "Y'all were literally up against the door."

    chandra "It wasn't even locked or anything."

    kozilek cross "It was dark.."

    chandra unamused "What were y'all even doing in there?"

    mc "Well--{nw}"

    chandra shrug "Actually, y'know what? Nevermind, I don't want to know."

    hide chandra with moveoutleft

    show kozilek:
        right
        linear 1.0 center

    mc "..."

    mc "So.."

    mc "What else is on this list?"

    kozilek "..."

    "But Kozilek turns their head and starts walking out."

    kozilek "Whatever. We don't need anything else today."

    mc "What about everything else on this list?"

    kozilek @ angry "Whatever!"

    hide kozilek with moveoutleft

    "Kozilek storms out of the room."

    mc "Fair enough."

    scene bg hall with dissolve

    "You follow Kozilek out into the hall where he's standing outside the
    door."

    show kozilek cross at center with dissolve

    mc "Oh, you didn't run away?"

    kozilek "No.{w} I mean, I could've."

    mc "But you didn't."

    kozilek "I just didn't feel like it."

    mc "Because you wanted to keep talking to me?"

    kozilek angry "No. That's stupid.{w} You're stupid!"

    mc "This is not false.. But you're evading the question."

    kozilek cross "..."

    "Kozilek looks away and doesn't answer."

    "Maybe you've been teasing too much."

    mc "So when do I get to see this play?"

    kozilek "Monday, I guess."

    mc "What role will you be playing?"

    kozilek "Just a minor part, it really doesn't matter."

    mc "You know I'm going to see it. So I'll know by Monday anyway."

    kozilek angry "It's just a stupid play, you shouldn't even bother coming."

    mc "Challenge accepted."

    kozilek cross "No! I mean..{w} It's embarrassing."

    mc "Embarrassing?"

    kozilek angry "Because it's you!"

    kozilek cross "I mean..{w} It would be..{w} For anybody..."

    kozilek @ angry "Just shut up! Baka!"

    "There it is again. That strange feeling."

    mc "Well, I'm just letting you know that I'm going to see this and there's
    nothing you can do to stop me."

    kozilek @ blush "O-okay."

    mc "I'm glad we understand."

    mc "Now, is there anything else you need to prepare before Monday."

    kozilek neutral "Uh, no it's fine. I'll do it over the weekend."

    mc "Are you sure? I can help you now."

    kozilek cross "No, no. It's fine,{w} I need to leave early anyways."

    mc "Huh, alright. Well, don't stress too much about it."

    kozilek blush "Okay, bye."

    hide kozilek with dissolve

    mc "Bye."

    "Well, that was..."

    "Interesting."

    python:
        date_2 = "kozilek"

    jump day3_scene5

    return

label day3_scene4_emrakul:

    scene bg library 3 with dissolve

    "You walk over to Emrakul who's curled up underneath the table."

    mc "Uhh.. Hey Emrakul-chan."

    emrakul "..."

    mc "You good?"

    emrakul "s q u i r r e l s."

    mc "Mhm, yep. That sounds about right."

    emrakul "so  m a n y."

    mc "I mean.. There were only like fifteen."

    mc "Although I suppose that's about fifteen more than I would expect in
    the middle of a school library."

    mc "Anyways, are you gonna get out from under that table anytime soon?"

    show emrakul scared at center with dissolve

    mc "Ahh, that's better."

    mc "So the {b}festival{/b}'s on Monday, what have you done to prepare for
    it?"

    emrakul "..."

    if date_1 == "emrakul":
        "Has she seriously done nothing but look at hentai this entire time?"

        emrakul point "Yeah..."

        mc "Yeah what?"

        emrakul scared "Yeah, I've done nothing but look at hentai this entire
        time."
    else:
        "Has she seriously done nothing to prepare for her event?"

        emrakul point "Yeah..."

        mc "Yeah what?"

        emrakul scared "Yeah, I've done nothing to prepare for my event."

    mc "..."

    mc "Oh, um.."

    mc "That doesn't sound very responsible."

    emrakul neutral "It's fine, the {b}festival{/b} isn't important anyways."

    mc "It isn't?"

    emrakul blush "No, I'd rather just spend this time with you."

    mc "That's both flattering and slightly terrifying."

    emrakul neutral "It's not terrifying at all. C'mon I know exactly the
    place."

    hide emrakul with moveoutright

    "Emrakul floats out of the library. And with nothing better to do with your
    time, you follow her."

    scene bg hall with dissolve
    show emrakul neutral at center with dissolve

    "She's probably right. There's nothing terrifying about this at all, you've
    just been reading too many yandere light novels."

    emrakul blush "Exactly, there's no need to be scared."

    mc "What?"

    emrakul point "Nothing."

    emrakul neutral "Here we are."

    play music hijinks fadeout 2.0 fadein 1.0

    scene bg classroom frontleft
    show emrakul neutral at center
    with dissolve

    "Emrakul leads you into an empty classroom."

    mc "So what are we doing here?"

    emrakul blush "I just thought we could use some privacy."

    "Your confidence in the level of creepiness of this situation is decreasing
    by the minute."

    emrakul neutral "Stop saying it's creepy."

    mc "I didn't say anything."

    emrakul point "Oh.."

    emrakul neutral @ blush "Just stay there then."

    mc "Sure..."

    "Emrakul pulls out a camera."

    "She takes a picture of you."

    "..."

    mc "I should probably be leaving."

    emrakul scared "Nonononono. Stay."

    mc "Don't you have work to do?"

    emrakul blush "It's fine."

    "Emrakul reaches into a large duffel bag you just noticed was brought into
    the room."

    if date_1 == "emrakul":
        "She pulls out a concerningly provocative outfit you recognize from the
        magazines she was looking at yesterday."
    else:
        "She pulls out a concerningly provocative outfit from the bag."

    emrakul clothes "Now put this on."

    mc "There's less actual cloth in that outfit than there are non-elk
    creatures in Throne of Eldraine Standard."

    emrakul point "You don't like it?"

    mc "I never said that."

    mc "But yes,{w} now that you mention it,{w} I hate it."

    emrakul clothes @ blush "That's okay, just put it on."

    "She smiles as if nothing's wrong."

    "Or, well..{w} She doesn't exactly have a mouth, but you can definitely
    tell she's smiling."

    "You struggle to fathom the sheer gap of logic present in Emrakul's
    deduction."

    emrakul "My logic is flawless, you should put on the costume because I want
    you to."

    "Like that Warlock invocation for {b}jump{/b}ing, except it applies to
    conclusions."

    emrakul "Warlock what?"

    "Oops, wrong game."

    emrakul wave "Game?"

    "Oh, Emrakul was talking this entire time. You should probably be paying
    attention to her."

    emrakul scared "Yes! Stop ignoring me!"

    mc "Yep, time to start ignoring Emrakul."

    "Oh wait. You said that one out loud."

    mc "Y'know, maybe I should just leave. You obviously have some important
    stuff to do. I wouldn't want to bother you."

    "You stand up to move toward the door. But Emrakul pushes you down into a
    chair."

    emrakul clothes @ blush "No, you should stay."

    mc "..."

    mc "Yep, way too much Yandere Simulator."

    "Although, the the if/else riddled spaghetti code is actually way more
    stroke-inducing than the actual game."

    "That's not the point though."

    "The point is, you need to leave immediately."

    "You stand up."

    mc "Ight Imma head out."

    "Emrakul watches as you leave the room."

    scene bg hall with dissolve

    play music library fadeout 2.0 fadein 1.0

    "You step out into the hall, leaving Emrakul to do God-knows-what back
    in the classroom."

    "You'd take more responsibility for her event if it weren't for...{w} Well,
    no. You wouldn't take any responsibility under any reasonable
    circumstance."

    "At least that means less guilt for you."

    "A win's a win. We take these."

    python:
        date_2 = "emrakul"

    jump day3_scene5

    return

label day3_scene4_nissa:

    "You walk over to Chandra and Nissa who both still seem to be digesting
    the situation that just played out."

    show chandra neutral at left with moveinleft

    show nissa uncomfortable at Position(xalign = 0.6) with dissolve

    nissa "What just happened?"

    "You all look down at the {b}char{/b}red mound of dead squirrels on the
    library floor."

    chandra "I find it's best not to think about it."

    chandra @ shrug "In fact, I find it's best not to think in general."

    "Chandra makes a sweeping motion with her hand and the pile of squirrels
    turns to {b}crumbling ashes{/b}."

    chandra "See. Don't worry about it."

    nissa distracted "Uhh.. Okay."

    chandra "Anyways, why don't we try actually being productive then?"

    nissa neutral @ smile "Yeah, yeah we should probably do that."

    chandra mischief "Oh wait. Really?{w} I was joking. You thought I actually
    wanted to be productive!?"

    nissa distracted "I--"

    chandra "Should know better than to think that? Yes, you really should."

    chandra neutral "Man, school events are so lame anyways. There's no
    spectacle, no drama."

    nissa point "Well, sure there's spectacle."

    chandra shrug "What, you mean your tea party? Does your tea party have
    eight fucking bears?"

    mc "holY shit!"

    nissa distracted "..."

    chandra neutral "Yeah, I didn't think so. Here, let me help you with your
    event. Hand me that organizing sheet."

    "Chandra reaches over and grabs the paper in front of Nissa before she can
    respond."

    chandra "Bowl, caddy, scoop, whisk, kimono, cushion. See, this is all
    boring paraphernalia.{w} You need something with flair."

    nissa uncomfortable @ horrified "We're not bringing eight bears onto school
    campus."

    chandra @ shrug "No, you're right. Eight fucking bears isn't nearly
    grandiose enough."

    mc "holY shit!"

    if gender == "male":
        chandra "What do you think [name_2]-kun? What would really elevate
        this {b}festival{/b} to the next level?"
    elif gender == "female":
        chandra "What do you think [name_2]-chan? What would really elevate
        this {b}festival{/b} to the next level?"
    else:
        chandra "What do you think [name_2]-san? What would really elevate
        this {b}festival{/b} to the next level?"

    mc "Hmm..{w} Oh! I got it."

    mc "{b}Goreclaw, Terror of Qal Sisma{/b}."

    chandra unamused "Hmmm..."

    mc "What's wrong?"

    chandra neutral @ shrug "Dies to {b}doomblade{/b}."

    mc "{b}Damn{/b}, you're right!"

    mc "..."

    mc "Okay, okay okay. This time I got it."

    mc "{b}Glyph Keeper{/b}."

    chandra @ shrug "Dies to playset of {b}doomblade{/b}s."

    mc "{b}Damn{/b}, right again."

    mc "..."

    mc "Hmm.. This is tough indeed."

    mc "Okay, How about.."

    mc "A giant 8/8 Octopus token!"

    chandra @ shrug "Dies to Steve's crossbow smh my head."

    mc "Heck."

    mc "..."

    mc "Okay. This time. This time I definitely got it."

    chandra mischief "Hit me."

    mc "{b}Yargle, Glutton of Urborg{/b}."

    chandra intrigue "..."

    chandra mischief "Oh my god, I think you've got it."

    chandra "The perfect addition to our tea party."

    nissa distracted "Tea ceremony."

    chandra shrug "Whatever."

    chandra mischief "There's no way any school event could be boring when
    Yargle's there. Yargle's the entire party."

    mc "You're absolutely right."

    chandra "C'mon, let's go get them. I have Yargle on speed dial."

    "Chandra stands up."

    nissa uncomfortable "Uh, what's happening?"

    chandra shrug "We're helping you!"

    hide chandra with moveoutright

    "Chandra runs out of the library. You and Nissa tentatively follow."

    scene bg hall with dissolve
    show chandra neutral at left with dissolve

    chandra "This way!"

    scene bg classroom frontleft with dissolve

    show nissa distracted at Position(xalign = 0.6) with dissolve

    nissa "Does anybody even use this classroom anymore?"

    mc "We are, of course."

    nissa "I see..."

    show chandra neutral at left with moveinleft

    "Chandra returns from the back closet carrying a box of red chalk and
    several scented candles."

    chandra "Ready to summon The Glutton of Urborg?"

    nissa "I really don't see how this is going to help my class' event."

    chandra shrug "Oh silly, we already explained this to you. We're inviting
    Yargle to your tea party."

    nissa "Tea ceremony."

    chandra neutral @ shrug "Whatever."

    "Chandra draws a pattern on the center desk with the red chalk and places
    the candles around the pattern."

    "She makes a motion with her hands and the candles ignite."

    "Billowing {b}smoke{/b} begins to spill out from the desk and the room
    starts to smell strongly of lavender."

    nissa uncomfortable "Umm.. What's going on?"

    stop music fadeout 2.0

    "Suddenly, a {b}brilliant spectrum{/b} of colored lasers start firing out
    of the {b}smoke{/b}."

    "The entire classroom lights up like a rave party as electro-synth pop
    music starts to blast out of the summoning desk in the middle."

    play music synth fadein 1.0

    show nissa:
        linear 0.5 xalign 1.2

    show chandra:
        linear 0.5 xalign -0.2

    show yargle cool at center with dissolve

    yargle "YARGLE'S COME TO BARGLE!!!"

    chandra "YARGLE!"

    mc "BARGLE ME YARGLE!!"

    nissa distracted "That actually worked?"

    chandra "Oh great Yargle, we humbly request that you bargle our tea party
    next week."

    nissa "Tea ceremony."

    chandra @ shrug "Whatever."

    yargle "Tea party you say?"

    yargle "Tea parties are the best for Bargling."

    mc "Thank you great Yargle!"

    nissa uncomfortable "I...{w} I'm just gonna leave.."

    hide nissa with moveoutleft

    "All" "BARGLE!!"

    stop music fadeout 2.0

    scene bg hall with dissolve

    "After Chandra finishes {b}unsummon{/b}ing Yargle she heads back to the
    library to help Nissa."

    "You wander out into the hallway with nothing to do."

    python:
        date_2 = "nissa"

    jump day3_scene5

    return

label day3_scene5:

    scene bg hall with dissolve

    "Nissa's staying late to help everybody with final preparations. You're
    already pretty drained from today so you decide to walk home by yourself."

    "She'll understand, you're sure."

    play music after_school_intro fadeout 2.0 fadein 1.0
    queue music after_school

    scene bg park with dissolve

    "Despite only starting to walk with Nissa for the past couple days, the
    {b}isolate{/b}d walk home feels unusually lonesome."

    "You're left alone with only your {b}wandering mind{/b} to keep you
    company."

    if date_2 == "ulamog":
        "Your {b}train of thought{/b} inevitably drifts toward Ulamog."

        "You {b}wonder{/b} how his class' event is going to turn out. It is
        quite ambitious after all."

        "But he's clearly passionate about it, so there shouldn't be any
        problems."

        "You do however, sincerely hope there will be no guillotines, or
        baguettes, or anything French related for that matter."

        "..."

        "Ewww, Fr*nce."
    elif date_2 == "kozilek":
        "Your {b}train of thought{/b} inevitably drifts toward Kozilek."

        "You {b}wonder{/b} how his class' event is going to turn out. He didn't
        end up getting much done today. Hopefully he'll be able to get
        everything ready in time for Monday."

        "His attitude toward you seems.. Fickle, at best. Maybe you should
        stop teasing him."

        "..."

        "Nah."

        "Way too much fun."

        "Maybe you'll consider it if he ever stops being so cliche."
    elif date_2 == "emrakul":
        "Your {b}train of thought{/b} inevitably drifts toward Emrakul."

        "You {b}wonder{/b} how her class' event is going to turn out.{w}
        Actually, you don't have to {b}wonder{/b} at all. You're confident it's
        going to be an absolute disasterpiece."
    elif date_2 == "nissa":
        "Your {b}train of thought{/b} inevitably drifts toward Nissa and
        Chandra."

        "You {b}wonder{/b} how Nissa's class event is going to turn out. She
        seems to have prepared pretty well considering all you and Chandra did
        was try to distract her the entire time."

        "But there's no use in worrying about it. There's absolutely no way
        she could mess up this tea party when Yargle will be there."

    scene bg street with dissolve

    "Oh well, it seems you've arrived at your house. A perfect excuse to stop
    thinking and start mindlessly scrolling through the void of social media
    until it's time to fall asleep."

    jump day4_scene1

    return

label day4_scene1:

    play music home_intro fadeout 2.0 fadein 1.0
    queue music home

    scene bg bedroom with dissolve

    "The weekend passes by in relative tedium as time skips often leave you
    sprawled out on the couch with nothing to do."

    "It's Monday morning now and you're struggling for reasons to get out of
    bed."

    "Food, you think to yourself."

    "Food's not a bad reason to get out of bed."

    "What about a shower? Shower's are nice."

    "Well, not really the showering part. Moreso just the standing under warm
    water part."

    "Hmm..."

    if date_2 == "ulamog":
        "Ulamog."

        "That's right. How could you forget?"

        "Ulamog's cooking thing is today."
    elif date_2 == "kozilek":
        "Kozilek."

        "That's right. How could you forget?"

        "Kozilek's play thing is today."
    elif date_2 == "emrakul":
        "Emrakul."

        "That's right. How could you forget?"

        "Emrakul's..."

        "Something, is today."
    elif date_2 == "nissa":
        "Yargle."

        "That's right. How could you forget?"

        "Nissa's tea party is today."

        "And Yargle'll be there."

    "That's enough to get you out of bed."

    "Maybe Monday's aren't as bad as everyone thinks they are."

    jump day4_scene2

    return

label day4_scene2:

    play music walking fadeout 2.0 fadein 1.0

    scene bg street with dissolve

    "There's nobody waiting for you outside."

    "Nissa must've gone to school early to help set up for the
    {b}festival{/b}."

    "You probably should've too, but you value your sleep too much."

    "Get it?"

    "It's a joke..{w} Because you didn't sleep at all."

    "Whatever."

    scene bg park with dissolve

    "You make the walk to school by yourself, the once familar path now foreign
    and solitary."

    "Walking back from school with Nissa and now walking to school by
    yourself."

    "It seems everything's flipped around."

    scene bg schoolgrounds with dissolve

    "You arrive at school fashionably late, as you always do."

    "There are significantly more students wandering the courtyard than usual."

    "There are no classes, the whole day has been blocked out for
    {b}festival{/b} events."

    scene bg hall with dissolve

    "You make it inside the main building to see more students roaming the
    halls."

    "Various classrooms have been renovated to make space for their events."

    "You wander around in {b}contemplation{/b} of where you should go first."

    if date_2 == "ulamog":
        jump day4_scene3_ulamog
    elif date_2 == "kozilek":
        jump day4_scene3_kozilek
    elif date_2 == "emrakul":
        jump day4_scene3_emrakul
    elif date_2 == "nissa":
        jump day4_scene3_nissa

    return

label day4_scene3_ulamog:

    play music jealous fadeout 2.0 fadein 1.0

    scene bg kitchen with dissolve

    "You enter the kitchen where Ulamog is preparing his event."

    show ulamog hands at center with dissolve

    if gender == "male":
        ulamog "Hi [name_2]-kun!"
    elif gender == "female":
        ulamog "Hi [name_2]-chan!"
    else:
        ulamog "Hi [name_2]-san!"

    mc "Hi there, are you preparing your cooking thing?"

    ulamog "I just finished!"

    mc "Oh my."

    "You look around the school kitchen. Various cooking paraphernelia are
    spread out across the counters and tables."

    mc "So how is this going to work?"

    ulamog neutral "I gathered a panel of expert judges to evaluate the
    dishes."

    "Ulamog gestures at a small group of tired students who look as if they'd
    rather be {b}eaten alive{/b} than sitting there right now."

    ulamog "Then we'll have the next few people that show up participate in the
    competition."

    mc "And who would that be?"

    show ulamog:
        linear 0.5 right

    show nissa neutral at left
    show chandra neutral at center
    with moveinright

    chandra "--told you Yargle's got it covered. I just want to set things on
    fire."

    ulamog hands "Hi guys!!"

    nissa smile "Hi Ulamog-kun!"

    ulamog "Omygosh! You two are the last ones we need."

    nissa neutral "What do you mean?"

    ulamog neutral "Do you know how to cook?"

    chandra mischief "I can set things on fire."

    ulamog hands "Perfect! You can enter our competition."

    nissa uncomfortable "Wait, what?"

    ulamog "C'mon, we're starting soon."

    "As soon as the realization sets in, a crowd of students begin to pour
    into the room buzzing with excitement."

    if gender == "male":
        ulamog "You too [name_2]-kun."
    elif gender == "female":
        ulamog "You too [name_2]-chan."
    else:
        ulamog "You too [name_2]-san."

    "Ulamog grabs your arm and drags you to the other side of the kitchen."

    hide nissa
    hide chandra
    with moveoutright

    show ulamog:
        right
        linear 0.5 center

    mc "Huh!?"

    ulamog "You'll be my partner!"

    mc "There are partners?"

    "Judge" "We will begin in three seconds."

    mc "What are even the rules?"

    "Judge" "There are no rules."

    mc "Oh..."

    "Judge" "Start!"

    play music legacy_intro fadeout 2.0 fadein 1.0
    queue music legacy

    hide ulamog with moveoutleft

    "On the word, Ulamog starts rushing around the kitchen grabbing metallic
    instruments of unknown use. You see Chandra and Nissa doing the same over
    on the other side of the kitchen."

    mc "What are we even making?"

    ulamog "Anything!"

    show ulamog neutral at left with moveinleft

    "Ulamog returns to the counter with four handfuls of food and tools."

    "You pick up a long serrated knife to examine."

    "You could definitely {b}eviscerate{/b} somebody with this."

    ulamog @ hands "Here! Fillet this!"

    "Ulamog throws a fish at you."

    "You barely react in time to {b}redirect{/b} it away from your face
    with a slap."

    "The fish flops onto the countertop. You start searching for a cutting
    board."

    ulamog "No time! Just cut it there."

    mc "Oh, okay."

    "That sounds unsanitary."

    hide ulamog with dissolve

    "You hastily make an incision in the fish's underside."

    "You think about how the fish must've felt when being caught."

    "It must be painful to have a hook in your mouth."

    "You make a {b}surgical extraction{/b} of the fish's spine and begin to
    slice up the flesh."

    "But more than that, you think about the fisherman who caught the fish."

    "You hope they're okay. After all, if there's anything Avacyn hates more
    than heretics, it's fishermen."

    "You finish filleting the fish and look over at Ulamog."

    show ulamog neutral at center with dissolve

    "He's tossing way too many ingredients to count into a giant wok in the
    center of the stove."

    "You throw the fish in as well and look around for the next thing to do."

    hide ulamog with dissolve

    show nissa excited at Position(xalign = 0.6)
    show chandra neutral at left
    with dissolve

    "Across the room you see Chandra and Nissa scurrying around their side of
    the kitchen while a comically oversized chicken breast {b}roast{/b}s over
    an {b}open fire{/b}."

    "The {b}blaze{/b} reaches higher as the {b}engulfing flames{/b} of the
    stove {b}threaten{/b} to {b}burn down the house{/b}."

    "Chandra's hair has also burst into flame, and Nissa occasionally passes
    a frying pan over her head to fry the collection of ingredients inside."

    "At the other end of the kitchen, a horde of students have shown up to
    cheer on the contestents."

    "The {b}roar of the crowd{/b} makes you feel {b}invigorate{/b}d."

    hide nissa with moveoutright

    show chandra:
        linear 0.5 center

    "You run up to the center of the kitchen thinking you might use that
    guillotine for something."

    chandra unamused "Eww, Fr*nce."

    mc "Hey, you're not wrong. But I'm not about to dice this onion with
    a regular knife, like a plebeian."

    chandra shrug "Oh honey, you don't have to worry about being a plebeian."

    chandra intrigue "With the food you'll be serving, you'll have more people
    lined up to see your beheading than any French aristocrat."

    mc "Oh? We're smack-talking now? It's on."

    chandra neutral @ unamused "It's on fire, yeah. Better stop talking and
    keep an eye on your dish."

    mc "You're one to talk, I heard they had to disable to {b}smoke{/b} alarms
    on your side of the room."

    "Chandra turns around."

    chandra unamused "Darn it Nissa-chan! What're you doing to the fire?"

    nissa "Uhhh..."

    hide chandra with moveoutright

    "You return to your side of the kitchen with onion and beheading device in
    hand."

    show ulamog neutral at center with dissolve

    mc "Okay Ulamog-kun. It gets serious now."

    ulamog hands "Oh boy! I love dramatic tension."

    mc "Yes, exactly. Now, what's our secret ingredient?"

    ulamog sheepish "Secret ingredient?"

    mc "Yes Ulamog-kun. Don't you know that every good recipe has a secret
    ingredient?"

    ulamog neutral "Oh.."

    ulamog hands "Well how about friendship?"

    mc "Perfect! There's no way we'll lose this competition with the power
    of friendship in our judge's mouths."

    mc "..."

    ulamog neutral "Question:"

    mc "Yes?"

    ulamog sheepish "How do we add friendship to our dish?"

    mc "Hmmm..."

    mc "Oh!"

    mc "We could scream like anime protagonists and cook in overly animated
    fashion."

    ulamog hands "That's a fantastic idea!"

    mc "Okay, ready?"

    ulamog "I've been training for this my entire life."

    "You and Ulamog look across the room to lock eyes with Chandra and Nissa."

    mc "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!"

    scene bg kitchen
    show ulamog hands at center
    with hpunch

    ulamog "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!"

    hide ulamog with dissolve

    show nissa neutral at far_right
    show chandra neutral at center
    with dissolve

    "Chandra and Nissa stare at you from the other side of the room."

    show nissa distracted at far_right with Dissolve(0.25)

    "They look at each other, then back at you."

    show nissa excited at far_right with Dissolve(0.25)

    chandra neutral @ notc "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!"

    "Chandra and Nissa start screaming as well. Even the fires {b}flicker{/b}
    higher in response to the increased excitement."

    play sound clapping

    "Then {b}the crowd goes wild{/b} and not a single person in the room isn't
    releasing a {b}bloodcurdling scream{/b}."

    "This is where the real cooking begins. You think to yourself."

    hide chandra
    hide nissa
    with dissolve

    show ulamog neutral at center with dissolve

    mc "Okay Ulamog-kun. It's time to go super saiyan, unleash your final
    form."

    if gender == "male":
        ulamog hands "No [name_2]-kun, we do it together."
    elif gender == "female":
        ulamog hands "No [name_2]-chan, we do it together."
    else:
        ulamog hands "No [name_2]-san, we do it together."

    mc "Yes Ulamog-kun. With the power of friendship, nothing can stop us."

    "You grab Ulamog's hand and together you raise the wok above your heads."

    "You look into Ulamog's eyes. And together you nod in silent
    understanding."

    scene bg kitchen
    show ulamog hands at center
    with hpunch

    "[name_1] and Ulamog" "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!"

    "The flames of both the stoves rise higher until they lap the ceiling of
    the kitchen."

    show ulamog:
        linear 0.5 left

    show rainbow at center with hpunch

    "A friendship rainbow explodes from your wok and fires into the air,
    breaking a hole through the roof."

    "The noise from your anime-empowered screams shake the entire building and
    {b}tremor{/b}s emenate from your stove."

    "All" "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!"

    stop music fadeout 2.0

    "..."

    "..."

    "When all is settled, a wave of {b}silence{/b} washes over the crowd."

    "You and Ulamog drop to the floor not having realized your anime powers
    temporarily {b}suspend{/b}ed you in the air."

    "Judge" "And the winner of the competition is..."

    play music legacy

    if gender == "male":
        "Judge" "Ulamog-kun and [name_2]-kun!!!"
    elif gender == "female":
        "Judge" "Ulamog-kun and [name_2]-chan!!!"
    else:
        "Judge" "Ulamog-kun and [name_2]-san!!!"

    play sound clapping

    "The crowd bursts into cheers and applause."

    ulamog "We did it! We did it!!"

    "For the event that he organized where the judges didn't even taste the
    food."

    "But that never really mattered."

    "You give Ulamog a {b}chef's kiss{/b}."

    ulamog "Yay!!!"

    jump final_scene

    return

label day4_scene3_kozilek:

    play music school fadeout 2.0 fadein 1.0

    scene bg theater with dissolve

    "You enter the school's theater and spot Kozilek in the wings holding a
    script."

    show kozilek neutral at center with dissolve

    mc "Hey Kozilek-kun."

    if gender == "male":
        kozilek "[name_2]-kun? What're you doing here?"
    elif gender == "female":
        kozilek "[name_2]-chan? What're you doing here?"
    else:
        kozilek "[name_2]-san? What're you doing here?"

    mc "I said I'd come didn't I?"

    kozilek cross "I-- Yeah, you did."

    kozilek neutral "But I didn't think you actually would."

    mc "I'm never one to turn down a challenge."

    "Stage Manager" "ON IN FIVE!!"

    "Student" "Thank you five!"

    kozilek "Oh, I have to go."

    mc "Okay then, \"Break a leg\" is it?"

    kozilek "I don't have legs."

    mc "Tentacle, then."

    stop music fadeout 2.0

    hide kozilek with dissolve

    scene bg theater close with fade

    "The lights dim on the house and the curtains rise."

    show kozilek god at center with dissolve

    "Standing center stage is Kozilek holding a mop to his chin to imitate a
    beard."

    play music jealous fadein 1.0

    "God Himself" "In the beginning, circa 2016, the people of Modern lived in
    relative harmony."

    "God Himself" "Recovering from the recent {b}splinter twin{/b} ban, the
    state of Modern was tumultulous but the future looked bright."

    "God Himself" "Hope was in the air, and a smile touched the face of every
    Modern player in the land."

    "God Himself" "The optimism was even enough to bring a semblence of warmth
    to the cold dead heart of the Grinch of Modern himself, Luis Scott-Vargas."

    "God Himself" "Until one fateful day, on February 7th of 2016. With Pro
    Tour Oath of the Gatewatch on the horizon, tension was thick."

    "God Himself" "There was great pressure for Pro Tour Oath of the Gatewatch
    to succeed."

    "God Himself" "The banning of {b}splinter twin{/b} may have left a sour
    taste in the mouths of Modern players, but that was only more reason for
    the upcoming Pro Tour to succeed."

    "God Himself" "As Modern players from all walks of life converged on
    Atlanta, Georgia and Twitch.tv a {b}titan's presence{/b} could be felt."

    "God Himself" "A {b}hidden horror{/b} was soon to awaken."

    play music hijinks fadeout 2.0 fadein 1.0

    hide kozilek with dissolve

    show eyeOfUgin at center
    show thoughtKnotSeer at far_right
    with dissolve

    "Eye of Ugin" "Ooooo. It is I, {b}Eye of Ugin{/b}."

    "Thought-Knot Seer" "And I, {b}Thought-Knot Seer{/b}."

    "Eye of Ugin" "And we are here to take over Modern."

    show affinity at left with dissolve

    "Affinity" "Stay back foul beasts! Our format diversity shall not be
    {b}corrupt{/b}ed by the likes of you."

    "Thought-Knot Seer" "And who are you to defy us?"

    "Affinity" "I am Affinity, the fastest aggro-combo deck in the format."

    "Affinity" "You are no match for turn 2 {b}cranial plating{/b} on
    {b}ornithopter{/b} for eight damage in the air."

    "Eye of Ugin" "Fool. {b}Eldrazi Temple{/b}, {b}Eldazi Mimic{/b} into
    {b}Eye of Ugin{/b} and {b}Thought-Knot Seer{/b}."

    "Thought-Knot Seer" "Now with {b}Reality Smasher{/b} and Chalice on zero,
    you cannot defeat our value curve."

    "Affinity" "Nooooooooo!"

    play music jealous fadeout 2.0 fadein 1.0

    hide affinity
    hide eyeOfUgin
    hide thoughtKnotSeer
    with dissolve

    show kozilek god at center with dissolve

    "God Himself" "The Eldrazi, both colorless and U/R variants, were
    {b}crush{/b}ing the metagame with their speed and value."

    "God Himself" "By the end of Day 1, they were {b}predict{/b}ed to have a
    near 80\% conversion rate into Day 2."

    "God Himself" "But while the Eldrazi were usurping Modern, an old menace
    was continuing to run rampant around the mythical land of Standard."

    play music hijinks fadeout 2.0 fadein 1.0

    hide kozilek with dissolve

    show magicRD at left
    show rhinos at right
    with dissolve

    "Thirty-four Siege Rhinos in a Trenchcoat" "Hello R&D. Yes, I am a fair and
    balanced Magic: The Gathering card, please print me into Standard."

    "Magic R&D" "Hmmm.. It makes a convincing argument. After all, three
    casting pips makes it difficult to play in just any deck."

    "Thirty-four Siege Rhinos in a Trenchcoat" "Yes, yes it does. Please ignore
    the fact that both fetchlands and tango lands in the same format allow
    4c/5c decks to be played with virtually no drawback."

    "Magic R&D" "Why yes, of course. And surely a fifth point of toughness
    won't do any harm."

    "Thirty-four Siege Rhinos in a Trenchcoat" "No, no of course not. And
    please ignore that five toughness renders both {b}savage knuckleblade{/b}
    and {b}languish{/b} ineffective."

    "Thirty-four Siege Rhinos in a Trenchcoat" "Along with making sure other
    rhinos bounce off each other, turning Standard into a painfully slow
    grindfest."

    "Magic R&D" "Naturally. Oh, and why not add a life drain ETB for good
    measure?"

    "Thirty-four Siege Rhinos in a Trenchcoat" "Splediferous! Now to just
    ignore that life gain and trample make me a powerhouse in all aggressive,
    midrange, and anti-aggro control strategies."

    "Magic R&D" "Perfect. Everything looks set. Welcome to Standard Mr.
    {b}Siege Rhino{/b}."

    show rhinos:
        linear 0.5 center

    show saffronOlive at right with moveinright

    "Saffron Olive" "*sniff*"

    "Saffron Olive" "*snifffffff*"

    "Saffron Olive" "Is that jank I smell?"

    play music jealous fadeout 2.0 fadein 1.0

    hide magicRD
    hide rhinos
    hide saffronOlive
    with dissolve

    show kozilek god at center with dissolve

    "God Himself" "Oath of the Gatewatch was The Rhino's last set in Standard,
    and it soon fell out of Modern fashion as well."

    "God Himself" "Not even thirty-four rhinos were a match for the
    {b}cosmic horror{/b} of the Eldrazi."

    "God Himself" "Going into Day 2 of Pro Tour Oath of the Gatewatch, it was
    just {b}as foretold{/b}. The Eldrazi decks surpassed even the most generous
    of estimates, reaching up to a 90\% conversion rate."

    "God Himself" "And if there as any optimism left, the six Eldrazi decks
    that entered the top eight made sure to {b}extinguish all hope{/b} left."

    "God Himself" "There could be no more {b}stubborn denial{/b}, everybody
    knew. The Eldrazi Winter had begun."

    hide kozilek with dissolve

    show eyeOfUgin at center
    show thoughtKnotSeer at right
    with dissolve

    "Thought-Knot Seer" "OoOooOoOOooooOOo."

    "Eye of Ugin" "{b}Fear{/b} usSssSSsSSSssSs!"

    hide eyeOfUgin
    hide thoughtKnotSeer
    with dissolve

    show kozilek god at center with dissolve

    stop music fadeout 2.0

    "God Himself" "Over the next few months, Modern was a cold and grueling
    place to be. Everywhere one looked, the Eldrazi had a {b}deathgrip{/b} on
    the format."

    "God Himself" "Nearly 40\% of the metagame was comprised of Eldrazi decks."

    "God Himself" "But just when it seemed Modern had reached its
    {b}darkest hour{/b}, the {b}light of hope{/b} rang through the
    {b}darkness{/b}."

    "God Himself" "April 4th, 2016. WoTC makes the greatly {b}anticipate{/b}d
    B&R announcement. Everybody knows what's coming, but the stakes are high
    enough to keep them anxious nonetheless."

    play music legacy_intro fadein 1.0
    queue music legacy

    "God Himself" "But the Gods are merciful and {b}Eye of Ugin{/b} is
    banned bringing The Eldrazi Winter to its {b}fateful end{/b}."

    "Affinity" "Wooooooo!!!"

    "Abzan Company" "Yeaahhhhhh!!"

    "Titanshift" "We are freeeeeeee!!!"

    play sound clapping

    "God Himself" "Cheers sound throughout the land and much celebration is
    had. Nobody is sad to see the Eldrazi go."

    "God Himself" "And thus brings an end to our cautionary tale, informing the
    safety of our beloved format. At least until October 4th, 2019."

    hide kozilek with fade

    "The stage lights dim and when they fade back in the rest of the cast is
    out on the stage taking a bow."

    "The {b}captive audience{/b} stares briefly before breaking out into
    applause."

    play sound clapping

    "After several rounds of bows and hands sore from clapping, the curtains
    finally close and lights come up in the house."

    play music after_school_intro fadeout 2.0 fadein 1.0
    queue music after_school

    show kozilek neutral at center

    kozilek "..."

    mc "Wow Kozilek-kun, you were amazing!"

    mc "God Himself, huh."

    kozilek @ blush "Uhh, yeah. Thank you for coming to see me."

    mc "Of course."

    kozilek blush "Would.. Would you like to maybe.."

    kozilek "Uhh.. Walk around the rest of the {b}festival{/b}.."

    kozilek neutral @ blush "With me?"

    "Oh."

    "Oh my gosh."

    "It's actually happening."

    "This is it."

    "Peak character development."

    "The pinnacle of character writing."

    mc "I would love to."

    jump final_scene

    return

label day4_scene3_emrakul:

    play music school fadeout 2.0 fadein 1.0

    scene bg hall with dissolve

    "You end up wandering the halls looking for somewhere to go."

    "As you walk by a classroom you notice a strange group of students inside."

    "You {b}peek{/b} through the window and see Emrakul among them."

    "Well, it's as good an excuse as any."

    scene bg classroom frontleft with dissolve

    "You enter the classroom and everyone turns to look at you."

    play sound door_open_close

    "As the door closes you hear a distinct click as it locks behind you."

    show emrakul blush at center

    "Well, that's mildly concerning."

    emrakul neutral "It's not concerning at all, come, take a seat."

    "You look around and see that the rest of the students have been bound and
    gagged to their seat."

    "How did you not notice that before? It's moderately concerning."

    emrakul @ scared "Stop saying it's concerning! Just sit down."

    mc "I didn't say anything."

    emrakul point "Oh..."

    "Majorly concerning."

    emrakul neutral @ blush "Here, I have a seat for you!"

    play music hijinks fadeout 2.0 fadein 1.0

    scene bg classroom frontleft
    show emrakul neutral at center
    with hpunch

    "Like a spell with split second, Emrakul shoves a chair underneath you
    before you have a chance to respond."

    "She {b}bind{/b}s your arms to the chair and wraps another strip of cloth
    around your mouth."

    emrakul @ blush "Yay! Another friend!"

    "Emrakul brings out a large duffel bag and starts rummaging through it."

    "She brings out a very tacky anime schoolgirl uniform and turns around to
    look at you and the rest of the students lined up and bound to chairs."

    "Oh no."

    emrakul clothes "Oh yes."

    "It was a mechanically dextrous process and more than likely required a bit
    of eldritch magic, but you and the rest of the students end up in a various
    array of cliche costumes."

    emrakul blush "Fufufufu."

    "You, of course, got the short end of the stick with barely any clothes
    at all."

    "There's probably more rope than clothes touching your body."

    "You bite down on the cloth covering your mouth, Emrakul didn't do a very
    good job of gagging you. It seems like it's more for presentation than
    anything."

    play music dramatic fadeout 2.0 fadein 1.0

    hide emrakul with moveoutleft

    "Emrakul floats over to the other end of the room to god-knows-what."

    "While she's distracted, you whisper to the student next to you."

    mc "Do you know why she's doing this?"

    "Student" "I don't know, she's crazy."

    "Student" "I was supposed to be helping her set up our class' event. She
    never got permission to do anything like this."

    mc "I think that's the least of our problems at the moment."

    mc "Is there any way we could get out of this?"

    "Student" "..."

    mc "Yeah, I suppose I was being too optimistic. She is the most powerful
    being in all the multiverse."

    "Student" "There may be one way..."

    mc "What? You mean fifteen flying squirrels?"

    "Student" "Huh?"

    mc "Oh, nevermind.."

    "Student" "They say there is a forbidden-jutsu that acts as a
    {b}reality anchor{/b} to all otherworldly beings."

    "Student" "If anyone is brave, or stupid, enough to make such a
    {b}dubious challenge{/b} in this forbidden-jutsu, the being must accept the
    conditions."

    mc "And if they fail?"

    "Student" "Then they are banished from reality, never to set foot on the
    material plane again."

    mc "Spooky."

    "Student" "This is serious."

    mc "Yeah, sure. What is this challenge then?"

    "The student leans closer to you and lowers their voice even further."

    "Student" "A best-of-one game of Legacy."

    mc "Okay, I was being sarcastic before, but this isn't even deserving of
    that. A game of Legacy? Who even plays Legacy anymore?"

    "Student" "Exactly, that's why nobody has succeeded this challenge in
    recorded history."

    mc "Well, if it's our only way out."

    "Student" "You're not actually thinking of doing it? I was just trying to
    be cryptic and mysterious."

    mc "Don't you know? I always keep a Legacy deck on me."

    "Student" "I have literally never seen you before."

    mc "Right. Anyways, I just so happen to have a tier 1 Legacy deck right
    here in my pocket."

    "You wiggle your chin until the gag has dropped below your mouth."

    play music hijinks fadeout 2.0 fadein 1.0

    mc "Emrakul! I invoke the forbbiden-jutsu. I challenge you to a game of
    Legacy!"

    show emrakul neutral at center with dissolve

    "Emrakul turns around, her single eye piercing through your mind."

    emrakul blush "Ohohoh. And what is it you desire for this challenge?"

    mc "I want our freedom, and for you to stop being so creepy."

    emrakul wave "Well, by eldritch law I must accept."

    "Emrakul floats over to you and unties you from the chair."

    "She lifts a tentacle to reach into an extra-dimensional pocket in space
    and produces a deckbox."

    "You reach into your normal pocket and pull out a pile of sixty Magic: The
    Gathering trading cards scuffed and worn from being played unsleeved on the
    blacktop during recess."

    stop music fadeout 2.0

    emrakul "Then let's {b}commence the endgame{/b}, high roll?"

    mc "No, low roll. My luck may be an on-fire dumpster but at least I can
    take advantage of that."

    emrakul "Fair enough."

    "Emrakul tosses the d20 across the classroom floor."

    "7."

    "You pick it up and do the same."

    "Natural 1. Just as planned."

    emrakul "Play or draw?"

    mc "I don't answer rhetorical questions."

    "You let Emrakul cut your deck and lay out seven cards before you."

    "As you fan your opening hand in front of you a smile creeps onto your
    face."

    "Your trusty Mono G Burn deck has never failed you, but this is on a whole
    different level. It's the closest statistical probability to a god-hand."

    "A veritable nut-draw."

    "You look up at Emrakul and say the well-practiced word."

    play music legacy_intro fadein 1.0
    queue music legacy

    mc "Keep."

    emrakul cards "Same."

    "You take the initiative and slam a basic {b}Forest{/b} onto the
    battlefield."

    "Then, after establishing your dominance, you look Emrakul in the eye and
    say:"

    mc "Pass."

    "Emrakul draws for turn and drops a basic {b}Wastes{/b} before passing to
    you."

    "Truly powerful magic you are playing."

    "You draw your card, drop a {b}Prismatic Vista{/b} and cast your first
    spell of the game."

    "{b}Wild Cantor{/b}."

    "Incredible, you just played a 1 mana 1/1. Emrakul must be shaking in
    {b}terror{/b}."

    "You pass the turn and Emrakul draws."

    "She plays another basic {b}Wastes{/b} and passes. You wonder what her
    {b}game plan{/b} could be."

    "You draw and drop another {b}Forest{/b}."

    "Now it's time to get into the red zone, you swing all out with your single
    {b}Wild Cantor{/b} and smack Emrakul in the face for a single damage."

    scene bg classroom frontleft
    show emrakul cards at center
    with hpunch

    "First blood, the students begin to murmur. Only turn three and you've
    already dealt a whole damage to your opponent. You're making fantastic
    progress."

    "But it's not over yet.{w} No, not in the least. This is powerful magic
    you're playing."

    "Post-combat main phase, you sacrifice the {b}Wild Cantor{/b} for a green
    mana and tap a {b}Forest{/b}."

    "With two green now floating you cast {b}Channel{/b}, now is when the real
    fun begins."

    "You pay 9 life, then pay another life to fetch a third {b}Forest{/b} from
    your deck with {b}Prismatic Vista{/b} and tap your last two
    {b}Forest{/b}s."

    "With two green and nine colorless floating you cast what could possibly be
    the most powerful card in your deck."

    "{b}Borrowing the East Wind{/b} for X = 9."

    scene bg classroom frontleft
    show emrakul cards at center
    with hpunch

    show emrakul scared at center with Dissolve(0.25)

    "You dome Emrakul in the face for 9 damage, dropping her to 10 life. Sure,
    you may have payed 10 life and also dealt 9 damage to yourself to pull it
    off, but that's just the Mono G Burn way."

    "With Emrakul at half her health and you down to 1/20th your health, you
    pass the turn feeling highly confident in yourself."

    show emrakul cards at center with Dissolve(0.25)

    "Emrakul draws and plays a third {b}Wastes{/b} before passing."

    "Pathetic, you think to yourself, now it's time to show her what real
    magic looks like."

    "You draw and drop a fourth {b}Forest{/b}. With four mana you point an
    {b}Unyaro Bee Sting{/b} at Emrakul."

    "You pass priority and the spell resolves. Emrakul takes 2 more damage
    and drops to 8."

    "Powerful magic, you reassert to yourself."

    "You pass the turn and Emrakul plays a fourth {b}Wastes{/b}. Then, she
    passes the turn back to you."

    show emrakul blush at center with Dissolve(0.25)

    "You're beginning to get nervous. Emrakul hasn't played anything but basic
    lands for the past four turns. What could she have in that hand of hers?"

    show emrakul cards at center with Dissolve(0.25)

    "But it's probably fine, you've already got an overwhelming amount of
    pressure on her with your four mana {b}Shock{/b}s there's no possible
    way she could get out of this."

    "You untap and draw. Then, with your four {b}Forest{/b}s you cast
    {b}Storm Seeker{/b}."

    "Because Emrakul hasn't cast any spells the entire game she's got a full
    grip of cards."

    show emrakul scared at center with Dissolve(0.25)

    "The situation couldn't be more perfect. {b}Storm Seeker{/b} deals a full
    7 damage to Emrakul dropping her to just 1 life."

    show emrakul cards at center with Dissolve(0.25)

    "You pass the turn feeling immensely confident. Emrakul's at 1 life with
    a full hand and you're also at 1 with only two cards in hand, there's no
    conceivable way for her to stabilize from this."

    "Emrakul draws and plays her fifth land, but this time it's not a
    {b}Wastes{/b}. It's a {b}Mountain{b}."

    "Hmmmmm.."

    stop music fadeout 2.0

    show emrakul blush at center with Dissolve(0.25)

    "Then she taps all her lands and casts {b}Through the Breach{/b}."

    "Uh oh."

    "The crowd audibly gasps."

    play music dramatic fadein 1.0

    show emrakul cards at center with Dissolve(0.25)

    "{b}Emrakul, the Aeons Torn{/b} hits the battlefield with haste and attacks
    you, {b}threaten{/b}ing 15 damage to your measly life total of 1."

    "Emrakul (the card, not the player), annihilates your board with her
    trigger and you're left with no board presence."

    "Emrakul passes priority before combat damage, a formality to be sure.
    There's nothing you can do to get out of this."

    stop music fadeout 2.0

    "Or is there.."

    "You look down at the last two cards in your hand, {b}Nourishing Shoal{/b}
    and {b}Autochthon Wurm{/b}."

    "Wait a second..."

    "You've got it!"

    play music legacy fadein 1.0

    "You exile the wurm from your hand to pay the alternate casting cost of
    {b}Nourishing Shoal{/b}, gaining exactly 15 life."

    "You're now sitting at a comfortable 16 life, just enough to survive
    a hit from {b}Emrakul, the Aeons Torn{/b}."

    "Emrakul (card version) slams you in the face for 15 damage, bringing you
    back down to 1."

    "It wasn't pretty, but now you get to live to see another untap."

    stop music fadeout 2.0

    show emrakul point at center with Dissolve(0.25)

    "At the end of turn, Emrakul (card version) shuffles back into Emrakul's
    library."

    play music dramatic fadein 1.0

    show emrakul cards at center with Dissolve(0.25)

    "You untap with zero cards in hand, zero permanents on the battlefield, and
    a life total of 1."

    "You tentatively take the top card of your library, as you turn it over in
    your hand you breathe a sigh of disappointment."

    "{b}Elvish Spirit Guide{/b}."

    "That doesn't help you at all."

    "You're forced to pass the turn as Emrakul untaps with all her lands and
    six cards in hand."

    show emrakul blush at center with Dissolve(0.25)

    "She makes only one play on her turn. A {b}Memnite{/b}, just enough
    power to kill you on her next turn.{w} Thank God it has summoning sickness,
    now you have one final chance to turn this game around."

    show emrakul cards at center with Dissolve(0.25)

    "You make it to what could be your last untap step, sadly untapping zero
    permanents.{w} You stare at the faded back of the Magic: The Gathering card
    resting face down on the top of your library.{w} You {b}hope against
    hope{/b} for anything that could save you this turn."

    "Both you and Emrakul are at 1 life, and Emrakul has lethal on board.
    You're not sure what could save you right now, much less that it's even
    in your deck."

    "But this is Mono G Burn, and it's never failed you yet."

    play music emotional fadeout 2.0 fadein 1.0

    "You turn your head to look at the row of students bound to their chairs.
    All their hope is pinned on you and this card you're about to draw."

    "You pass priority to Emrakul on your upkeep."

    "She passes back."

    "Now it's your draw step. You rest your hand on top of your library,
    preparing to reveal the card when you feel something inside you."

    "A newfound feeling of hope and {b}vigor{/b}. You feel a sudden {b}rush of
    vitality{/b}."

    "What is this feeling?{w} But you already know,{w} it's the heart of the
    cards."

    "You let your faith do the work, believing in the heart of the cards you
    flip the top card of your library."

    stop music fadeout 2.0

    "The stray murmurs among the captives suddenly {b}silence{/b}."

    "It's a miracle."

    "No, not the mechanic miracle. A literal miracle."

    "You look down at the face up card now over the battlefield."

    play music legacy_intro fadein 1.0
    queue music legacy

    "It's a {b}Hornet Sting{/b}."

    "You exile the {b}Elvish Spirit Guide{/b} from your hand and cast the
    {b}Hornet Sting{/b}."

    play sound clapping

    "{b}The crowd goes wild{/b}. Muffled cheers erupt from behind gags and
    the sound of chair legs hitting the floor as the students rock back and
    forth."

    emrakul scared "I-I just wanted to *hic* h-have a harem of anime
    schoolgirls."

    "Emrakul mumbles into the floor."

    "You stand up and begin untying the rest of the students from their
    respective chairs."

    "You're not really sure what to say to Emrakul."

    "But thankfully that burden is lifted as a teacher walks through the door."

    stop music
    stop sound

    "Teacher" "What the fuck?"

    mc "Uhhhhhhhhhhhhhhhhhhhhhhh."

    hide emrakul with dissolve

    scene bg hall with dissolve

    "You walk out of the classroom. The rest of the students can explain what
    happened, or at least try to."

    play music school fadein 1.0

    "You think you've had enough existing for today. It's time to go home and
    {b}sleep{/b} so you no longer need to see, think, or feel."

    "Yes, yes that sounds quite nice."

    "You already had your attendance recorded anyways, you don't need to be
    at school for the rest of the day."

    jump final_scene

    return

label day4_scene3_nissa:

    play music school fadeout 2.0 fadein 1.0

    scene bg tea room with dissolve

    "You enter Nissa's classroom to see that it's be {b}refurbish{/b}ed into
    a traditional tea room."

    show nissa neutral at Position(xalign = 0.6)
    show chandra neutral at left
    with dissolve

    "Chandra and Nissa are there along with a few other students."

    if gender == "male":
        nissa @ smile "Oh, hi [name_1]-kun."
    elif gender == "female":
        nissa @ smile "Oh, hi [name_1]-chan."
    else:
        nissa @ smile "Oh, hi [name_1]-san."

    mc "Hello."

    chandra "Hey hey."

    mc "So where's this tea I've been promised?"

    nissa excited "Follow me."

    scene bg tea room with dissolve

    show nissa neutral at Position(xalign = 0.6) with dissolve

    "Nissa escorts you to the front of the room and hands you a cup of hot
    water."

    show nissa smile at Position(xalign = 0.6) with Dissolve(0.25)

    "You exchange silent bows and Nissa leads you through the motions of the
    ceremony."

    show nissa neutral at Position(xalign = 0.6) with Dissolve(0.25)

    show nissa:
        linear 1.0 xalign 1.2

    "You start near the front of the room with the water basin."

    "As you're {b}purify{/b}ing yourself in the water basin, you hear a loud
    {b}crash{/b} from the entrance behind you."

    play sound explosion

    scene bg tea room
    show nissa horrified at Position(xalign = 1.2)
    with hpunch

    show yargle neutral at center with hpunch

    play music synth fadeout 2.0 fadein 1.0

    yargle "YARGLE'S COME TO BARGLE!"

    show nissa uncomfortable at Position(xalign = 1.2)
    show chandra neutral at left
    with hpunch

    chandra "Yooo! Yargle! You made it!"

    yargle "Yargle always arrives fashionably late."

    chandra "Please, help us Yargle. This tea party is so boring without you.
    We need your partying expertise."

    yargle "Do not fret, Yargle knows exactly what this party needs."

    play sound clapping

    show yargle cool at center with hpunch

    "Student 1" "Yeah Yargle!"

    "Student 2" "I love you Yargle!!"

    nissa distracted "Ummm.. Hi Yargle."

    yargle "Nissaaaaa! What's crackin'? This is a killer tea party Nissa."

    nissa smile "Oh, uh. Thank you Yargle-san."

    nissa distracted "Yargle-san, you're so cool. Why did you choose our tea
    ceremony?"

    yargle "Nissa, Nissa, Nissa. This lack of confidence thing is really
    killing the vibe at this party."

    yargle "I want you to repeat after me."

    yargle "I am the best. My tea party is the best."

    nissa uncomfortable "Uhhhh...{w} I am the best.."

    yargle "Go on."

    nissa "My tea party is the best."

    yargle "My tea party slays. I can do anything."

    nissa "My tea party slays. I can do anything?"

    yargle "It's not a question. It's an affirmation."

    yargle "I am the tea. I can kill God."

    nissa @ horrified "Wait, what?"

    yargle "Repeat it Nissa."

    nissa distracted "I-I am the tea. I can... I can kill God."

    yargle "Yell it Nissa! Yell it!"

    nissa excited "I am tea incarnate. I will kill God!!"

    yargle "Yes Nissa!! The world is your teacup. Make God kneel before you!"

    yargle "Yeahhhhhhh!!!!!"

    show nissa neutral at Position(xalign = 1.2) with dissolve

    "Yargle shouts and gets {b}absorb{/b}ed into the noticably larger crowd in
    the back."

    play music emotional fadeout 2.0 fadein 1.0

    hide yargle with dissolve

    show nissa:
        linear 1.0 right

    chandra mischief "You could definitely kill God Revane-chan."

    nissa @ distracted "Uhhhh.. Thank you?"

    chandra shrug "You're quite welcome."

    chandra neutral "So, are you liking your tea party so far?"

    nissa distracted "Tea ceremony."

    chandra @ shrug "Whatever."

    nissa neutral "It's... Not what I expected."

    chandra shrug "Yargle often exceeds expectations, it's true."

    nissa distracted "Why did you do this, Nalaar-san?"

    chandra neutral "Do what?"

    nissa "I mean.."

    "Nissa gestures around her."

    nissa "This."

    nissa "You're not even in my class, why did you go through so much trouble
    to help with this."

    chandra "I really didn't do anything, you did all this yourself."

    nissa "No, you organized everything, and gathered all the supplies, and
    summoned Yargle."

    if gender == "male":
        nissa "You just pretended to slack off in front of [name_1]-kun
        because.."
    elif gender == "female":
        nissa "You just pretended to slack off in front of [name_1]-chan
        because.."
    else:
        nissa "You just pretended to slack off in front of [name_1]-san
        because.."

    nissa smile "Well, I don't really know why."

    nissa neutral "But you definitely did most of the work."

    chandra shrug "Oop. I guess I did. Oh well."

    nissa distracted "You still haven't answered the question."

    chandra intrigue "Isn't it obvious Revane-chan?"

    chandra shrug "I like you."

    nissa "You like me?"

    chandra unamused "Yes."

    nissa blush "Like, like like me?"

    chandra neutral "Yes, I do."

    nissa excited "Really?"

    stop music

    chandra notc "No."

    nissa uncomfortable "Huh?"

    chandra "No, I don't like you Revane-san."

    chandra "I'm only interested in decidedly-male Gideon."

    nissa "What?"

    mc "Ayo, you good Nalaar-san?"

    play music synth fadein 1.0

    show yargle neutral at center

    yargle "Do I smell corporate diversity retconning?"

    mc "Oh gosh, yes. Please help us Yargle!{w} They're trying to retcon
    Chandra into being straight."

    yargle "Well we can't have that now, can we."

    yargle "This calls for an {b}urgent exorcism{/b}. We must flush the evil
    NotC spirits from her body."

    nissa "What's going on?"

    yargle cool "Fear not dear Nissa, you shall have your happy ending. Quick,
    get the Twitter Cancel threats ready!"

    nissa "The what?"

    mc "I got it Yargle!"

    "You pull out your mobile device and start preparing to Twitter Cancel
    Wizards of the Coast."

    "Your fingers fly across the screen, spewing out tweet after tweet."

    yargle neutral "Nissa, I need you to hold Chandra down while I prepare the
    {b}forbidden ritual{/b}."

    nissa horrified "Wait, why is it forbidden!?"

    yargle "There's no time for plot exposition, just hold on to Chandra!"

    nissa uncomfortable "Okay okay!"

    show nissa:
        linear 0.5 xalign -0.3

    show yargle:
        linear 0.5 xalign 1.0

    "Nissa grabs Chandra and holds her in place."

    "You tweet your final cancellation threat and go to help Nissa as well."

    "Yargle begins to chant in an ancient language."

    "As the ritual begins Chandra starts to rise into the air, her irises blank
    until her eyes are pools of blinding white void."

    "You and Nissa struggle to pull her down, within range of the ritual."

    play music dramatic fadeout 2.0 fadein 1.0

    "Yargle's chanting grows louder, the music stops and the rest of the
    students turn to watch."

    "The chanting crescendos and Chandra's body starts to spasm in the air."

    "Nissa hugs her as you try to keep her appendages in place."

    "You notice a wispy figure start to emerge from Chandra body in the
    distinct shape of Nic Kelman."

    "The crowd waits in bated breath, another ghost gets exorcized from
    Chandra, this time in the shape of Greg Weisman."

    "Yargle's chanting stops and he turn to the crowd."

    yargle "The ritual is almost complete."

    yargle "It just needs one more thing."

    yargle "For everybody in this room to raise a hearty middle finger at these
    malicious spirits!!"

    play sound clapping

    "The crowd cheers and everyone raises their hands to flip off the
    malevolent ghosts of queerbaiting writers.{w} (and questionable amounts of
    pedophilia from one of them, but that has less evidence)"

    "Nic Kelman and Greg Weisman begin to writhe and squirm in the space above
    Chandra."

    "Their incorporeal forms shift and stretch, their mouths agape in silent
    screams."

    "Some of the students raise a second middle finger to speed up the
    process."

    "And before long, the ghosts have popped out of existence. Banished to The
    Shadow Realm."

    "The force keeping Chandra afloat {b}dispel{/b}s, and she drops into
    Nissa's arms."

    play sound clapping

    hide chandra with dissolve

    play music synth fadeout 2.0 fadein 1.0

    show yargle cool at Position(xalign = 1.0) with Dissolve(0.25)

    "{b}The crowd goes wild{/b} with screams of joy."

    "Chandra's eyes {b}flicker{/b} open to see Nissa above her."

    show chandra neutral at Position(xalign = 0.25) with dissolve

    nissa distracted "I-I--"

    "Nissa stumbles over her words before Chandra interrupts her by grabbing
    her neck."

    play music emotional fadeout 2.0 fadein 1.0

    nissa blush "..."

    "They share {b}true love's kiss{/b} with Nissa's eyes still wide open."

    yargle "Well, it looks like Yargle's Bargled today quite well."

    yargle "You can thank me later."

    hide yargle with dissolve

    "He vanishes in a {b}smoke shroud{/b}."

    jump final_scene

    return

label final_scene:

    stop music fadeout 2.0

    "And they all lived {b}happily ever after{/b}."

    "THE END."

    jump credits

    return

label credits:

    play music "audio/menu.ogg" fadein 1.0

    $ credits_speed = 50
    scene black
    show credits_image at Move((0.5, 1.0), (0.5, -4.0), credits_speed,
                  xanchor=0.5, yanchor=0)
    with Pause(credits_speed+10)

    return
