define nissa = Character("Nissa")
define chandra = Character("Chandra")
define sorin = Character("Sorin")
define nahiri = Character("Nahiri")
define ulamog = Character("Ulamog")
define kozilek = Character("Kozilek")
define emrakul = Character("Emrakul")

# credit house of imagi studio

# and add
# “[Eldrazi Dating Sim] is unofficial Fan Content permitted under the Fan
# Content Policy. Not approved/endorsed by Wizards. Portions of the materials
# used are property of Wizards of the Coast. ©Wizards of the Coast LLC.”

python:
    name_1 = "mc1"
    name_2 = "mc2"
    gender = "non-binary"

    # flags
    date_1 = ""
    date_2 = ""
    date_3 = ""

    emrakul_date_1 = ""

label start:

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

    scene bg bedroom

    "Wednesday"

    "Wednesdays are the worst"

    "Yes, even worse than Mondays"

    "Because Wednesdays reside right in the middle of the week"

    "The day when all your energy from the weekend has been depleted"

    "And unlike Thursdays when you can tell yourself \"There's only one day
    left to go\""

    "Wednesdays are only halfway through the week. Which means there's still a
    whole other half of a week left to endure"

    mc "*sigh*"

    "You woke up early today"

    "Not by choice you grumble to yourself"

    "The birds outside have reached the concerted decision that today is
    the perfect day to screech louder than a harpy clawing its way up from the
    ninth circle of hell"

    "And at 6:00 in the morning no less"

    "A rather unfortunate situation, you think to yourself"

    "And although this would be a problem on any day of the week, today is a
    Wednesday"

    "And Wednesdays suck"

    "Well, since you're up this early. You might as well try getting some
    homework done"

    mc "Hehe"

    "That was a funny joke"

    "Well, okay. It wasn't that funny"

    "You mostly laughed to be facetious, hiding your problems under a thin
    veneer of light-hearted charm"

    "To avoid the mountain of stress that would come crashing down were you
    to actually acknowledge your problems as being legitimate sources of
    stress in your life"

    "It's not a very effective coping mechanism considering you've already
    started trying to meta-cognitively justify why you can't avoid problems
    in this manner"

    "Whatever, the point is you're not doing any homework this morning"

    "You've already exhausted all you mental energy explaining to yourself
    why you're not doing homework. Leaving no energy remaining to actually do
    said homework"

    "Oh well. After a feat of mental gymnastics that would leave an olympic
    judge with their jaw on the floor, it's almost already 6:30"

    "You suppose it's time to start getting ready for school"

    "You grab your backpack off the floor and a protein bar from the pantry
    which will need to suffice as your breakfast for the day"

    "You grab your keys and stare at the front door, preparing to mentally
    disassociate yourself from reality for the next eight or so hours"

    scene bg street with dissolve

    show nissa at left

    if gender == "male":
        nissa "[name_1]-kun!!"
    elif gender == "female":
        nissa "[name_1]-chan!!"
    else:
        nissa "[name_1]-san!!"

    nissa "You're early today! Eheheh"

    "Oh... Right. You almost forgot"

    "Well, actually.. You did forget. But you'd feel bad admitting that, so
    to keep your fragile moral conscious intact you'll leave it at 'almost
    forgot'"

    "That's Nissa. She's your neighbor and childhood friend"

    "You've known each other basically since you were born due to the
    inherently entropic nature of early developmental friendships predicated
    almost entirely on geography and familial connections"

    "It's hard to imagine you becoming friends in any other situation. Y'know,
    the kind of person you seem to associate with purely out of circumstance"

    "Not that you're complaining, she's super nice and always finds ways to
    make your life..."

    "Well... Interesting, to say the least"

    "Normally she's the one to wake you up. But as both of you noticed, that
    didn't happen today"

    show nissa:
        left
        linear 1.0 xpos 1.0

    "Without waiting for your response, Nissa grabs your arm and starts
    dragging you down the steps of your porch"

    "She never did harbor any patience for your internal monologues"

    nissa "C'mon! Let's go~"

    "It's only 6:45, at this rate you'll arrive at school way too early"

    scene bg park with moveinleft

    "Nissa's hand begins to swing your arm back and forth as you slow to a
    normal pace"

    "She begins to talk at you, but you're not really paying attention"

    "You free your arm from her {i}binding grasp{/i} and return your hands to
    your pockets"

    "The trees are in {i}lush growth{/i} and the flowers in {i}vernal bloom{/i}
    despite it being late October"

    "And yet it still feels cold and dreary as the {i}autumnal gloom{/i} lurks
    beneath the {i}veil of summer{/i}"

    "Nissa's going on about the Mul Daya and being generally low-key kinda
    racist"

    "But her words pass through your mind as the {i}creeping chill{/i} of
    the upcoming day of school fills you with {i}dread{/i}"

    scene bg schoolgrounds with dissolve

    "You arrive at school with nearly half and hour to spare"

    "Nissa leaves to get to her class, as you should probably be doing too"

    jump day1_scene2

    return

label day1_scene2:

    scene bg classroom backleft with dissolve

    "The abysmal mundanity of school makes its cycle, taking with it eight
    more hours of your fleeting existence"

    "The day seems to have passed by in {i}slow motion{/i}"

    "At the very least you were able to {i}recover{/i} some of your lost
    {i}sleep{/i}"

    "You feel marginally {i}revitalize{/i}d. Well, as much as one can after
    falling unconscious against a $5 IKEA chair with the spinal posture of a
    scoliotic shrimp performing pilates"

    "By the time you acknowledge your situation, the classroom is already
    empty"

    "You curse your internal monologue for keeping you longer than absolutely
    necessary and make your way to the classroom door"

    show nissa at center

    if gender == "male":
        nissa "[name_1]-kun!!"
    elif gender == "female":
        nissa "[name_1]-chan!!"
    else:
        nissa "[name_1]-san!!"

    nissa "You're late, eheheh. I caught you this time"

    mc "How did you know I'd stay late?"

    nissa "I didn't. I do this every day, but this time you're the last one
    here. I guess today's my luck day~"

    "Gee. She does this every day? And you never knew. Now you feel like
    the asshole"

    nissa "C'mon! C'mon! Let's go"

    "Nissa pulls at your arm with a playful smile on her face"

    mc "Go where?"

    nissa "We're planning our class' event for the school {i}festival{/i}"

    "That's right.. Nissa's the class president this year"

    "Also the school {i}festival{/i} is coming up... Apparently"

    "You probably slept through that part"

    "You were never really one to partake in school events"

    "You vaguely {i}recall{/i} Nissa's {i}relentless assault{/i} of invitations
    to previous school {i}festival{/i}s and events"

    "Well, actually. You remember them quite {i}clear{/i}ly. You've just
    selectively ignored those {i}agonizing memories{/i} to avoid the
    {i}burden of guilt{/i} you'd feel for systematically declining them"

    "And look where that's gotten you. Staring down the exact thing you've been
    trying to avoid while actively feeling guilty about trying to avoid it"

    if gender == "male":
        nissa "[name_1]-kun?"
    elif gender == "female":
        nissa "[name_1]-chan?"
    else:
        nissa "[name_1]-san?"

    "{i}Damn{/i}. You really need to keep your internal monologues in check"

    "Well, you're already feeling guilty for avoiding her invitations. So it
    looks like there's no way out of this one"

    mc "Sure, sounds good"

    "You give the most half-assed response despite your heart's best
    intentions"

    nissa "Yay!! C'mon c'mon!"

    "But Nissa's jubilant reaction shows no sign of disappointment"

    "You don't deserve her"

    scene bg hall with dissolve

    "Nissa drags you out into the hallway"

    mc "So where exactly are we going?"

    nissa "The library!"

    "The library? Only nerds and blue players hang out at the library"

    "Although that's a bit redundant considering the venn diagram between
    nerds and blue players is literally just a circle"

    "You {i}opt{/i} not to say that out loud however"

    jump day1_scene3

    return

