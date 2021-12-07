define nissa = Character("Nissa")
define chandra = Character("Chandra")
define sorin = Character("Sorin")
define nahiri = Character("Nahiri")
define ulamog = Character("Ulamog")
define kozilek = Character("Kozilek")
define emrakul = Character("Emrakul")

# credit house of imagi studio

python:
    name_1 = "mc1"
    name_2 = "mc2"
    gender = "non-binary"

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

    "Well, actually. You remember them quite {i}clear{i}ly. You've just
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

    show ulamog at xpos 0.3
    show kozilek at xpos 0.6
    show chandra at right

    nissa "Hi hi everyone! Sorry I'm late"

    nissa "This is my friend [name_2]-san"

    mc "Uh.. Hi guys"

    if gender == "male":
        ulamog "Hi [name-2]-kun!!"
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
    as a way to circumvent censorship laws at the time"

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

    emrakul "They argued this did not violate the censorship laws at the time
    due to it being mostly suggestive in nature"

    emrakul "This form of censorship evasion became wildly popular. And as a
    result, much of modern hentai still depicts tentacles despite the relevant
    censhorship laws having been {i}repeal{i}ed years ago"

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

    emrakul "I just thought-- Because [name-2]-san.."

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

    "You have a 25% success rate. Which is a significant step up from your
    usual 4% on short answer questions"

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

    "You don't have anything to put away considering you didn't take any
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
            jump day2_scene3_ulamog
        "Kozilek":
            jump day2_scene3_kozilek
        "Emrakul":
            jump day2_scene3_emrakul
        "Nissa":
            jump day2_scene3_nissa

label day2_scene3_ulamog:

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

    "Ulamog makes a brisk pace down the hall with a skip in their step"

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

    scene bg library 2 with dissolve

    show nissa at left
    show ulamog at center

    nissa "Oh, there you 

label day2_scene3_kozilek:

    show kozilek at center

    return

label day2_scene3_emrakul:

    show emrakul at center

    return

label day2_scene3_nissa:

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

    chandra "Well I had brought up to her that the fact we know chameleons
    even exist means they suck at their job"

    chandra "But Revane-chan, for some god-forsaken reason, knows that
    chameleons apparently change color as a means of communication rather than
    camoflauge"

    chandra "Sexual communication, she made that part quite explicit"

    nissa "Well, when you put it like that..."

    chandra "Which of course, like any respectable pursuers of science, left us
    {i}wonder{/i}ing which color means \"I want to bang\""

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

            chandra "And right now you are very close to losing that privelege"

            mc "Uhhh.. Okay?"

            chandra "I'm glad you understand. Now please,"
        "Blue":
            mc "I think it'd probably have to be blue"

            chandra "Blue!? Excuse you! Only incels and legacy players get
            horny at the sight of blue"

            chandra "g"
        "Black":
            pass
        "Red":
            mc "Well red's pretty sexy I guess"

            chandra "What!? Who looks at red and thinks \"Yeah, I'd bang that\""
        "Green":
            pass
        "Colorless":
            "Maybe answering \"Colorless\" to a question that expects a color as
            an answer isn't the smartest move"

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

            pass

    return

label day2_scene4:

    scene bg hall with dissolve

    "I exit the classroom in time to see Ulamog turn the corner at the end
    of the hallway"

    menu:

        "Maybe I should do something about that?"

        "Go after Ulamog":
            jump day2_scene4_chase
        "Continue to class":
            jump day2_scene4_class
        "Skip class":
            jump day2_scene4_skip

    return

label day2_scene4_chase:

    scene bg hall

    "I chase after Ulamog weaving my wave through the {i}mob{/i} of students"

    "It's tough to keep up with Ulamog's pace, but fortunately he's
    {i}tall as a beanstak{/i} and his distinct coloring makes him easily
    stand out from the crowd"

    scene bg monele with dissolve # courtyard

    "I finally catch up to Ulamog under a tree in the courtyard"

    show ulamog at center

    "He's sitting with his head in two hands while the other two hug his
    knees (bent tentacles?) to his chest"

    mc "Hey Ulamog-kun. Are you okay?"

    ulamog "Oh, hi senpai. I'm fine"

    mc "Are you sure? You didn't seem fine in class"

    ulamog "Oh, um. I shouldn't've said those things. I didn't really mean
    them"

    ulamog "It's okay if other colors have card advantage. I shouldn't compare
    myself to others"

    "// TODO: finish this without being any more cringe"

    return

