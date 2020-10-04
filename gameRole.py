import pygame
import random
import math

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 900

TYPE_SMALL = 1
TYPE_MIDDLE = 2
TYPE_BIG = 3

n=1
noth = pygame.image.load('nothing.png')
alert = pygame.image.load('alert.png')
fire1 = pygame.image.load('boss_fire.png')
ice1 = pygame.image.load('boss_ice.png')
fire2 = pygame.image.load('boss_fire2.png')
ice2 = pygame.image.load('boss_ice2.png')
icel = pygame.image.load('icicleltr.png')
icer = pygame.image.load('iciclertl.png')
icet = pygame.image.load('iciclettb.png')
iceb = pygame.image.load('iciclebtt.png')
icell = pygame.image.load('ice_l.png')
icevv = pygame.image.load('ice_v.png')
gb = pygame.image.load('goldboss.png')
gb2 = pygame.image.load('goldboss2.png')
gb3 = pygame.image.load('goldboss3.png')
gb4 = pygame.image.load('goldboss4.png')
gb5 = pygame.image.load('goldboss5.png')
BOSSimg = pygame.image.load('boss_mid_no.png')
BOSSfimg = pygame.image.load('boss_mid_fire.png')
BOSSiimg = pygame.image.load('boss_mid_ice.png')
BOSSdimg = pygame.image.load('boss_mid_dark.png')

stumpimg = pygame.image.load('stump.png')
# 子弹类
class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(bullet_img)
        self.rect = self.image.get_rect()
        self.rect.midbottom = init_pos
        self.speed = 8
    def move(self):
        self.rect.top -= self.speed

class Enemy_Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(bullet_img)
        self.rect = self.image.get_rect()
        self.rect.midbottom = init_pos
        self.speed = 4
    def move(self):
        self.rect.top -= self.speed
    

