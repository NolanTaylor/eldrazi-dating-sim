"I arrive at homeroom after an unsuccessful attempt at killing time"

"To my surprise somebody else is also waiting in front of the classrooom"

"A tall figure with legs of tentacles and arms that split at the joints to
form two sets of forearms. Thick grey {i}carapace{/i} potrudes from exposed
muscle and sinew creating bone-like patterns along the reddish surface"

show ulamog at center

ulamog "[name_1]-senpai!!"

"A Lovecraftian {i}cosmic horror{/i} of unimaginable {i}terror{/i}"

ulamog "Look at this cute bunny I drew!!"

"A being {i}not of this world{/i} whose presence is a {i}beacon of
destruction{/i} for
anyone in sight"

ulamog "It's got a little bowtie, and a cute little tail~"

"The {i}embodiment of agonies{/i}, a {i}waking nightmare{/i}, the
manifestation of everyone's
{i}worst fears{/i}"

ulamog "And it's nibbling on some grass ~eeeek!"

"A {i}ceaseless hunger{/i}"

"An {i}infinite gyre{/i}"

mc "Hey Ulamog-kun"

ulamog "So what do you think!?"

mc "Is that the math homework you drew it on?"

ulamog "Yeah, uh, I got bored and it was the only paper I had with me"

# bell rings

ulamog "Oh, that's the bell, let's go"

show ulamog:
    center
    linear 1.0 xpos 1.0

scene bg classroom frontleft with dissolve

"We're the first ones inside the classroom"

"Ulamog takes a front row seat"

show ulamog:
    xpos 1.0
    linear 1.0 center

"I move to take my usual seat in the back, but Ulamog waves me over in
protest"

ulamog "C'mon [name_1]-senpai! Sit up front with me"

mc "Yeah.. Sure"

hide ulamog

scene bg classroom backright with dissolve

"I take my seat next to Ulamog. Great, now this means I'll need to look
like I'm actually paying attention"

"Students start to trickle into the classroom and takes their seats"

"I look over at Ulamog. He's pulling out various school supplies from his
bag"

"He takes out two notebooks, an assortment of colored pens, and a jar of
glitter ink"

mc "What is all that for?"

ulamog "Taking notes!"

"Seems excessive, but I won't judge"

"I look into my own bag. I should probably make it look like I'm taking
notes too"

"I find an old notebook, but nothing to write with"

"Ulamog is neatly arranging his brightly colored pens by gradient"

mc "Hey uhh, Ulamog-kun. Could I borrow a pen?"

ulamog "Sure!"

"He presents me with the {i}brilliant spectrum{/i} of colors spread out on
his desk"

"I take the black pen at the end of the table"

mc "Thanks"

# second bell rings

"The class quiets down as the second bell rings"

"The teacher stands up begins their lesson on some highly emperical math
concept"

"I'm trying to follow along, or at least look like I am, but I don't
understand a thing"

"I don't even recognize half the {i}unspeakable symbol{/i}s on the whiteboard"

"And why are there letters? In fact, there are more letters than there are
numbers. I thought this was math, not English"

"I look over at Ulamog. He's {i}absorb{/i}ed in his notes, copying down
formulas in two notebooks with two sets of hands"

"..."

# bell rings

"The bell finally rings, marking the end of the period"

"I pack up my notebook and return the pen I borrowed from Ulamog"

mc "Hey, thanks for the pen Ulamog-kun"

show ulamog at center

ulamog "Of course, anytime senpai"

ulamog "Oh, wait up for me. Are we gonna walk to class together?"

mc "Yeah, sure"

jump day1_scene3

scene bg hall with dissolve

scene bg classroom backleft with dissolve

# bell rings

"Ugh.. Culture studies"

"I take a seat in the very back of class"

"Ulamog won't ever convince me to sit in the front of this class,
even the most {i}compelling argument{/i} won't sway me"

"Ulamog sits down next to me, I guess a front row seat is a small
{i}sacrifice{/i} to make"

