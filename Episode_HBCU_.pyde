import scene_1
import scene_2
import scene_3
import scene_4
import scene_5
import scene_6
import think
import speech
import left_convo_2
import right_convo_2
import bubble_class
import bubble_class_1
import think_class

def setup():
    size(1400, 750)
    global scene
    global bubble
    global bubble_c
    global bubble_t
    global texts
    global classroom
    global tree
    global dialogue
    global dialogue_c
    global dialogue_t
    global goToNextScene
    global goToNextBubble
    global think_x
    global think_y
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
    bubble_t = 1
    goToNextScene = True
    goToNextBubble = True

    # Texts for scene two in front of FAMU
    dialogue = 0
    texts = [
        {
            "talk": "Hey Penny girl!! Can you \nbelieve we are in college now? \nI am so excited! No parents, no rules,\nand a whole lot of fun, girl! \nIt's about to be a act up school year!",
            "x": 70,
            "y": 210
        },
        {
            "talk": "LOL hey Dijonay! ",
            "x": 970,
            "y": 260
        },
        {
            "talk": " Have you heard of this twitter \naccount named HBCU confessions?? \nIT'S WILD GIRL!",
            "x": 70,
            "y": 240
        },
        {
            "talk": "No I haven't.",
            "x": 970,
            "y": 260
        },
        {
            "talk": "Oh wow! That really is crazy.",
            "x": 970,
            "y": 260
        },
        {
            "talk": "IK GIRL!! I can spend all day reading \nthese things they're so juicy.  ",
            "x": 70,
            "y": 240
        },
        {
            "talk": "Well I can't, I've gotta go to class. \nI'll catch you later Dijonay. ",
            "x": 960,
            "y": 260
        },
        {
            "talk": "Alright, bye Penny girl!",
            "x": 70,
            "y": 210
        },
    ]

    # texts for classroom
    dialogue_c = 0
    classroom = [
        {
            "talk": "Good morning class I am Mrs. Grant, \nwelcome to African American Studies! \nHas everyone done the summer reading? ",
            "x": 560,
            "y": 100
        },
        {
            "talk": " OMG!! I never even knew that we had\n summer reading!! Should I...",
            "x": 400,
            "y": 100
        },
        {
            "talk": "Excuse me Mrs. Johnson, I didn't\n do the reading.",
            "x": 100,
            "y": 100
        },
        {
            "talk": "Thats ok, I appreciate your honesty. \nYou can take the pop quiz next week.",
            "x": 530,
            "y": 100
        },
        {
            "talk": "Yes ",
            "x": 100,
            "y": 100
        },
        {
            "talk": "OK great! So everyone has done the \nreading! Time for a pop quiz!! ",
            "x": 530,
            "y": 100
        },
    ]

    dialogue_t = 0
    tree = [
        {
            "talk": "I am so glad that I was honest today in class",
            "x": 360,
            "y": 250
        },
         {
            "talk": "I can't believe I failed my first quiz...\nI dont think this day can get any worse.",
            "x": 370,
            "y": 230
        },
        {
            "talk": "Penny, what do you think you're doin?",
            "x": 530,
            "y": 100
        },
        {
            "talk": "I'm just sitting down.",
            "x": 100,
            "y": 250
        },
        {
            "talk": "Well, little girl, you should not be sitting \nhere!! This is my sorority plot. Now get off!!.",
            "x": 530,
            "y": 100
        }
    ]


def draw():
# SECOND SCENE
    global scene
    global dialogue
    global dialogue_c
    global dialogue_t
    global bubble
    global bubble_c
    global bubble_t
    global texts
    global classroom
    global tree
    global goToNextScene
    global goToNextBubble
    global think_x
    global think_y
    global speech_x
    global speech_y
# SCENE 1
    if keyPressed and key == 's' and scene == 1 and goToNextScene == True:
        scene_1.scene_1()
        scene += 1
        goToNextScene = False
        print("clicked once", scene)


# SCENE 2
    elif keyPressed and key == 's' and scene == 2 and goToNextScene == True:
        scene_2.scene_2()
        fill(134, 222, 27, 160)
        rect(100, 50, 310, 50)
        n = createFont("Ubuntu-Medium.ttf", 18)
        textFont(n)
        fill(0, 0, 0)
        text("Click 'C' to continue the conversation", 100, 80)
        scene += 1
        goToNextScene = False
        print("clicked twice", scene)