label day1_scene3:

    scene bg library 3 with dissolve

    "You arrive at the library with Nissa"

    "You can't believe you're wasting your valuable free time at school"

    "Free time, whose entire definition is predicated on not being at school"

    "And yet, here you are. At school"

    "And in the library no less"

    show nissa at right

    if gender == "male":
        nissa "Over here [name_1]-kun!"
    elif gender == "female":
        nissa "Over here [name_1]-chan!"
    else:
        nissa "Over here [name_1]-san!"

    scene bg library 2 with dissolve

    "Nissa waves you over to a corner of the library"

    "There are a few others sitting around a table, presumably other class
    presidents"

    "What are you doing here again?"

    show nissa:
        right
        linear 0.2 left

    show ulamog at Position(xpos = 0.3)
    show kozilek at Position(xpos = 0.6)
    show chandra at right

    nissa "Hi hi everyone! Sorry I'm late"

    nissa "This is my friend [name_2]-san"

    mc "Uh.. Hi guys"

    if gender == "male":
        ulamog "Hi [name_2]-kun!!"
    elif gender == "female":
        ulamog "Hi [name_2]-chan!!"
    else:
        ulamog "Hi [name_2]-san!!"

    ulamog "I'm Ulamog! Nice to meet you"

    "The tall figure greets you with a smile. Its legs are made of tentacles
    and its arms split at the elbows to form two sets of forearms.
    Thick grey {i}carapace{/i} potrudes from exposed muscle and sinew creating
    bone-like patterns along the reddish surface"

    kozilek "... Hey.."

    show ulamog:
        xpos 0.3
        linear 0.2 xpos 0.5

    ulamog "Kozi-kun! You have to be nicer than that"

    kozilek "..."

    kozilek "Hi.. I'm Kozilek"

    ulamog "Mmmmm hehehe~"

    "The other Eldrazi, apparently named Kozilek, is more reluctant to greet
    you but does so nonetheless"

    emrakul "Emrakul.. Fufufu"

    show ulamog:
        xpos 0.5
        linear 0.2 xpos 0.3

    chandra "Yo"

    chandra "Chandra Nalaar"

    "The remainder of the, presumably, class presidents greet you as you
    take a seat"

    "You feel an {i}uncomfortable chill{/i} as the realization sets in"

    "You are sitting in a room with three--"

    "Hot"

    "Sexy"

    "Romantically avaliable"

    "Lovecraftian Eldritch {i}Abomination{/i}s"

    "Oh, and there's like a hot red head chick too.. But, like, yea.. Eldrazi"

    "It's a precarious situation to be in. Will you be able to win the hearts
    of one of these Eldrazi?"

    "It's often cited that the perils of high school romance are much akin to
    bringing Ladies Looking Left tribal to cEDH night"

    "Well, actually.. No, nobody says that. But it certainly seems that way"

    "Maybe if you play your cards correctly (pun most definitely intended)
    you'll reach {i}semester's end{/i} one Eldrazi happier than you started"

    "Nissa begins the meeting, discussing various plans for the upcoming school
    {i}festival{/i}. Her words pass through your mind and {i}leave no trace{/i}"

    "You become {i}lost in thought{/i} as your mind wanders off"

    "It's a Herculean task not fantasizing about the three Eldrazi sitting in
    front of you"

    "But this isn't Theros, and your {i}iron will{/i} eventually {i}crumble{/i}s
    as you {i}succumb to temptation{/i}"

    "Maybe you shouldn't've read all those tentacle doujinshi. You're starting
    to recognize them {i}exert influence{/i} over the direction of your
    fantasies"

    "But your erotic daydreaming is cut short by a sudden
    {i}burning inquiry{/i}: Why tentacles of all things?"

    "It's seems quite arbitrary to have gained such footing in popular media"

    "And to only add to your frustration, it's not exactly helping to have
    three very sexually arousing tentacle monsters sitting across the table"

    emrakul "Actually tentacles became so ubiquitous in Japanese pornography
    as a way to circumvent {i}censorship{/i} laws at the time"

    "Wait"

    emrakul "During the allied forces occupation of Japan during World War II
    they believed Japan's sexual culture to be the cause of their belligerent
    and aggressive behavior"

    "Huh?"

    emrakul "They thusly implemented a ban on most forms of porn, the strictest
    of which being on male genitalia"

    emrakul "In response, one animator in particular started using tentacles
    instead for their phallic nature and ability to show angles that would
    normally be obstructed by a human body"

    "What is going on?"

    emrakul "They argued this did not violate the {i}censorship{/i} laws at the
    time due to it being mostly suggestive in nature"

    emrakul "This form of {i}censorship{/i} evasion became wildly popular. And
    as a result, much of modern hentai still depicts tentacles despite the
    relevant {i}censorship{/i} laws having been {i}repeal{i}ed years ago"

    "Did you say all that out loud?"

    "You thought you had your monologing problem resolved"

    "You haven't needed to see a therapist in years. Is this a relapse?"

    "No, it couldn't be. You're confident you didn't say all that embarrasing
    tentacle stuff out loud"

    "Then what could have prompted Emrakul's sudden regurgitation of obscure
    hentai knowledge?"

    nissa "Umm..."

    nissa "Emrakul-chan?"

    emrakul "Umm... Oh, sorry"

    emrakul "I just thought-- Because [name_2]-san.."

    emrakul "Nevermind.. I'm sorry"

    chandra "No, wait. Please, tell me more"

    nissa "Oh, no. It's okay, um.. Let's just try to focus, okay?"

    "What just happened? You can't seem to wrap your head around it"

    "Possibly because your mind's only fixation for the past half-hour has been
    on the idea of being tied up and groped as Emrakul's slimy appendages
    invade your every orifice in an erotic {i}crush of tentacles{/i}"

    "But also maybe because... Well no, that was probably the reason"

    "You emerge from your mind's enclosure of fantasy in an effort to
    pay attention to the conversation happening around you"

    "Or whatever {i}shambling remains{/i} of a conversation there is, as any
    semblence of rational thought appears to have been catastrophically
    derailed hours ago"

    ulamog "Nico nico ni!"

    ulamog "Nico nico ni!"

    ulamog "Nico nico--"

    kozilek "Ulamog! Shut the FUCK up before I NICO NICO break your KNEECAPS!!"

    ulamog "..."

    ulamog "WAAAAAAAHH!! Kozi-kun, you're so mean!"

    "Despite their previous exclamation, Ulamog takes Kozilek in their arms
    and squeezes them while still wailing"

    kozilek "..."

    kozilek "Okay okay.. Sorry"

    ulamog "Awwwww. It's okay Kozi-kun"

    "Maybe it's time you go back to daydreaming"

    "Kozilek frees himself from Ulamog's grip and ever so slightly scoots his
    chair way. Not enough to be outside Ulamog's melee range, but enough to
    signal Kozilek's discomfort"

    "\"Like swinging with a {i}Birds of Paradise{/i}\" you think to yourself.
    It's not about the damage, it's about sending a message"

    "But that message is obviously not received as Ulamog simply latches back
    on to Kozilek"

    kozilek "Ugh. Don't you have homework to do or something?"

    ulamog "I was doing homework, but I drew all over it, now I can't read
    any of my work"

    "Both you and Kozilek look down, and sure enough Ulamog's notebook is
    covered in doodles of pies, chains, and hospitals"

    "An interesting assortment of drawings, but you don't question it"

    kozilek "Well that's your fault, so don't go asking me for help"

    ulamog "Waaa!? Kozi-kun please, just one question"

    kozilek "Hmph, fine. But you have to stop hugging me"

    ulamog "Yay! Okay. What's the derivative of pi?"

    kozilek "Huh?"

    ulamog "What's the derivative of pie?"

    kozilek "But pi's just a constant"

    ulamog "Mmmm. Constantly delicious"

    kozilek "..."

    "Yep. Definitely time to go back to daydreaming"

    nissa "Okay! Umm.. Everyone. I think that wraps up today's meeting"

    nissa "Thank you for sharing your ideas, umm.. We'll meet up again
    tomorrow"

    "Nissa's closure isn't exactly the most elegant you've ever heard"

    "If you might so boldly proclaim, it likely wasn't the second most elegant
    either"

    "Now that you're thinking about it... Yes, you're positive. That was the
    least elegant closure you've ever heard"

    "But that wouldn't be a very kind sentiment to audibly express"

    "In fact, considering today's events, you probably shouldn't even be
    thinking it"

    "Since Nissa's still in the room"

    "Only Nissa, actually, it seems everybody left during yet another one of
    your seemingly {i}time warp{/i}ing internal monologues"

    if gender == "male":
        nissa "C'mon [name_1]-kun"
    elif gender == "female":
        nissa "C'mon [name_1]-chan"
    else:
        nissa "C'mon [name_1]-san"

    mc "Hm?"

    nissa "Let's walk home together"

    mc "Oh, yeah. Sure"

    "The {i}crippling fatigue{/i} of the day washes over you and you're too
    tired to say no. Not that you could've said 'no' to Nissa even if you
    had the energy"

    "Regardless of the reason, you agree to Nissa's proposal and follow her
    out of the library"

    jump day1_scene4

    return

label day1_scene4:

    scene bg park with dissolve

    "You and Nissa tread down the {i}homeward path{/i}"

    "While you walk to school every day, Nissa is very involved with
    extra curriculars and after school activites, so you seldom walk back
    from school with her"

    "Maybe it's the break from routine. Maybe it's the guilt for
    ignoring her entire meeting. But you find yourself actually paying
    attention to Nissa for once"

    show nissa at center

    if gender == "male":
        nissa "So, [name_1]-kun? How do you think the {i}festival{/i} will
        turn out this year?"
    elif gender == "female":
        nissa "So, [name_1]-chan? How do you think the {i}festival{/i} will
        turn out this year?"
    else:
        nissa "So, [name_1]-san? How do you think the {i}festival{/i} will
        turn out this year?"

    "Heck. It is entirely your own fault that you aren't able to genuinely
    engage with this question"

    "It was you and your infinite hubris that lead you down the path of
    tentacle fantasies rather than responsible social awareness"

    "But an answer you must give, and you wouldn't want to disappoint Nissa
    any further than you surely already have"

    mc "Oh, great. Sounds like it'll be a blast"

    "Not the answer she deserves, but the best you can give"

    nissa "Oh yay! I'm glad you think so"

    nissa "Who's ideas did you like the most?"

    "Oh boy, okay. Considerably easier. You are an expert when it comes to
    multiple choice"

    "You have a 25 percent success rate. Which is a significant step up from
    your usual 4 percent on short answer questions"

    "But you're getting ahead of yourself. Right now you just need to pick an
    answer"

    menu:
        "Who's ideas did you like the most"

        "Ulamog":
            mc "I thought Ulamog's ideas were pretty neat"

            nissa "Ooo! Yeah, Ulamog's a lot of fun"

            nissa "He's quite ambitious, but I think we can make it work"
        "Kozilek":
            mc "I really liked Kozilek's ideas"

            nissa "Ahh. Heh, yeah. He's normally so shy, it's surprising to see
            him suggest something so out of his comfort zone"

            nissa "It might be difficult, maybe you can help him organize it
            all"

            mc "Um.. Yeah... Maybe"
        "Emrakul":
            mc "I thought Emrakul's ideas were really good"

            nissa "Oh, umm.. Yeah. that's..."

            nissa "That's fine I guess.. I just mean, I just don't think a
            hentai curation booth would be very school appropriate"

            nissa "But I mean. If both of you really wanted it, maybe we could
            find a compromise"

            mc "..."
        "Chandra":
            mc "I thought Chandra's ideas were the best"

            nissa "What? Silly, Chandra didn't propose anything. She's not
            even a class president"

            mc "Oh, umm.. Wait, why was she even there then?"

            nissa "Uhh.. She kind of forced herself in"

            nissa "Well.. I mean, I didn't say no or anything but..."

    scene bg street with dissolve

    nissa "Oh, well looks like this is our neighborhood"

    nissa "I'll see you tomorrow!"

    "You both say your goodbyes as you head toward your separate homes"

    jump day2_scene1

    return