"Or maybe he just likes me that much... The thought of which feels nice"

"The teacher begins their lesson on the ancient tribes of Bala-Ged"

"It's like watching a storm player go off for the nth time but not being
able to scoop because \"bUt ThEY cOuLd FizZLe!1!\""

"I stare down at my desk praying for the bell to ring already"

"It feels like {i}time stretch{/i}s out forever, I'm on a {i}journey to
eternity{/i}"

"Every turn feels like it takes three turns"

"heh heh.."

"get it? 'cuz {i}time stretch{/i}.. gives you.."

"two extra.. yeah? heh"

"..."

"..."

"please laugh"

"..."

# door opening sound

"Huh?"

"Suddenly, the door opens, interrupting the teacher's lesson"

show sorin at center

"I look over to see a tall and {i}captivating vampire{/i} standing in the
doorway"

"We lock eyes and he give me a {i}baleful stare{/i}"

sorin "..."

"Edgelord"

"Teacher" "Ahem, yes. Please take a seat"

"The teacher waves them down with a slight irritation in their voice for
having their lesson interrupted"

show sorin:
    center
    linear 1.0 xpos 1.5

"The rest of the class stares as Sorin make his way to the back row of
desks and take their seat"

"Teacher" "Okay class, eyes back over here"

scene bg classroom backright with dissolve

"The class continues for the rest of the period without disturbance"

# bell rings

jump day1_scene4

return

scene bg hall with dissolve

"Gosh, school is such a {i}crippling fatigue{/i}"

"Not even halfway through the second trimester and I can already feel the
senioritis setting in"

"I haven't even started studying for entrance exams yet"

"Most kids already started studying in second year"

"At this point, even if I did start acting diligent it wouldn't change much"

menu:
    "And third period is the worst of them all"

    "Attend third":
        jump day1_scene4_class
    "Skip class":
        jump day1_scene4_skip
        $ skip_flag = True

return

label day1_scene4_class:

scene bg hall

"But I supposed my attendance isn't doing to well from last trimester"

"And graduating is important"

scene bg classroom frontleft with dissolve

"I enter the classroom?"

jump day1_scene5

return

label day1_scene4_skip:

scene bg hall

"I figure my attendance record can take one more hit"

"I turn the corner ahead of my class and look for somewhere to slack off"

"I stop in front of the library. It's only supposed to be open after class
but they never lock it during the day"

"There's not much of interest in there, just books. And I don't like
reading"

# bell rings

"Well, I guess that's my cue"

"I don't want to be caught in the halls after the second bell"

"I resign myself to hiding behind a bookshelf and browsing 4chan"

"Not ideal, but it's admittedly better than being in class"

scene bg library 2 with dissolve

"I enter the library"

"Nobody's at the desk so I don't need to worry about making up
an excuse for being here"

scene bg library 1 with dissolve

"I head to the end of the row of bookshelves"

"And to my surprise, somebody's also there"

show kozilek at center

"A humanoid figure, but with a mass of tentacles in place of legs.
They're sitting, leaned up against a shelf and reading a book"

"Their eyes meet mine briefly before they {i}flicker{/i} back
to the book in their hands"

"They're not a teacher so I don't have anything to {i}distress{/i}
over"

"I sit down across from them and pull out my phone"

"They {i}peek{/i} over their book and again we meet eyes. But none of
us say anything"

"I return my gaze to my phone and scroll through various chatrooms"

hide kozilek

"..."

"Nothing's catching my eye"

"The internet can be quite boring at times"

mc "So what are you reading?"

show kozilek

kozilek "None of your business"

mc "\"Iona-tan's tentacle adven--\""

# book slam sound

kozilek "NOTHING!!!"

"They slam the book shut with a {i}force of vigor{/i} and hastily shove it
into their {i}bag of holding{/i}"

"Fair enough"

"I find a thread on ttrpg {i}horror{/i} stories and return my attention to my
phone"

