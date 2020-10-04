# -*- coding: utf-8 -*-
from sys  import exit
import pygame
from gameRole import *
from pygame.locals import *
import random
import time

def clear():
    global game_start,Settlement,Attack_Start,canattack
    bg_sound.stop()
    gifts.empty()
    gplay.empty()
    enemies1.empty()
    fireball.empty()
    darkball.empty()
    tree.empty()
    ice.empty()
    mainplayer.gifttmp1 = 0
    mainplayer.gifttmp2 = 0
    mainplayer.bullets.empty()
    game_start = False
    Settlement = True
    Attack_Start = False
    canattack = False
    BOSS.restart([SCREEN_WIDTH/2-150,0])


#初始設定(名稱.大小)
pygame.init()
window_surface = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('天空之戰')
clock = pygame.time.Clock() 

#變數設定
bt_pos = 460                                #主畫面按鈕
bt_pl = 80                                  #主畫面按鈕間距
score = 0                                   #分數
shoot_f = 1                                 #射擊計數
enemy_f = 0                                 #敵人出現頻率
fire_f = 0                                  #火球出現頻率
tree_f = 0                                  #樹出現頻率
Dark_f = 0                                  #暗球出現頻率
ice_f = 0
bulspd = 20                                 #射擊頻率
gtime1 = 0                                  #道具1計時器
gtime2 = 0                                  #道具2計時器
gtime3 = 0                                  #道具3計時器
background_pos = [0,0]                      #場景滾動
kc = 0                                      #上下左右鍵盤放開檢查
haveHeavy = False                           #控制大隻出現量
Action = True                               #控制行動暫停(達分)
enemyice = False                            #敵人行動暫停(道具)
Boss_time = False                           #敵人行動(boss)
FireBall_Attack = False                     #火球控制
DarkBall_Attack = False                     #暗球控制
Tree_Attack = False                     #樹控制
Ice_Attack = False
DarkBall_time = False                     #暗球控制
fire_time = False                            #火閃爍
ice_time = False                            #冰閃爍
Attack_Start = False  
canattack = False

#群組設定
enemies1 = pygame.sprite.Group()            #一般敵人群
gifts = pygame.sprite.Group()               #道具掉落
gplay = pygame.sprite.Group()               #道具友軍群
fireball = pygame.sprite.Group()            #火球群
darkball = pygame.sprite.Group()            #黑球群
tree = pygame.sprite.Group()            #樹群
ice = pygame.sprite.Group()            #冰群
game_start = False                          #模式開始遊戲
game_init = True                            #模式遊戲初始化
Settlement = False                          #模式結算畫面
game_Introduction = False                   #模式介紹畫面
game_member = False                         #模式成員畫面

#圖片載入
titleground = pygame.image.load('titleground.png')
memberpng = pygame.image.load('member.png')
methodpng = pygame.image.load('method.png')
lose = pygame.image.load('lose.png')
Frame = pygame.image.load('Frame.png')
button = pygame.image.load('button.png')
prppbox = pygame.image.load('prop_box.png')
background = pygame.image.load('backgroundf.png')
backgroundc = pygame.image.load('backgroundf.png')
bulimg = 'bul.png'
mainimg = pygame.image.load('plane.png')
mainlimg = pygame.image.load('planeleft.png')
mainrimg = pygame.image.load('planeright.png')
enemyimg = pygame.image.load('enemy.png')
enemybigimg = pygame.image.load('enemybig.png')
enemyheavyimg = pygame.image.load('enemyheavy.png')
gift = pygame.image.load('gift.png')
gift2 = pygame.image.load('gift2.png')
gift3 = pygame.image.load('gift3.png')
gift4 = pygame.image.load('gift4.png')
giftiron = pygame.image.load('giftiron.png')
gift2iron = pygame.image.load('gift2iron.png')
gift3iron = pygame.image.load('gift3iron.png')
gift4iron = pygame.image.load('gift4iron.png')
giftplan = pygame.image.load('giftplan1.png')
giftplan2 = pygame.image.load('giftplan2.png')
giftplan3 = pygame.image.load('giftplan3.png')
giftplan4 = pygame.image.load('giftplan4.png')
firebp = pygame.image.load('fireball.png')
darkbp = pygame.image.load('darkball.png')
BOSSfireimg = pygame.image.load('boss_fire.png')
BOSSiceimg = pygame.image.load('boss_ice.png')
treebeforeimg = pygame.image.load('tree_before.png')
BOSSeye = pygame.image.load('eye.png')

