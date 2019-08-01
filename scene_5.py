def scene_5():
    
    img = loadImage("timecard.jpg")
    image(img, 0, 0, 1400, 750)


    f = createFont("Some Time Later.otf", 150)
    textFont(f)
    fill(237, 219, 19)
    text("FOUR YEARS \n  LATER...", 400, 350)