label day2_scene1:

    scene bg bedroom with fade

    "Thursday"

    "Thursdays are fine you suppose"

    "Not a lot of people seem to appreciate Thursdays"

    "They're not great, mind you"

    "But you still maintain that Thursdays are criminally underrated"

    scene bg street with dissolve

    show nissa at center

    if gender == "male":
        nissa "C'mon [name_1]-kun, we're gonna be late"
    elif gender == "female":
        nissa "C'mon [name_1]-chan, we're gonna be late"
    else:
        nissa "C'mon [name_1]-san, we're gonna be late"

    mc "Yes yes, I'm coming"

    jump day2_scene2

    return

label day2_scene2:

    scene bg classroom backleft with dissolve

    "You cast a {i}baleful stare{/i} on the clock at the front of the
    classroom"

    "Conveniently located just around eye level of the teacher such that upon
    a cursory glance you appear to be paying attention"

    "The clock ticks towards the final bell. But each tick seems to be longer
    than the last"

    "{i}Time stretch{/i}es out as the gap between you and freedom grows
    exponentially larger"

    "Like watching a storm player pop off, but not being able to concede
    because \"BuT tHeY cOUlD fiZzLe!!1!\""

    "Like \"No Theo, you just flashbacked {i}past in flames{/i} after milling
    over half your deck with {i}traumatize{/i}. I'm not watching you play
    solitaire in the time it could take me to get a college level education
    in Zimbabwe\""

    "..."

    "Umm..."

    "It seems the bell has already rung"

    "Students around you are packing up and preparing to leave"

    "You don't have anything to {i}put away{/i} considering you didn't take any
    notes or even remotely engage with the class on any level"

    "So you just take you bag and walk out the door"

    scene bg hall with dissolve

    "You are free"

    "The next sixteen hours are yours to command"

    "You could go to {i}study hall{/i}"

    "Play video games"

    "Join the {i}cult of the waxing moon{/i} and {i}devour flesh{i} and
    {i}innocent blood{/i} as you {i}descend upon the sinful{/i}"

    "So many options, you buzz with excitement and the {i}thrill of
    possibilities{i}"

    "As you exit the classroom, you {i}enter the infinite{/i}"

    "But before you can further contemplate your situation, a string of
    {i}nagging thoughts{/i} overtake your mind"

    "Nissa's planning committee is meeting again today. She'd surely be
    disappointed if you didn't come back"

    "You can think of a million reasons to not go to the library right now. And
    you can think of only one reason you should"

    "But the {i}crooked scales{/i} of 'The Big Horny' leave each side
    looking just as enticing as the other"

    jump day2_scene3

    return

label day2_scene3:

    scene bg library 3 with dissolve

    "You end up walking through the library doors. Nissa and the rest are
    already seated at their usual table"

    scene bg library 2 with dissolve

    show nissa at left

    "You walk over a take a seat with them"

    if gender == "male":
        nissa "Oh, [name_1]-kun, you actually came"
    elif gender == "female":
        nissa "Oh, [name_1]-chan, you actually came"
    else:
        nissa "Oh, [name_1]-san, you actually came"

    mc "Oh, was I not expected?"

    nissa "No! No, that's great. I'm happy you made it"

    nissa "Umm.. I guess let's get started then"

    nissa "We can start working on the projects we came up with yesterday"

    nissa "Umm... Yeah, so just start planning I think. If you need help umm,
    just ask I guess"

    "Nissa simply exudes confidence. A {i}radiant fountain{/i} of self-esteem
    for all to behold. She has nearly as much confidence as you have sarcasm,
    and that's saying something"

    if gender == "male":
        nissa "Oh, hey [name_1]-kun"
    elif gender == "female":
        nissa "Oh, hey [name_1]-chan"
    else:
        nissa "Oh, hey [name_1]-san"

    nissa "I guess you wouldn't have much to do here huh"

    nissa "Sorry I dragged you into this, but I feel better when you're around
    so thanks for coming ehheh"

    nissa "If you'd like, you can help any of the other presidents with their
    class activities. I'm sure they'd love your help, but I don't mean to
    pressure you any further"

    mc "No no, no worries. I'll stick around a while longer. Thanks Nissa-chan"

    nissa "Okay! Cool"

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

    show ulamog at center

    mc "Hey Ulamog"

    if gender == "male":
        ulamog "Hi [name_2]-kun!!"
    elif gender == "female":
        ulamog "Hi [name_2]-chan!!"
    else:
        ulamog "Hi [name_2]-san!!"

    ulamog "Would you like to help with my class' activiy?"

    mc "I'd love to. What is it you're planning?"

    ulamog "Well, I was thinking we could host a baking competition like you
    see on TV"

    mc "Oh my, that's quite ambitious of you"

    ulamog "Oh? Do you think it's too much?"

    mc "No, no. It's just that, well.. The school {i}festival{/i}s have all
    been pretty.. Uuh. Crappy. So it's just surprising to see you doing
    something so elaborate"

    ulamog "Oh. Well I just think it'd be a lot of fun! And I'm willing to
    put in the work to make it happen"

    mc "Wow that's great. So where are you starting?"

    ulamog "Ummm... Well, that's the thing. I have no idea where to start"

    mc "Oh, well. The contestants will need to be baking, right? So you could
    start with whatever is needed to bake"

    ulamog "Yeah, that's good. Uhhh.. Like, ingredients?"

    mc "Ingredients, a kitchen, probably tools"

    ulamog "Oh! Maybe we can borrow the school's kitchen"

    mc "I think that might be your only option, but how would you go about
    doing that?"

    ulamog "I'll just go up and ask!"

    mc "Just go up and ask?"

    "But Ulamog has already stood up and is dashing out of the library"

    mc "Huh.."

    "You suppose you might as well follow. It could be interesting"

    scene bg hall with dissolve

    "Ulamog makes an {i}expedite{/i}d pace down the hall with a skip in their step"

    "Well, not a literal skip as they have tentacles in place of legs, but a
    metaphorical skip"

    "Ulamog turns the corner to the principal's office and you hear the door
    {i}crack open{/i}. What you don't hear is any knock or indication of
    Ulamog's entrance"

    "You round the corner yourself and see Ulamog standing outside the office"

    show ulamog at center

    ulamog "They said yes!!"

    mc "Wait. Didn't you just enter that door?"

    ulamog "Yes. And I asked, and they said yes!"

    mc "That took like 6 seconds"

    ulamog "Talking is a free action"

    mc "..."

    mc "What?"

    ulamog "Uhh.. Wrong game, nevermind. C'mon let's go!"

    show ulamog:
        center
        linear 0.5 xpos 1.0

    "Ulamog runs past you back toward the library"

    "You stand {i}stun{/i}ned, {i}bound in silence{/i}"

    "Maybe it's best not to {i}dwell on the past{/i}, you turn around and
    start walking back as well"

    scene bg library 3 with dissolve

    show nissa at left
    show ulamog at center

    nissa "Oh, there you are. Where did you two go?"

    ulamog "We got a kitchen!!"

    nissa "You got a kitchen?"

    mc "I am just as {i}bewilder{/i}ed as you are"

    mc "No, actually. Probably a bit more"

    ulamog "Now we just need to get dough and flour and baking soda..."

    "Ulamog starts to ramble off ingredients as he moves toward his usual spot
    at the back of the library"

    show ulamog:
        center
        linear 0.5 xpos 1.0

    nissa "So umm... I see it went well"

    mc "As well as one might expect I suppose"

    ulamog "... And parchment paper and rollers and trays..."

    nissa "Well, I'm glad you two are getting along"

    mc "Yeah, I guess that just--"

    show ulamog:
        xpos 1.0
        linear 0.25 center

    ulamog "YOINK!!"

    show ulamog:
        center
        linear 0.25 xpos 1.0

    show bg library 3 with moveinright

    show ulamog at center

    "And with that, Ulamog grabs your arm and pulls you toward the tables in
    the back"

    "You spend the rest of the time ironing out details with Ulamog as you
    craft your {i}brilliant plan{/i}"

    python:
        date_1 = "ulamog"

    jump day2_scene5

    return

