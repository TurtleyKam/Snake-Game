#import modules

import pygame

import random

import time

    #creates apples
def create_apples(apple_position):
    pygame.draw.rect(display,apple_color,pygame.Rect(apple_position[0],apple_position[1],10,10))
    pygame.display.update()
    
def collision_with_apple(apple_position, score):
    apple_position = [random.randint(0,50)*10, random.randint(0,50)*10]
    score = score + 1
    return apple_position, score

def collision_with_boundaries(snake_head):

    # if snake is outside of boundaries return 1
    if snake_head[0]>=display_width or snake_head[0]<0 or snake_head[1]>=display_height or snake_head[1]<0:
        return 1
    else:
        return 0

def generate_snake(snake_head, snake_position, apple_position, button_direction, score):

    #uses button_direction to decide where snake head will go
    if button_direction == 1:
        snake_head[0] += 10
    elif button_direction == 0:
        snake_head[0] -= 10
    elif button_direction == 2:
        snake_head[1] += 10
    elif button_direction == 3:
        snake_head[1] -= 10       
        
    if snake_head == apple_position:
        apple_position, score = collision_with_apple(apple_position, score)
        snake_position.insert(0,list(snake_head))
        
    else:
        snake_position.insert(0,list(snake_head))
        snake_position.pop()
    
    return snake_position,apple_position, score

def display_snake(snake_position):

    #uses list of snake's positions to display snake
    for position in snake_position:
        
        pygame.draw.rect(display,player_color,pygame.Rect(position[0],position[1],10,10))

def play_game(snake_head, snake_position, button_direction, apple_position, score):

    crashed = False
    
    while crashed is not True:

        for event in pygame.event.get():

            #ends game if you click on X
            if event.type == pygame.QUIT:
                crashed = True

            #sets variable used to move snake using arrow keys
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    button_direction = 0
                elif event.key == pygame.K_RIGHT:
                    button_direction = 1
                elif event.key == pygame.K_UP:
                    button_direction = 3
                elif event.key == pygame.K_DOWN:
                    button_direction = 2              


        #moves snake position
        snake_position, apple_position, score = generate_snake(snake_head, snake_position, apple_position, button_direction, score)
        pygame.display.set_caption("Snake Game"+" "+"SCORE: "+str(score))

        

        #display background and snake
        display.fill(window_color)
        display_snake(snake_position)
        create_apples(apple_position)
        pygame.display.update()

        

        #ends game loop if snake leaves the boundary
        if collision_with_boundaries(snake_head) == 1:
            crashed = True


        clock.tick(20)
    return score

def display_final_score(display_text, final_score):
    largeText = pygame.font.Font("freesansbold.ttf",45)
    TextSurf = largeText.render(display_text, True, (175,0,225))
    TextRect = TextSurf.get_rect()
    TextRect.center = ((display_width/2),(display_height/2))
    display.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)



if __name__ == "__main__":

    # set variables

    display_width = 500

    display_height = 500

    player_color = (100,225,100)

    window_color = (225,100,100)
    
    apple_color = (225,0,0)

    clock=pygame.time.Clock()

    

    #create the snake

    snake_head = [250,250]

    snake_position = [[250,250],[240,250],[230,250]]
    
    apple_position = [random.randint(0,50)*10, random.randint(0,50)*10]
    
    score = 0
    
    



    #initialize pygame modules    

    pygame.init()
    

    

    #display game window

    display = pygame.display.set_mode((display_width,display_height))

    display.fill(window_color)

    pygame.display.set_caption("Snake Game")

    pygame.display.update()

    

    #start the game loop

    final_score = play_game(snake_head, snake_position, 1, apple_position, score)
    display_text = "Your Score Is: " + str(final_score)
    display_final_score(display_text, final_score)



    pygame.quit()