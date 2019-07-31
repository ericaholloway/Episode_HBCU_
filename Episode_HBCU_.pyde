import scene_1
import scene_2
import scene_3
import scene_4
import speech
import left_convo_2
import right_convo_2
import bubble_class

def setup():
    size(1400, 750)
    global scene
    global bubble
    global bubble_c
    global texts
    global classroom
    global dialogue
    global dialogue_c
    global goToNextScene
    global goToNextBubble
    global speech_x
    global speech_y

    img = loadImage("sky.png")
    image(img, 0, 0, 1400, 750)

    # episode
    f = createFont("Pacifico-Regular.ttf", 150)
    textFont(f)
    fill(0, 0, 0)
    text("Episode", 450, 350)
    
    # HBCU Edition
    h = createFont("Nosifer-Regular.ttf", 50)
    textFont(h)
    fill(179, 7, 7)
    text("H", 425, 450)
    fill(14, 117, 26)
    text("B", 475, 450)
    fill(0, 0, 0)
    text("C", 525, 450)
    fill(250, 219, 20)
    text("U", 575, 450)
    fill(0, 0, 0)
    text("Edition", 675, 450)

    # click s to start
    c = createFont("Inconsolata-Regular.ttf", 50)
    textFont(c)
    fill(0, 0, 0)
    text("Click 's' to Start", 460, 650)
    scene = 1
    bubble = 1
    bubble_c = 1
    goToNextScene = True
    goToNextBubble = True
    
    #Texts for scene two in front of FAMU
    dialogue = 0
    texts = [
             {
              "talk": "Hey Penny girl!! Can you \nbelieve we are in college now? \nI am so excited! No parents, no rules,\nand a whole lot of fun, girl! \nIt's about to be a act up school year!",
              "x":70,
              "y":210
              },
              {
              "talk": "LOL hey Dijonay! ",
              "x":970,
              "y":260
              },
              {
              "talk": " Have you heard of this twitter \naccount named HBCU confessions?? \nIT'S WILD GIRL!",
              "x":70,
              "y":240
              },
              {
              "talk": "No I haven't.",
              "x":970,
              "y":260
              },
              {
              "talk": "Oh wow! That really is crazy.",
              "x":970,
              "y":260
              },
              {
              "talk": "IK GIRL!! I can spend all day reading \nthese things they're so juicy.  ",
              "x":70,
              "y":240
              },
              {
              "talk": "Well I can't, I've gotta go to class. \nI'll catch you later Dijonay. ",
              "x":960,
              "y":260
              },
              {
              "talk": "Alright, bye Penny girl!",
              "x":70,
              "y":210
              },
             ]
    
    
    
    
    #texts for classroom
    dialogue_c = 0        
    classroom = [
            {
              "talk": "Good morning class I am Mrs. Grant, \nwelcome to African American Studies! \nHas everyone done the summer reading? ",
              "x":700,
              "y":260
              },
              {
              "talk": " OMG!! I never even knew that we had\n summer reading!! Should I ….",
              "x":70,
              "y":210
              },
              {
              "talk": "Excuse me Mrs. Grant, I didn't\n to the reading.",
              "x":700,
              "y":260
              },
              {
              "talk": "Thats ok, I appreciate your honesty. \nYou can take the pop quiz next week.",
              "x":70,
              "y":210
              },
              {
              "talk": "Yes ",
              "x":700,
              "y":260
              },
              {
              "talk": "OK great! So everyone has done the \nreading! Time for a pop quiz!! ",
              "x":70,
              "y":210
              },
             ]



def draw():
# SECOND SCENE
    global scene
    global dialogue
    global dialogue_c
    global bubble
    global bubble_c
    global texts
    global classroom
    global goToNextScene
    global goToNextBubble
    global speech_x
    global speech_y
#SCENE 1
    if keyPressed and key == 's' and scene == 1 and goToNextScene == True:
        scene_1.scene_1()
        scene += 1
        goToNextScene = False
        print("clicked once", scene)





#SCENE 2
    elif keyPressed and key == 's' and scene == 2 and goToNextScene == True:
        scene_2.scene_2()
        fill (134, 222, 27, 160)
        rect(100, 50, 310, 50)
        n= createFont ("Ubuntu-Medium.ttf",18)
        textFont(n)
        fill (0, 0, 0)
        text("Click 'C' to continue the conversation",100, 80)
        scene += 1
        goToNextScene = False
        print("clicked twice", scene)
#Left SPEECH BUBBLE
    if keyPressed and key == 'c' and goToNextBubble == True and ((bubble % 2 == 1 and bubble <= 4) or (bubble % 2 == 0 and bubble > 8 and bubble < 12 )) :
        left_convo_2.left_convo_2()
        blurb = texts[dialogue]
        words = blurb["talk"]
        x = blurb ["x"]
        y = blurb ["y"]
        n= createFont ("RobotoCondensed-Bold.ttf",20)
        textFont(n)
        text(words,x,y)
        print("1dialogue")
        fill (134, 222, 27, 160)
        rect(100, 50, 310, 50)
        n= createFont ("Ubuntu-Medium.ttf",18)
        textFont(n)
        fill (0, 0, 0)
        text("Click 'C' to continue the conversation",100, 80)
        dialogue += 1
        bubble += 1
        goToNextBubble = False
