def scene_2():
    img= loadImage("famu.jpg")
    image(img, 0, 0, 1400, 750)

    img= loadImage("dijonay.PNG")
    image(img, 150, 400, 200, 300)

    #Penny
    img = loadImage ("penny1.PNG")
    image(img,1020,400,200,300)

    #Click S to continue 
    fill (240, 10, 63, 160)
    rect(100, 650, 230, 50)
    n= createFont ("Ubuntu-Medium.ttf",18)
    textFont(n)
    fill (0, 0, 0)
    text("Click 'C' to continue the conversation",100, 680)