# Left SPEECH BUBBLE
    if keyPressed and key == 'c' and goToNextBubble == True and ((bubble % 2 == 1 and bubble <= 4) or (bubble % 2 == 0 and bubble > 8 and bubble < 12)):
        left_convo_2.left_convo_2()
        blurb = texts[dialogue]
        words = blurb["talk"]
        x = blurb["x"]
        y = blurb["y"]
        n = createFont("RobotoCondensed-Bold.ttf", 20)
        textFont(n)
        text(words, x, y)
        print("1dialogue")
        fill(134, 222, 27, 160)
        rect(100, 50, 310, 50)
        n = createFont("Ubuntu-Medium.ttf", 18)
        textFont(n)
        fill(0, 0, 0)
        text("Click 'C' to continue the conversation", 100, 80)
        dialogue += 1
        bubble += 1
        goToNextBubble = False
# Right SPEECH BUBBLE
    elif keyPressed and key == 'c' and goToNextBubble == True and ((bubble % 2 == 0 and bubble <= 4) or (bubble % 2 == 1 and bubble > 8 and bubble < 12)):
        right_convo_2.right_convo_2()
        blurb = texts[dialogue]
        words = blurb["talk"]
        x = blurb["x"]
        y = blurb["y"]
        n = createFont("RobotoCondensed-Bold.ttf", 20)
        textFont(n)
        text(words, x, y)
        print("2dialogue")
        fill(134, 222, 27, 160)
        rect(100, 50, 310, 50)
        n = createFont("Ubuntu-Medium.ttf", 18)
        textFont(n)
        fill(0, 0, 0)
        text("Click 'C' to continue the conversation", 100, 80)
        dialogue += 1
        bubble += 1
        goToNextBubble = False
# CLICK 'C' CHANGES TO CLICK 'T'
    elif goToNextBubble == True and bubble == 5:
        fill(220, 61, 235, 250)
        rect(100, 50, 310, 50)
        n = createFont("Ubuntu-Medium.ttf", 18)
        textFont(n)
        fill(0, 0, 0)
        text("Click 'T' to read the tweet", 100, 80)
        bubble += 1
        goToNextBubble = False


# CONFESSION 1
    if keyPressed and key == 't' and goToNextBubble == True and bubble == 6:
        # iPhone
        img = loadImage("iphone2.PNG")
        image(img, 250, 0, 850, 750)
        # Tweet
        img = loadImage("confess1.PNG")
        image(img, 506, 100, 358, 543)
        print ("hbcu1")
        bubble += 1
        goToNextBubble = False
# CONFESSION 2
    elif keyPressed and key == 't' and goToNextBubble == True and bubble == 7:
        # iPhone
        img = loadImage("iphone2.PNG")
        image(img, 250, 0, 850, 750)
        # Tweet
        img = loadImage("confess2.PNG")
        image(img, 506, 100, 358, 543)
        print ("hbcu2")
        bubble += 1
        goToNextBubble = False
# CONFESSION 3
    elif keyPressed and key == 't' and goToNextBubble == True and bubble == 8:
        # iPhone
        img = loadImage("iphone2.PNG")
        image(img, 250, 0, 850, 750)
        # Tweet
        img = loadImage("confess3.PNG")
        image(img, 506, 100, 358, 543)
        fill(134, 222, 27, 240)
        rect(100, 50, 310, 50)
        n = createFont("Ubuntu-Medium.ttf", 18)
        textFont(n)
        fill(0, 0, 0)
        text("Click 'C' to continue the conversation", 100, 80)
        print ("hbcu3")
        bubble += 1
        goToNextBubble = False
# CLICK 'S' TO GO TO THE NEXT SCREEN
    elif bubble == 12 and goToNextBubble == True:
        fill(240, 10, 63, 250)
        rect(100, 50, 310, 50)
        n = createFont("Ubuntu-Medium.ttf", 18)
        textFont(n)
        fill(0, 0, 0)
        text("Click 'S' to go to class", 100, 80)
        dialogue += 1
        bubble += 1
        goToNextBubble = False