#Right SPEECH BUBBLE
    elif keyPressed and key == 'c' and goToNextBubble == True and ((bubble%2 == 0 and bubble <= 4) or (bubble % 2 == 1 and bubble > 8 and bubble < 12)):
        right_convo_2.right_convo_2()
        blurb = texts[dialogue]
        words = blurb["talk"]
        x = blurb ["x"]
        y = blurb ["y"]
        n= createFont ("RobotoCondensed-Bold.ttf",20)
        textFont(n)
        text(words,x,y)
        print("2dialogue")
        fill (134, 222, 27, 160)
        rect(100, 50, 310, 50)
        n= createFont ("Ubuntu-Medium.ttf",18)
        textFont(n)
        fill (0, 0, 0)
        text("Click 'C' to continue the conversation",100, 80)
        dialogue += 1
        bubble += 1
        goToNextBubble = False
#CLICK 'C' CHANGES TO CLICK 'T'
    elif goToNextBubble == True and bubble == 5:
        fill (220, 61, 235, 250)
        rect(100, 50, 310, 50)
        n= createFont ("Ubuntu-Medium.ttf",18)
        textFont(n)
        fill (0, 0, 0)
        text("Click 'T' to read the tweet",100, 80)
        bubble += 1
        goToNextBubble = False


#CONFESSION 1
    if keyPressed and key == 't' and goToNextBubble == True  and bubble == 6:
        #iPhone
        img = loadImage("iphone2.PNG")
        image(img, 250, 0, 850, 750)
        #Tweet
        img = loadImage("confess1.PNG")
        image(img, 506, 100, 358, 543)
        print ("hbcu1")
        bubble += 1
        goToNextBubble = False
#CONFESSION 2
    elif keyPressed and key == 't' and goToNextBubble == True  and bubble == 7:
        #iPhone
        img = loadImage("iphone2.PNG")
        image(img, 250, 0, 850, 750)
        #Tweet
        img = loadImage("confess2.PNG")
        image(img, 506, 100, 358, 543)
        print ("hbcu2")
        bubble += 1
        goToNextBubble = False
#CONFESSION 3
    elif keyPressed and key == 't' and goToNextBubble == True  and bubble == 8:
        #iPhone
        img = loadImage("iphone2.PNG")
        image(img, 250, 0, 850, 750)
        #Tweet
        img = loadImage("confess3.PNG")
        image(img, 506, 100, 358, 543)
        fill (134, 222, 27, 240)
        rect(100, 50, 310, 50)
        n= createFont ("Ubuntu-Medium.ttf",18)
        textFont(n)
        fill (0, 0, 0)
        text("Click 'C' to continue the conversation",100, 80)
        print ("hbcu3")
        bubble += 1
        goToNextBubble = False
#CLICK 'S' TO GO TO THE NEXT SCREEN
    elif bubble == 12 and goToNextBubble == True:
        fill (240, 10, 63, 250)
        rect(100, 50, 310, 50)
        n= createFont ("Ubuntu-Medium.ttf",18)
        textFont(n)
        fill (0,0,0)
        text("Click 'S' to go to class",100, 80)
        dialogue += 1
        bubble += 1
        goToNextBubble = False









#TRANSITION FROM CONFESSION SCREEN BACK TO THE SCENE 3

    if keyPressed and key == 's' and scene == 3 and goToNextScene == True and bubble == 13:
        scene_3.scene_3()
        fill (134, 222, 27, 160)
        rect(100, 50, 310, 50)
        n= createFont ("Ubuntu-Medium.ttf",18)
        textFont(n)
        fill (0, 0, 0)
        text("Click 'C' to continue the conversation",100, 80)
        bubble+=1
        scene += 1
        goToNextScene = False
        print("clicked 3 times", scene)


#TALKING IN THE CLASSROOM
        #Right SPEECH BUBBLE
    if keyPressed and key == 'c' and goToNextBubble == True and bubble_c % 2 == 1 and bubble_c == 1:
        bubble_class.bubble_class()
        blurb_c = classroom[dialogue_c]
        words_c = blurb_c["talk"]
        x = blurb_c ["x"]
        y = blurb_c ["y"]
        n= createFont ("RobotoCondensed-Bold.ttf",20)
        textFont(n)
        text(words_c,x,y)
        print("1dialogue classroom")
        fill (134, 222, 27, 160)
        rect(100, 50, 310, 50)
        n= createFont ("Ubuntu-Medium.ttf",18)
        textFont(n)
        fill (0, 0, 0)
        text("Click 'C' to continue the conversation",100, 80)
        dialogue_c += 1
        bubble_c += 1
        goToNextBubble = False
        
    if keyPressed and key == 's' and scene == 4 and goToNextScene == True:
        scene_4.scene_4a()
        scene += 1
        
        
def keyReleased():
    global goToNextScene
    global goToNextBubble
    goToNextScene = True
    goToNextBubble = True
    
