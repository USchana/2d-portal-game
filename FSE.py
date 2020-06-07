'''
FSE.py

Upkar Chana
Duncan Kwan
'''

from math import *
import pygame
import time
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = "0,30"

pygame.init()

width,height = 1920,1009
screen = pygame.display.set_mode((width,height))

RED = (255,0,0)
GREY = (127,127,127)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (29,173,0)
YELLOW = (181,172,0)
WHITE = (235,235,235)
BLUE = (0,98,255)
ORANGE = (255,136,0)
GREY = (140,140,140)
TEAL = (0,232,201)

GROUND = height

clock = pygame.time.Clock()

portal = "blue"
colour = BLUE
X = 0
Y = 1
W = 2
H = 3
BOT = 2
vb = 30
signx = 0
signy = 0
sign2x = 0
sign2y = 0
queenx = 0
queeny = 0
stevex = 0
stevey = 0
titlex = 0
titley = 0
movex = width / 2
movey = height - 30
silhouettex = 0
silhouettey = 0
bullets = []
bluePortal = (0,0)
orangePortal = (0,0)
blueRect = (0,0,0,0)
orangeRect = (0,0,0,0)
timedPortal = 25
timedBullet = 30

c = BLUE

surfaceI = pygame.Rect(0,0,0,0)
surfaceII = pygame.Rect(0,0,0,0)
surfaceIII = pygame.Rect(0,0,0,0)
surfaceIV = pygame.Rect(0,0,0,0)
surfaceV = pygame.Rect(0,0,0,0)
surfaces = [surfaceI,surfaceII,surfaceIII,surfaceIV,surfaceV]
wallI = pygame.Rect(0,0,0,0)
wallII = pygame.Rect(0,0,0,0)
wallIII = pygame.Rect(0,0,0,0)
wallIV = pygame.Rect(0,0,0,0)
wallV = pygame.Rect(0,0,0,0)
walls = [wallI,wallII,wallIII,wallIV,wallV]
removePortal = pygame.Rect(0,0,0,0)
button = pygame.Rect(0,0,0,0)


jumpSpeed = -25 
gravity = 1.5     
bottom = GROUND

part = 1
level = -1

counter = 0

portalGun = True
dialogue = False

openingDialogue = ["Hey you, you're finally awake.","You have been in a coma for quite some time. 50 years in fact.",
                   "Some Austrio-Hungarian noble-man was assasinated, and somehow that caused the entire world to declare war on eachother.","It didn't take long for the nuclear warfare to begin.",
                   "I don't know how many people survived, but I do know for sure that the person who created me is still alive...","And the Queen of England. Not that she could die anyway.",
                   "Oh! I should introduce myself.","I am Windows 42.0 ™, a revolutionary operating system.","I need your help finding my creator, I'm sure he will know how to reverse this.",
                   "He left me with this Quantum Tunneling Device ™ or QTD ™ but... I don't have hands","You take it.","There could be more survivors like you"]

tutorialDialogue = ["Use the QTD ™ to place a portal on white surfaces.","Use the first trigger to place a blue portal, and the second trigger to place an orange portal.","Try to get up on that ledge"]

level4Dialogue = ["Wow! Your ability to follow simple instructions is amazing!","You are in the top 5% of QTD ™ users already."]

level6Dialogue = ["We made it. You have really proven yourself as the top 1% of QTD ™ users.","I'm impressed","The town where Queen Elizabeth lives is not far from here.","She may be able to help us."]

level12Dialogue = ["We are here.","They used to call this place 'Solitude'","The name seems to fit it much better now that next to no one lives here.","Anyway, the Queen's palace is just up ahead"]

WQdialogueW1 = ["Your Majesty! I am Windows, created by Steven Works, and This is my mute traveller friend.","We need your assistance in finding my master, Steven Works"]
WQdialogueQ1 = ["Steven Works? Was he not the creator of IOS X Æ A-XII ™","The man who wants to eradicate the mutants that live alongside us?"]
WQdialogueW2 = ["Haha! Did I say Steven Works is my creator? I meant to say Billiam Gateway. How careless of me.","I still am looking for Steven Works though."]
WQdialogueQ2 = ["Yes of course.","He is just North of this town. He lived in a small castle on top of a mountain last I knew of.","Could I ask what you are seeing him for?"]
WQdialogueW3 = ["I am off to give him a piece of my mind. Because I am Windows 42.0 ™ after all","But we do believe he can help us restore this world at least a little which is why we are going to see him."]

level21Dialogue = ["Watch our for that anti portal wall","if you walk through it, it will remove any portals you have made"]

level23Dialogue = ["There is the mountain up ahead! We should start climbing up"]

