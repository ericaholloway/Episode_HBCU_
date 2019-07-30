import scene_1
import scene_2
import speech
import left_convo_2
import right_convo_2

def setup():
    size(1400, 750)
    global scene
    global bubble
    global texts
    global dialogue
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
    goToNextScene = True
    goToNextBubble = True
    
    #Texts
    dialogue = 0
    texts = [
             {
              "talk": "Hello 1",
              "x":70,
              "y":300
              },
              {
              "talk": "Hello 2",
              "x":900,
              "y":230
              },
              {
              "talk": "Hello 3",
              "x":10,
              "y":230
              },
              {
              "talk": "Hello 4",
              "x":900,
              "y":230
              }
             ]
    

def draw():
# SECOND SCENE
    global scene
    global dialogue
    global bubble
    global texts
    global goToNextScene
    global goToNextBubble
    global speech_x
    global speech_y

    if keyPressed and key == 's' and scene == 1 and goToNextScene == True:
        scene_1.scene_1()
        scene += 1
        goToNextScene = False
        print("clicked once", scene)
    elif keyPressed and key == 's' and scene == 2 and goToNextScene == True:
        scene_2.scene_2()
        speech.speech(10, 230)
        scene += 1
        goToNextScene = False
        print("clicked twice", scene)
    if keyPressed and key == 'c' and goToNextBubble == True and bubble % 2 == 1:
        right_convo_2.right_convo_2()
        while dialogue <= 3:
            blurb = texts[dialogue]
            words = blurb["talk"]
            x = blurb ["x"]
            y = blurb ["y"]
            text(words,x,y)
            print("dialogue")
            dialogue += 2
        bubble += 1
        goToNextBubble = False
    elif keyPressed and key == 'c' and goToNextBubble == True and bubble%2 == 0:
        left_convo_2.left_convo_2()
        bubble += 1
        goToNextBubble = False
        
def keyReleased():
    global goToNextScene
    global goToNextBubble
    goToNextScene = True
    goToNextBubble = True
    