# TRANSITION FROM CONFESSION SCREEN BACK TO THE SCENE 3

    if keyPressed and key == 's' and scene == 3 and goToNextScene == True and bubble == 13:
        scene_3.scene_3()
        fill(134, 222, 27, 160)
        rect(100, 50, 310, 50)
        n = createFont("Ubuntu-Medium.ttf", 18)
        textFont(n)
        fill(0, 0, 0)
        text("Click 'C' to continue the conversation", 100, 80)
        bubble += 1
        scene += 1
        goToNextScene = False
        print("clicked 3 times", scene)


# TALKING IN THE CLASSROOM
        # Teacher's SPEECH BUBBLE
    if keyPressed and key == 'c' and goToNextBubble == True and bubble_c == 1:
        bubble_class.bubble_class()
        blurb_c = classroom[dialogue_c]
        words_c = blurb_c["talk"]
        x = blurb_c["x"]
        y = blurb_c["y"]
        n = createFont("RobotoCondensed-Bold.ttf", 20)
        textFont(n)
        text(words_c, x, y)
        print("1dialogue classroom")
        fill(134, 222, 27, 160)
        rect(100, 50, 310, 50)
        n = createFont("Ubuntu-Medium.ttf", 18)
        textFont(n)
        fill(0, 0, 0)
        text("Click 'C' to continue the conversation", 100, 80)
        dialogue_c += 1
        bubble_c += 1
        goToNextBubble = False
    elif keyPressed and key == 'c' and goToNextBubble == True and bubble_c == 2:
        think_class.think_class()
        fill(255, 255, 255, 180)
        rect(500, 332, 500, 50)
        n = createFont("Ubuntu-Medium.ttf", 18)
        textFont(n)
        fill(0, 0, 0)
        text(
            " 'A': \n Admit to the teacher that I haven't done summer reading", 500, 350)
        fill(255, 255, 255, 180)
        rect(500, 402, 520, 50)
        fill(0, 0, 0)
        text(
            " 'B': \n Act like I know what shes talking about and hope for the best ", 500, 420)
        blurb_c = classroom[dialogue_c]
        words_c = blurb_c["talk"]
        x = blurb_c["x"]
        y = blurb_c["y"]
        n = createFont("RobotoCondensed-Bold.ttf", 20)
        textFont(n)
        text(words_c, x, y)
        print("2dialogue classroom")
        dialogue_c += 1
        bubble_c += 1
        goToNextBubble = False


# CHOICE "A"
# Classroom scene
    if keyPressed and key == 'a' and goToNextBubble == True and dialogue_c == 2 and bubble_c == 3:
        bubble_class_1.bubble_class_1()
        blurb_c = classroom[dialogue_c]
        words_c = blurb_c["talk"]
        x = blurb_c["x"]
        y = blurb_c["y"]
        n = createFont("RobotoCondensed-Bold.ttf", 20)
        textFont(n)
        text(words_c, x, y)
        print("1dialogue classroom")
        fill(134, 222, 27, 160)
        rect(500, 50, 310, 50)
        n = createFont("Ubuntu-Medium.ttf", 18)
        textFont(n)
        fill(0, 0, 0)
        text("Click 'C' to continue the conversation", 500, 80)
        dialogue_c += 1
        bubble_c += 1
        goToNextBubble = False
    elif keyPressed and key == 'c' and goToNextBubble == True and dialogue_c == 3 and bubble_c == 4:
        bubble_class.bubble_class()
        blurb_c = classroom[dialogue_c]
        words_c = blurb_c["talk"]
        x = blurb_c["x"]
        y = blurb_c["y"]
        n = createFont("RobotoCondensed-Bold.ttf", 20)
        textFont(n)
        text(words_c, x, y)
        print("1dialogue classroom")
        fill(240, 10, 63, 250)
        rect(100, 50, 310, 50)
        n = createFont("Ubuntu-Medium.ttf", 18)
        textFont(n)
        fill(0, 0, 0)
        text("Click 'S' to go next the scene", 100, 80)
        dialogue_c += 1
        bubble_c += 1
        goToNextBubble = False




# TREE SCENE 5: Choice A
    
    elif keyPressed and key == 's' and scene == 4 and goToNextScene == True and dialogue_c == 4 and bubble_c == 5:
        print("scene 4", scene)
        scene_4.scene_4a()
        fill(134, 222, 27, 160)
        rect(100, 50, 310, 50)
        n = createFont("Ubuntu-Medium.ttf", 18)
        textFont(n)
        fill(0, 0, 0)
        text("Click 'C' to continue the conversation", 100, 80)
        bubble_c += 1
        scene += 1
        dialogue_c += 1
        dialogue_t = 0
        bubble_t = 1
        goToNextScene = False
        print("clicked 4 times", scene)
