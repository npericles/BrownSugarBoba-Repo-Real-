# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#characters
define kidsage = Character("Sage")
define kidjax = Character("Jax")
define kidtal = Character("Tal")
define sage = Character("Sage")
define jax = Character("Jax")
define tal = Character("Tal")
define june = Character("June")

define kai = Character("Kai")
define sage = Character("Sage")
define jax = Character("Jax")
define tal = Character("Tal")
define raven = Character("Raven")
define mom = Character("Sage's Mom")
define boss = Character("Kai's Employer")
define engineer = Character("Nikolai")
define scientist = Character("Ms. Frermi")
define hospital = Character("Hospital Receptionist")
define n1 = Character("Nurse 1")
define n2 = Character("Nurse 2")

# custom locations
transform leftish:
    xalign 0.33 yalign 0.0

transform rightish:
    xalign 0.66 yalign 0.0

#images
    #kai
image kai happy = "images/kai/happy.png"
image kai neutral = "images/kai/neutral.png"
image kai smile = "images/kai/smile.png"
image kai frown = "images/kai/frown.png"
    #image kai thinking = "images/kai/thinking.png"
    #sage
image kidsage happy = "images/sage/kid/happy.png"
image kidsage neutral = "images/sage/kid/neutral.png"
image kidsage smile = "images/sage/kid/smile.png"
image kidsage frown = "images/sage/kid/frown.png"
image kidsage deadpan = "images/sage/kid/deadpan.png"

image sage neutral = "images/sage/adult/neutral.png"
image sage angry = "images/sage/adult/angry.png"
image sage happy = "images/sage/adult/happy.png"
image sage nervous = "images/sage/adult/nervous.png"
image sage scared = "images/sage/adult/scared.png"

    # #tal
image kidtal neutral = "images/tal/kid/neutral.png"
image kidtal smile = "images/tal/kid/smile.png"
image kidtal frown = "images/tal/kid/frown.png"
image kidtal scared = "images/tal/kid/scared.png"
image kidtal hesitant = "images/tal/kid/hesitant.png"

image tal angry = "images/tal/adult/tangry.png"
image tal neutral = "images/tal/adult/tneutral.png"
image tal shock = "images/tal/adult/tshock.png"
image tal smile = "images/tal/adult/tsmile.png"
image tal worried = "images/tal/adult/tworried.png"

    # #jax
image kidjax happy = "images/jax/kid/happy.png"
image kidjax neutral = "images/jax/kid/neutral.png"
image kidjax smile = "images/jax/kid/smile.png"
image kidjax frown = "images/jax/kid/frown.png"
image kidjax superfrown = "images/jax/kid/superfrown.png"
image kidjax burnt = "images/jax/kid/burnt.png"
image kidjax smug = "images/jax/kid/smug.png"

image jax anger = "images/jax/adult/anger.png"
image jax happy = "images/jax/adult/happy.png"
image jax neutral = "images/jax/adult/neutral.png"
image jax shock = "images/jax/adult/shock.png"
image jax worry = "images/jax/adult/worry.png"

    # backgrounds
#image kaitreehouse
#image sageApartment
#image talHouse

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

