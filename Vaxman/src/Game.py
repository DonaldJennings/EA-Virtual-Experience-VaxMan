import pygame
from .Wall import Wall
from .Player import Player
from .Ball import Ball
from .Ghost import Ghost
from .Inky import Inky
from .Pinky import Pinky
from .Clyde import Clyde
from .Blinky import Blinky

class Game:

    # DEFINE VARIABLES FOR GAME
    black = (0,0,0)
    white = (255,255,255)
    blue = (0,0,255)
    green = (0,255,0)
    red = (255,0,0)
    purple = (255,0,255)
    yellow   = (255,255,0)
    _MAX_ENEMY_ALLOWED = 3*32
    _timer_event = pygame.USEREVENT + 1
    _timer_interval = 30000

    #DEFAULT SPAWN LOCATIONS
    w                  = 303-16 #Width
    PACMAN_SPAWN_ROW   = (7*60)+19  #Pacman height
    MOSTER_SPAWN_ROW   = (4*60)+19 #Monster height
    BLINKY_SPAWN_ROW   = (3*60)+19
    INKY_SPAWN_COL     = 303 - 16 - 32
    CLYDE_SPAWN_COL    = 303+(32-16)  #Clyde width
    
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode([500,500])
    pygame.time.set_timer(_timer_event, _timer_interval)
    pygame.font.init()
    font = pygame.font.SysFont("Calibri", 24)
    background = pygame.Surface(screen.get_size())


    def initialiseGame(self, width, height):
        vaxmanIcon=pygame.image.load('util/pacman.png')
        pygame.display.set_icon(vaxmanIcon)

        #Add music
        pygame.mixer.init()
        pygame.mixer.music.load('util/pacman.mp3')
        pygame.mixer.music.play(-1, 0.0)


        # Call this function so the Pygame library can initialize itself
        pygame.init()
        
        # Create an 606x606 sized screen
        self.screen = pygame.display.set_mode([width, height])

        # This is a list of 'sprites.' Each ball in the program is
        # added to this list. The list is managed by a class called 'RenderPlain.'


        # Set the title of the window
        pygame.display.set_caption('Pacman')

        # Used for converting color maps and such
        self.background = self.background.convert()
        
        # Fill the screen with a black background
        self.background.fill(self.black)


    # This creates all the walls in room 1
    def setupRoomOne(self, all_sprites_list):
        # Make the walls. (x_pos, y_pos, width, height)
        wall_list=pygame.sprite.RenderPlain()
        
        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [ [0,0,6,600],
                [0,0,600,6],
                [0,600,606,6],
                [600,0,6,606],
                [300,0,6,66],
                [60,60,186,6],
                [360,60,186,6],
                [60,120,66,6],
                [60,120,6,126],
                [180,120,246,6],
                [300,120,6,66],
                [480,120,66,6],
                [540,120,6,126],
                [120,180,126,6],
                [120,180,6,126],
                [360,180,126,6],
                [480,180,6,126],
                [180,240,6,126],
                [180,360,246,6],
                [420,240,6,126],
                [240,240,42,6],
                [324,240,42,6],
                [240,240,6,66],
                [240,300,126,6],
                [360,240,6,66],
                [0,300,66,6],
                [540,300,66,6],
                [60,360,66,6],
                [60,360,6,186],
                [480,360,66,6],
                [540,360,6,186],
                [120,420,366,6],
                [120,420,6,66],
                [480,420,6,66],
                [180,480,246,6],
                [300,480,6,66],
                [120,540,126,6],
                [360,540,126,6]
                ]
        
        # Loop through the list. Create the wall, add it to the list
        for item in walls:
            wall=Wall(item[0],item[1],item[2],item[3],self.blue)
            wall_list.add(wall)
            all_sprites_list.add(wall)
            
        # return our new list
        return wall_list

    def setupGate(self, all_sprites_list):
        gate = pygame.sprite.RenderPlain()
        gate.add(Wall(282,242,42,2, self.white))
        all_sprites_list.add(gate)
        return gate


    def doNext(self, message, left, all_sprites_list, ball_list, ghost_list, pacman_collide, wall_list,gate):
      while True:
      # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.key == pygame.K_RETURN:
                del self.all_sprites_list
                del ball_list
                del ghost_list
                del pacman_collide
                del wall_list
                del gate
                self.startGame()

        #Grey background
        w = pygame.Surface((400,200))  # the size of your rect
        w.set_alpha(10)                # alpha level
        w.fill((128,128,128))           # this fills the entire surface
        self.screen.blit(w, (100,200))    # (0,0) are the top-left coordinates

        #Won or lost
        text1 = self.font.render(message, True, self.white)
        self.screen.blit(text1, [left, 233])

        text2 = self.font.render("To play again, press ENTER.", True, self.white)
        self.screen.blit(text2, [135, 303])
        text3 = self.font.render("To quit, press ESCAPE.", True, self.white)
        self.screen.blit(text3, [165, 333])

        pygame.display.flip()

        self.clock.tick(10)

    def startGame(self): 

        all_sprites_list = pygame.sprite.RenderPlain()
        ball_list = pygame.sprite.RenderPlain()
        ghost_list = pygame.sprite.RenderPlain()
        pacman_collide = pygame.sprite.RenderPlain()
        wall_list = self.setupRoomOne(all_sprites_list)
        gate = self.setupGate(all_sprites_list)

        p_turn = 0
        p_steps = 0

        b_turn = 0
        b_steps = 0

        c_turn = 0
        c_steps = 0

        wall_list = self.setupRoomOne(all_sprites_list)
        gate = self.setupGate(all_sprites_list)

        # Create the player paddle object
        Pacman = Player( self.w, self.PACMAN_SPAWN_ROW, "util/pacman.png" )
        all_sprites_list.add(Pacman)
        pacman_collide.add(Pacman)

        pinky = Pinky(self.w, self.MOSTER_SPAWN_ROW, "util/Pinky.png")
        ghost_list.add(pinky)
        all_sprites_list.add(pinky)
        
        blinky = Blinky(self.w, self.BLINKY_SPAWN_ROW, "util/Blinky.png")
        ghost_list.add(blinky)
        all_sprites_list.add(blinky)
        inky = Inky(self.INKY_SPAWN_COL, self.MOSTER_SPAWN_ROW, "util/Inky.png")
        ghost_list.add(inky)
        all_sprites_list.add(inky)
    

        # Draw the grid
        for row in range(19):
            for column in range(19):
                if (row == 7 or row == 8) and (column == 8 or column == 9 or column == 10):
                    continue
                else:
                    ball = Ball(self.yellow, 4, 4)

                    # Set a random location for the ball
                    ball.rect.x = (30*column+6)+26
                    ball.rect.y = (30*row+6)+26

                    b_collide = pygame.sprite.spritecollide(ball, wall_list, False)
                    p_collide = pygame.sprite.spritecollide(ball, pacman_collide, False)
                    if b_collide:
                        continue
                    elif p_collide:
                        continue
                    else:
                        # Add the ball to the list of objects
                        ball_list.add(ball)
                        all_sprites_list.add(ball)

        bll = len(ball_list)
        score = 0
        done = False
        i = 0

        while not done:

            # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == self._timer_event:
                    for ghost in ghost_list:
                        new_ghost = ghost.reproduce()
                        ghost_list.add(new_ghost)
                        all_sprites_list.add(new_ghost)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        Pacman.changespeed(-30,0)
                    elif event.key == pygame.K_RIGHT:
                        Pacman.changespeed(30,0)
                    elif event.key == pygame.K_UP:
                        Pacman.changespeed(0,-30)
                    elif event.key == pygame.K_DOWN:
                        Pacman.changespeed(0,30)

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        Pacman.changespeed(30,0)
                    elif event.key == pygame.K_RIGHT:
                        Pacman.changespeed(-30,0)
                    elif event.key == pygame.K_UP:
                        Pacman.changespeed(0,30)
                    elif event.key == pygame.K_DOWN:
                        Pacman.changespeed(0,-30)
                
            # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
        
            # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
            Pacman.update(wall_list,gate)


            for ghost in ghost_list:
                returned = ghost.changeSpeed()
                ghost.setTurns(returned[0])
                ghost.setSteps(returned[1])
                ghost.changeSpeed()
                ghost.update(wall_list, False)
                


            # See if the Pacman ball has collided with anything.
            ball_collision_list = pygame.sprite.spritecollide(Pacman, ball_list, True)
            
            # Check the list of collisions.
            if len(ball_collision_list) > 0:
                score +=len(ball_collision_list)
            
            # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
        
            # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
            self.screen.fill(self.black)
                
            wall_list.draw(self.screen)
            gate.draw(self.screen)
            all_sprites_list.draw(self.screen)
            ghost_list.draw(self.screen)

            text = self.font.render("Score: "+str(score)+"/"+str(bll), True, self.red)
            scoreText = self.font.render("Enemies Left: " + str(len(ghost_list))+"/"+str(self._MAX_ENEMY_ALLOWED), True, self.red)
            self.screen.blit(text, [10, 10])
            self.screen.blit(scoreText, [420,10])

            if score == bll or len(ghost_list) == 0:
                self.doNext("Congratulations, you won!",145,all_sprites_list, ball_list, ghost_list,pacman_collide,wall_list,gate)


            ghost_hit_list = pygame.sprite.spritecollide(Pacman, ghost_list, True)

            if len(ghost_list) > self._MAX_ENEMY_ALLOWED:
                self.doNext("Game Over",235,all_sprites_list,ball_list, ghost_list,pacman_collide,wall_list,gate)

            # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
            
            pygame.display.flip()
            
            self.clock.tick(10)