label day2_scene4_class:

    "Well, knowing Ulamog, it's prolly not a big deal"

    "I continue on to class"

    show chandra at left

    show nissa at xpos 0.25

    "Outside the classroom Chandra and Nissa are talking to each other"

    "Although, Chandra seems to be doing most of the talking as Nissa just
    stares at the floor sheepishly"

    "As I enter earshot, I can hear Chandra complaining about schoolwork"

    chandra "--Even is the use of flectomancy? I mean, to be honest, most of
    these problems could be solved with fire"

    nissa "Is that why you're here?"

    chandra "What?"

    nissa "You set your math homework on fire again?"

    chandra "Hey! Just who do you think I am?"

    chandra "..."

    chandra "No, I didn't set my math homework on fire"

    nissa "Oh, okay. I just thought-- Since, I mean.. I could've helped you.
    Finish it. If you did, but you didn't so--"

    chandra "Wait. Is that what I think it is? Hold that thought"

    "Chandra reaches into her bag and pulls out a thin stack of papers"

    "Then, with one swift motion, she conjures a {i}pillar of flame{i} beneath
    the papers and lights the edge on fire"

    "The flame travels up the stack, eating away the papers until all that's
    left is a thin layer of ash on the floor which Chandra nonchalantly
    sweeps away with her foot"

    chandra "So? You were saying you wanted to help me with my homework?"

    nissa "Umm..."

    chandra "Then, the library, after school. I'll see you there"

    # bell rings

    show chandra:
        left
        linear 1.0 xpos -0.5

    "Chandra walks away with a smirk just as the bell rings"

    "Nissa stands there unmoving as the rest of the students funnel into the
    classroom"

    hide nissa

    scene bg classroom backright with dissolve

    "..."

    # bell rings

    show nissa at center

    if gender == "male":
        nissa "Umm.. [name_1]-kun?"
    elif gender == "female":
        nissa "Umm.. [name_1]-chan?"
    else:
        nissa "Umm.. [name_1]-san?"

    mc "Yes?"

    nissa "I don't know if you overheard, but I kind of agreed to help
    Nalaar-san with her homework after school"

    mc "Yeah, I heard something like that, why?"

    nissa "Well, if it's not too much to ask. Would you be there with me?"

    mc "What? It seems to me like Nalaar-san wants only you to be there"

    nissa "Mmmph, but I don't want to go alone"

    mc "That's silly, why not?"

    nissa "She's scary"

    mc "Scary? How so?"

    menu:

        nissa "Please, can you just come?"

        "Agree to go":
            mc "Alright, I'll go"
            $ chandra_homework_flag = True
        "Make up an excuse":
            mc "Sorry, I already made plans after school today"

    # jump next scene

    return

label day2_scene4_skip:

    "Well, knowing Ulamog, it's prolly not a big deal"

    if skip_flag:
        jump day2_scene4_skip_library2
    else:
        jump day2_scene4_skip_library1
        $ skip_flag = True

    return