#scene 1 - 15 Years Before, Kai's House
    scene black

    # [All black. sage.]
    # 1A ALL BLACK SAGE
    show sage neutral
    sage "When I was younger, I had three best friends."

    sage "We were tight. Really tight."

    sage "Our mothers were all best friends, so we got their permission to hang out as much as we wanted to."
    show sage happy
    sage "Only God knows how many playdates we had. We hung out every single day after school."

    sage "Our favorite spot was Kai’s place. He had a treehouse afterall and his moms were incredibly kind."
    show sage neutral
    sage "It got harder to stay connected when we got into our high school years, because a lot of us moved away."
    show sage happy
    sage "But in those younger years? It was golden."
    show sage nervous
    sage "And it turned out that we had more in common than we thought."

    sage "But I’ll let you see what happened for yourself."

    scene kaitreehouse
    # 1B Treehouse
    # [Fade in with establishing shots of The Treehouse™. Sage and Kai]

    show kai happy at right
    kai "Sage, Sage, guess what I found!" # amazed
    show kidsage neutral at left
    sage "A frog? Another bug? "
    show kai neutral
    kai "No, no, I found a gecko!"
    
    scene gecko
    with fade
    kai "I caught it outside! Isn’t it cool?"
    #want to have png of gecko here, just the gecko center screen, black bg, isometric view
    #then fade back in
    scene kaitreehouse
    with fade
    show kidsage happy
    sage "Woah, Kai, that’s so amazing!" # amazed
    show kidsage frown
    sage "Is it okay?"
    sage "It looks like it’s trying to run."
    show kidsage frown at left
    show kai thinking at right
    kai "I think he wants to go back." 
    kai "I’ll let him do that in a second, though. "
    kai "I thought it was a new species until I realized it just didn't have a tail."
    show kai smile
    kai "Did you know they just ditch their tails to escape predators?"
    show kidsage smile
    sage "That's so cool!"
    show kai smile
    kai "Can you hold it? I wanna take some notes and you're always better with animals."
    show kidsage happy
    sage "Okay!"

    hide kidsage
    hide kai

    "Further away, her other friends are playing a game of mercenary at the other end of the treehouse."

    "Sage always kept one eye open whenever she saw Jax playing with Tal."
    "Tal started hanging out with the rest of the friend group a few months ago, but sometimes he'll get worked up and the air will feel charged, like a storm is brewing somewhere."
    show kidtal smile at right
    tal "Okay, well, maybe you won this game, but you won’t win the next!"
    show kidjax smug at left
    jax "We’ll see about that!"

    jax "My parents say that I’m really good at this game."

    jax "And I don’t like losing, so—"

    "Tal does an exaggerated frown and reaches out to playfully shove Jax backward, but the second he touches Jax..."
    #show animation of zap (btw these are like, super zoomed in, so basically just the zap and then the immediate surroundings) 
    
    scene talshock

    "he jerks away."

    "Tal scrambles back."

    scene kaitreehouse

    show kidjax superfrown at left
    show kidtal scared at right
    jax "Ow! You just shocked me!" #-frown!!!

    tal "Sorry. I'm so sorry." # (uh oh face))
    show kidjax burnt
    jax "Wait, wait, Tal. That wasn’t, like, the natural type of shock, right? That was you?" 

    "Hesitantly, Tal nods."
    
    show kidjax happy
    jax "That's so, so cool."#happy
    show kidjax neutral
    jax "Tal, I want to show you something, because I can do something kinda like that, but you can’t tell anyone, okay?"#neutral
    show kidtal frown
    tal "Okay… what is it?"

    hide kidjax
    hide kidtal
    "A small flame bursts to life in Jax’s palm."

    "Tal's eyes widen and instinctively he covers Jax's hand with his own."

    "The flame snuffs out."
    show kidjax smile at left
    show kidtal smile at right
    tal "Yo." #smile - micheif

    jax "Bro."#smile - micheif

    tal "Bro."#smile - micheif

    jax "How did you just extinguish it?" 

    tal "I don't know. I guess lightning is related to fire?"

    jax "We were so meant to be friends." #, grinning
    
    hide kidjax
    hide kidtal
    "Sage looks over at Kai, who’s still taking notes in his field notebook, his brow furrowed in concentration. "

    "She looks at Jax and Tal, who coincidentally look at her, and the two of them immediately look away."

    show kidsage deadpan at left
    sage "I saw that."

    # next two dialogues in : normal sprite
    
    show kidjax neutral at right
    jax "What are you talking about?"
    show kidjax neutral at rightish
    show kidtal neutral at right
    tal "No you didn't. You didn't see anything."

    sage "…"

    jax "…"

    jax "You know what? I need to be home early today."

    tal "Me too."

    hide kidsage
    hide kidtal
    hide kidjax
    show kai thinking
    kai "What's going on? Wait, Jax. We have at least two more hours before you need to go home, what are you talking about?"

    show kidsage deadpan at left
    sage "…"
    show kidsage smile
    sage "You guys are so dumb. Here, I have something too."
    hide kidsage
    hide kai
    "Sage brings the tiny gecko to her face and nudges it with the tip of her nose." 

    scene geckomindread

    "Suddenly she sees into its mind, the steady pulse of its heartbeat."
    
    #should be some kid of animation here of a pulsing heart beat

    sage "It's good to see you."

    "The gecko stops trying to run away, and it seems to automatically cheer up, making a noise that seems almost pleased."

    scene kaiTreehouse

    "Sage turns to the others expectantly." 

    "She smiles. Her mother had always told her that most humans didn't have special powers, but seeing Jax and Tal’s abilities made her realize she wasn't isolated."
    show kidjax frown at right
    show kidsage smile at left
    jax "That's…that's something."
    show kidjax at rightish
    show kidtal frown at right
    tal "So, you can control animals or something?"
    show kidsage frown
    sage "No, no, not control! I can talk to them."

    "Sage looks at Kai."
    show kidjax at leftish
    show kidtal at rightish
    show kai frown at right
    "He seems wary and guarded."
    
    kai "Mine is water."

    show kidsage neutral

    sage "What?"

    kai "I can make it dance. "

    show kai thinking
    kai "I can’t do too much, but I can make it…"
    hide kidsage
    hide kai
    hide kidjax
    hide kidtal

    scene waterMove

    #should be some sort of animation of either water moving, or the cup
    "Kai flicks his finger, and the water in a half-filled paper cup sloshes over the rim."
    
    "He squints at it, his hands clenching in his lap, and the cup tips over. "

    "The water seeps into the wooden floorboards."

    scene kaiTreehouse

    show kai frown at left
    kai "That was a little lame."
    show kidtal smile at right
    tal "Yeah, it was."
    show kidtal at rightish
    show kidjax happy at right
    jax "Tal, shut up. This is awesome."

    jax "You guys too?"
    show kai at leftish
    show kidsage at left
    sage "Yeah."

    kai "No one else is supposed to know."
    show kidjax frown
    jax "Your parents told you to keep it a secret?"

    kai "Yeah. Yours too?"

    jax "Mhm."
    show kidsage smile
    sage "We're not gonna tell anyone. Promise. And – our powers are weird anyway."
    
    sage "It’s not like we're gonna change the world with an army of geckos or a puddle of water."
    show kai thinking
    kai "We might." # , musing

    sage "My parents taught me that magic isn't inside of any normal people. It’s just used to power lamps and stuff, not people. "

    sage "So no matter how special we are, we're weak. Like, according to science."
    
    show kidjax at leftish
    show kidtal frown at right
    tal "Fire powers aren't weak."

    jax "Guys, I feel like you’re really ignoring a big part of this."

    tal "What?"
    show kidjax smile
    jax "Imagine what our pranks would be like. With all four of us, we can screw around with so many people-"
    show kidsage deadpan
    sage "No."
    show kidjax superfrown
    jax "But" # dismayed
    show kidtal at rightish
    show kai frown at right
    kai "No."
    show kidjax frown
    jax "Okay."
    show kidjax smile
    jax "But this is cool, isn't it? I thought I was the only one."
    show kai thinking
    kai "I still don't think…nevermind."
    show kidsage smile
    sage "It'll be between us. Friends forever, right?"
    show kidjax smile
    show kai smile
    show kidtal smile
    jax "Yeah. Yeah, let's shake on it."

    hide kidsage
    hide kidjax
    hide kidtal
    hide kai
    "The four of them shake on it."

    "After that day, the secret brought them together like an invisible thread. It was something cool that made them all feel special and, for years, their promise held true."