label day2_scene4_kozilek:

    "You spot Kozilek reading in the corner of the library sitting up against a
    bookshelf"

    scene bg library 1 with dissolve

    show kozilek at center

    "You wander over and take a seat next to him"

    "As you sit down Kozilek glances up at you"

    "But when your eyes meet he quickly averts his {i}otherworldly gaze{/i}
    back down to his book"

    mc "So... \"Kozi-kun\" huh?"

    kozilek "Don't call me that"

    mc "Hmm.. \"Kozilek-tan\" then?"

    kozilek "..."

    "Kozilek moves their body to {i}turn against{/i} you, but in doing so
    pushes himself closer to you"

    mc "Alright alright, message received. \"Kozilek-kun\" then"

    mc "Shouldn't you be preparing your class' event?"

    kozilek "What does it look like I'm doing?"

    "You lean over Kozilek's shoulder to get a better glimpse of what he's
    reading"

    mc "They ran their slimy tentacles across my body, the black {i}void{/i}
    of their eyes looking deeply in--"

    # book slam sound

    kozilek "NOTHING!!"

    "They slam the book shut before you can read any further"

    kozilek "It's research obviously, ugh. You are such a {i}nuisance
    engine{/i}. Don't you have anything better to do!?"

    mc "Well, I thought I could help you organize and plan..."

    mc "But it looks like you've got everything sorted out"

    "You stand up"

    kozilek "Wait no!"

    kozilek "I mean.. I do have everything sorted but.. You don't need to
    leave"

    mc "You want me to stay?"

    kozilek "Yes!"

    kozilek "No!"

    kozilek "Umm... I mean you..."

    "Kozilek finishes the rest of their sentence in an incomprehensible mumble"

    mc "Pardon me, could you repeat that?"

    kozilek "Ugh, just stay.."

    mc "Apologies, a bit louder this time?"

    kozilek "Okay fine!! Just stay idiot!"

    mc "Very well"

    "You find your seat back on the floor and lean up against the bookshelf
    next to Kozilek"

    kozilek "I'm not reading this because I like it or anything, just saying"

    mc "Hm? I didn't think you were"

    kozilek "Oh.. Yeah, well I'm just letting you know. It really is for
    research"

    mc "I believe you"

    kozilek "I thought our class could perform a short play for the
    {i}festival{/i} based on a historical event"

    mc "Quite a realistic endeavor"

    kozilek "So I needed to do some research to make sure our representation
    was historically accurate"

    mc "That's a very reasonable assessement of the situation"

    kozilek "STOP DOING THAT!!"

    mc "Doing what?"

    kozilek "That!"

    kozilek "You keep agreeing with me!"

    mc "You want me to disagree with you?"

    kozilek "NO!"

    kozilek "I mean.. But you don't need to be so nonchalant about it"

    mc "You want me to agree with you enthusiastically?"

    kozilek "Ugh, nevermind! Just stop talking"

    mc "..."

    "You hold out a thumbs-up to signal your understanding"

    kozilek "..."

    "The next several minutes pass in awkward silence"

    "Well, awkward for Kozilek, you're more just amused"

    "Kozilek tries pretending to read his book but it's obvious he's just
    uncomfortably ignoring you"

    "His eyes flick back and forth between you and the open book, never
    stopping to scan the words or flip the page"

    "After an {i}hour of eternity{/i}--or well, more like four minutes--Kozilek
    slams the book shut for the second time today and gets up"

    kozilek "Ugh! Why do you have to make it so awkward!?"

    mc "Awkward? I'm not doing anything"

    kozilek "Exactly!"

    "Kozilek aggressively shoves the book into his bag and gets up"

    mc "You're done reading?"

    kozilek "Whatever, I don't need more research anyway"

    mc "Alright, good for you"

    kozilek "I'm going to go draft the script now"

    mc "Enjoy"

    show kozilek:
        center
        linear 0.5 xpos 1.0

    show kozilek:
        xpos 1.0
        linear 0.5 right

    kozilek "Aren't you going to come with me?"

    mc "Oh, did you want me to?"

    kozilek "Yes. No! I mean..."

    kozilek "I don't really care. You can come if you want to"

    "Well that's awfully kind of you"

    scene bg library 3 with dissolve

    show kozilek at center

    "You follow Kozilek back to the tables as he sits down with blank lined
    paper"

    mc "I should ask, as I never did find out. What is it exactly your play
    is about?"

    kozilek "It's about the Eldrazi Winter, not like you would understand"

    mc "No, I suppose not. After all, it's not like I wasn't living under
    a rock during 2016"

    kozilek "No, you weren't. So just don't bother alright?"

    mc "Mhm"

    "There were too many negative comparatives for you to process in that
    interaction"

    "You could probably figure out what Kozilek meant. But the warranty on your
    braincell has already expired, so it might be a bad idea to stress it too
    much"

    "You pass the rest of the time in relative comfort as Kozilek makes a crude
    attempt to {i}reconstruct history{/i}"

    "With you correcting him on several key details"

    python:
        date_1 = "kozilek"

    jump day2_scene5

    return

label day2_scene4_emrakul:

    show emrakul at center

    mc "Uhhh.. Emrakul, right?"

    "But Emrakul doesn't reply. Instead, she looks up at you and raises a
    tentacle in greeting"

    "Or, at least, you think she looks at you. The massive eye in the center
    of Emrakul's body seems to pierce your very soul"

    mc "What're you working on?"

    "You take a seat next to Emrakul and look down to see a mildly concerning
    amount of pornographic light novels spread out across the floor"

    mc "Ummm..."

    "Emrakul doesn't seem to notice your {i}falter{/i}, she just looks down and
    idly moves the hentai comics around with her tentacle"

    mc "Maybe I should leave..?"

    emrakul "I think you'd look good in this one"

    "Emrakul holds up a comic to reveal a suggestively posed human clad
    in what barely qualifies as clothing"

    menu:
        "Compliment her back":
            "Without a second thought to your social setting, or a first regard
            to what card game you're playing, you flick your wrist and down
            your sleeve flies your trusty old UNO reverse card"

            "You twist your fingers to let the metaphorical ace up your sleeve
            face Emrakul"

            "You mutter the {i}magic word{/i}s \"Go fish\" and prepare to banish
            her to the shadow realm"

            "Then, with a fervent {i}display of dominance{/i}, you thrust the
            UNO reverse card in Emrakul's face and scream"

            mc "NO U!!"

            mc "You would look far better in that attire than myself"

            python:
                emrakul_date_1 = "compliment"
        "Sit in awkward silence":
            "You look at the near-naked human drawn in the comic, then back at
            Emrakul"

            "Then back at the drawing, all the while maintaining the most
            uncomfortable aura between you and Emrakul"

            "She seems to get the message as she lowers the comic and turns
            away from you"

            python:
                emrakul_date_1 = "silence"
        "Run out of the library screaming":
            "It's a {i}rouse{/i}, you can smell it"

            "Emrakul is trying to seduce you, but you won't fall for it"

            "You will not be tempted by her {i}captivating glance{/i}"

            "Bitches are temporary, the sigma grindset is eternal"

            "You prepare to {i}declare dominance{/i} by sprinting out of the
            library screaming at the top of your lungs"

            "But just as you stand up to T-Pose, Chandra and Nissa walk up
            behind you"

            python:
                emrakul_date_1 = "scream"

    show nissa at left
    show chandra at right

    nissa "Hey guys, what's going on over here?"

    chandra "Quite the cultured collection you've got, respect"

    nissa "EEEEEEEEEEEEK!!"

    "It seems Nissa too, fell victim to the classic blunder: looking down"

    nissa "E-Emrakul-chan, I told you yesterday that this isn't appropriate for
    a school event"

    chandra "You said nothing of the sort"

    nissa "I had meant to, b-but I shouldn't need to!"

    nissa "Emrakul-chan, can you please just put these away for now"

    "Nissa looks away and gestures a sweeping motion toward the floor covered
    in disproportionate drawings of naked humans"

    chandra "Now hold on a minute. I think this is exactly what our school
    {i}festival{/i} needs this year"

    "Chandra leans over and takes a comic to {i}select for inspection{/i}"

    "Nissa averts her eyes as Chandra gives the hentai a {i}careful study{/i}"

    "After few too many seconds of {i}silence{/i} Chandra nods in impressed
    approval and tosses the comic back on the floor"

    chandra "Why don't we let these two carry on with their endeavors"

    show chandra:
        right
        linear 1.0 xpos 0.25

    "Chandra turns Nissa around and walks her away from the scene"

    chandra "And we'll worry about your own event"

    show nissa:
        left
        linear 1.0 xpos -1.0

    show chandra:
        xpos 0.25
        linear 1. xpos -1.0

    if emrakul_date_1 == "compliment":
        mc "Huh"

        mc "Well"

        "You return the UNO card to your sleeve, having served its purpose"
    elif emrakul_date_1 == "silence":
        mc "Huh"
    elif emrakul_date_1 == "scream":
        mc "Huh"

        mc "Well"

        "You sit back down, the threat to your sigma ways having
        {i}dissipate{/i}d"

    mc "Are you uhh.. Sure you should be doing this?"

    emrakul "I think it's fine"

    mc "Remind me again. What is it you're doing exactly?"

    emrakul "Mmmmmm..."

    "Emrakul gestures to the ungodly quantity of porn strewn across the
    floor"

    mc "Ah, I see"

    "You do not see"

    mc "Well then, is there any way I can help?"

    emrakul "Fufufufufu"

    mc "Oh, wonderful"

    "Not wonderful"

    show emrakul:
        center
        linear 0.5 xpos 1.0

    show emrakul:
        xpos 1.0
        linear 0.5 center

    "Emrakul floats over to the tables and returns with a set of..."

    "Technically clothes, in the same way {i}mind rot{/i} is technically
    draw because it's card advantage"

    "Which is to say, it's not draw at all"

    "And similarly, what Emrakul's holding in her tentacles aren't really
    clothes at all"

    "You recognize them from the hentai drawing she just showed you"

    mc "Uhhh, wait.. Is that?"

    mc "Why do you have that!?"

    emrakul "Fufufu. Put it on"

    mc "You brought that to school?"

    emrakul "Just put it on!"

    "She extends a tentacle for you to grab the questionable attire"

    "You reach your hand out and grab the clothes"

    mc "I'm not putting this on in a public library"

    emrakul "B-b-but"

    emrakul "Pleeeeaaase"

    "Emrakul's one eye scrunches up in the most pitiful manner"

    "Gosh, how can you say no to that?"

    "Well, you can think of many ways to say no"

    mc "Fine, I'll do it"

    "..."

    "Why did you say yes?"

    emrakul "Yay~"

    mc "Uhh..."

    scene bg library 2 with dissolve

    "You wander around the library, the {i}shock{/i} of the entire situation
    still setting in"

    show nissa at left

    if gender == "male":
        nissa "Oh, uhh.. What're you doin' [name_1]-kun?"
    elif gender == "female":
        nissa "Oh, uhh.. What're you doin' [name_1]-chan?"
    else:
        nissa "Oh, uhh.. What're you doin' [name_1]-san?"

    mc "I.. Uh..."

    "Nissa glances down at your hands"

    nissa "..."

    nissa "Do I umm.."

    "Umm.. Need to end the meeting today?"

    mc "..."

    nissa "So umm... Hey guys!"

    show ulamog:
        xpos 1.0
        linear 0.25 center

    show kozilek:
        xpos 1.0
        linear 0.25 xpos 0.6

    show emrakul:
        xpos 1.0
        linear 0.25 xpos 0.8

    nissa "I think we should stop here for today, you've all done great work"

    ulamog "Awwwww, but it's only been an hour, the library doesn't close until
    18:00"

    nissa "Oh, well uh.. The library was reserved today. By another club, so
    we need to clean up before they get here"

    ulamog "Awww"

    kozilek "Hmphf"

    show ulamog:
        center
        linear 0.25 xpos 1.0

    show kozilek:
        xpos 0.6
        linear 0.25 1.0

    show emrakul:
        xpos 0.8
        linear 0.25 1.0

    "The rest shuffle out of the library leaving you, Nissa, and dubious set of
    clothes in your arms"

    scene bg hallway with dissolve

    show nissa at center

    nissa "So I'll uh.. See you tomorrow?"

    mc "Yeah yeah, that uh.. Sounds about right, sure"

    python:
        date_1 = "emrakul"

    jump day3_scene1

    return