label day2_scene4_skip_library2:

    "I remember telling Kozilek I'd see them today"

    "Maybe I should follow through with that"

    scene bg library 2 with dissolve

    scene bg library 1 with dissolve

    show kozilek at center

    "I find Kozilek sitting in the back of the library just as they said"

    "I sit down next him and he looks over at me"

    "But when our eyes meet he quickly averts his gaze back to his book"

    if ulamog_lunch_flag:
        mc "So.. \"Kozi-kun\" huh"

        kozilek "Don't call me that"

        mc "Hmm.. \"Kozilek-tan\" then?"

        kozilek "..."

        show kozilek:
            center
            linear 2.0 xpos 0.5

        "Kozilek turns their body away from me, and in doing so pushes up
        against me such that their back is resting against my arm"

        mc "Okay okay, \"Kozilek-kun\" then?"

        kozilek "..."

    mc "So? What're you reading today?"

    "I look over Kozilek's shoulder at the book in their hands"

    mc "They ran their slimy tentacles across my body, the black {i}void{/i}
    of their eyes looking deeply in--"

    # book slam sound

    kozilek "NOTHING!!"

    "They slam the book shut before I can read any further"

    kozilek "Ugh, you're such a {i}nuisance engine{/i}. Don't you have anything
    better to do than bother me all day?"

    mc "Aren't you the one who asked me to come today?"

    kozilek "I never said anything like that!"

    mc "Hmm.. I remember it differently"

    kozilek "Well you're wrong, stupid"

    mc "Fair enough, I'll take my leave then"

    "I stand up"

    show kozilek:
        xpos 0.5
        linear 0.5 center

    kozilek "Wait!"

    kozilek "I mean.. You don't have to. I can't make you leave
    {i}by force{/i} or anything"

    mc "So you want me to stay?"

    kozilek "Yes!"

    kozilek "No!"

    kozilek "Umm.. I mean you..."

    "Kozilek finishes the rest of their sentence in an incomprehensible mumble"

    mc "Pardon me, would you repeat that?"

    kozilek "Ugh, just stay.."

    mc "Apologies, a bit louder this time?"

    kozilek "Okay fine! Just stay idiot!"

    mc "Very well"

    "I sit back down and pass the rest of the period"

    jump day2_scene5

    return

label day2_scene4_skip_library1:

    return

label day2_scene5:

    scene bg classroom backright with dissolve

    scene bg hall with dissolve

    "Ugh, finally, I step out of 4th period ready for lunch break"

    show ulamog at center

    "Waiting for me outside is Ulamog"

    "He grabs my arm and starts draggin me down the hallway"

    ulamog "C'mon [name_1]-senpai! You're eating lunch with us, we need more
    friendos"

    mc "Wait, the cafeteria's the other way"

    ulamog "Oh, don't worry about that. I brought lots of food"

    mc "Well don't you seem happy, weren't you sulking just an hour ago?"

    ulamog "Eheheh, yeah. But that was an hour ago, now hurry up"

    "Ulamog drags me out to the courtyard where a picnic blanket is layed out
    under a tree"

    show chandra at left

    "Already sitting there is Chandra with a bemused smile on her face"

    "Ulamog sits down on the blanket and pats the spot next to them, inviting
    me to sit down"

    ulamog "Have you met Chandra-chan senpai?"

    chandra "Yo"

    mc "Yeah, I've seen her around"

    "I take a seat next to Ulamog"

    if skip_flag:
        show kozilek at right

        "As I'm sitting down, Kozilek shows up at the picnic blanket"

        ulamog "Ooo, Kozi-kun!! You said you weren't coming!"

        kozilek "Uhh, well. I mean.. I just happened to be--"

        ulamog "Yay! Sit down. More friendos!"

    "Ulamog produces stacks of bento boxes from his bag and passes them
    around to everyone"

    "Chandra opens her top box and makes an O with her mouth"

    "I open my box and immediately understand her reaction"

    "Meticulously arranged in the box are an assortment of quality foods"

    mc "Wow Ulamog-kun, where'd you get all this?"

    ulamog "I made it!"

    "Ulamog's face lights up with pride"

    chandra "Damn Ulamog-kun, this is impressive"

    ulamog "Thank you!"

    "No further words are spoken as everyone is eager to start eating"

    hide ulamog

    hide chandra

    hide kozilek

    "I look down at by box"

    "It's {i}clelar{/i} how much effort was put into making this"

    "Cutlet strips are stacked neatly in corners"

    "Rice balls are shaped like cat faces with dried seaweed for whiskers"

    "Omelettes are folded and cut into hearts or stars"

    "It all looks so perfect, I'd feel guilty eating it"

    "But I figure Ulamog'd feel bad if I didn't eat anything"

    "As I begin eating I notice a familiar presence in my mind"

    "How long it's been there, I can't be sure"

    "I scan the field, but it's not long before I spot it"

    show emrakul at center

    "Floating across the courtyard, poorly hidden behind a tree is the familiar
    shape"

    show ulamog at left

    ulamog "What're you looking at senpai?"

    mc "Oh, just--"

    ulamog "Oo! It's Emmy-chan!!"

    "Ulamog starts excitedly waving and motioning for Emrakul to join us"

    "Emrakul floats over to our picnic blanket"

    ulamog "Yay! More friendos!"

    ulamog "This is Emmy-chan, she's super sweet"

    "Emrakul raises a tentacle in greeting"

    emrakul "Hi"

    ulamog "Join us Emmy-chan!"

    "Ulamog hands a stack of bento boxes to Emrakul"

    "I watch as Emrakul struggles to hold the chopsticks in her tentacles"

    show chandra at right

    chandra "Aww, is Emwakul-tan having twouble wiff her chopsticks"

    emrakul "Nnnnnn"

    chandra "Haha, here let me help"

    show chandra:
        right
        linear 1.0 xpos 0.5

    "Chandra takes a string and ties a chopstick to Emrakul's tentacle"

    show chandra:
        xpos 0.5
        linear 1.0 right

    "Emrakul uses the fastened chopstick to skewer a fish cake from her
    bento"

    emrakul "Thank you Nalaar-san"

    # bell rings

    # fade black

    if chandra_homework_flag:
        jump day2_scene6
    else:
        jump day3_scene1

    return