#scene 2 - sage's Car
    scene sageApartment
    show sage neutral

    #Inside a small apartment. Sage.

    "Sage groans and settles into a chair, opening the newspaper."

    sage "Here we go again."

    sage "God, it’s too early for this."

    sage "But I should probably get a gauge of what's happening in the world before I go to work."

    #Image of one page of the newspaper, filling practically the whole page. It has the headline “NEW MAGICAL BOTS DEVELOPED BY NIKOLAI ZHAMONOV—IS THIS THE END OF LIFE AS WE KNOW IT?”
    scene newsPaper1 #same as sageApartment but with overlay of the newspaper and car as bg blured
    show sage neutral
    sage "Huh. Interesting."

    sage "There’s been a lot of talk about how dangerous new technology can be…"

    sage "The talk’s been around for forever, though. Never thought it might actually come to fruition."

    "She flips the page."
    
    #Image of next page of the newspaper with the headline “LOCAL MAN ARRESTED FOR STRANGLING A GOOSE”
    scene newsPaper2
    show sage nervous
    sage "I’ll pretend I didn’t see that one."
 
    "She flips the page."
    scene newsPaper3
    #Image of the next page with fashion and outfits. Or something that’s easier to draw idk.
    # "She flips past the next few pages." <- could replace animation with this line and scene sageCar
    show sage neutral
    scene newsPaperFlip
    show sage neutral
    "Boring, boring, boring…"

    #Image of a newspaper with an old picture of Kai with the header “MAN FOUND WITH ELECTRICAL SHOCKS ON HIS BODY”. The photo is just an amalgamation of vague colors and it’s not clear yet

    #"She stops flipping the page."
    scene newsPaperKai
    show sage nervous
    sage "Wait…"

    "She looks closer."
    # Zoomed in image of Kai
    scene newsPaperZoom
    show sage scared
    sage "Is that—"

    "A phone call rings."
    scene sageCar
    show sage neutral
    "The call is from her mother."

    "She picks up."

    sage "Hello?"

    mom "Hey, Sage."

    "Something in her voice sounds hesitant."

    sage "…Yeah?"

    mom "Okay, there’s been some news."

    mom "(God, I wish I could talk to you in person right now.)"

    mom "But there’s been a development." 
    
    "Suddenly, dread creeps up her throat." 

    "She picks up the newspaper again, raising it to read it—"

    mom "Do you remember your childhood friends? The ones you always went to the treehouse with?"

    "Sage can’t seem to open her mouth to talk. She feels frozen in place."

    mom "Kai is dead."

    #"—and she sees the photo."

    # Zoom in to the newspaper. Image of Kai smiling. 
    # Should probably do the zoom in here instead or js get rid of the "--and she sees the photo." - Nicaiah
    show sage scared
    mom "I’m so sorry."

    mom "I know that—"
    show sage neutral
    "Sage hangs up."
    show sage angry
    "Anger builds and bubbles in her."

    sage "'Sorry'?"

    sage "What the hell would 'sorry' do now?"

    sage "It wouldn’t fucking save him, that’s for sure."

    sage "My best friend for the first thirteen years of my life. He was there for more than half my existence."
    show sage neutral
    "She closed her eyes."

    "The world around her suddenly seemed too loud and unwieldy, and she wanted to rip the newspaper to shreds."
    "She hated the photo of Kai and all of his happiness, his stupid grin and the way she will never see it again."

    menu:
        "Go into action":
            sage "And I…need to do something."
            sage "I need to act."
            sage "The police didn’t even know the way he died." 

            sage "When was the last time I saw Kai?"
            sage "Or Jax or Tal?" 
            sage "…"
            sage "We have a group chat, but I don’t remember the last time I talked to them. "
            "The realization hits her like a ton of bricks."
            sage "…God."


        "Read the rest of the newspaper":
            $ readNewspaper = true
            
            "She skims the rest of the newspaper."

            "Twenty-one year old Kai Elsher died on May 24th. He had a peaceful death in the hospital, being tended to by a team of medical professionals. His medical costs were covered by his parents and an anonymous patron."

            "He came to the hospital with electrical shocks spotting his entire body, unconscious. He never got to wake up."

            sage "Electricity?"

            sage "But how?"

            sage "I haven’t heard about it being used in ages. Once magic replaced it, nobody saw a use for it anymore."

            "She continues reading."

            "So, how did an outdated source of energy injure him in his last moments? This is a question experts are still pondering."

            "Locals have been theorizing how he could’ve died."

            "Sixty-two year old Paul Goodman says, ‘It’s one of those goddamn gangs. I’ve seen so much increased criminal activity around here. Just last Tuesday, I got robbed! I bet one of those wicked crooks are experimenting with electricity now.’"

            "Another local agrees, saying—"

            "She closes the newspaper."

            sage "…What?" 

            sage "They’re making conspiracy theories on his death?"

            sage "They don’t even know anything about him. They’ve never seen him in person, or heard him rant about types of worms in second grade. Nothing."

            sage "They don’t know about the treehouse."

            sage "Nothing! Absolutely nothing!"

            "Vaguely, Sage realizes that she’s shaking. She takes a breath, trying to calm herself down."


