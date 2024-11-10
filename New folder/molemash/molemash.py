import pygame
import random
import time
pygame.init()
screen = pygame.display.set_mode((900, 900))
pygame.display.set_caption("Whack-a-Mole")

bg = pygame.image.load("moley.jpg")
bg = pygame.transform.scale(bg, (900, 900))
mole = pygame.image.load("moleyer.webp")
mole = pygame.transform.scale(mole, (100, 100))
score1 = 0

def score():
    sc = pygame.font.SysFont("Arial", 20)
    text = sc.render("Score: " + str(score1), True, "black")
    screen.blit(text, (10, 10))  # Blit the score at a valid position

def gameover():
    sc = pygame.font.SysFont("Arial", 20)
    text = sc.render("Game Over", True, "black")
    screen.blit(text, (350, 450))  # Blit the game over message at a valid position
mole_position=[(104,104),(404,104), (704,104),(104,404),(404,404),(704,404),(104,704),(404,104),(704,704)]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  # Exit properly after quitting
        if event.type==pygame.MOUSEBUTTONDOWN:
            x,y=pygame.mouse.get_pos()
            for molex,moley in mole_position:
                mole_rect=pygame.Rect(molex,moley,mole.get_width(), mole.get_height())
                if mole_rect.collidepoint(x,y):
                    score1+=1
                                 
    rand=random.randint(1,9)
    screen.blit(bg, (0, 0))  # Draw the background
      # Call the score function to display the score
    
    if rand==1:
        mole_pause=(104,104)
        screen.blit(mole,mole_pause)
    
    if rand==2:
        mole_pause=(404,104)
        screen.blit(mole,mole_pause)

    if rand==3:
        mole_pause=(704, 104)
        screen.blit(mole,mole_pause)
    
    if rand==4:
        mole_pause=(404, 404)
        screen.blit(mole,mole_pause)

    if rand==5:
        mole_pause=(704, 404)
        screen.blit(mole,mole_pause)
    
    if rand==6:
        mole_pause=(104, 704)
        screen.blit(mole,mole_pause)

    if rand==7:
        mole_pause=(404, 704)
        screen.blit(mole,mole_pause)

    if rand==8:
        mole_pause=(704, 704)
        screen.blit(mole,mole_pause)
    




    # Draw circles in valid positions
    pygame.draw.circle(screen, "black", (150, 150), 80)
    pygame.draw.circle(screen, "black", (450, 150), 80)
    pygame.draw.circle(screen, "black", (750, 150), 80)
    pygame.draw.circle(screen, "black", (150, 450), 80)
    pygame.draw.circle(screen, "black", (450, 450), 80)
    pygame.draw.circle(screen, "black", (750, 450), 80)
    pygame.draw.circle(screen, "black", (150, 750), 80)
    pygame.draw.circle(screen, "black", (450, 750), 80)
    pygame.draw.circle(screen, "black", (750, 750), 80)
    screen.blit(mole,mole_pause)
    time.sleep(2)
    score()
    pygame.display.update()
pygame.quit()

#-----------------------------------------Assignment---------------------------
#complete gameover in mole mash game.