#音樂載入
bg_sound = pygame.mixer.Sound('bgmusic.wav')
bulsound = pygame.mixer.Sound('BombSound_solider.wav')

#初始精靈
mainplayer = Player(mainimg, [200,700])
BOSS = BOSS([SCREEN_WIDTH/2-150,0])
eye = BOSS_eye(BOSSeye,[BOSS.rect.center[0]-19,BOSS.rect.center[1]-54])
iBOSS = ice_BOSS(BOSS.rect.center)
while True:
    if game_Introduction:
        bg_sound.stop()
        window_surface.blit(methodpng, [0,0])
        head_font = pygame.font.Font("DFGothic-EB.ttc", 30,italic=True)
        window_surface.blit(button, (350,810))
        text_surface = head_font.render('返回主畫面',True,(0,0,0))
        window_surface.blit(text_surface,(370,820))
        if event.type == MOUSEBUTTONDOWN:
            if(pygame.mouse.get_pos()[0] > 350 and pygame.mouse.get_pos()[0] < 550 and pygame.mouse.get_pos()[1] > 810):
                game_Introduction=False
    elif game_member:
        window_surface.blit(memberpng, [0,0])
        bg_sound.stop()
        head_font = pygame.font.Font("DFGothic-EB.ttc", 30,italic=True)
        window_surface.blit(button, (350,810))
        text_surface = head_font.render('返回主畫面',True,(0,0,0))
        window_surface.blit(text_surface,(370,820))
        if event.type == MOUSEBUTTONDOWN:
            if(pygame.mouse.get_pos()[0] > 350 and pygame.mouse.get_pos()[0] < 550 and pygame.mouse.get_pos()[1] > 810):
                game_member=False
    elif game_start:
        if game_init:
            Attack_Start = False
            bg_sound.play()
            Boss_time = False 
            bulspd = 20   
            score = 0
            gtime1 = 0
            gtime2 = 0
            gtime3 = 0
            haveHeavy = False                          
            Action = True                           
            enemyice = False      
            shoot_f = 1
            enemy_f = 0
            fire_f = 0
            mainplayer = Player(mainimg, [200,700])
            game_init = False
            Boss_time = False          
            FireBall_Attack = False    
            DarkBall_Attack = False 
            Tree_Attack = False
            Ice_Attack = False
            fire_time = False                        
            ice_time = False  
            enemyice = False
            canattack = False
            
        clock.tick(60)
        window_surface.fill(0)
        window_surface.blit(background, background_pos)
        window_surface.blit(backgroundc, (background_pos[0], -SCREEN_HEIGHT+background_pos[1]))
        window_surface.blit(mainplayer.image,mainplayer.rect)
        
        #play control
        if shoot_f % bulspd == 0:
            mainplayer.shoot(bulimg)
            
        shoot_f += 1
        if shoot_f > bulspd:
            shoot_f = 1

        #bullet control
        for bullet in mainplayer.bullets:
            bullet.move()
            if(bullet.rect.bottom < 0):
                mainplayer.bullets.remove(bullet)

        #enemy control
        for enemy in enemies1:
            if enemyice == False:
                enemy.move()
            if enemy.type == 3:
                haveHeavy = True
            if pygame.sprite.collide_circle_ratio(0.8)(enemy,mainplayer) :
                clear()
            if enemy.rect.top > SCREEN_HEIGHT-30:
                enemies1.remove(enemy)

        if Action:
            if enemyice == False:
                if haveHeavy:
                    enemy_kind = random.randint(1,95)
                else:
                    enemy_kind = random.randint(1,100)

                if enemy_f % 40 == 0:
                    enemy_pos = [random.randint(0, SCREEN_WIDTH-57), 0]
                    if enemy_kind > 95 :
                        enemy = Enemy_Heavy(enemyheavyimg, enemy_pos)
                    elif enemy_kind > 85 :
                        enemy = Enemy_Big(enemybigimg, enemy_pos)
                    else:
                        enemy = Enemy(enemyimg, enemy_pos)
                    enemies1.add(enemy)
                enemy_f += 1
                if enemy_f >= 40:
                    enemy_f = 0

        
        enemies1.draw(window_surface)
        
        #enemy bullet collide
        BEcollide = pygame.sprite.groupcollide(enemies1, mainplayer.bullets,0,1)
        for n in BEcollide:
            if n.hp == 1:
                score += n.score
                bulsound.play()
                bulsound.set_volume(0.4)
                enemies1.remove(n)
                if mainplayer.gifttmp1 == 0 or  mainplayer.gifttmp2 == 0:
                    if n.gift == 1:
                        gifts.add(Gift(gift,[n.rect[0],n.rect[1]],1))
                    if n.gift == 2:
                        gifts.add(Gift(gift2,[n.rect[0],n.rect[1]],2))
                    if n.gift == 3:
                        gifts.add(Gift(gift3,[n.rect[0],n.rect[1]],3))
                    if n.gift == 4:
                        gifts.add(Gift(gift4,[n.rect[0],n.rect[1]],4))
            else:
                n.hp -= 1

        #gift control
        for a in gifts:
            a.move()
        gifts.draw(window_surface)

        for n in gifts:
            if pygame.sprite.collide_circle_ratio(0.8)(n,mainplayer):
                if mainplayer.gifttmp1 == 0:
                    mainplayer.gifttmp1 = n.type
                else:
                    mainplayer.gifttmp2 = n.type
                gifts.remove(n)
                
        #gift1連射
        if gtime1 > 0:
            gtime1 += 1
            bulspd = 5
        if gtime1 > 200:
            gtime1 = 0
            bulspd = 20

        #gift2小飛機
        if gtime2 == 1:
            gtime2 += 1
            gplay.add(Gift_Player(giftplan,[SCREEN_WIDTH/6,800]))
            gplay.add(Gift_Player(giftplan2,[2*SCREEN_WIDTH/6,800]))
            gplay.add(Gift_Player(giftplan3,[4*SCREEN_WIDTH/6,800]))
            gplay.add(Gift_Player(giftplan4,[5*SCREEN_WIDTH/6,800]))

        if gtime2 > 400:
            for friend in gplay:
                friend.moveout()
                if friend.rect.top > 900:
                    gtime2 = 0
                    gplay.empty()
                    
        elif gtime2 > 1:
            gtime2 += 1
            for friend in gplay:
                friend.move()
                if friend.shootf % bulspd == 0:
                    friend.shoot(bulimg)
                friend.shootf += 1
                if friend.shootf > bulspd:
                    friend.shootf = 1
                for bullet in friend.bullets:
                    mainplayer.bullets.add(bullet)
                    friend.bullets.remove(bullet)
                #     bullet.move()
                #     if(bullet.rect.bottom < 0):
                #         friend.bullets.remove(bullet)
                # friend.bullets.draw(window_surface)
                # BEcollide = pygame.sprite.groupcollide(enemies1, friend.bullets,0,1)
                # for n in BEcollide:
                #     if n.hp == 1:
                #         score += n.score
                #         enemies1.remove(n)
                #     else:
                #         n.hp -= 1
        gplay.draw(window_surface)

        #gift1凍結
        if gtime3 > 0:
            gtime3 += 1
            enemyice = True
        if gtime3 > 300:
            gtime3 = 0
            enemyice = False

        #Boss
        if score >= 20000:       #*********************************
            Action = False
            if len(enemies1) == 0:
                Boss_time = True

        if Boss_time:
            BOSS.move()
            window_surface.blit(eye.image,[BOSS.rect.center[0]-19,BOSS.rect.center[1]-54])
            # window_surface.blit(fBOSS.image,fBOSS.rect)
            # window_surface.blit(iBOSS.image,iBOSS.rect)
            if BOSS.dirup == False:
                pygame.draw.rect(window_surface, (200, 0, 0), (BOSS.rect.left+52, 20, SCREEN_WIDTH-400, 20))
                pygame.draw.rect(window_surface, (0, 200, 0), (BOSS.rect.left+52, 19, float(SCREEN_WIDTH-400)*(float(BOSS.hp)/224), 20))
                Attack_Start = True
                BOSS.f += 1
            if  BOSS.f == 1:
                canattack = True                          
            # if fire_time:
            #     fBOSS.flash()
            # if ice_time:
            #     iBOSS.flash()
            

            if BOSS.hp == 100:
                mainplayer.speed = 6
                BOSS.hp=99
                BOSS.atr = 4
                fireball.empty()
                darkball.empty()
                tree.empty()
                Attack_Start = False
                canattack = False
                BOSS.cangetime = True
                # if BOSS.cangedone:
                #     canattack = True
                #     BOSS.cangetime = False
                #     BOSS.cangedone = False
                #     Attack_Start = True
            elif BOSS.hp % 25 == 0:
                mainplayer.speed = 6
                BOSS.atr = 0
                git = random.randint(0,100)
                if git > 30 :
                    gifts.add(Gift(gift2,BOSS.rect.center,2))
                else:
                    gifts.add(Gift(gift,BOSS.rect.center,1))
                fireball.empty()
                darkball.empty()
                tree.empty()
                BOSS.Attributes()
                Attack_Start = False
                canattack = False
                BOSS.cangetime = True
                print(BOSS.atr)
                BOSS.hp-=1

            if BOSS.cangedone:
                canattack = True
                BOSS.cangetime = False
                Attack_Start = True
                BOSS.cangedone = False
            
            window_surface.blit(BOSS.image,BOSS.rect)
            
            if Attack_Start:
                if BOSS.atr == 0:
                    Ice_Attack = False
                    Tree_Attack = False
                    FireBall_Attack = False
                    DarkBall_Attack = False
                if BOSS.atr == 1:
                    Ice_Attack = False
                    Tree_Attack = True
                    FireBall_Attack = False
                    DarkBall_Attack = False
                if BOSS.atr == 2:
                    Ice_Attack = False
                    FireBall_Attack = True
                    Tree_Attack = False
                    DarkBall_Attack = False
                if BOSS.atr == 3:
                    Ice_Attack = True
                    Tree_Attack = False
                    FireBall_Attack = False
                    DarkBall_Attack = False
                if BOSS.atr == 4:
                    Ice_Attack = False
                    DarkBall_Attack = True
                    Tree_Attack = False
                    FireBall_Attack = False
            else:
                Ice_Attack = False
                Tree_Attack = False
                FireBall_Attack = False
                DarkBall_Attack = False
        if Tree_Attack:
            if tree_f % 20 == 0:
                tree.add(Attack_tree())
                tree_f = 0
            tree_f += 1
            for tr in tree:
                if tr.die:
                    tree.remove(tr)
                    continue
                tr.boom()
                if tr.boo:
                    window_surface.blit(tr.image,tr.rect)
                else:
                    window_surface.blit(pygame.transform.scale(treebeforeimg, (tr.rad,tr.rad)),tr.rect)

                if pygame.sprite.collide_circle_ratio(0.8)(tr,mainplayer) and tr.boo:
                    clear()
        #attack ice
        if Ice_Attack:
            mainplayer.speed = 4
            if ice_f % 300 == 0:
                icetmp = random.randint(2,295)
                for i in range(3):
                    ice.add(Attack_ice([0,300*i+icetmp],1))
            if ice_f % 200 == 0:
                icetmp = random.randint(2,295)
                for i in range(2):
                    ice.add(Attack_ice([300*i+icetmp,0],2))
            ice_f += 1
            for ic in ice:
                ic.alertiron()
                if ic.rect.top >SCREEN_HEIGHT or ic.rect.left > SCREEN_WIDTH:
                    ice.remove(ic)
                if pygame.sprite.collide_circle_ratio(0.8)(ic,mainplayer):
                    clear()
            ice.draw(window_surface)

        #attack fire
        if FireBall_Attack:
            if fire_f % 60 == 0:
                fireballpos = [random.randint(0,SCREEN_WIDTH-60), 0]
                fireball.add(Attack_fireball(firebp,fireballpos))
                fire_f = 0
            fire_f += 1
            
            for ball in fireball:
                ball.alertiron()
                if pygame.sprite.collide_circle_ratio(0.8)(ball,mainplayer) :
                    clear()
            fireball.draw(window_surface)

        if DarkBall_Attack:
            canattack = False
            if Dark_f % 100 == 0:
                DarkBall_time = True
            Dark_f+=1
            if DarkBall_time:
                darkball.add(Attack_darkball(darkbp,BOSS.rect.center))
                DarkBall_time = False
            for ball in darkball: 
                ball.move()
                if ball.die:
                    darkball.remove(ball)
                    if BOSS.hp%5 == 0:
                        BOSS.hp -= 5
                    else:
                        BOSS.hp -= BOSS.hp%5
                if pygame.sprite.collide_circle_ratio(0.8)(ball,mainplayer):
                    clear()

            BEcollide = pygame.sprite.groupcollide(darkball, mainplayer.bullets,0,1)
            for n in BEcollide:
                n.dhp()
        
            darkball.draw(window_surface)
            
            if BOSS.hp < 0:
                mainplayer.speed = 6
                Boss_time = False
                Action = True
                Ice_Attack = False
                Tree_Attack = False
                FireBall_Attack = False
                DarkBall_Attack = False

        mainplayer.bullets.draw(window_surface)

        if canattack:
            for b in mainplayer.bullets: 
                if pygame.sprite.collide_circle_ratio(0.8)(b,BOSS):
                    print(BOSS.hp)
                    BOSS.dhp()
                    mainplayer.bullets.remove(b)

        if pygame.sprite.collide_circle_ratio(0.8)(BOSS,mainplayer):
            clear()

        #鍵盤控制
        kc = 0
        key_pressed = pygame.key.get_pressed()
        if key_pressed[K_w] or key_pressed[K_UP]:
            mainplayer.moveUp()
            kc = 1
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            mainplayer.moveDown()
            kc = 1
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            mainplayer.moveLeft()
            mainplayer.image = mainlimg
            kc = 1
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            mainplayer.moveRight()
            mainplayer.image = mainrimg
            kc = 1
        if key_pressed[K_j]:
            if mainplayer.gifttmp1 == 1:
                gtime1 = 1
            if mainplayer.gifttmp1 == 2:
                gtime2 = 1
            if mainplayer.gifttmp1 == 3:
                gtime3 = 1
            if mainplayer.gifttmp1 == 4:
                for enemy in enemies1:
                    enemy.hp -= 8
                    if enemy.hp < 1:
                        score += enemy.score
                        enemies1.remove(enemy)
            mainplayer.gifttmp1 = 0

        if key_pressed[K_k]:
            if mainplayer.gifttmp2 == 1:
                gtime1 = 1
            if mainplayer.gifttmp2 == 2:
                gtime2 = 1
            if mainplayer.gifttmp2 == 3:
                gtime3 = 1
            if mainplayer.gifttmp2 == 4:
                for enemy in enemies1:
                    enemy.hp -= 8
                    if enemy.hp < 1:
                        score += enemy.score
                        enemies1.remove(enemy)
            mainplayer.gifttmp2 = 0
        if kc == 0:
            mainplayer.image = mainimg

        #background control
        background_pos[1] += 1
        if background_pos[1] == SCREEN_HEIGHT:
            background_pos[1] = 0
        
        #score
        head_font = pygame.font.Font("DFGothic-EB.ttc", 30,italic=True)
        text_surface = head_font.render('分數:'+str(score),True,(255,186,96))
        window_surface.blit(text_surface,(10,10))
        window_surface.blit(prppbox,(10,60))
        if mainplayer.gifttmp1 == 1:
            window_surface.blit(giftiron,(25,75))
        if mainplayer.gifttmp1 == 2:
            window_surface.blit(gift2iron,(25,75))
        if mainplayer.gifttmp1 == 3:
            window_surface.blit(gift3iron,(25,75))
        if mainplayer.gifttmp1 == 4:
            window_surface.blit(gift4iron,(25,75))

        if mainplayer.gifttmp2 == 1:
            window_surface.blit(giftiron,(105,75))
        if mainplayer.gifttmp2 == 2:
            window_surface.blit(gift2iron,(105,75))
        if mainplayer.gifttmp2 == 3:
            window_surface.blit(gift3iron,(105,75))
        if mainplayer.gifttmp2 == 4:
            window_surface.blit(gift4iron,(105,75))
        #pygame.draw.rect(window_surface,[255,0,0],[25,75,50,50],0)
        #pygame.draw.rect(window_surface,[255,0,0],[105,75,50,50],0)
        
    elif Settlement:
        bg_sound.stop()
        window_surface.blit(lose, [0,0])
        head_font = pygame.font.SysFont('GothicE',100)
        text_surface = head_font.render('GAME',True,(0,0,0))
        window_surface.blit(text_surface,(SCREEN_WIDTH/2-text_surface.get_width()/2,180))
        text_surface = head_font.render('OVER',True,(0,0,0))
        window_surface.blit(text_surface, (SCREEN_WIDTH/2-text_surface.get_width()/2,280))
        window_surface.blit(button, (80,510))
        window_surface.blit(button, (330,510))
        head_font = pygame.font.Font("DFGothic-EB.ttc", 30,italic=True)
        text_surface = head_font.render('最終得分:'+str(score),True,(0,0,0))
        window_surface.blit(text_surface,(SCREEN_WIDTH/2-text_surface.get_width()/2,410))
        head_font = pygame.font.Font("DFGothic-EB.ttc", 30,italic=True)
        text_surface = head_font.render('再玩一次',True,(0,0,0))
        window_surface.blit(text_surface,(120,520))
        text_surface = head_font.render('返回選單',True,(0,0,0))
        window_surface.blit(text_surface,(370,520))
        
    else:
        bg_sound.stop()
        #print(pygame.font.get_fonts())
        window_surface.blit(titleground, [0,0])
        #pygame.draw.rect(window_surface,[255,0,0],[100,400,300,400],0)
        window_surface.blit(Frame, (150,400))
        window_surface.blit(button, (200,bt_pos))
        window_surface.blit(button, (200,bt_pos+bt_pl))
        window_surface.blit(button, (200,bt_pos+2*bt_pl))
        window_surface.blit(button, (200,bt_pos+3*bt_pl))
        head_font = pygame.font.Font("DFGothic-EB.ttc", 30,italic=True)
        text_surface = head_font.render('開始遊戲',True,(0,0,0))
        window_surface.blit(text_surface,(240,bt_pos+10))
        text_surface = head_font.render('玩法介紹',True,(0,0,0))
        window_surface.blit(text_surface,(240,bt_pos+bt_pl+10))
        text_surface = head_font.render('開發人員',True,(0,0,0))
        window_surface.blit(text_surface,(240,bt_pos+2*bt_pl+10))
        text_surface = head_font.render('離開遊戲',True,(0,0,0))
        window_surface.blit(text_surface,(240,bt_pos+3*bt_pl+10))
        #window_surface.blit(background, (0, 0))
        #window_surface.blit(title, (SCREEN_WIDTH/2,60))
        head_font = pygame.font.Font("DFGothic-EB.ttc", 100,italic=True)
        text_surface = head_font.render('天  空',True,(0,127,255))
        window_surface.blit(text_surface,(SCREEN_WIDTH/2-text_surface.get_width()/2-20,60))
        text_surface = head_font.render(' 之  戰',True,(0,127,255))
        window_surface.blit(text_surface,(SCREEN_WIDTH/2-text_surface.get_width()/2-10,200))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            if(pygame.mouse.get_pos()[0] > 150 and pygame.mouse.get_pos()[0] < 400 and pygame.mouse.get_pos()[1] > bt_pos and game_start == False and Settlement == False):
                if(pygame.mouse.get_pos()[1] < bt_pos+bt_pl):
                    game_start = True
                    game_init = True
                elif(pygame.mouse.get_pos()[1] < bt_pos+2*bt_pl):
                    game_Introduction = True
                elif(pygame.mouse.get_pos()[1] < bt_pos+3*bt_pl):
                    game_member = True
                elif(pygame.mouse.get_pos()[1] < bt_pos+4*bt_pl):
                    pygame.quit()
                    exit()
            if(pygame.mouse.get_pos()[1] > 500 and pygame.mouse.get_pos()[1] < 550 and pygame.mouse.get_pos()[0] > 30 and Settlement and game_start == False):
                if(pygame.mouse.get_pos()[0] < 230):
                    game_start = True
                    game_init = True
                    Settlement == False
                elif(pygame.mouse.get_pos()[0] < 480 and pygame.mouse.get_pos()[0] > 280):
                    game_start = False
                    Settlement = False