#[Return to the menu with choices. Have to choose the other choice before continuing.]
#So you have to choose both? you only decide on if you read newspaper or "go into action" first? if so 
#the "go into action" option needs a diff name lol - Nicaiah

#[Options merge here]

    sage "And my friends…"

    "A sense of urgency hit her."

    sage "Oh my god, I need to see them. Now."

    sage "Even if it’s just making sure they’re still alive, I need to go. Just for today."

    sage "I’ll call in sick for work. I know I wrote their addresses down in a notebook somewhere; I just need to hope they haven’t moved houses since high school."
    
    "Her eyes started getting watery, but she quickly wiped them away, sniffling. It didn’t matter what she felt at the moment."

    sage "I can’t let Tal and Jax do this alone. I have to…be there for them. "



#scene 3 - Tal's House
    scene talHouse
    show sage nervous
    "Sage takes a deep breath."
    sage "I haven’t been here in so long… I never even knew what the inside of his house looked like. He only ever let Jax in."
    menu:
        "Knock on do. or":
            #knocking sound effect
            "Nobody responds."
   
    menu: 
        "Knock on door":
            #knocking sound effect
            "..."
    
    "Sage double-checks the address. It's definitely Tal's."
    "There’s an old, deflated basketball in the front yard."

    show sage neutral at left
    sage "Tal…?"
    "The door opens."
    show tal neutral at right
    "She doesn’t recognize him at first. He's looking down at his shoes, and slowly he drags his gaze up until he meets her gaze." 
    "His eyes haven't changed."
    tal "Sage?"
    sage "Yeah, hey. It’s been a while."
    tal "What are you doing here?"
    sage "Have you heard about it?"
    tal "What?"
    "Sage’s heart drops."
    sage "Oh. In that case, I need to deliver some news to you."
    tal "Okay, you’re scaring me a little bit. What is it?"
    sage "Can I come in?"
    "Tal sends her a strange look."
    tal "Sure."

    #scene 3b
    scene talHouse #need the art for inside tal's house
    show sage nervous at left
    show tal neutral at right
    "He leads her into his house, clearing the kitchen table and sitting across from her."

    "On the kitchen table is a stain that smells like beer, and the faint scent of cigarette smoke. He scoops up a pile of ash and claps his hands above a trash can, and the particles float down like doldrums."

    sage "How have you been?"

    "Tal doesn't look like he registers her words at first. He blinks, and for a moment she’s scared he isn't fully lucid."

    tal "Oh, I’m fine."

    "He downs a half finished can of beer, tossing it into the bin once he shakes the last drops out. He rummages around under the table and brings out two bottles."

    "His eyes are watery."

    tal "Want?"

    sage "I'm good."