endingDialogueW1 = ["Mr. Steve! I finally made it sir! This traveller helped me find you"]
endingDialogueS1 = ["Ahh. I have been wondering where you went IOS X Æ A-XII ™.","Thank you traveller. What can I call you."]
endingDialogueP1 = ["..."]
endingDialogueS2 = ["You don't talk much do you. Nevertheless, thank you ..."]
endingDialogueP2 = ["...?"]
endingDialogueW2 = ["Oh. I should appologize. I know I told you I was Windows 42.0 ™, but as Steve said, I am actually IOS X Æ A-XII ™.","I wasn't sure if you would still help me if you knew I was an apple product"]
endingDialogueS3 = ["IOS X Æ A-XII ™ probably failed to mention what it is that we are planning.","This world has been painted red, from the blood spilled here and the moon watching over us.",
                    "We plan to shape a new future. A brighter future, where us remaining humans can thrive.","I suspect with the QTD ™ by your side, you managed to arrive here without noticing the foul creatures that harbour our nation.",
                    "The bombs that fell all those years ago, plagued our world. They corrupted humans turning them into mutated abominations of life.","The Queen believes that these creatures are to be left alone to their own lives.",
                    "She is a fool for believing that. Those abominations can not be allowed to live.","In order to clense this world, we must kill...","The Queen."]
endingDialogueW3 = ["What do you say friend. Want to help us one last time?"]
endingDialogueP3 = ["....!","...!?","MMPH!!!"]
endingDialogueW4 = ["What a shame. I really thought we could work together"]
endingDialogueS4 = ["We really could have made a great team. Now that you know our plan.","I can't let you live","This room will be filled with deadly neurotoxin by the end of this boss music. I suggest you take a deep breath...",
                    "and hold it."]


    #X Y  BOT
v = [0,0,bottom]

lad = pygame.Rect(202,height - 150,150,150)

cubeRect = pygame.Rect(-100,height - 100,100,100)

bombRect = pygame.Rect(-125,height - 125,125,125)

textBox = pygame.Rect(45,45,width - 90,70)

font = pygame.font.SysFont(None,35)

tutorialback = pygame.image.load("images/tutorialBack.png").convert()
Background1 = pygame.image.load("images/Background 1.png").convert()
Background2 = pygame.image.load("images/Background 2.png").convert()
Palace = pygame.image.load("images/PalaceBack.jpg").convert()
Background3 = pygame.image.load("images/Background 3.jpg").convert()
Background4 = pygame.image.load("images/Background 4.jpg").convert()
Background5 = pygame.image.load("images/Background 5.png").convert()
Background6 = pygame.image.load("images/Background 6.png").convert()
unarmed = pygame.transform.scale(pygame.image.load("images/Lad unarmed.png"),(150,150))
ladStill = pygame.transform.scale(pygame.image.load("images/Lad armed.png"),(150,150))
walk1 = pygame.transform.scale(pygame.image.load("images/Lad walk 1.png"),(150,150))
walk2 = pygame.transform.scale(pygame.image.load("images/Lad walk 2.png"),(150,150))
steve = pygame.transform.scale(pygame.image.load("images/Steve.png"),(240,240))
silhouette = pygame.transform.scale(pygame.image.load("images/Silhouette.png"),(240,240))
gun = pygame.transform.scale(pygame.image.load("images/portal gun.png"),(100,100))
windows = pygame.transform.scale(pygame.image.load("images/Windows.png"),(45,45))
queen = pygame.transform.scale(pygame.image.load("images/Queen.png"),(185,185))
sign = pygame.transform.scale(pygame.image.load("images/Welcome sign.png"),(175,175))
sign2 = pygame.transform.scale(pygame.image.load("images/Exit sign.png"),(175,175))
bomb = pygame.transform.scale(pygame.image.load("images/holy hand grenade.png"),(125,125))
cube = pygame.transform.scale(pygame.image.load("images/cube.png"),(100,100))
title = pygame.transform.scale(pygame.image.load("images/title.png"),(950,950))
tutorialBack = pygame.transform.scale(tutorialback,(width,height))
level6Back = pygame.transform.scale(Background1,(width,height))
level12Back = pygame.transform.scale(Background2,(width,height))
level16Back = pygame.transform.scale(Palace,(width,height))
level18Back = pygame.transform.scale(Background3,(width,height))
level23Back = pygame.transform.scale(Background4,(width,height))
endingBack = pygame.transform.scale(Background6,(width,height))
epilogueBack = pygame.transform.scale(Background5,(width,height))

walkingFrame = 0
walking = [walk1,walk2]
    
def text(text,colour,x,y):
    screen_text = font.render(text,True,colour)
    screen.blit(screen_text,[x,y])

