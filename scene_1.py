def scene_1():
    
    img = loadImage ("howard.jpg")
    image(img,0,0,1400,750)
    
    img = loadImage ("penny1.PNG")
    image(img,400,400,200,300)
    
    fill (235, 223, 12, 160)
    rect(50, 10, 1250, 120)
    
    n= createFont ("Ubuntu-Light.ttf",32)
    textFont(n)
    fill (0, 0, 0)
    text("It's your first day at HBC University! You've just said your goodbyes to your family", 100, 50)
    text("and now you're on your own. Time to figure things out, and fast!", 100, 82)
    text("Your first class starts in 10  minutes, don't be late!", 100, 114)

    fill (240, 10, 63, 160)
    rect(100, 650, 230, 50)
    
    n= createFont ("Ubuntu-Medium.ttf",18)
    textFont(n)
    fill (0, 0, 0)
    text("Click 'S' to continue to class",100, 680)