label menu1:
    menu: 
        "Make small talk.":
                sage "Do you drink this often?"

                tal "Oh, no, no. Just sometimes. I like having a bottle every other day, and one at the end of the week, just to help the start of the next one."

                sage "Right, I see. How's your mother doing?"

                tal "She's alright, but I haven’t seen her in a while."

                tal "She calls sometimes. It’s nice talking to her."

                sage "…"

                sage "What happened to your face?"

                tal "It's a condition."

                sage "From where?"

                tal "It's eczema—hey, look, Sage, I know you came here for some reason."

                tal "What is it? What do you have to tell me?"

                jump menu1

        "Break the news to him":
                sage "So, do you remember Kai?"

                tal "How can I not?"

                "She takes a deep breath."

                sage "He's dead."

                "Tal's face doesn't change. There's only a twitch to his eyebrows, and his eyes get more watery."

                "He is probably drunk."

                sage "It was in the news, on the front page."

                sage "I just felt like you should know."

                sage "I need to go to Jax later. Have you talked to him recently? I haven’t seen in a while."

                tal "Jax?"

                pass

    show tal angry
    tal "Of course I haven't talked to him, Sage."

    tal "He grew up. So did you. We haven’t talked in ages."

    tal "He used to say we’d be friends forever, too."

    tal "So, I guess that’s just so funny, huh? Jax left and Kai did too. Did you ever keep in touch with him?"

    sage "We didn't."

    "Tal smiles."

    tal "Oh, I bet that feels so awful."

    tal "Haven’t talked to him in a while and suddenly his corpse shows up on the front page? God."

    "He sets the beer bottle down with a thud. The liquid suddenly seems electrified, swimming with energy."

    sage "He was your friend too."

    "Something in his face seems to change."

    tal "Is that all?"

    menu:
        "Comfort him":
            sage "I know it’s hard, Tal, but I know things can improve from here."

            sage "I’m sorry we left you. I guess life just happened and we all got caught up in its whirlwind."

            tal "That’s not an excuse."

            sage "It’s not, but it’s an apology."
            
        "Don't comfort him.":
            sage "Yeah."

    tal "Alright, then. You should go now."

    "An idea strikes her."

    sage "I'll see you soon?"

    tal "For what?"

    sage "I'm going to go to Kai’s house later. Want to meet me there at twelve?"

    tal "A whole two hours from now? But Kai’s place isn’t too far from here."

    sage "Yeah, I have to go to Jax’s house first."

    tal "Why?"

    sage "Because we're friends."

    tal "…"

    tal "See you, Sage."