label day2_scene6:

    scene bg library 2 with dissolve

    "I arrive at the library after school"

    "I'm a bit late, as I almost forgot that I had promised Nissa I'd be here"

    "Nissa and Chandra are already sitting at a table with textbooks open"

    scene bg library 3 with dissolve

    show nissa at left

    show chandra at center

    "I walk over and take a seat next to Nissa"

    mc "Hey"

    nissa "Oh, hi"

    "Nissa says with audible relief"

    if gender == "male":
        nissa "Um.. Nalaar-san, this is [name_1]-kun. I thought they could
        join us"
    elif gender == "female":
        nissa "Um.. Nalaar-san, this is [name_1]-chan. I thought they could
        join us"
    else:
        nissa "Um.. Nalaar-san, this is [name_1]-san. I thought they could
        join us"

    chandra "You never said anything about them coming"

    nissa "Oh, well.. They're really good at math so..."

    mc "I am a literal {i}garbage fire{/i} when it comes to math"

    nissa "Anyways!"

    nissa "Um.. We can start with the chain rule"

    "Nissa begins timidly explaining math terms. It goes through one ear and
    out the other"

    "Looking over at Chandra, I can tell she isn't understanding anything
    either. But she's still looking at Nissa and smiling"

    "As Nissa gets further into the homework she grows less aware of Chandra
    and me, becoming more confident in herself"

    "Although I'm not really paying attention to anything she's saying,
    it's nice to see her feeling more comfortable"

    hide nissa with fade

    hide chandra with fade

    "As I stare off into space, I start to get that familiar feeling"

    # show emrakul behind window

    "Across the library, I can see Emrakul hovering just outside the window"

    # hide emrakul

    "The presence leaves my mind and they quickly drop down, below my field
    of view"

    "That's mildly concerning.. If not outright creepy"

    "I'm starting to get a bad feeling"

    "This whole situation is just screaming GTFO"

    "Nissa's consumed in her homework, she probably wouldn't even notice if
    I left"

    show chandra at center

    "I look up at Chandra, she gives me a wink"

    "I guess I'll take that as my cue to leave"

    "I get up from my chair with bag in hand"

    "Nissa doesn't notice and I don't bother telling her"

    "I wave goodbye to Chandra and step out of the library"

    return

label day3_scene1:

    scene bg bedroom with dissolve

    "Fridays are overrated"

    "Yeah, I said it"

    "People don't seem to understand that Fridays are still an entire day of
    work"

    "You still need to go to school for the same amount of time as any other
    weekday"

    "Now, don't get me wrong, Fridays are still great. After all, unlike other
    weekdays, there's no homework because it's all been pushed back to Sunday"

    "But despite this, Fridays are still way overvalued"

    jump day3_scene2

    return