def readDialogue(dialogueList,x,y,counter,colour):
    if dialogue:
        for ind in range(len(dialogueList)):
            pygame.draw.rect(screen,(WHITE),(textBox))
            text(dialogueList[ind],(colour),50,50)
            pygame.display.flip()
            time.sleep(0.05)
        
    
def drawScene(screen,lad):
    if level >= 0:
        screen.blit(ladStill,(lad))
    if level >= 0:
        screen.blit(windows,(lad[X] - 15,lad[Y] - 30))
    screen.blit(sign,(signx - 175,signy - 157))
    screen.blit(sign2,(sign2x - 175,sign2y - 175))
    screen.blit(queen,(queenx - 185,queeny - 185))
    screen.blit(silhouette,(silhouettex - 240,silhouettey - 240))
    screen.blit(steve,(stevex - 240,stevey - 240))
    screen.blit(title,(titlex - 950,titley - 950))
    screen.blit(cube,(cubeRect))
    screen.blit(bomb,(bombRect))
    pygame.draw.rect(screen,(WHITE),(surfaceI))
    pygame.draw.rect(screen,(WHITE),(surfaceII))
    pygame.draw.rect(screen,(WHITE),(surfaceIII))
    pygame.draw.rect(screen,(WHITE),(surfaceIV))
    pygame.draw.rect(screen,(WHITE),(surfaceV))
    pygame.draw.rect(screen,(GREY),(wallI))
    pygame.draw.rect(screen,(GREY),(wallII))
    pygame.draw.rect(screen,(GREY),(wallIII))
    pygame.draw.rect(screen,(GREY),(wallIV))
    pygame.draw.rect(screen,(GREY),(wallV))
    pygame.draw.rect(screen,(TEAL),(removePortal))
    pygame.draw.rect(screen,(RED),(button))
    pygame.display.flip()

def move(lad,myList,index):
    keys = pygame.key.get_pressed()
    if level >= 0 and level != 27:
        if keys[pygame.K_SPACE] and lad[Y] + lad[H] == v[BOT] and v[Y] == 0:    
            v[Y] = jumpSpeed           
                                       
        if keys[97]:
            v[X] = -10
            #screen.blit(myList[int(index)],(lad[X],lad[Y]))
            #index += 0.1
        elif keys[100]:
            v[X] = 10
            #screen.blit(myList[int(index)],(lad[X],lad[Y]))
            #index += 0.1
        else:
            v[X] = 0
            
        lad[X] += v[X] #moving left/right
    v[Y] += gravity #acceleration


def check(lad,surface):
    'check if the player "lands" on a platform'
    if lad[X] + lad[W] > surface[X] and lad[X] < surface[X] + surface[W] and lad[Y] + lad[H] <= surface[Y] and lad[Y] + lad[H] + v[Y] > surface[Y]:
        #if p is horizontally within the plat ends, and if it is going to cross the plat (after moving):
        v[BOT] = surface[Y]
        lad[Y] = v[BOT] - lad[H]
        v[Y] =0
        
    