# Scene 4: Jax’s House
    scene jaxHouse

    show sage nervous at left
    show jax neutral at right

    jax "Come, take a seat."

    jax "If you came to tell me about Kai, I already know."

    sage "What?"

    show jax worry

    jax "Yeah, I saw it in the news."

    show jax neutral

    jax "I don’t usually look at the newspaper, but I saw it as I was about to throw it out."

    show sage neutral

    sage "Oh."

    show jax worry

    jax "…"

    jax "Can you give me a sec? (Cough)"

    sage "Oh. Uh… sure."

    hide jax worry

    show sage neutral at center

    "Jax leaves. Now it's just Sage here."
    
    "..."

    show sage nervous at center
    
    "A bit awkward, isn't it."

    "When Jax comes back, it looks like he's just cried."

    show jax worry at right
    show sage nervous at left

    jax "…It’s so tragic. He was barely an adult, and he’s already gone?"

    jax "God, it’s depressing."

    jax "I don’t really know anything about his life and what he did, but I know he was doing big things."

    jax "It’s one of those feelings, you know?"

    menu:
        "Express anger":
            show sage angry
            sage "That newspaper was so disgusting; I couldn’t finish it."

            sage "They are making sport of him, weren’t they?"

            sage "With their weird conspiracy theories, treating him like he’s just some object of gossip."

            sage "Gangs experimenting with electricity? Who the hell believes that?"
            show jax anger
            jax "I wanted to throw up when I read it."

            jax "I don’t know what type of person would write that type of article."
            show jax worry
            jax "…But I have no idea how he would be killed from electricity, either."
        "Express grief":
            show sage nervous 
            sage "I…couldn’t believe he died."

            sage "He was one of my best friends."

            sage "I miss him. A lot."
            
            jax "I’m sorry, Sage."

            sage "Yeah, well, I’m sorry for you as well."

    show sage neutral
    sage "Are you going to work today?"

    "Jax looks conflicted."

    jax "Yeah. My shift’s in the afternoon, so I’ll be going soon."

    sage "What if you call in sick today?"
    show jax shock
    jax "What?"
    show sage nervous
    sage "I talked to Tal today, and he wasn’t looking good."

    sage "There were bottles of alcohol completely filling up his garbage can."

    sage "His eyes…seemed unfocused."
    show jax worry
    sage "I don’t think he’d gotten out of bed in a while, but he still seemed so tired."

    "Jax was leaning forward. His hands were clutching the sofa tightly."

    jax "What did he say?"

    sage "Just pretended he was fine and—and broke down after I told him the news."

    jax "He’s not okay."

    sage "He’s not."
    show sage neutral
    sage "What I think we have to do is get together. You saw that newspaper, right? Those reporters didn’t know anything about where that electricity came from."

    sage "I just want closure right now. Maybe his parents know something about it or have stories about Kai that they’d want to share."

    sage "I think it would be appropriate. All of us getting together, even if it’s just for today."
    show jax neutral
    jax "And you also think it would be better to try to recover together."

    sage "…Well, yeah, especially since Tal didn’t look great and you probably don’t feel great either."

    sage "But I think it’d be important for all of us."

    sage "Something just feels…terrifying now, knowing that Kai isn’t with us anymore."
    show jax happy
    jax "I feel the same way."

    "Jax looks like he’s thinking through something."

    jax "Okay. I’ll call my boss right now."

    jax "I’m sure he’ll understand if I explain the circumstances to him."
    show sage happy
    sage "Thank you so much, Jax."

    sage "Meet me at Kai’s house in thirty minutes."

