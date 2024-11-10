#Pygame is a library that is use to create games. Turtle library is also used to create games 
#but it can only create small and limited games due to its functionality
#that is why we have a pygame which has more functionality and can create bigger games and animations
#Step 1:Basic structure import pygame
import pygame
#Step 2: use pygame.init to initialize or start the pygame.
pygame.init()
#Step 3:Use pygame.set_mode to give the geometry of the screen and pygame.set_caption.
screen=pygame.display.set_mode((999,801))
pygame.display.set_caption("pygame shapes")
#Step 4:score func and game over func are created in case of games.
#Step 5:Use while loop so that the game keeps on going.
while True:

#Step 6:So when we click on close button the screen should close but in pygame it does not close rather it stays so if we want to close it
#then we use pygame.QUIT event. So first of all remember pygame.quit is an event. event meams when we do something something else happend. 
#events are : keydown, mousepress, mousedown,. keyreleased, keypress etc.. are al events so whenver we want to use any of them or quit we first do the following things:
#1. we apply for loop on pygame.event.get() so we can get all events.
#2. then we use if then check and say which event we want to use. if pygame.QUIt, keydown etc...
   for event in pygame.event.get():
    if event.type == Pygame.QUIT:
        pygame.quit() # 20, 21, 22 lines are always given in pygame progames and games so taht when we click on close option screen gets closed.
   #Use shapes like rectangle, line, point, circle, ellipse(oval or circle), polygon (any shape, triangle, hexagon, hectagon, dodecagon and many more)
#Step 7 : to create shape in while loop (pneumonoultramicroscopicsilicovolcanoconiosis is a lung disease.)
   pygame.draw.rect("screen", "red", pygame.Rect(100,100,50,2))#x/y/width/height
   pygame.draw.ellipse("screen", "green", pygame.Rect(100,100,50,50))
   pygame.draw.circle("screen", "blue", pygame.Rect(100, 100, 40))#x,y,radius
   pygame.draw.line("screen", "yellow", pygame.Rect((100, 100),(200,200)))#x1,y1,x2,y2
   pygame.draw.polygon("screen", "orange", pygame.Rect(100, 100, 60, 30))
   #Step 8:Use update function at the end of the code.
   pygame.display.update()