"..."

kozilek "Can you just stop doing that!?"

mc "What?"

kozilek "Just stop!"

mc "What am I doing?"

kozilek "Just... That!"

mc "I'm not doing anything!"

kozilek "Okay! Then just stop it!"

mc "Should I leave?"

kozilek "NO!!"

kozilek "I mean... Just, stay there!"

mc "But I thought you didn't--"

kozilek "Fine! Then just continue what you were doing! Whatever..."

mc "Okay..."

"I try to {i}refocus{/i} my attention back to my phone, but I can
feel Kozilek's {i}prying eyes{/i} watching me"

"The rest of the period passes in awkward {i}silence{/i}"

# bell rings

"..."

"I suppose that was fun, but I really can't afford to skip anymore
classes today"

kozilek "Are you leaving?"

mc "Uh, well, I should get to class"

kozilek "I'll be here tomorrow"

mc "Okay.."

kozilek "I mean you can come if you want to. But it's not like I care or
anything..."

mc "Sure. Well then, see you tomorrow maybe"

jump day1_scene5

return

label day1_scene5:

scene bg hall with dissolve

# bell rings

"It was a {i}struggle // survive{/i} but I made it through 4th period"

"Now comes the second best part of school"

"Lunch break"

"The cafeteria is crowded as always and all the good food is taken"

"I grab some anpan off the counter, pay, and make a {i}narrow escape{/i}
before I'm {i}crush{/i}ed underneath the {i}overwhelming stampede{/i} of
students vying for the remaining food of actual quality"

scene bg monele with dissolve # courtyard

"I step out into the courtyard and begin my search for a quiet place to sit"

"But it's not long before my search is interrupted"

show nissa at right

if gender == "male":
    nissa "[name_1]-kun!! Come sit with us!"
elif gender == "female":
    nissa "[name_1]-chan!! Come sit with us!"
else:
    nissa "[name_1]-san!! Come sit with us!"

"I suppose my endeavors were for naught"

show chandra at left

"I walk over to Nissa"

"She's sitting with another girl"

mc "I'm not interrupting anything am I?"

chandra "Just our conversation about chameleons. Take a seat"

mc "Uhh... Chameleons?"

chandra "Well I had brought up to Revane-chan that the fact we know
chameleons exist mean they suck at their job"

chandra "But she for some reason knows that chameleons actually change
color as a means of communication rather than camoflauge"

chandra "Sexual communication, mostly"

chandra "Which left us {i}wonder{/i}ing which color means \"I want to
bang\""

nissa "Only you wanted to know that"

chandra "I think it's green. She thinks it's red"

menu:

    chandra "You don't have to answer if you don't want to"

    "Green":
        jump day1_scene5_green
    "Red":
        jump day1_scene5_red
    "Blue":
        jump day1_scene5_blue
    "Decline to answer; Leave":
        jump day1_scene5_leave
        $ ulamog_lunch_flag = True

return

label day1_scene5_green:

mc "Well green's pretty sexy I guess"

chandra "See! I told you, green is the universal color of sex"

chandra "Even chameleons understand that the power of horny eclipses
all language barriers"

chandra "Not like red"

chandra "Red's for {i}burning cinder fury of crimson chaos fire{/i}!!
Not sex"

return

label day1_scene5_red:

mc "Well red's pretty sexy I guess"

chandra "What!? Who looks at red and thinks \"Yea, I'd bang that\"?"

jump day1_scene5_color

return

label day1_scene5_blue:

mc "Well, I guess blue's pretty sexy"

chandra "Blue!? Only incels and legacy players get horny at the sight
of blue"

chandra "Nah, green's the way to go"

chandra "It's smooth and sexy"

chandra "Unlike red"

chandra "Red's for {i}burning cinder fury of crimson chaos fire{/i}!!
Not sex"

jump day1_scene5_color

return

label day1_scene5_color:

nissa "I think red's a very romantic color"