# PENNY'S THOUGHT BUBBLE
    elif keyPressed and key == 'c' and goToNextScene == True and bubble_t == 1 and dialogue_c == 5 and bubble_c == 6 and dialogue_t == 0:
        think_class.think_treea()
        blurb_t = tree[dialogue_t]
        words_t = blurb_t["talk"]
        x = blurb_t["x"]
        y = blurb_t["y"]
        n = createFont("RobotoCondensed-Bold.ttf", 20)
        textFont(n)
        text(words_t, x, y)
        print("1dialogue tree choice a")
        fill(134, 222, 27, 160)
        rect(100, 50, 310, 50)
        n = createFont("Ubuntu-Medium.ttf", 18)
        textFont(n)
        fill(0, 0, 0)
        text("Click 'C' to continue the conversation", 100, 80)
        goToNextBubble = False
        dialogue_t += 2
        dialogue_c += 1
        bubble_t += 1
        bubble_c += 1
        print("YAYYYY")
        return



# CHOICE B
    # Classroom scene
    if keyPressed and key == 'b' and goToNextBubble == True and bubble_c == 3:
        bubble_class_1.bubble_class_1()
        dialogue_c = 4
        blurb_c = classroom[dialogue_c]
        words_c = blurb_c["talk"]
        x = blurb_c["x"]
        y = blurb_c["y"]
        n = createFont("RobotoCondensed-Bold.ttf", 20)
        textFont(n)
        text(words_c, x, y)
        print("1dialogue classroom choice b")
        fill(134, 222, 27, 160)
        rect(500, 50, 310, 50)
        n = createFont("Ubuntu-Medium.ttf", 18)
        textFont(n)
        fill(0, 0, 0)
        text("Click 'C' to continue the conversation", 500, 80)
        dialogue_c += 1
        bubble_c += 1
        goToNextBubble = False
    elif keyPressed and key == 'c' and goToNextBubble == True and dialogue_c == 5 and bubble_c == 4:
        bubble_class.bubble_class()
        blurb_c = classroom[dialogue_c]
        words_c = blurb_c["talk"]
        x = blurb_c["x"]
        y = blurb_c["y"]
        n = createFont("RobotoCondensed-Bold.ttf", 20)
        textFont(n)
        text(words_c, x, y)
        print("1dialogue classroom")
        fill(240, 10, 63, 250)
        rect(100, 50, 310, 50)
        n = createFont("Ubuntu-Medium.ttf", 18)
        textFont(n)
        fill(0, 0, 0)
        text("Click 'S' to go next the scene", 100, 80)
        dialogue_c += 1
        bubble_c += 1
        goToNextBubble = False
    elif keyPressed and key == 's' and scene == 4 and goToNextScene == True and dialogue_c == 6 and bubble_c == 5:
        print("scene 4", scene)
        scene_4.scene_4a()
        fill(134, 222, 27, 160)
        rect(100, 50, 310, 50)
        n = createFont("Ubuntu-Medium.ttf", 18)
        textFont(n)
        fill(0, 0, 0)
        text("Click 'C' to continue the conversation", 100, 80)
        bubble_c += 1
        scene += 1
        dialogue_c += 1
        dialogue_t += 1
        goToNextScene = False
        print("clicked 4 times", scene)