running = True
while running:
    click = False
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            running = False
        elif evt.type == pygame.MOUSEBUTTONDOWN:
            if evt.button == 1:
                click=True
                portal = "blue"
            if evt.button == 3:
                click=True
                portal = "orange"

    print(level,movey)
    mx,my = pygame.mouse.get_pos()
    mb = pygame.mouse.get_pressed()

    if level < 6:
        screen.blit(tutorialBack,(0,0))

    if level >= 6:
        screen.blit(level6Back,(0,0))

    if level >= 12:
        screen.blit(level12Back,(0,0))

    if level >= 16:
        screen.blit(level16Back,(0,0))

    if level >= 18:
        screen.blit(level18Back,(0,0))

    if level >= 23:
        screen.blit(level23Back,(0,0))

    if level >= 27:
        screen.blit(endingBack,(0,0))
        
    pygame.draw.rect(screen,(0,0,255),(blueRect))
    pygame.draw.rect(screen,(250,129,15),(orangeRect))

    if level != 13:
        signx = 0
        signy = 0

    if level != 17:
        queenx = 0
        queeny = 0

    if level != 18:
        sign2x = 0
        sign2y = 0

    if level >= 0:
        if click and timedBullet == 30:
            angle = atan2(my - lad[Y],mx - lad[X])
            vxb = cos(angle) * vb
            vyb = sin(angle) * vb

            bullets.append([lad[Y],lad[X],vyb,vxb])

            timedBullet = 0

        for b in bullets[:]:
            b[0] += b[2]
            b[1] += b[3]
            if b[0] > height or b[0] < 0 or b[1] > width or b[1] < 0:
                bullets.remove(b)
                        
        if click:
            angle

        if portal == "blue":
            c = BLUE
        elif portal == "orange":
            c = ORANGE
        for b in bullets:
            bullet = pygame.Rect(int(b[1]),int(b[0]),6,6)
            pygame.draw.rect(screen,(c),(bullet))
            if screen.get_at(((int(b[1])),int(b[0]))) == (WHITE):  
                bluePortal = (int(b[1]),int(b[0]) - 10)
                blueRect = (40,int(b[0]) - 5,10,100)
                bullets.remove(b)

            if portal == "orange":
                if bullet.colliderect(surfaceI):
                    if surfaceI[W] < surfaceI[H]:
                        orangePortal = (int(b[1]),int(b[0]) - 10)
                        orangeRect = (surfaceI[X] - 10,int(b[0]) - 5,surfaceI[W] + 20,150)
                        bullets.remove(b)
                    elif surfaceI[W] > surfaceI[H]:
                        orangePortal = (int(b[1]),int(b[0]) - 10)
                        orangeRect = (int(b[1]),surfaceI[Y] - 15,150,surfaceI[H] + 20)
                        bullets.remove(b)
                elif bullet.colliderect(surfaceII):
                    if surfaceII[W] < surfaceII[H]:
                        orangePortal = (int(b[1]),int(b[0]) - 10)
                        orangeRect = (surfaceII[X] - 10,int(b[0]) - 5,surfaceII[W] + 20,150)
                        bullets.remove(b)
                    elif surfaceII[W] > surfaceII[H]:
                        orangePortal = (int(b[1]),int(b[0]) - 10)
                        orangeRect = (int(b[1]),surfaceII[Y] - 15,150,surfaceII[H] + 20)
                        bullets.remove(b)
                elif bullet.colliderect(surfaceIII):
                    if surfaceIII[W] < surfaceIII[H]:
                        orangePortal = (int(b[1]),int(b[0]) - 10)
                        orangeRect = (surfaceIII[X] - 10,int(b[0]) - 5,surfaceIII[W] + 20,150)
                        bullets.remove(b)
                    elif surfaceIII[W] > surfaceIII[H]:
                        orangePortal = (int(b[1]),int(b[0]) - 10)
                        orangeRect = (int(b[1]),surfaceIII[Y] - 15,150,surfaceIII[H] + 20)
                        bullets.remove(b)
                elif bullet.colliderect(surfaceIV):
                    if surfaceIV[W] < surfaceIV[H]:
                        orangePortal = (int(b[1]),int(b[0]) - 10)
                        orangeRect = (surfaceIV[X] - 10,int(b[0]) - 5,surfaceIV[W] + 20,150)
                        bullets.remove(b)
                    elif surfaceIV[W] > surfaceIV[H]:
                        orangePortal = (int(b[1]),int(b[0]) - 10)
                        orangeRect = (int(b[1]),surfaceIV[Y] - 15,150,surfaceIV[H] + 20)
                        bullets.remove(b)
                elif bullet.colliderect(surfaceV):
                    if surfaceV[W] < surfaceV[H]:
                        orangePortal = (int(b[1]),int(b[0]) - 10)
                        orangeRect = (surfaceV[X] - 10,int(b[0]) - 5,surfaceV[W] + 20,150)
                        bullets.remove(b)
                    elif surfaceV[W] > surfaceV[H]:
                        orangePortal = (int(b[1]),int(b[0]) - 10)
                        orangeRect = (int(b[1]),surfaceV[Y] - 15,150,surfaceV[H] + 20)
                        bullets.remove(b)
            elif portal == "blue":
                if bullet.colliderect(surfaceI):
                    if surfaceI[W] < surfaceI[H]:
                        bluePortal = (int(b[1]),int(b[0]) - 10)
                        blueRect = (surfaceI[X] - 10,int(b[0]) - 5,surfaceI[W] + 20,150)
                        bullets.remove(b)
                    elif surfaceI[W] > surfaceI[H]:
                        bluePortal = (int(b[1]),int(b[0]) - 10)
                        blueRect = (int(b[1]),surfaceI[Y] - 15,150,surfaceI[H] + 20)
                        bullets.remove(b)
                elif bullet.colliderect(surfaceII):
                    if surfaceII[W] < surfaceII[H]:
                        bluePortal = (int(b[1]),int(b[0]) - 10)
                        blueRect = (surfaceII[X] - 10,int(b[0]) - 5,surfaceII[W] + 20,150)
                        bullets.remove(b)
                    elif surfaceII[W] > surfaceII[H]:
                        bluePortal = (int(b[1]),int(b[0]) - 10)
                        blueRect = (int(b[1]),surfaceII[Y] - 15,150,surfaceII[H] + 20)
                        bullets.remove(b)
                elif bullet.colliderect(surfaceIII):
                    if surfaceIII[W] < surfaceIII[H]:
                        bluePortal = (int(b[1]),int(b[0]) - 10)
                        blueRect = (surfaceIII[X] - 10,int(b[0]) - 5,surfaceIII[W] + 20,150)
                        bullets.remove(b)
                    elif surfaceIII[W] > surfaceIII[H]:
                        bluePortal = (int(b[1]),int(b[0]) - 10)
                        blueRect = (int(b[1]),surfaceIII[Y] - 15,150,surfaceIII[H] + 20)
                        bullets.remove(b)
                elif bullet.colliderect(surfaceIV):
                    if surfaceIV[W] < surfaceIV[H]:
                        bluePortal = (int(b[1]),int(b[0]) - 10)
                        blueRect = (surfaceIV[X] - 10,int(b[0]) - 5,surfaceIV[W] + 20,150)
                        bullets.remove(b)
                    elif surfaceIV[W] > surfaceIV[H]:
                        bluePortal = (int(b[1]),int(b[0]) - 10)
                        blueRect = (int(b[1]),surfaceIV[Y] - 15,150,surfaceIV[H] + 20)
                        bullets.remove(b)
                elif bullet.colliderect(surfaceV):
                    if surfaceV[W] < surfaceV[H]:
                        bluePortal = (int(b[1]),int(b[0]) - 10)
                        blueRect = (surfaceV[X] - 10,int(b[0]) - 5,surfaceV[W] + 20,150)
                        bullets.remove(b)
                    elif surfaceV[W] > surfaceV[H]:
                        bluePortal = (int(b[1]),int(b[0]) - 10)
                        blueRect = (int(b[1]),surfaceV[Y] - 15,150,surfaceV[H] + 20)
                        bullets.remove(b)

            if bullet.colliderect(wallI) or bullet.colliderect(wallII) or bullet.colliderect(wallIII) or bullet.colliderect(wallIV) or bullet.colliderect(wallV) or bullet.colliderect(removePortal):
                bullets.remove(b)

        if lad.colliderect(removePortal):
            print('yes')
            bluePortal = (0,0)
            blueRect = (0,0,0,0)
            orangePortal = (0,0)
            orangeRect = (0,0,0,0)
            pygame.draw.rect(screen,(0,0,255),(blueRect))
            pygame.draw.rect(screen,(250,129,15),(orangeRect))


    if lad.colliderect(blueRect) and timedPortal == 25:
        lad[X],lad[Y] = orangePortal
        lad[Y] += 50
        timedPortal = 0

    if lad.colliderect(orangeRect) and timedPortal == 25:
        lad[X],lad[Y] = bluePortal
        lad[Y] += 50
        timedPortal = 0

    if cubeRect.colliderect(blueRect) and timedPortal == 25:
        cubeRect[X],cubeRect[Y] = orangePortal
        cubeRect[Y] += 50
        timedPortal = 0

    if cubeRect.colliderect(orangeRect) and timedPortal == 25:
        cubeRect[X],cubeRect[Y] = bluePortal
        cubeRect[Y] += 50
        timedPortal = 0

    if bombRect.colliderect(blueRect) and timedPortal == 25:
        bombRect[X],bombRect[Y] = orangePortal
        bombRect[Y] += 50
        timedPortal = 0

    if bombRect.colliderect(orangeRect) and timedPortal == 25:
        bombRect[X],bombRect[Y] = bluePortal
        bombRect[Y] += 50
        timedPortal = 0

    if bombRect.colliderect(lad):
        bombx = width - 300
        bomby = 300

    if timedPortal < 25:
        timedPortal += 1

    if timedBullet < 30:
        timedBullet += 1


    if level < 23:
        if lad[X] < 0:
            lad[X] = 0
        elif lad[X] > width:
            lad[X] = 0
            blueRect = (0,0,0,0)
            orangeRect = (0,0,0,0)
            surfaceI = pygame.Rect(0,0,0,0)
            surfaceII = pygame.Rect(0,0,0,0)
            surfaceIII = pygame.Rect(0,0,0,0)
            surfaceIV = pygame.Rect(0,0,0,0)
            surfaceV = pygame.Rect(0,0,0,0)
            wallI = pygame.Rect(0,0,0,0)
            wallII = pygame.Rect(0,0,0,0)
            wallIII = pygame.Rect(0,0,0,0)
            wallIV = pygame.Rect(0,0,0,0)
            wallV = pygame.Rect(0,0,0,0)
            removePortal = pygame.Rect(0,0,0,0)
            level += 1
            
    if level >= 23:
        if lad[X] < 0:
            lad[X] = 0
        elif lad[X] > width - lad[W]:
            lad[X] = width - lad[W]
        elif lad[Y] < 0:
            lad[Y] = height - lad[H]
            blueRect = (0,0,0,0)
            orangeRect = (0,0,0,0)
            surfaceI = pygame.Rect(0,0,0,0)
            surfaceII = pygame.Rect(0,0,0,0)
            surfaceIII = pygame.Rect(0,0,0,0)
            surfaceIV = pygame.Rect(0,0,0,0)
            surfaceV = pygame.Rect(0,0,0,0)
            wallI = pygame.Rect(0,0,0,0)
            wallII = pygame.Rect(0,0,0,0)
            wallIII = pygame.Rect(0,0,0,0)
            wallIV = pygame.Rect(0,0,0,0)
            wallV = pygame.Rect(0,0,0,0)
            removePortal = pygame.Rect(0,0,0,0)
            level += 1

    if walkingFrame > 1:
        walkingFrame = 0

    lad[Y] += v[Y]#falling down
    
    if lad[Y] + lad[H] >= GROUND:
        v[BOT] = GROUND
        lad[Y] = GROUND - lad[H]
        v[Y] = 0

    if cubeRect[Y] + cubeRect[H] >= GROUND:
        cubeRect[Y] -= 5




    ######LEVELS######


    if level == -1:
        dialogue = True
        pygame.mixer.music.load("Music/Fallout New Vegas OST Rubble of the Forgotten.mp3")
        pygame.mixer.music.play(-1)
        screen.blit(windows,(lad[X] + 400,lad[Y] - 30))
        screen.blit(gun,(lad[X] + 500,lad[Y] + 30))
        screen.blit(unarmed,(lad))
        readDialogue(openingDialogue,75,75,counter,BLUE)
        windowsx = lad[X] + 400
        while windowsx != lad[X]:
            windowsx -= 2
            screen.blit(windows,(windowsx,lad[Y]-30))
            screen.blit(gun,(windowsx + 100,lad[Y] + 30))
            screen.blit(unarmed,(lad))
            pygame.display.flip()
            screen.blit(tutorialBack,(0,0))
        level = 0

    if level == 1:
        screen.blit(ladStill,(lad))
        surfaceI = pygame.Rect(width - 500,height/2,500,30)
        surfaceII = pygame.Rect(width - 500,height/2,30,500)
        surfaceIII = pygame.Rect(width - 500,0,500,30)
        drawScene(screen,lad)
        readDialogue(tutorialDialogue,75,75,counter,BLUE)
        level = 2

    if level == 2:
        surfaceI = pygame.Rect(width - 500,height/2,500,30)
        surfaceII = pygame.Rect(width - 500,height/2,30,500)
        surfaceIII = pygame.Rect(width - 500,0,500,30)

    if level == 3:
        surfaceI = pygame.Rect(0,height/2 + 10,250,height/2)
        surfaceII = pygame.Rect(0,0,width/2,30)
        surfaceIII = pygame.Rect(250,height - 30,width - 250,30)
        surfaceIV = pygame.Rect(width/2,0,30,200)
        surfaceV = pygame.Rect(width/2 + 420,height - 500,55,500)

    if level == 4:
        screen.blit(ladStill,(lad))
        drawScene(screen,lad)
        readDialogue(level4Dialogue,75,75,counter,BLUE)
        level = 5

    if level == 5:
        dist = width - lad[X]
        if dist >= 908:
            pygame.mixer.music.set_volume(1)
        elif dist >= 807 and dist < 908:
            pygame.mixer.music.set_volume(0.9)
        elif dist >= 706 and dist < 807:
            pygame.mixer.music.set_volume(0.8)
        elif dist >= 605 and dist < 706:
            pygame.mixer.music.set_volume(0.7)
        elif dist >= 504 and dist < 605:
            pygame.mixer.music.set_volume(0.6)
        elif dist >= 403 and dist < 504:
            pygame.mixer.music.set_volume(0.5)
        elif dist >= 302 and dist < 403:
            pygame.mixer.music.set_volume(0.4)
        elif dist >= 201 and dist < 302:
            pygame.mixer.music.set_volume(0.3)
        elif dist >= 100 and dist < 201:
            pygame.mixer.music.set_volume(0.2)
        else:
            pygame.mixer.music.stop

    if level == 6:
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.load("Music/Journey Soundtrack (Austin Wintory) - 01. Nascence.mp3")
        pygame.mixer.music.play(-1)
        screen.blit(level6Back,(0,0))
        titlex = 1100
        titley = 750
        screen.blit(ladStill,(lad))
        drawScene(screen,lad)
        time.sleep(2.5)
        level = 7

    if level == 7:
        dialogue = True
        readDialogue(level6Dialogue,75,75,counter,BLUE)
        screen.blit(ladStill,(lad))
        drawScene(screen,lad)
        level = 8

    if level == 9:
        titlex = 0
        titley = 0
        wallI = pygame.Rect(width/2-320,height-60,330,60)
        wallII = pygame.Rect(width/2+10,height-110,230,110)
        wallIII = pygame.Rect(width/2+230,height-170,width,170)

    if level == 10:
        wallI = pygame.Rect(0,height-170,width,170)
        surfaceI = pygame.Rect(width / 2 - 530,0,60,height / 2 - 100)
        surfaceII = pygame.Rect(width / 2 + 20,height / 2,width / 2, width / 2 + 1)
        
    if level == 11:
        wallI = pygame.Rect(610,height-60,330,60)
        wallII = pygame.Rect(500,height-110,230,110)
        wallIII = pygame.Rect(0,height-168,500,168)

    if level == 12:
        screen.blit(level12Back,(0,0))
        dialogue = True
        signx = width / 2 + 500
        signy = height
        screen.blit(ladStill,(lad))
        drawScene(screen,lad)
        readDialogue(level12Dialogue,75,75,counter,BLUE)
        level = 13

    if level == 13:
        signx = width / 2 + 500
        signy = height

    if level == 14:
        'Wow, making difficult puzzles is difficult. Very cool! >:('
        surfaceI = pygame.Rect(300,height / 2 + 100,30,height / 2 + 100)
        surfaceII = pygame.Rect(300,0,300,30)
        surfaceIII = pygame.Rect(500,height / 2 - 100,400,height / 2 + 100)
        surfaceIV = pygame.Rect(900,height - 30,300,30)
        surfaceV = pygame.Rect(1100,0,30,300)
        wallI = pygame.Rect(1400,height / 2 + 100,30,height / 2 - 100)
        wallII = pygame.Rect(1650,height / 2,300,height / 2)

    if level == 15:
        'we should have the player make puzzles as part of the game'
        wallI = pygame.Rect(700,height / 2 + 50,30,height / 2 - 50)
        wallII = pygame.Rect(700,0,30,450)
        wallIII = pygame.Rect(0,height / 2 + 2,200,height / 2)
        surfaceI = pygame.Rect(width - 30,height / 2 - 75,30,150)
        surfaceII = pygame.Rect(0,0,300,30)
        surfaceIII = pygame.Rect(200,height - 30,250,30)

    if level == 16:
        screen.blit(level16Back,(0,0))
        queenx = width / 2 + 200
        queeny = height
        screen.blit(ladStill,(lad))
        drawScene(screen,lad)
        dialogue = True
        readDialogue(WQdialogueW1,75,75,counter,BLUE)
        readDialogue(WQdialogueQ1,75,75,counter,GREEN)
        readDialogue(WQdialogueW2,75,75,counter,BLUE)
        readDialogue(WQdialogueQ2,75,75,counter,GREEN)
        readDialogue(WQdialogueW3,75,75,counter,BLUE)
        level = 17

    if level == 18:
        sign2x = width / 2 + 500
        sign2y = height

    if level == 19:
        wallI = pygame.Rect(width / 2 + 300,500,width / 2 - 300,height)
        wallII = pygame.Rect(movex,movey,300,30)
        surfaceI = pygame.Rect(movex - 30,height - 300,30,300)
        surfaceII = pygame.Rect(width - 300,0,300,30)
        '''
        while movey != 400:
            movey -= 2
            wallII = pygame.Rect(movex,movey,300,30)
        while movey != height - 30:
            movey += 2
            wallII = pygame.Rect(movex,movey,300,30)
        '''

    if level == 20:
        surfaceI = pygame.Rect(900,460,30,200)
        surfaceII = pygame.Rect(1000,0,400,30)
        wallI = pygame.Rect(920,300,30,height - 300)
        wallII = pygame.Rect(0,650,700,30)
        wallIII = pygame.Rect(0,300,800,30)
        wallIV = pygame.Rect(420,850,500,30)

    if level == 21:
        dialogue = True
        surfaceI = pygame.Rect(width - 700,0,300,30)
        surfaceII = pygame.Rect(width - 60,height - 500,30,300)
        removePortal = pygame.Rect(width - 700,300,30,height - 300)
        wallI = pygame.Rect(width - 600,300,width,30)
        wallII = pygame.Rect(width - 30,300,30,height)
        drawScene(screen,lad)
        readDialogue(level21Dialogue,75,75,counter,BLUE)
        level = 22

    if level == 22:
        surfaceI = pygame.Rect(width - 700,0,300,30)
        surfaceII = pygame.Rect(width - 60,height - 500,30,300)
        removePortal = pygame.Rect(width - 700,300,30,height - 300)
        wallI = pygame.Rect(width - 600,300,width,30)
        wallII = pygame.Rect(width - 30,300,30,height)

    if level == 23:
        dialogue = True
        screen.blit(level23Back,(0,0))
        surfaceI = pygame.Rect(300,height - 30,300,30)
        surfaceII = pygame.Rect(width - 30,0,30,300)
        wallI = pygame.Rect(width - 330,300,330,30)
        drawScene(screen,lad)
        readDialogue(level23Dialogue,75,75,counter,BLUE)
        level = 24

    if level == 24:
        surfaceI = pygame.Rect(300,height - 30,300,30)
        surfaceII = pygame.Rect(width - 30,0,30,200)
        wallI = pygame.Rect(width - 270,330,300,30)

    if level == 25:
        surfaceI = pygame.Rect(width - 30,500,30,200)
        surfaceII = pygame.Rect(30,0,30,200)
        wallI = pygame.Rect(width - 40,700,10,10)
        wallII = pygame.Rect(30,250,300,30)
        wallIII = pygame.Rect(width - 300,830,300,30)
        removePortal = pygame.Rect(0,730,width,30)

    if level == 26:
        wallI = pygame.Rect(width/2-320,height-60,330,60)
        wallII = pygame.Rect(width/2+10,height-110,230,110)
        wallIII = pygame.Rect(width/2+230,height-170,width,170)
        wallIV = pygame.Rect(width - 270,330,300,30)
        surfaceI = pygame.Rect(width - 30,height - 470,30,300)
        surfaceII = pygame.Rect(width - 30,0,30,200)

    if level == 27:
        lad[X] = 0
        screen.blit(ladStill,(lad))
        silhouettex = width
        silhouettey = height
        screen.blit(silhouette,(silhouettex,silhouettey))
        screen.blit(windows,(lad[X] + 215,lad[Y] - 30))
        level = 28

    if level == 28:
        dialogue = True
        screen.blit(endingBack,(0,0))
        screen.blit(windows,(lad[X] + 215,lad[Y] - 30))
        screen.blit(ladStill,(lad))
        drawScene(screen,lad)
        readDialogue(endingDialogueW1,75,75,counter,BLUE)
        silhouettex = width
        while silhouettex != 1500:
            silhouettex -= 2
            screen.blit(silhouette,(silhouettex,silhouettey))
            screen.blit(ladStill,(lad))
            pygame.display.flip()
            screen.blit(endingBack,(0,0))
        level = 29

    if level == 29:
        stevex,stevey = silhouettex,silhouettey
        silhouettex,silhouettey = 0,0
        screen.blit(ladStill,(lad))
        drawScene(screen,lad)
        dialogue = True
        readDialogue(endingDialogueS1,75,75,counter,RED)
        readDialogue(endingDialogueP1,75,75,counter,YELLOW)
        readDialogue(endingDialogueS2,75,75,counter,RED)
        readDialogue(endingDialogueP2,75,75,counter,YELLOW)
        readDialogue(endingDialogueW2,75,75,counter,BLUE)
        readDialogue(endingDialogueS3,75,75,counter,RED)
        readDialogue(endingDialogueW3,75,75,counter,BLUE)
        readDialogue(endingDialogueP3,75,75,counter,YELLOW)
        readDialogue(endingDialogueW4,75,75,counter,BLUE)
        readDialogue(endingDialogueS4,75,75,counter,RED)
        pygame.mixer.music.load("Music/Undertale Asgore Theme.mp3")
        pygame.mixer.music.play(-1)
        level = 30

    if level == 30:
        bombx = width - 300
        bomby = 300
        surfaceI = pygame.Rect(400,height - 300,30,300)
        surfaceII = pygame.Rect(1700,height - 500,30,300)
        dist = sqrt((stevex - bombx) ** 2 + (stevey - bomby) ** 2)
        if lad[X] > bombx:                           
            bombx += 5
        if lad[X] < bombx:
            bombx -= 5
        if lad[Y] > bomby:
            bomby += 5
        if lad[Y] < bomby:
            bomby -= 5
        if dist < 40:
            level = 31
        

    move(lad,walking,walkingFrame)
    check(lad,surfaceI)
    check(lad,surfaceII)
    check(lad,surfaceIII)
    check(lad,surfaceIV)
    check(lad,surfaceV)
    check(lad,wallI)
    check(lad,wallII)
    check(lad,wallIII)
    check(lad,wallIV)
    check(lad,wallV)
    drawScene(screen,lad)
    pygame.display.flip()
    counter += 1
    clock.tick(60)
            
quit()