chandra "Pffft, romantic? Sex isn't romantic?"

chandra "You think chameleons like romance?"

nissa "Well I don't know.. I just like the color red"

chandra "Heh, do you think I'm romantic then?"

"Chandra gestures to her body clad in various shades of red"

"Dyed red leather armor under a vibrant red breastplate and a red
cloak pinned to her waist"

"Even her hair is known to burst into flames on occasion. All making
for a very striking image"

nissa "Um.. Well, you look very..."

"Nissa mumbles the rest of her sentence down into her food"

"And although her expression is hidden, I wouldn't be surprised if
she was also turning quite red"

jump day1_scene6

return

label day1_scene5_leave:

mc "Yeah, I think I'll pass this time"

chandra "Fair enough"

show chandra:
    left
    linear 1.0 xpos 1.5

show nissa:
    right
    linear 1.0 xpos 1.5

"I take my leave before the conversation can get any weirder"

"I head off in the opposite direction, but before I can find a spot, a
voice calls out"

show ulamog at right

ulamog "[name_1]-senpai!! Come sit with us!"

"I guess the {i}whims of fate{/i} just don't want me to sit alone today"

show kozilek at left

ulamog "You've met Kozi-kun right?"

mc "Kozi-kun?"

kozilek "Just \"Kozilek-kun\" if fine"

mc "Kozilek-kun"

"I sit down next to Ulamog and notice the massive {i}mountain{/i} of food
laid out before him"

mc "Wow, you're going to eat all that in a forty minute lunch period?"

ulamog "Oh this? This is nothing"

"Ulamog casually {i}dismiss{/i}es me and before you could say \"in
response\" he's already exiled two food tokens off the table"

"Kozilek sits and picks at his own food like it's nothing out of
the ordinary"

"I spend the entire time just watching Ulamog voraciously consume his food
that I almost forget to eat my anpan"

"By the end of the lunch break Ulamog's exiled an entire edh deck's worth
of food tokens"

jump day1_scene6

return

label day1_scene6:

scene bg classroom backleft with dissolve

"The {i}sanity grinding{/i} drudgery of my final periods is almost
at an end"

"The teacher just won't shut up about {i}zendikar's roil{/i}"

"If it's that interesting why don't they go {i}into the roil{/i}
themselves"

"Oh right... {i}Certain death{/i}"

mc "*sigh*"

"Something outside the window catches my eye"

"A floating mass of tentacles and flesh-like protrustions"

"It has nothing remotely resembling eyes, and yet I can feel it watching me"

"More than that I'm distinctly aware of a foreign presence in my mind"

"Like my thoughts are not entirely my own"

"What could it be?"

"fufufu, i'm emrakul"

"Wait.. I'm not Emrakul"

"ofc not silly, i'm emrakul"

"Emrakul-san? Is thay you outside the window?"

"fufufu"

"I'll take that as a yes"

"..."

"So um.. How can you read minds?"

"magic"

"Right.. Magic exists"

"I sit and stare at my desk as Emrakul {i}thought scour{i}s me"

"I'm trying my hardest to {i}clear the mind{/i} of anything too
embarrasing, but it's becoming a bit of a struggle"

"The more I try not to think of anything, the more cringe worthy
moments surface themselves in my {i}whirlwind of thought{/i}s"

"Emrakul's not saying anything, but I can still feel them in my head"

"..."

# bell rings

"The bell finally rings, freeing me from the {i}uncomfortable chill{/i} of
Emrakul's {i}thoughtseize{/i}"

scene bg hall with dissolve

"I determindly make my way down the hall"

"And as I get farther away from the classroom, I feel Emrakul's presence
{i}fade away{/i}"

jump day2_scene1

return

if skip_flag:
    nissa "You were {i}unexpectedly absent{/i} from third period yesterday"

    mc "Ugh, history's so boring"

    nissa "You really shouldn't be skipping class so much. Your graduation
    status is already in {i}grave peril{/i} from your poor attendance last
    trimester"

    mc "I know, I know. I'll try to be better this trimester"