label day2_scene4_nissa:

    show nissa at center

    if gender == "male":
        nissa "Oh, [name_1]-kun"
    elif gender == "female":
        nissa "Oh, [name_1]-chan"
    else:
        nissa "Oh, [name_1]-san"

    show chandra at left

    chandra "Hey hey"

    nissa "We were just discussing our plans for our class' activity"

    chandra "We absolutely were not. In fact, we were discussing about the
    farthest thing from {i}festival{/i} activities"

    nissa "Well, that's what we should've been discussing"

    chandra "Well it's too late for that. We're not changing the subject
    until we finish this discussion"

    mc "Am I interrupting something?"

    chandra "Yeah, just our conversation about chameleons. Sit down"

    mc "Umm.. Chameleons?"

    chandra "Well I had brought up to her that the fact we know
    chameleons even exist means they suck at their job"

    chandra "But Revane-chan, for some god-forsaken reason, knows that
    chameleons actually change color as a means of communication rather than
    camoflauge"

    chandra "Sexual communication, she made that part quite explicit"

    nissa "Well, when you put it like that..."

    chandra "Which of course, like any respectable pursuers of science, left us
    {i}wonder{/i}ing which color means \"I want to fuck\""

    nissa "Only you wanted to know that"

    chandra "I think it's green, she thinks it's red"

    nissa "I didn't say anything about that"

    chandra "You very distinctly and coherently mumbled the words
    \"No, it'd  be red\" into your chest after I said \"Definitely green\""

    nissa "..."

    if gender == "male":
        chandra "Anyways, [name_2]-kun, this is a question of utmost
        importance. You must be our tie-breaker, you must deliver the
        {i}supreme verdict{/i}"
    elif gender == "female":
        chandra "Anyways, [name_2]-chan, this is a question of utmost
        importance. You must be our tie-breaker, you must deliver the
        {i}supreme verdict{/i}"
    else:
        chandra "Anyways, [name_2]-san, this is a question of utmost
        importance. You must be our tie-breaker, you must deliver the
        {i}supreme verdict{/i}"

    "What color best represents the ever-expanding complexities of sexual
    arousal?"

    menu:

        "Which color means \"I want to bang\"?"

        "White":
            mc "Well, I think white is pretty sexy"

            chandra "..."

            nissa "..."

            mc "What?"

            chandra "Contrary to mainstream media, having an opinion is a
            privilege, not a right"

            chandra "And right now you are very close to losing that
            {i}priveleged position{/i}"

            mc "Uhhh.. Okay?"

            chandra "I'm glad you understand. Now please, take a seat. Your
            mother and I need to have a serious talk with you"

            "Chandra attempts her best Dad-voice and places her hand on top
            of Nissa's"

            "Nissa looks away, but doesn't move her hand"

            "You take take a seat, like a child about to be disciplined"

            mc "Look, if this is about the children in the basement, I already
            said I'm sorry"

            if gender == "male":
                chandra "No [name_2]-kun, I couldn't give a {i}tarmogoyf{/i}'s
                toughness about your \"collection\""
            elif gender == "female":
                chandra "No [name_2]-chan, I couldn't give a {i}tarmogoyf{/i}'s
                toughness about your \"collection\""
            else:
                chandra "No [name_2]-san, I couldn't give a {i}tarmogoyf{/i}'s
                toughness about your \"collection\""

            chandra "We need to address your attitude towards the color pie"

            mc "But Dad! All colors are equal"

            chandra "That is NOT how I raised you!"

            chandra "Green must be able to do everything the other colors can,
            but better. That way it's balanced!"

            mc "But what about color diversity!?"

            chandra "After all this time? You're still spouting that
            \"Balanced Design\" {i}conspiracy{/i} nonsense"

            chandra "That's it, go to your room!"

            mc "But--"

            chandra "One more word and I replace your modern deck with seventy
            five {i}colossal dreadmaw{/i}s"

            mc "..."

            nissa "What is  h a p p e n i n g ?"
        "Blue":
            mc "I think it'd probably have to be blue"

            chandra "Blue!? Excuse you! Only incels and legacy players get
            horny at the sight of blue"

            chandra "..."

            chandra "Oh, wait. Unless you play merfolk.."

            chandra "Do you play merfolk?"

            mc "Uhh...."

            if gender == "male":
                chandra "Answer the question [name_2]-kun"
            elif gender == "female":
                chandra "Answer the question [name_2]-chan"
            else:
                chandra "Answer the question [name_2]-san"

            chandra "Do you play merfolk?"

            mc "I play Mono U Tron, does that count?"

            chandra "..."

            chandra "....."

            "Chandra stares at you with {i}harsh scrutiny{/i}, the weight
            of her judgment pressing down on you"

            chandra "........."

            chandra "Acceptable"

            if gender == "male":
                chandra "But you are {i}on thin ice{/i} [name_2]-kun"
            elif gender == "female":
                chandra "But you are {i}on thin ice{/i} [name_2]-chan"
            else:
                chandra "But you are {i}on thin ice{/i} [name_2]-san"

            nissa "I am so  c o n f u s e d"
        "Black":
            mc "Oh, black for sure. no contest"

            chandra "You do realize there's more to Magic than
            {i}thoughtseize{/i} and {i}Liliana of the Veil{/i}"

            mc "Like {i}leyline of the void{/i}?"

            chandra "No, that doesn't count"

            mc "What about {i}fatal push{/i}?"

            chandra "One more black card out of your mouth and I'll
            {i}fatal push{/i} you out this window"

            mc "You wouldn't {i}defenestrate{/i} me on the second story now
            would you?"

            chandra "Alright, that's it"

            nissa "What is  h a p p e n i n g ?"
        "Red":
            mc "Well red's pretty sexy I guess"

            chandra "What!? Who looks at red and thinks \"Yeah, I'd fuck
            that\"?"

            nissa "I think red's a very romantic color"

            chandra "Pffft, romantic? Sex isn't romantic"

            chandra "You think chameleons like romance?"

            nissa "Well I don't know.. I just like the color red"

            chandra "Heh, do you think I'm romantic then?"

            "Chandra gestures to her body clad in various shades of red"

            "Dyed red leather armor under a vibrant red breastplate and a red
            cloak pinned to her waist"

            "Even her hair is known to burst into flames on occasion. All
            making for a very striking image"

            nissa "Um.. Well, you look very..."

            "Nissa mumbles the rest of her sentence down into her chest"

            "And although her expression is hidden, you wouldn't be surprised
            if she was also turning quite red"
        "Green":
            mc "Well, I think green's pretty sexy"

            chandra "Ahhh, finally!"

            chandra "See! I told you, green is the universal color of sex"

            chandra "Even chameleons understand that the power of horny eclipse
            all language barriers"

            chandra "Not like red"

            chandra "Red's for
            {i}burning cinder fury of crimson chaos fire{/i}!! Not sex"

            nissa "I just thought red looked romantic.."

            chandra "Well you're objectively, scientifically, empirically
            wrong"

            nissa "Uhhh.. Okay"
        "Colorless":
            "Maybe answering \"Colorless\" to a question that expects a color
            as an answer isn't the smartest play"

            "But considering you can count the number of braincells you have
            on one hand, maybe logic and reason aren't the most effective
            decision-making tools at your disposal"

            mc "Oh, colorless is definitely the sexiest"

            chandra "..."

            chandra "I bet you're one of those people who think Caw-Blade was
            a {i}Storm Crow{/i} tribal deck with equipment"

            mc "Wait, Caw-Blade wa-"

            chandra "Yes?"

            mc "... Nevermind"

            chandra "Good"

            chandra "I'm glad I didn't need to bring out the
            {i}ankle shanker{/i}, slash your Achilles tendons"

            mc "Hey, my Achilles tendons have nothing to do with this, you
            leave them out of it!"

            if gender == "male":
                chandra "Sorry [name_2]-kun, that's just business"
            elif gender == "female":
                chandra "Sorry [name_2]-chan, that's just business"
            else:
                chandra "Sorry [name_2]-san, that's just business"

            chandra "It's a {i}cruel reality{/i}"

            nissa "What the  h e c k"

    chandra "So anyways, did you have plan for your class' event Revane-chan?"

    nissa "Uhhhh..."

    "The sudden change in subject doesn't seem to help Nissa's {i}increasing
    confusion{/i}"

    "But she {i}rebound{/i}s surprisingly quickly and moves on"

    nissa "Oh, I uhh.. Was thinking of hosting a tea ceremony"

    nissa "There's a classroom with tatami we could borrow and--"

    chandra "Nah, that's boring, your class should host a {i}death match{/i} in
    the courtyard. {i}Last one standing{/i} gets free college admittance"

    nissa "Oh my gosh, no! We aren't going to have a freaking {i}fight to the
    death{/i} in the middle of school"

    mc "Oh oh, how about ceremonial human {i}sacrifice{/i} to the {i}Lord of
    Extinction{/i}?"

    chandra "My, well aren't you just a {i}well of ideas{/i}. What a splendid
    suggestion"

    mc "Happy to be of service"

    nissa "No! No sacrifices to the extinction lord whoever thing"

    mc "How about the {i}Lord of the Forsaken{/i}?"

    chandra "Or the {i}Lord of the Void{/i}?"

    mc "Or {i}Lord of the Pit{/i}"

    chandra "You've got plenty of options"

    nissa "Why are there so many lords?"

    mc "That's not even half of them"

    nissa "Okay okay, stop. I shouldn't've asked"

    chandra "You definitely shouldn't've"

    nissa "We're not doing that. There will be no killing or death during the
    {i}festival{/i}"

    if gender == "male":
        chandra "Well [name_2]-kun, how does it feel to have
        {i}death denied{/i}?"
    elif gender == "female":
        chandra "Well [name_2]-chan, how does it feel to have
        {i}death denied{/i}?"
    else:
        chandra "Well [name_2]-san, how does it feel to have
        {i}death denied{/i}?"

    mc "Not great, I won't lie. It's a bit of a {i}crushing disappointment{/i}"

    chandra "Understandable. Oh well, there's always next year right?"

    mc "That's the spirit"

    nissa "Can we please get back on topic?"

    chandra "Right right, of course. Where were we? Tea ceremony, no death"

    mc "I can't even {i}poison the cup{i}s?"

    chandra "I would argue that matcha is already poison, but no, no poisoning
    the drinks unfortunately"

    mc "This is a tragedy, I suppose I'll have to settle for spiking them with
    ketamine"

    nissa "No spiking the drinks either"

    mc "Not even Mexican black-tar heroin?"

    "Nissa plants her face in her hands and leans over the table"

    nissa "I just wanted to plan our class' event"

    chandra "Ooooo, I think we broke her"

    mc "Okay okay, sorry. I'll stop"

    "You and Chandra try to refrain from any more {i}murder{/i} jokes as Nissa
    starts actually planning her event"

    "The rest of the time passes in relative tedium as productivity often
    scales inversely with fun"

    "But by the end Nissa seems to be proud of what she's accomplished, not
    that you really payed attention"

    "It was mostly Chandra helping her while you watched and occasionally
    interjected with meaningless comments"

    show bg hall with dissolve

    show nissa at center

    if gender == "male":
        nissa "Hey [name_1]-kun"
    elif gender == "female":
        nissa "Hey [name_1]-chan"
    else:
        nissa "Hey [name_1]-san"

    nissa "Walk home with me?"

    mc "Certainly"

    show bg park with dissolve

    "You and Nissa make the typical {i}harrowing journey{/i} out of school
    and down the path toward your respective homes"

    "Nissa is unusually quite the entire time, like she's {i}ponder{/i}ing
    something important"

    nissa "..."

    if gender == "male":
        nissa "Hey [name_1]-kun?"
    elif gender == "female":
        nissa "Hey [name_1]-chan?"
    else:
        nissa "Hey [name_1]-san?"

    mc "Yeah?"

    nissa "..."

    nissa "Do you like Nalaar-san?"

    mc "..."

    mc "You think I like her?"

    nissa "Well, I dunno. That's why I'm asking"

    mc "She likes you"

    nissa "Huh?"

    mc "You seriously haven't noticed?"

    mc "She takes every opportunity to be near you"

    mc "She's not even a class president, why do you think she hangs out at
    the library?"

    nissa "Because she wants to be involved with school spirit?"

    mc "It's because of you"

    show bg street with dissolve

    mc "Well, anyways. I'll let you have your crisis in {i}solitude{/i}, This
    is my house"

    nissa "... Oh uhh.. Okay, bye then"

    mc "Bye"

    python:
        date_1 = "nissa"

    jump day3_scene1

    return

