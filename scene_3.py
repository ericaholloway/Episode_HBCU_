def scene_3():
    
    img = loadImage ("classroom.jpg")
    image(img,0,0,1400,750)
    
    img = loadImage ("teacher.PNG")
    image(img,910,140,170,170)
    
    img = loadImage ("penny1.PNG")
    image(img,300,250,200,450)


    fill (255, 255, 255, 180)
    rect(500, 332, 500, 50)
    n= createFont ("Ubuntu-Medium.ttf",18)
    textFont(n)
    fill (0, 0, 0)
    text(" 'A': \n Admit to the teacher that I haven't done summer reading",500, 350)
    
    fill (255, 255, 255, 180)
    rect(500, 402, 520, 50)
    n= createFont ("Ubuntu-Medium.ttf",18)
    textFont(n)
    fill (0, 0, 0)
    text(" 'B': \n Act like I know what shes talking about and hope for the best ",500, 420)
