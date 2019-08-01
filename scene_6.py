def scene_6():
    
    img = loadImage("graduate.jpg")
    image(img, 0, 0, 1400, 750)
    
    img = loadImage("gradcap.PNG")
    image(img, 1000, 250, 300, 300)
    
    strokeWeight(4)
    stroke(255, 107, 186)
    fill(255, 143, 203, 160)
    rect(65, 50, 550, 155)
    n = createFont("Ubuntu-Medium.ttf", 20)
    textFont(n)
    fill(0, 0, 0)
    text("Four years later you've graduated from HBC University!! \nIt took you a little bit to get the hang of the HBCU life, \nbut once you did, you took the world by storm. \nBy your senior year you were on the executive board for\nmultiple clubs and you even pledged as an AKA. Congrats !!", 70, 80)