label day2_scene5:

    show bg hall with dissolve

    show nissa at center

    if gender == "male":
        nissa "[name_1]-kun!"
    elif gender == "female":
        nissa "[name_1]-chan!"
    else:
        nissa "[name_1]-san!"

    mc "Hey Nissa-chan"

    nissa "I saw you helping today, you looked like you were having fun"

    mc "Yeah, I guess you could say that"

    nissa "Anyways, walk home with me?"

    mc "Always"

    show bg park with dissolve

    "You and Nissa make the typical {i}harrowing journey{/i} out of school
    and down the path toward your respective homes"

    "Nissa is unusually quite the entire time, like she's {i}ponder{/i}ing
    something important"

    nissa "..."

    if gender == "male":
        nissa "Hey [name_1]-kun?"
    elif gender == "female":
        nissa "Hey [name_1]-chan?"
    else:
        nissa "Hey [name_1]-san?"

    mc "Yeah?"

    nissa "..."

    if date_1 == "ulamog":
        nissa "Do you like Ulamog-kun?"
    elif date_1 == "kozilek":
        nissa "Do you like Kozilek-kun?"

    mc "Yeah, I do"

    nissa "No, I meant like, likelike--"

    mc "I know what you meant"

    nissa "Oh"

    if date_1 == "ulamog":
        nissa "Hehe, that give me cavities"

        mc "Cavities?"

        nissa "Because it's so sweet~"

        nissa "I think you and Ulamog-kun would be very sweet together"
    elif date_1 == "kozilek":
        nissa "Haha, that sounds like fun"

        nissa "Uhh, I just mean. You two might have a fun time courting each
        other"

        mc "Courting?"

        nissa "Well, if he comes off as abrasive at first don't be too
        discouraged"

    mc "Uhh, okay. I will keep it in mind, thank you"

    show bg street with dissolve

    nissa "Well, looks like we split here. I'll see you tomorrow!"

    mc "Bye.."

    jump day3_scene1

    return

label day3_scene1:

    scene bg bedroom with dissolve

    "Fridays are overrated"

    "Yeah, it's true"

    "People don't seem to understand that Fridays are still an entire day of
    work"

    "You still need to go to school for the same amount of time as any other
    weekday"

    "Now, don't get it wrong, Fridays are still great. After all, unlike other
    weekdays, there's no homework because it's all been pushed back to Sunday"

    "But despite this, Fridays are still massively overvalued"

    jump day3_scene2

    return

label day3_scene2:

    scene bg classroom backleft with dissolve

    "The teacher stands up begins their lesson on some highly empirical math
    concept"

    "Immediately, it feels like a {i}winter orb{/i} hit the battlefield and
    nobody has artifact removal"

    "You're trying to follow along, or at least look like you are, but you
    don't understand a thing"

    "You don't even recognize half the {i}unspeakable symbol{/i}s on the
    whiteboard"

    "And why are there letters? In fact, there are more letters than there are
    numbers. You thought this was math, not English"

    "The {i}journey to eternity{/i} begins as you trudge your way through the
    group slug of public education"

    scene bg hall with dissolve

    "Class ends, leaving you with just enough {i}stamina{/i} to survive a trip
    to the library"

    "And so that's exactly what you end up doing"

    jump day3_scene3

    return