# 玩家类
class Player(pygame.sprite.Sprite):
    def __init__(self, plane_img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = plane_img                                # 用来存储玩家对象精灵图片的列表
        self.gifttmp1 = 0
        self.gifttmp2 = 0
        self.rect = self.image.get_rect()                # 初始化图片所在的矩形
        self.rect.topleft = init_pos                    # 初始化矩形的左上角坐标
        self.speed = 6                             # 初始化玩家速度，这里是一个确定的值
        self.bullets = pygame.sprite.Group()            # 玩家飞机所发射的子弹的集合
        #self.is_hit = False                             # 玩家是否被击中

    def shoot(self, bullet_img):
        bullet = Bullet(bullet_img, self.rect.midtop)
        self.bullets.add(bullet)

    def moveUp(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed

    def moveDown(self):
        if self.rect.top >= SCREEN_HEIGHT - self.rect.height:
            self.rect.top = SCREEN_HEIGHT - self.rect.height
        else:
            self.rect.top += self.speed

    def moveLeft(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed

    def moveRight(self):
        if self.rect.left >= SCREEN_WIDTH - self.rect.width:
            self.rect.left = SCREEN_WIDTH - self.rect.width
        else:
            self.rect.left += self.speed

# 敌人类
class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.type = 1
        self.hp = 1
        self.score = 500
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        self.speed = random.randint(2, 5)
        if random.randint(0,100) > 90:
            kind = random.randint(0,100)
            if kind < 60:
                self.gift = 1
            elif kind < 70:
                self.gift = 2
            elif kind < 90:
                self.gift = 3
            else:
                self.gift = 4
        else:
            self.gift = 0

    def move(self):
        self.rect.top += self.speed

class Enemy_Big(pygame.sprite.Sprite):
    def __init__(self, enemy_img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.type = 2
        self.hp = 3
        self.score = 1500
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        self.speed = 2
        if random.randint(0,100) > 70:
            kind = random.randint(0,100)
            if kind < 60:
                self.gift = 1
            elif kind < 70:
                self.gift = 2
            elif kind < 90:
                self.gift = 3
            else:
                self.gift = 4
        else:
            self.gift = 0

    def move(self):
        self.speed = 1+(self.rect.topleft[1])*10/SCREEN_HEIGHT
        self.rect.top += self.speed
    
class Enemy_Heavy(pygame.sprite.Sprite):
    def __init__(self, enemy_img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.type = 8
        self.hp = 10
        self.score = 2500
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        self.speed = 2
        if random.randint(0,100) > 20:
            kind = random.randint(0,100)
            if kind < 60:
                self.gift = 1
            elif kind < 70:
                self.gift = 2
            elif kind < 90:
                self.gift = 3
            else:
                self.gift = 4
        else:
            self.gift = 0

    def move(self):
        global n
        self.rect.topleft = [self.rect.topleft[0]+self.speed*n,self.rect.topleft[1]+self.speed]
        if self.rect.right > SCREEN_WIDTH-30:
            n = -1
        if self.rect.left < 0:
            n = 1


class Gift(pygame.sprite.Sprite):
    def __init__(self, gift_img,init_pos,gtype):
       pygame.sprite.Sprite.__init__(self)
       self.image = gift_img
       self.rect = self.image.get_rect()
       self.rect.topleft = init_pos
       self.number = 1
       self.speed = 4
       self.type = gtype

    def move(self):
        self.rect.top += self.speed

#道具小飛機
class Gift_Player(pygame.sprite.Sprite):
    def __init__(self, plane_img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = plane_img                                # 用来存储玩家对象精灵图片的列表
        self.rect = self.image.get_rect()                # 初始化图片所在的矩形
        self.rect.midbottom = [init_pos[0],900]                 # 初始化矩形的左上角坐标
        self.bullets = pygame.sprite.Group()            # 玩家飞机所发射的子弹的集合   
        self.shootf = 1

    def move(self):
        if self.rect.top > 810:
            self.rect.top -= 5

    def moveout(self):
            self.rect.top += 5

    def shoot(self, bullet_img):
        bullet = Bullet(bullet_img, self.rect.midtop)
        self.bullets.add(bullet)

#攻擊
class Attack_fireball(pygame.sprite.Sprite):
    def __init__(self, fire_img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = alert                    
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        self.speed = 20
        self.tmp = fire_img
        self.changeball = False
        self.time = 1
        self.chantime = 0
        

    def move(self):
        self.rect.top += self.speed

    def alertiron(self):
        if self.changeball == False:
            if self.time % 30 == 0:
                self.image = noth
            if self.time % 50 == 0:
                self.image = alert            
                self.time = 1
                self.chantime +=1
            self.time+=1
        else:
            self.rect.top += self.speed
        if self.chantime == 4:
            self.changeball = True
            self.image = self.tmp

class Attack_ice(pygame.sprite.Sprite):
    def __init__(self,pos,x):
        pygame.sprite.Sprite.__init__(self)  
        if x == 1:
            self.image = icel
        if x == 2:
            self.image = icet
                     
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = 20
        self.changeice = False
        self.time = 1
        self.n = x

    def alertiron(self):
        if self.changeice == False:
            if self.time % 120 == 0:      
                self.time = 1
                self.changeice = True
            self.time+=1
        else:
            if self.n == 1:
                self.rect.right += self.speed
            if self.n == 2:
                self.rect.bottom += self.speed

class Attack_darkball(pygame.sprite.Sprite):
    def __init__(self, dark_img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = dark_img                    
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        self.speed = 8
        self.time = 1
        self.n = 1
        self.m = 1
        self.sita = random.randint(20,70)
        self.sitb = random.randint(20,70)
        self.hp = 4
        self.mv = True
        self.die = False

    def move(self):
        if self.mv:
            self.rect.topleft = [self.rect.topleft[0]+self.speed*math.cos(self.sita)*self.n,self.rect.topleft[1]+self.speed*math.sin(self.sitb)*self.m]
            if self.rect.right > SCREEN_WIDTH-30:
                self.n = -1
                self.sita = random.randint(20,70)
            if self.rect.left < 0:
                self.n = 1
                self.sita = random.randint(20,70)
            if self.rect.top < 0:
                self.m = 1
                self.sitb = random.randint(20,70)
            if self.rect.bottom > SCREEN_HEIGHT-30:
                self.m = -1
                self.sitb = random.randint(20,70)
        else:
            self.speed = 20
            self.time += 1
            if self.time >= 50 :
                self.rect.topleft = [self.rect.topleft[0]-((self.rect.topleft[0]-SCREEN_WIDTH/2)/100)*(self.time-50),self.rect.topleft[1]-((self.rect.topleft[1]-50)/100)*(self.time-50)]
            if self.time >= 100 :     
                self.die = True       
                

    def dhp(self): 
        self.hp -= 1
        if self.hp == 3:
            self.image = pygame.image.load('darkball2.png')
        if self.hp == 2:
            self.image = pygame.image.load('darkball3.png')
        if self.hp == 1:
            self.image = pygame.image.load('darkball4.png')
        if self.hp == 0:
            self.image = pygame.image.load('darkballf.png')
            self.mv = False

class Attack_tree(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = stumpimg                    
        self.rect = self.image.get_rect()
        self.rect.center = [random.randint(10,SCREEN_WIDTH-10),random.randint(350,SCREEN_HEIGHT-10)]
        self.time = 1
        self.die = False
        self.rad = 1
        self.boo = False

    def boom(self):
        if self.boo:
            self.time += 1
            if self.time == 20:
                self.die = True

        else:
            if self.rad == 60:
                self.boo = True
                self.time = 1
            else:
                self.time += 1
                if(self.time % 2 == 0):
                    self.rad += 1
        



class BOSS(pygame.sprite.Sprite):
    def __init__(self, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.hp = 224
        self.image = BOSSimg
        self.rect = self.image.get_rect()
        self.rect.bottomleft = init_pos
        self.speed = 2
        self.n = 1
        self.f = 0
        self.atrfir = 0
        self.time = 0
        self.timef = 0
        self.atr = 1    #1tree 2ice 3fire 4dark
        self.dirup = True
        self.cangetime = False
        self.cangedone = False

    def move(self):
        if self.dirup:
            self.rect.top += self.speed
            if self.rect.top > 70:
                self.dirup = False
                self.speed = 1
        elif self.cangetime:
            self.timef+=1
            if self.timef % 10 == 0:
                self.time+=1
            if self.time % 4 == 1:
                self.image = BOSSimg
            if self.time % 4 == 2:
                self.image = BOSSfimg
            if self.time % 4 == 3:
                self.image = BOSSiimg
            if self.time % 4 == 0:
                self.image = BOSSdimg
            if self.time == 12:
                self.cangedone = True
                if self.atr == 1:
                    self.image = BOSSimg
                if self.atr == 2:
                    self.image = BOSSfimg
                if self.atr == 3:
                    self.image = BOSSiimg
                if self.atr == 4:
                    self.image = BOSSdimg
                self.time = 0
                self.timef = 0
        else:
            self.rect.topleft = [self.rect.topleft[0]+self.speed*self.n,self.rect.topleft[1]]
            if self.rect.right > SCREEN_WIDTH:
                self.n = -1
            if self.rect.left < 0:
                self.n = 1

    def dhp(self): 
        self.hp -= 1

    def Attributes(self):
        a = random.randint(0,100)
        if a < 30:
            self.atr = 1
        elif a < 60:
            self.atr = 2
        elif a < 90:
            self.atr = 3
        else:
            self.atr = 4

    def restart(self,init_pos): 
        self.hp = 224
        self.image = BOSSimg
        self.rect = self.image.get_rect()
        self.rect.bottomleft = init_pos
        self.speed = 2
        self.n = 1
        self.f = 0
        self.atrfir = 0
        self.time = 0
        self.timef = 0
        self.atr = 1    #1tree 2ice 3fire 4dark
        self.dirup = True
        self.cangetime = False
        self.cangedone = False

class BOSS_eye(pygame.sprite.Sprite):
    def __init__(self, img,init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.hp = 200
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = init_pos
        self.cankill = False

    def dhp(self): 
        if self.cankill:
            self.hp -= 1

class fire_BOSS(pygame.sprite.Sprite):
    def __init__(self, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.hp = 100
        self.image = fire1
        self.rect = self.image.get_rect()
        self.rect.center = [init_pos[0]+120,init_pos[1]+80]
        self.speed = 2
        self.n = 1
        self.time=1
        self.dirup = True

    def move(self,pos):
        self.rect.center = [pos[0]+120,pos[1]+80]
    
    def flash(self):
        if self.time % 25 == 0:
            self.image = fire2
        if self.time % 50 == 0:
            self.image = fire1            
            self.time = 1
        self.time+=1

    def dhp(self): 
        self.hp -= 1
        

class ice_BOSS(pygame.sprite.Sprite):
    def __init__(self, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.hp = 100
        self.image = ice1
        self.rect = self.image.get_rect()
        self.rect.center = [init_pos[0]-120,init_pos[1]+80]
        self.speed = 2
        self.n = 1
        self.time=1
        self.dirup = True

    def move(self,pos):
        self.rect.center = [pos[0]-120,pos[1]+80]

    def flash(self):
        if self.time % 25 == 0:
            self.image = ice2
        if self.time % 50 == 0:
            self.image = ice1            
            self.time = 1
        self.time+=1