label day3_scene2:

    scene bg classroom backright w/ dissolve

    show nahiri at center

    nahiri "Ahem, so as you all know our school's Bunka no Hi celebration
    will be held next week"

    "I had absolutely no knowledge of this"

    nahiri "You will all be required to help"

    "Heck"

    nahiri "And because of the testing schedule this year preparations will
    need to take place over the weekend"

    "Double Heck"

    nahiri "Now we need to decide what our class will be doing for the
    {i}festival{/i}"

    nahiri "If you have an suggestion, write it down and you can turn it in
    up front"

    nahiri "I'd say there are no bad ideas, but after last year I think I'll
    refrain"

    "Some kids take out scraps of paper to write on"

    "I don't have any ideas myself, and I was never really fond of Culture
    Day to begin with"

    "After some time a few students walk to the front of the class to deposit
    their suggestions, but it's not many"

    "When it seems like nobody else has anything to add, the class president
    picks up the meager stack of papers"

    nahiri "Well aren't you guys just a {i}well of ideas{/i} today"

    nahiri "*sigh* Let's see what we have"

    nahiri "\"{i}Death match{/i} in the quad, {i}last one standing{/i} gets
    college admittance\""

    nahiri "What? What does that even mean?"

    nahir "And oh my gosh, we are not going to have a freaking {i}fight to the
    death{i} in the middle of the school {i}festival{/i}"

    nahiri "\"Human sacrificial rituals on the {i}altar of dementia{/i}\""

    nahiri "What is wrong with all of you!? We are not going to be killing
    people!"

    nahiri "*sigh*"

    nahiri "What the hell!? I'm not reading that!"

    nahiri "Next"

    nahiri "\"Drag race\""

    nahiri "*sigh*"

    nahiri "\"Baking contest\""

    nahiri "Finally! Something actually reasonable!"

    nahiri "And of course it ends there"

    nahiri "Well, y'all're voting between the baking and I guess the
    cross-dressing because everything else we absolutely cannot do"

    nahiri "Write your vote on paper and leave it up front I guess"

    show nahiri:
        center
        linear 1.0 left

    "Nahiri unceremoniously dumps the suggestions in the trash before returning
    to her seat"

    hide nahiri

    "I guess my choice is between a baking competition and a cross-dressing
    event"

    "Next to me, Ulamog is looking at me expectantly"

    "I already know what he wants me to vote for"

    "I don't have any particularly strong feelings either way, so I suppose
    I'll help Ulamog's effort"

    "I write down my vote and leave it on the teacher's desk"

    show nahiri at center

    "Once everyone's cast their vote Nahiri gathers the papers and starts
    counting"

    nahiri "And the winner is.. Baking"

    nahiri "Although it was disturbingly close"

    # bell rings

    nahiri "Okay, we start preparations tomorrow, please be here"

    if skip_flag:
        jump day3_scene3
    else:
        jump day3_scene4

    return

label day3_scene3:

    scene bg hall with dissolve

    "Well it's third period and I absolutely do not have the mental energy
    to deal with that hot mess of a class"

    scene bg library 2 with dissolve

    scene bg library 1 with dissolve

    show kozilek at center

    "Kozilek is in the library as I've come to expect"

    "I sit down across from him"

    mc "So.. What's your class doing for culture day"

    kozilek "A historical play or something. I don't really care"

    mc "Does that mean I get to see you in a yukata?"

    "Kozilek pushes his face further into his book"

    kozilek "It's not that kind of play"

    mc "Hmm.. A cat-maid outfit maybe?"

    kozilek "N-no. I would never agree to something like that"

    mc "Anime schoolgirl uniform"

    kozilek "Shut up!"

    mc "Now that's something I'd pay to see"

    jump day3_scene4

    return