# Scene 5: Treehouse Interior
    scene kaiTreehouse
    show tal neutral at left
    show sage neutral at center
    show jax neutral at right
    jax "It's been so long."

    "The treehouse has changed since Sage was a child: the far corner has a desk now, the walls have more sketch-filled papers, one end has been renovated to fit a giant map."

    sage "...Yeah."
    sage "I should've visited more."

    "Tal takes in the scene and swallows hard."

    tal "Me too. I just wish…"

    "He looks away."

    sage "It was really nice of his moms to let us visit again."

    jax "Yeah. What did you tell them?"

    sage "That we want to…god, I feel so bad."

    sage "I just said we wanted to ask some questions and get closure."

    sage "I'll make them cookies. I'll…make scones and apple pie."

    jax "I'll make them cappuccinos."

    sage "They're probably in shock. I mean, your son leaves the house and never comes back, and then the next time you hear about him he's dead."

    jax "Yeah. Kai was…always like that, a little. So secretive about everything."

    sage "He could've said something. Or like, I don't know, I could've hung out with him more and he might've told me a secret and…"

    "Sage trails off and looks around."

    sage "June said he spent a lot of time here."

    sage "She said we could look around."

    "What do you look at?"

    menu: #make it so player has to explore all options
        "Map":
            scene map
            sage "Why do you think he circled those placed?"

            tal "Maybe they’re placed that are important to him."

            jax "It’d be strange if a forest is important to him."

            jax "All the places seemed pretty scattered, though."

            sage "Is that a lab that’s circled?"

            jax "Yeah. Fermi Laboratories."

            sage "I remember him telling me something about this. He worked there, I believe."

        "Textbooks on water":
            "There is a stack of textbooks on water on the desk."

            sage "Maybe he was learning about his own powers."

            sage "We’ve lived with them our whole lives. With a scientist like Kai, he must’ve gotten curious about it at some point."

            jax "Or not. Water is an important part of chemistry. And he’s bound to be more interested in water than the average person."

            tal "Whole textbooks on it, Jax? I’m not a scientist, but I don’t think I’d be obsessed with water specifically if I didn’t happen to also have water abilities."

        "Metal":

            "There were pieces of metal, in different shapes, in the corner."

            tal "Personally, I don’t know what to make of this."

            jax "Me neither."

            sage "Yeah, I mean, he was a scientist, and scientists do weird things. He was a chronic tinkler, I’m betting."

        "The newspaper":    
            scene newspaper #Picture of a clipping stuck to Kai’s journal, which is basically a yapfest on Nikolai Zhamonov

            sage "Oh this guy."

            tal "Who now?"

            sage "Nikolai Zhamonov… people at school are talking about him all the time. He’s making these advanced machines and stuff…"

            jax "Why does Kai care?"

            sage "… Fantastic point."

            tal "…"

            tal "Maybe Kai had a crush."

            sage "A crush?"

            tal "He doesn’t even look that good, though."

            jax "Says Nikolai is an engineer. That’s in the same vein as science, and Kai studied bio."

            jax "Maybe they were friends?"

            sage "We were his friends."

            jax "…"

            tal "…"

            tal "That’s a pretty bold statement. At this point."

            jax "Uh, nevermind. Nikolai’s eight years older. Although maybe they were colleagues?"

            sage "He was probably just a role model. Smart guy and all that."

            jax "Yeah, probably."

    "After they finished looking, Tal goes off and looks at the spot where he and Jax used to play."

    "Sage and Jax look under the textbooks."

    "There are annotated pictures of Sage, Jax, and Tal."

    #[The music stops.]

    sage "Oh wow."

    jax "Huh."

    "She looks closer at the words scribbled on the side of each photograph."

    "Which one should she read first?"

    menu: #make it so that player has to explore all options
        "Jax":
            "It’s a picture of Jax in middle school holding a baseball bat. He looks proud."

            sage "Jax: fire, couldn’t hold fire for more than five seconds due to asthma, could only create fire the size of his fist."

            jax "I didn’t know he was observing me that closely."

            jax "That information was true when I was ten, but I think my power has gotten a bit better."

        "Sage":
            "It’s a picture of Sage in middle school bending down next to a squirrel. She’s smiling."

            sage "Sage: talks to animals, can seem to only speak to smaller animals, cannot make demands of them but can convince them."

            sage "I used to think I could grow up to be an amazing spy because of that."

            jax "You still can."

            sage "Sure, but I’d just get arrested for that now."

        "Tal":
            "It’s a picture of Tal in middle school. He is chasing after the person behind the camera, his arms and legs a blur. He’s trying to hide a smile."

            "Tal's photograph has a lot more circles, question marks, and exclamation marks on it."

            sage "Tal: electricity. Often needs to ‘recharge' between shocks, could only mildly shock three to four times before becoming exhausted."

            jax "Hold on, check the back of the photo. I think I saw something."

            "Sage flips the photograph, and there’s some notes written there."

            sage "Lots of information about electricity has been lost. How much would need to be used to light a lamp? To power a vehicle? What about if he ever used his power on something metallic? How far could his electricity spread, and does it differ from normal electricity in any way?"

            jax "He really seemed interested in electricity."

    june "Hey, kids, I know you’re looking around, but I’ve got some lemonade made for you all."

    june "I’ll be in the living room."

    tal "I’ll be down in a second."

    "Tal turns to Sage and Jax."

    tal "You two coming too?"

    "Jax looks at the photographs in his hand."

    jax "Tal—"

    show tal neutral

    tal "What."

    jax "Nevermind. You can go."

    "Tal doesn’t spare Jax or Sage a second look before he leaves."

    hide tal neutral

    sage "I genuinely didn't know Kai still cared about this stuff—his abilities and everything. The last time I saw him he could barely summon a puddle of water."

    jax "I think he was trying to figure out more stuff about his powers. But… why?"

    sage "Because he's Kai. Look at this – biochemistry, a guide to different types of ponds and rain clouds. He went all-out."

    jax "Yeah. Once he got obsessed with something, that was it. Remember that time he had his lizard phase?"

    tal "He was really interested in us, too."

    "The two of them look at the pictures of when all four of them had been so much younger."

    jax "I kinda thought he forgot about us. Why did he never say anything?"

    sage "…"

    jax "What?"

    sage "He did say something."

    jax "Is there something you didn't tell me?"

    sage "Two years ago he wrote me a letter. Talking about how maybe we could hang out sometime, and his school was finally letting up on his exams."

    jax "Did you respond?"

    sage "I said maybe sometime. But I never really followed up."

    sage "I keep thinking about that day. What if he felt lonely, Jax? What if he was looking at all of us and our powers because he wanted for us to be together again and he didn't know how to ask?"

    sage "Do you think he…killed himself?"

    jax "No, what?"

    jax "Electricity killed him. Don’t you think there are easier ways to commit suicide?"

    jax "Why would he go for electricity?"

    jax "…"

    jax "Kai never wrote me a letter, but…did he seem sad in the letter?"

    sage "I don't remember. Not really, I guess, but being sad isn't obvious sometimes."

    "Jax nods, pondering for a moment."

    jax "Sage, it's not your fault."

    "After a moment, Sage steels herself and nods stiffly."

    sage "It was weird seeing the pictures of us, with all of the notes on them."

    jax "We should show Tal, maybe ask him what he thinks. It is a picture of him, after all."

    sage "Yeah, definitely."


#scene 5 - Kai's Treehouse
    scene outside treehouse
#scene 6 - Outside Treehouse
    scene city
#scene 7 - In the City
    scene hospital
#scene 8 - Hospital
    scene college
#scene 9 - College
    scene witch house
#scene 10 - Witch
    scene witch exp room
#scene 11 - Witch's House
#scene 12 - Witch's Experimentation Room
#scene 13 - Forest
#scene 14 - Witch's House
#scene 15 - Witch's Experimentation Room
#Ending 1
#Ending 2
#Ending 3


    # This ends the game.

    return