# TREE SCENE 5: Choice B
    # PENNY'S THOUGHT BUBBLE
    elif keyPressed and key == 'c' and goToNextScene == True and bubble_t == 1 and bubble_c == 6 and dialogue_c == 7 and dialogue_t == 1:
        think_class.think_treeb()
        blurb_t = tree[dialogue_t]
        words_t = blurb_t["talk"]
        x = blurb_t["x"]
        y = blurb_t["y"]
        n = createFont("RobotoCondensed-Bold.ttf", 20)
        textFont(n)
        text(words_t, x, y)
        print("1dialogue tree")
        fill(134, 222, 27, 160)
        rect(100, 50, 310, 50)
        n = createFont("Ubuntu-Medium.ttf", 18)
        textFont(n)
        fill(0, 0, 0)
        text("Click 'C' to continue the conversation", 100, 80)
        dialogue_t += 1
        bubble_t += 1
        dialogue_c += 1
        bubble_c += 1
        goToNextBubble = False
        return
    

    if keyPressed and key == 'c' and goToNextScene == True and bubble_t == 2 and dialogue_t == 2 and ((dialogue_c == 6 and bubble_c == 7) or (bubble_c == 7 and dialogue_c == 8)) :
        bubble_class.bubble_tree()
        dialogue_t == 2
        blurb_t = tree[dialogue_t]
        words_t = blurb_t["talk"]
        x = blurb_t["x"]
        y = blurb_t["y"]
        n = createFont("RobotoCondensed-Bold.ttf", 20)
        textFont(n)
        text(words_t, x, y)
        print("1dialogue tree")
        fill(134, 222, 27, 160)
        rect(100, 50, 310, 50)
        n = createFont("Ubuntu-Medium.ttf", 18)
        textFont(n)
        fill(0, 0, 0)
        text("Click 'C' to continue the conversation", 100, 80)
        dialogue_t += 1
        bubble_t += 1
        dialogue_c += 1
        bubble_c += 1
        goToNextBubble = False
    elif keyPressed and key == 'c' and goToNextScene == True and bubble_t == 3 and dialogue_t == 3 and ((dialogue_c == 7 and bubble_c == 8) or (bubble_c == 8 and dialogue_c == 9)) :
        bubble_class_1.bubble_tree_1()
        blurb_t = tree[dialogue_t]
        words_t = blurb_t["talk"]
        x = blurb_t["x"]
        y = blurb_t["y"]
        n = createFont("RobotoCondensed-Bold.ttf", 20)
        textFont(n)
        text(words_t, x, y)
        print("2dialogue tree ")
        fill(134, 222, 27, 160)
        rect(100, 50, 310, 50)
        n = createFont("Ubuntu-Medium.ttf", 18)
        textFont(n)
        fill(0, 0, 0)
        text("Click 'C' to continue the conversation", 100, 80)
        dialogue_t += 1
        bubble_t += 1
        dialogue_c += 1
        bubble_c += 1
        goToNextBubble = False
    elif keyPressed and key == 'c' and goToNextScene == True and bubble_t == 4 and dialogue_t == 4 and ((dialogue_c == 8 and bubble_c == 9) or (bubble_c == 9 and dialogue_c == 10)) :
        bubble_class.bubble_tree()
        blurb_t = tree[dialogue_t]
        words_t = blurb_t["talk"]
        x = blurb_t["x"]
        y = blurb_t["y"]
        n = createFont("RobotoCondensed-Bold.ttf", 20)
        textFont(n)
        text(words_t, x, y)
        print("3dialogue tree ")
        fill(240, 10, 63, 250)
        rect(100, 50, 310, 50)
        n = createFont("Ubuntu-Medium.ttf", 18)
        textFont(n)
        fill(0, 0, 0)
        text("Click 'S' to go to next scene", 100, 80)
        dialogue_t += 1
        bubble_t += 1
        dialogue_c += 1
        bubble_c += 1
        goToNextBubble = False
    if keyPressed and key == 's' and scene == 5 and goToNextScene == True and bubble_t == 5:
        scene_5.scene_5()
        fill(240, 10, 63, 250)
        rect(100, 50, 310, 50)
        n = createFont("Ubuntu-Medium.ttf", 18)
        textFont(n)
        fill(0, 0, 0)
        text("Click 'S' to go to next scene", 100, 80)
        bubble_t += 1
        scene += 1
        goToNextScene = False
        print("clicked 5 times", scene)
    if keyPressed and key == 's' and scene == 6 and goToNextScene == True and bubble_t == 6:
        scene_6.scene_6()
        scene += 1
        goToNextScene = False
        print("clicked 5 times", scene)

        

    #elif keyPressed and key == 's' and scene == 4 and goToNextScene == True and dialogue_c == 7 and bubble_c == 5:
    #print(key, scene, goToNextScene, dialogue_c, dialogue_t, bubble_c, bubble_t)


def keyReleased():
    global goToNextScene
    global goToNextBubble
    goToNextScene = True
    goToNextBubble = True