label day3_scene3:

    scene bg library 3 with dissolve

    "You spot the usual suspects just where they're expected and head over to
    them"

    scene bg library 2 with dissolve

    show nissa at left

    show ulamog at center

    show kozilek at right

    nissa "Well, the {i}festival{/i} starts on Monday so today's our last day
    get everything together unless we want to be working over the weekend"

    nissa "I guess we can get started then. Is everybody here?"

    "You look around the library. And count: 1, 2 humanoids; and 1, 2 eldrazi.
    Hmmmm.. Upon closer inspection there seems to be a distinct lack of
    Emrakul in the room"

    ulamog "Oh no!! We're missing Emmy-chan!"

    "Yes, keen observation Ulamog"

    nissa "That's strange, she's never late. Where could she be?"

    scene bg library 2 with hpunch

    emrakul "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

    "Suddenly, a {i}resounding scream{/i} rings out from the hallway outside
    the library"

    nissa "What was that? It sounded like Emrakul-chan"

    show ulamog:
        center
        linear 0.25 right

    show kozilek:
        right
        linear 0.25 xpos 0.6

    "Ulamog runs over to the windows"

    ulamog "Emmy-chan!!"

    emrakul "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

    "Another shrill screech of pure, unadulterated {i}terror{/i} pierces the
    hallways"

    "That's strange"

    "What could possibly scare the most powerful being in all the multiverse?"

    "{i}Emrakul, the Aeons Torn{/i}, master of time and space"

    "Who bends the {i}field of reality{/i} at a whim"

    emrakul "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

    "What deeply unfathomable {i}twisted abomination{/i}?"

    "What unspeakable {i}horror of horrors{/i} could elicit such a {i}shriek
    of dread{/i} from {i}Emrakul, the Promised End{/i}?"

    emrakul "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

    emrakul "FIFTEEN FLYING SQUIRRELS!!!!"

    "..."

    "Oh.."

    "Yes, you suppose a massive flying {i}squirrel mob{/i} would be
    understandably scary"

    "But somehow you still feel an inkling of disillusionment"

    show kozilek:
        xpos 0.6
        linear 0.25 xpos 1.0

    show nissa:
        left
        linear 0.25 xpos 0.25

    show chandra at left

    show emrakul at center

    emrakul "HEELLLLPP!"

    "Emrakul bursts through the library doors with, indeed, fifteen flying
    squirrels behind her"

    "Everybody else stares blankly as the squirrels mindlessly flap around the
    room"

    nissa "Ummmm.."

    chandra "Maybe we should.. Deal with that..?"

    "A quick {i}blazing volley{/i} from Chandra {i}incinerate{/i}s the
    squirrels and Emrakul breathes an audible sigh of relief"

    show chandra:
        left
        linear 0.5 xpos -0.5

    show emrakul:
        center
        linear 0.5 xpos 1.0

    show ulamog:
        right
        linear 0.5 xpos 1.0

    nissa "So..."

    nissa "Everybody's here"

    nissa "I guess we should get started.."

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

    "You wander over to Ulamog who's scribbling down on a sheet of paper"

    show ulamog at center

    "Just as you approach him, he stands up"

    if gender == "male":
        ulamog "Oh. Hi [name_2]-kun"
    elif gender == "female":
        ulamog "Oh. Hi [name_2]-chan"
    else:
        ulamog "Oh. Hi [name_2]-san"

    ulamog "I was just about to go {i}hunt down{/i} all the stuff I need"

    ulamog "Come with me!"

    mc "Sure"

    scene bg hall with dissolve

    if date_1 == "ulamog":
        mc "So baking huh. What's it you're looking for then?"

        ulamog "Well, I was gonna check the kitchen we borrowed for all the
        tools and ingredients we need"

        mc "Sounds like a plan"
    else:
        mc "So what're you planning for your event?"

        ulamog "We're going to host a baking contest"

        ulamog "So I was gonna check the school kitchen for all the tools and
        ingredients we need"

        mc "Oh my, well that sounds ambitious"

        ulamog "It sounds fun!"

    scene bg kitchen with dissolve

    "You and Ulamog arrive at the kitchen you'll be using"

    "It's significantly more impressive than you expected from this school"

    ulamog "Alright, so we just need to clean it and make sure it has all the
    supplies"

    show ulamog:
        center
        linear 2.0 xpos 2.0

    scene bg kitchen with dissolve

    show ulamog at center

    ulamog "Ooooo! It looks so professional"

    ulamog "I'm so excited! I can't wait to cook in here!"

    show ulamog:
        center
        linear 0.25 left

    "Ulamog scurries around the room, opening every cabinet and drawer like
    a {i}rummaging goblin{/i}"

    show ulamog:
        left
        linear 0.5 right

    ulamog "Woah! So many utensils"

    show ulamog at center with fade

    "After Ulamog is done beholding the kitchen he pulls out a checklist of
    tools and cooking ware"

    "You don't know the names of many them, so you just read them off as Ulamog
    finds them"

    mc "Stainless steel cooking pot"

    ulamog "Check"

    mc "Cast iron wok"

    ulamog "Check"

    mc "Knives"

    ulamog "Many"

    mc "Cutting boards"

    ulamog "Check"

    mc "Food processor"

    ulamog "Would a food processor put food tokens from exile into the
    graveyard?"

    mc "I have no clue, do we have one or not?"

    ulamog "No, no. Food tokens, not clue tokens"

    mc "Tokens can't exist outside of the battlefield"

    ulamog "What about {i}bone rattler{/i}?"

    mc "..."

    mc "Do we have a food processor or not?"

    ulamog "Oh, um.. Yes we do"

    mc "{i}Pulverize{i/}r"

    ulamog "Check"

    mc "Meat tenderizer"

    ulamog "Check"

    mc "These are very violent names"

    ulamog "It's fine, don't worry about it"

    mc "Shredder"

    ulamog "Let's see..."

    mc "This can't be real right?"

    ulamog "Ah, here it is"

    mc "Geez, okay"

    mc "Guillotine!?"

    ulamog "Um.. Let me check"

    mc "Why would we possibly need a guillotine in the kitchen?"

    ulamog "You've never used a guillotine before?"

    mc "Can't say I have"

    ulamog "The guillotine is a staple of any kitchen arsenal"

    ulamog "It brings the oft lacking {i}gratuitous violence{/i} into home
    gastronomy"

    ulamog "Vive la révolution!"

    mc "Uhh.. So is there actually a guillotine in the school kitchen?"

    ulamog "Oui oui, je viens d'en trouver un dans ce placard"

    mc "Oh, you actually speak French?"

    ulamog "Well of course, it's easy!"

    mc "Really? Will you teach me?"

    ulamog "Teach you?"

    mc "Yeah, teach me. Since you seem to be quite fluent"

    ulamog "Oh, silly. You can't learn French"

    mc "What?"

    ulamog "Didn't you know? You only gain the ability to speak French by
    inserting a baguette into your asshole"

    mc "I'm sorry, what the fuck?"

    ulamog "In fact, most Frenchmen are born with baguettes already in their
    ass"

    mc "No, no. I wasn't being rhetorical, it's a genuine question. What the
    actual fuck?"

    ulamog "C'mon, I'll show you!"

    scene bg bathroom with dissolve

    "Ulamog takes your hand and pulls you into a nearby bathroom"

    "He shoves you into a stall and manifests a 60cm baguette seemingly from
    thin air"

    ulamog "Now pull your pants down and bend over"

    menu:

        mc "Um..."

        "Do as Ulamog says":
            jump baguette_comply
        "Blow the rape whistle":
            jump baguette_whistle

    return

label baguette_comply:

    "You do as Ulamog says"

    "You rest your hands on the toilet seat and {i}brace for impact{/i}"

    "You can see Ulamog preparing the baguette in the reflection of the
    porcelain"

    "Then it starts"

    "One centimeter"

    "Then another"

    mc "Is this really necessary?"

    ulamog "It's this, or take your chances with the Duolingo owl"

    mc "Continue then"

    "You feel the crusty exterior of the bread {i}explore{/i} deeper inside
    you"

    "Suddenly, you feel a {i}rush of knowledge{/i} flowing into you mind"

    "Words fill your head in a {i}swirling torrent{/i} of language"

    "The baguette continues, pushing further into your rectum"

    "And as the doughy enema reaches its climax, a {i}flood of recollection{/i}
    washes over you"

    "Vocabulary, grammar, pronunciation. In a {i}flash of insight{/i} you've
    gained the entirety of the French language without so much as picking up
    a book"

    jump day3_scene4_ulamog_french

    return

label baguette_whistle:

    "You pull the rape whistle from your pocket and blow into it as hard as you
    can"

    # whistle sound

    "The shrill sound {i}reverberate{i}s around the room"

    mc "RAPE!!!"

    "Then, as if summoned, a blue light tears through the air opening a
    {i}planar portal{/i} in the bathroom stall"

    "From the portal, out step two sharp men in uniforms"

    "And in heavy French accents they start yelling"

    "Man 1" "Arret!"

    "Man 2" "Au sol!"

    "The first man tackles Ulamog to the floor and pins their arms down"

    ulamog "Wait! Wait! I can explain!"

    if gender == "male":
        "Man 2" "There will be no explanation necessary. How dare you try to
        violate this young man"
    elif gender == "female":
        "Man 2" "There will be no explanation necessary. How dare you try to
        violate this young lady"
    else:
        "Man 2" "There will be no explanation necessary. How dare you try to
        violate this young person"

    ulamog "No, please! I was just trying to teach my friend French"

    "Man 1" "Hm?"

    ulamog "See, I have the baguette in my hand"

    "Man 2" "Well, so he does"

    "Man 1" "Oh my, we are terribly sorry"

    "The man removes himself from Ulamog"

    "Man 2" "Please, continue. French is such a beautiful language"

    mc "Wait! What!?"

    "The men step back into the portal and {i}disappear{/i} from reality"

    "Ulamog picks himself up from the bathroom floor and grabs the baguette"

    ulamog "So?"

    menu:

        ulamog "So?"

        "Continue":
            jump baguette_whistle_continue
        "Decline":
            jump baguette_whistle_decline

    return

label baguette_whistle_continue:

    mc "Okay"

    ulamog "Then you'll do it?"

    mc "Sure, I guess"

    ulamog "Wonderful!"

    jump baguette_comply

    return