else:
    pass

# bell rings

mc "*sigh*"

"I'm sitting next to Ulamog again"

"He's studiously taking notes while I'm moving my pen over my notebook
pretending to pay attention"

show ulamog at left

ulamog "Psssst! [name_1]-senpai"

mc "Mhmm?"

"I interject in paralinguistic fashion"

ulamog "What's the derivative of pi?"

mc "What?"

ulamog "Mmmm, I want some pie.."

mc "Isn't pi just a constant?"

ulamog "Constantly delicous.."

mc "Um.. Sure"

"Ulamog returns to solving their math problem"

"Probably not correctly if they need the derivative of a constant"

"I return to staring at the blank notebook on my desk"

"The teacher's droning on about hospitals and chains or something"

"My eyes wander over to Ulamog sitting at the desk next to me"

"I watch as they struggle through the problems in their mind"

"Their four hands move methodically across two notebooks"

"Two hands clamp down the notebooks. One hand is struggling to draw
integral symbols, the other hand is doodling pies on the corners of
the paper"

"..."

# bell rings

"Before I know it, the period is already over"

"Time seems to have passed by in the {i}blink of an eye{/i}"

jump day2_scene3

return

"I take my usual seat in the very back of class"

"Ulamog decides to sit next to me again"

"Not that I'm complaining I suppose"

"The teacher begins their lesson"

"Immediately it feels like a {i}winter orb{i} hit the battlefield and
nobody has removal"

"..."

mc "*sigh*"

"..."

ulamog "Ugh, at least white can tax others, colorless doesn't get any draw"

"What?"

"I wasn't paying attention to anything the teacher said just now"

"But before I get the {i}opportunity{/i} to comprehend Ulamog's comment,
somebody else speaks up from the other side of the classroom"

show nahiri at center

nahiri "Excuse me Akiri-sensei, I don't think it's acceptable to hate on
white for not having card draw. White has many other tools such as taxing
and parity to gain effective card advantage in a way that is unique to
their color pie identity"

ulamog "Mmm.. Pie..."

nahiri "We should be supporting white for what it can do instead of
criticizing it for what it can't"

"Teacher" "Ahem, okay. Well, thank you for that Nahiri-san but in the
future let's refrain from bringing politics into class discussions"

"From the back of the class it looks like Sorin, who's sitting next to
Nahiri, is saying something to her but I can't make it out"

nahiri "Okay just SHUT UP!! You got {i}opposition agent{/i}!"

show nahiri:
    center
    linear 1.0 left

show sorin at xpos 0.5

sorin "It's an established and unequivocal part of black's identity to
tutor and prevent tutoring"

sorin "It's by no means a stretch of the imagination to combine the two"

nahiri "Yeah, and here I am stuck with {i}aven mindcensor{/i}, how is that
fair!?"

"Teacher" "Okay! Class, please settle down. We are getting off topic. This
is not a constructive atmosphere we have created here"

"Flustered by the outbreak, the teacher tries to get the class in order but
the situation is only escalating as the sounds of students arguing fills
the classroom"

hide nahiri

hide sorin

show ulamog at center

ulamog "IT'S NOT FAIR!!!"

"..."

ulamog "Colorless doesn't get anything. I'm so embarrased waiting
for other players to draw cards so I can pay 1 for {i}mind's eye{/i}"

"The rest of the class falls in {i}swift silence{/i} after Ulamog's
unexpected {i}outbreak{/i}"

"The teacher uses this chance to regain control of the class"

"Teacher" "Umm... Okay Ulamog-kun, let's try to keep a respectful tone of
voice"

show ulamog:
    center
    linear 2.0 xpos 1.0

"Ulamog slinks back into their seat in embarrasment, realizing what they've
done"

# bell rings

"Once the bell rings Ulamog hurries out the door without another word"

jump day2_scene4

return