label day3_scene4:

    scene bg hall with dissolve

    # bell rings

    "And it's only lunch break"

    "I grab some bread from the cafeteria and walk out to the courtyard"

    scene bg monele with dissolve # courtyard

    "Chandra and Nissa are sitting together in their usual spot"

    "Ulamog is uncharacteristically sitting alone on the opposite side of the
    court"

    menu:
        "Sit with Chandra and Nissa":
            jump day3_scene4_chandraNissa
        "Sit with Ulamog":
            jump day3_scene4_ulamog

    return

label day3_scene4_chandraNissa:

    # snitties?

    return

label day3_scene4_ulamog:

    "I walk across the field to Ulamog and take a take a seat next to him"

    show ulamog at center

    mc "Hey Ulamog-kun"

    ulamog "[name_1]-senpai!"

    ulamog "Would you like some pie?"

    mc "You brought an entire pie to school?"

    ulamog "Mmhm, I woke up extra early to bake it"

    mc "Wow, I can't imagine waking up any earlier than it takes to get to
    school"

    ulamog "So..?"

    mc "Yes, I would love some"

    "Ulamog cuts a generous slice and hands it to me on a paper plate"

    mc "So our class is doing a bake-off, huh"

    mc "It tastes like you'd be quite talented at that"

    ulamog "Well, Nahiri-chan thought baking might be too restrictive so we
    broadened it to include cooking as well"

    mc "That sounds like a mess"

    mc "I mean.. Uh, it sounds like a lot of fun"

    ulamog "You'll be helping with preparations right?"

    mc "I dunno.. My weekends are something of an inestimable treasure for all
    the world holds dear"

    ulamog "Please, I think you would have a lot of fun"

    # bell rings

    mc "..."

    mc "Well, I'll think about it. Thanks for the pie Ulamog-kun"

    jump day4_scene1

    # fade to black?

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

    "Y'know, I'm starting to have {i}second thoughts{/i} about all this"

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

    show kozilek at xpos 0.5

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

    ulamog "We needs to clean it and make sure it has all the supplies"

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

    "I don't know the names of many them, so I just read them off as Ulamog
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

    mc "..."

    mc "Do we have a food processor or not?"

    ulamog "Oh, um.. Yes we do"

    mc "Pulverizer"

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

    # shameless inserts from the one npr show with the kitche executioner
    # also use that to segue into the french thing (viva la revolution)

    # somehow get ulamog to speak in french, i dunno..

    return

label baguette_scene:

    scene bg hass with dissolve

    show ulamog at center

    mc "Wow Ulamog, you know French?"

    ulamog "Well of course, it's easy!"

    mc "Really? Will you teach me?"

    ulamog "Teach you?"

    mc "Yeah, teach me. Since you seem to be quite fluent"

    ulamog "Oh, silly senpai. You can't learn French"

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

    "Ulamog takes my hand and pulls me into a nearby bathroom"

    "He shoves me into a stall and manifests a 60cm baguette seemingly from
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

    "I do as Ulamog says"

    "I rest my hands on the toilet seat and {i}brace for impact{/i}"

    "I can see Ulamog preparing the baguette in the reflection of the
    porcelain"

    "Then it starts"

    "One centimeter"

    "Then another"

    mc "Is this really necessary?"

    ulamog "It's this, or take your chances with the duolingo owl"

    mc "Continue then"

    "I feel the crusty exterior of the bread {i}explore{/i} deeper inside me"

    "Suddenly I feel a {i}rush of knowledge{/i} flowing into my mind"

    "Words fill my mind in a {i}swirling torrent{/i} of language"

    "The baguette continues, pushing further into my asshole"

    "And as the doughy enema reaches its climax, a {i}flood of recollection{/i}
    washes over me"

    "Vocabulary, grammar, pronunciation. In a {i}flash of insight{/i} I've
    gained the entirety of the French language without so much as picking up
    a book"

    return

label baguette_whistle:

    "I pull the rape whistle from my pocket and blow into it as hard as I can"

    # whistle sound

    "The shrill sound {i}reverberate{i}s around the room"

    mc "RAPE!!!"

    "Then, as if summoned, a blue light tears through the air opening a
    portal in the bathroom stall"

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

    "We awkwardly leave the bathroom without any more words"

    return