label baguette_whistle_decline:

    mc "Please, I'd rather not do this"

    ulamog "Oh, okay.."

    "Ulamog lowers the baguette looking dejected"

    scene bg hall with dissolve

    "You awkwardly leave the bathroom without any more words"

    jump day3_scene4_ulamog_english

    return

label day3_scene4_ulamog_french:

    scene bg hall with dissolve

    show ulamog at center

    mc "C'est vraiment fou, je peux parler français maintenant"

    ulamog "Isn't it great!?"

    mc "I don't know if I should be impressed or concerned"

    ulamog "Impressed!"

    mc "Concerned it is then"

    jump day3_scene4_ulamog_enlgish

    return

label day3_scene4_ulamog_english:

    scene bg library 3 with dissolve

    "You return to the library just as the rest of the group is wrapping up"

    scene bg library 2 with dissolve

    show ulamog at center

    mc "So did you find everything you needed"

    ulamog "Yep, I think we're ready. Now I just need to show up to school
    early on Monday so I can set up"

    if gender == "male":
        ulamog "Come help me [name_2]-kun!"
    elif gender == "female":
        ulamog "Come help me [name_2]-chan!"
    else:
        ulamog "Come help me [name_2]-san!"

    mc "Uh, and wake up at 6:00am?"

    ulamog "C'mon it'll be fun"

    mc "I'll set my quantum alarm clock. Might happen, might not"

    ulamog "Hmmm.. Okay. Well, either way I'll see you Monday right?"

    mc "Yeah, I'll be there"

    ulamog "Yay!"

    python:
        date_2 = "ulamog"

    jump day3_scene5

    return

label day3_scene4_kozilek:

    closet scene

    return

label day3_scene4_emrakul:

    more hentai or smth idk

    return

label day3_scene4_nissa:

    snitties?

    return

label day3_scene5:

    scene bg hall with dissolve

    "Nissa's staying late to help everybody with final preparations. You're
    already pretty drained from today so you decide to walk home by yourself"

    "She'll understand you're sure"

    scene bg park with dissolve

    "Despite only starting to walk with Nissa for the past couple days, the
    {i}isolate{/i}d walk home feels unusually lonesome"

    "You're left alone with only your {i}wandering mind{/i} to keep you
    company"

    if date_2 == "ulamog":
        "Your {i}train of thought{/i} inevitably drifts toward Ulamog"
    elif date_2 == "kozilek":
        "Your {i}train of thought{/i} inevitably drifts toward Kozilek"
    elif date_2 == "emrakul":
        "Your {i}train of thought{/i} inevitably drifts toward Emrakul"
    elif date_2 == "nissa":
        "Your {i}train of thought{/i} inevitably drifts toward Nissa and
        Chandra"

    return

label day4_scene1:

    scene bg bedroom with dissolve

    "Saturday"

    "Saturdays are the best days"

    "Unlike Fridays, you get the entire day free. And unlike Sundays, there's
    no homework or the lingering {i}dread{/i} of the following Monday"

    "Saturdays truly are the best"

    "But not this Saturday"

    "No, today I need to help my class with preparations"

    "They say it's mandatory, but they prolly wouldn't even notice if I
    ditched"

    jump day4_scene2

    return

label day4_scene2:

    scene bg schoolgrounds with dissolve

    "Despite my *not derisions, I find I've ended up at school anyways"

    "Starting since 2002 schools have stopped requiring students to attend
    on Saturdays. I'm starting to realize how much I took that for granted"
    # ^ fact check this pls

    scene bg hall with dissolve

    "I'm a bit late, so the halls are pretty empty"

    "I stand in front of my homeroom door. Looking inside, not even half the
    class showed up. Maybe this was a mistake"

    "I mentally prepare myself for whatever awaits me inside"

    # door opening sound

    scene bg classroom frontleft with dissolve

    show nahiri at right

    if gender == "male":
        nahiri "[name_2]-kun, wow. You are the last person I expected to show
        up today"
    else:
        nahiri "[name_2]-san, wow. You are the last person I expected to show
        up today"

    nahiri "Well, I already explained everything. And I'm not doing it twice,
    so ask someone for the details and get to work"

    if kozilek_points > 10:
        jump day4_scene2_kozilek
    else:
        jump day4_scene2_ulamog

    return

label day4_scene2_kozilek:

    "Y'know, I'm starting to have yee haw about all this"

    "Everybody's leaving the classroom, already knowing what to do"

    scene bg hall with dissolve

    "I stand outside feeling clueless"

    "I know I should ask somebody what I can help with, but I really don't have
    the motivation to bother anybody about it"

    "It's not even my fault. Nahiri absolutely could've explained whatever
    she needed to twice and this all could've been avoided"

    show kozilek at center

    kozilek "Hey!"

    mc "Kozilek-kun?"

    kozilek "I need you to help with our class' event"

    mc "Your class isn't doing that?"

    kozilek "Well, uh.. Not enough people showed up so..."

    mc "I'd be happy to help"

    kozilek "Oh, okay"

    mc "What do you need help with?"

    show kozilek:
        center
        linear 2.0 xpos 2.0

    kozilek "This way"

    "Kozilek turns around and walks down the hallway without answering my
    question"

    "I follow"

    show kozilek at center

    mc "So remind me again, what is you class doing?"

    kozilek "Some kind of play, I don't really care"

    mc "And how are we helping?"

    kozilek "We're gathering props, okay, just shut up and follow me"

    kozilek "I'm only asking you to help because our class ran out of people"

    kozilek "So don't get the wrong idea"

    kozilek "It's not like I like you or anything, baka" # we did it bois

    "Fair enough"

    # scene bg closet with dissolve

    mc "A janitor's closet?"

    kozilek "We need a mop, our class president said we could borrow one from
    here"

    # door opening sound

    hide kozilek

    # scene bg closet open with dissolve
    # mmm you know exactly what's going here

    "..."

    mc "Um..."

    # door slamming sound

    scene bg hall # with dissolve?

    show kozilek

    kozilek "..."

    kozilek "There's another custodial closet on the other side of school"

    mc "Yeah, let's do that"

    kozilek "..."

    mc "..."

    kozilek "..."

    # scene bg closet with dissolve

    kozilek "Okay, this is it. Just get in there and find a mop, don't make
    this any more awkward than it needs to be"

    mc "Why? Is this awkward for you?"

    kozilek "No!"

    kozilek "I mean.. Just go!"

    mc "Hai hai, wakatta"

    hide kozilek

    # scene bg closet dark with dissolve

    mc "It's dark in here"

    kozilek "Turn on the light, idiot"

    mc "I can't find it"

    kozilek "Ugh"

    mc "..."

    mc "I don't think there's even a light in here"

    kozilek "Okay! Then just find the mop, you don't need a light!"

    mc "Alright"

    # shuffling noises

    mc "..."

    mc "I think I found the mop"

    kozilek "You think?"

    mc "I don't know, it's dark"

    mc "I can't reach it, can you help?"

    kozilek "Ugh, fine. But I'm not doing this for you"

    show kozilek at center

    mc "Sure"

    kozilek "Shut up!"

    kozilek "Where?"

    "I point"

    kozilek "Ugh"

    # more shuffling noises

    "Kozilek grabs the mop and pulls"

    # crashing sound

    # delay, then door slamming sound

    hide kozilek

    # scene bg black without any transition

    kozilek "AAAH!"

    kozilek "What did you do!?!"

    mc "I didn't do anything!"

    kozilek "Get it off!"

    mc "I can't see anything"

    # more crashing noises

    kozilek "Just AAAAAH!"

    mc "Are you okay"

    "I fumble my hand through the dark until I can feel Kozilek's bony
    exterior"

    kozilek "Don't touch me!"

    "Despite what he says, Kozilek grabs my hand"

    "I can't see anything in the pitch black closet, but holding Kozilek's
    hand in mine is enough to get my heart racing" # hnnnnngh, the cringe

    scene bg classroom frontleft with dissolve

    show kozilek at center

    show chandra at left

    mc "Thanks again Nalaar-san"

    chandra "Y'all were literally up against the door"

    chandra "It wasn't even locked or anything"

    kozilek "It was dark.."

    chandra "What were y'all even doing in there?"

    mc "Well--"

    chandra "Actually, y'know what? Nevermind, I don't want to know"

    show chandra:
        left
        linear 1.0 xpos -1.0

    show kozilek:
        xpos 0.5
        linear 1.0 center

    mc "Is that everything you need then?"

    kozilek "Yeah, I think so"

    mc "So when do I get to see this play?"

    kozilek "I don't really know"

    mc "Surely you must, you're helping prepare it"

    kozilek "I guess I wasn't really paying attention"

    mc "What role will you be playing?"

    kozilek "Just a minor part, it really doesn't matter"

    mc "You know I'm going to see it. So I'll know by the end of the week
    anyway"

    kozilek "It's just a stupid play, you shouldn't even bother coming"

    mc "Challenge accepted"

    kozilek "No! I mean.. It's embarrassing"

    mc "Embarrassing?"

    kozilek "Because it's you!"

    kozilek "I mean.. It would be.. For anybody..."

    kozilek "Just shut up! Baka!"

    show kozilek:
        center
        linear 0.5 xpos -1.0

    # running and door slamming sound

    return

label day4_scene2_ulamog:

    show ulamog at center

    ulamog "I can help you senpai!"

    mc "Oh, hi Ulamog-kun"

    ulamog "Let's go"

    "Ulamog takes my arm without even passing priority and drags me out of the
    classroom"

    scene bg hall with dissolve

    ulamog "Okay, so we're borrowing the school kitchen for our event"
