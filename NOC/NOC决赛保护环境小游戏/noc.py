import pygame,sys,time,random
from pygame.locals import *
pygame.init()
canvas=pygame.display.set_mode((1000,700))
pygame.display.set_caption('保护海洋，垃圾分类')
start=pygame.image.load("start.jpg")
bg=pygame.image.load("bg.jpg")
button=pygame.image.load("button.png")
worldmap=pygame.image.load("worldmap.png")
arrowhead=pygame.image.load("arrowhead.png")
arrowhead1=pygame.image.load("arrowhead1.png")
ground=pygame.image.load("ground.jpg")
ground1=pygame.image.load("ground1.jpg")
cleaner1=pygame.image.load("cleaner1.png")
cleaner2=pygame.image.load("cleaner2.png")
enemy1=pygame.image.load("enemy.jpg")
enemy2=pygame.image.load("enemy2.jpg")
b=pygame.image.load("block.jpg")
lb=pygame.image.load("longblock.jpg")
lb1=pygame.image.load("longblock1.jpg")
lkbk=pygame.image.load("luckyblock.jpg")
lkbk1=pygame.image.load("luckyblock.png")
cl=pygame.image.load("coral.png")
net=pygame.image.load("net.png")
flag=pygame.image.load("flag.jpg")
flag1=pygame.image.load("flag2.png")
gold=pygame.image.load("gold.png")
shark=pygame.image.load("shark.png")
rb1=pygame.image.load("rubbishbin1.png")
rb2=pygame.image.load("rubbishbin2.png")
rb3=pygame.image.load("rubbishbin3.png")
lj1=pygame.image.load("laji1.png")
lj2=pygame.image.load("laji2.png")
lj3=pygame.image.load("laji3.png")
win=pygame.image.load("WIN.jpg")

state="START"
astate="NONE"
def handleEvent():
    global state
    for event in pygame.event.get():
        if event.type == QUIT :
            pygame.quit()  
            sys.exit() 
        if event.type==MOUSEBUTTONDOWN and event.button==1:
            x=event.pos[0]
            y=event.pos[1]
            if 405<=x<=596 and 500<=y<=640:
                state="READDY"
            if ah.x1<=x<=ah.x1+ah.width and ah.y1<=y<=ah.y1+ah.height:
                state="RUNNING"
            if ah.x2<=x<=ah.x2+ah.width and ah.y2<=y<=ah.y2+ah.height:
                state="RUNNINGO"
            print(state)
        if event.type==KEYDOWN and event.key==K_RIGHT and p.keystate=="ONE":
            g.state="ONE"
            p.state="ONE"
        if event.type==KEYUP and event.key==K_RIGHT and p.keystate=="ONE":
            g.state="NONE"
            e.state="NONE"
        if event.type==KEYDOWN and event.key==K_LEFT and p.keystate=="ONE":
            g.state="TWO"
            p.state="TWO"  
        if event.type==KEYUP and event.key==K_LEFT and p.keystate=="ONE":
             g.state="NONE"
             e.state="NONE"
        if event.type==KEYDOWN and event.key==K_UP and p.keystate=="ONE":
            p.jump="ONE"
            p.speedY=8
        
class Arrowhead():
    def __init__(self,x,x1,x2,y,y1,y2,width,height,img,img1,speedY):
        self.x=x
        self.x1=x1
        self.x2=x2
        self.y=y
        self.y1=y1
        self.y2=y2
        self.width=width
        self.height=height
        self.img=img
        self.img1=img1
        self.speedY=speedY
    def paint(self):
        canvas.blit(self.img1,(self.x1,self.y1))
        canvas.blit(self.img1,(self.x2,self.y2))   
        fillText("Indian Ocean",(self.x1+3,self.y1+20),25) 
        fillText("Pacific Ocean",(self.x2+3,self.y2+20),25) 
    def move(self):
        self.y+=self.speedY
        self.y1+=self.speedY
        self.y2+=self.speedY
        if self.y>=80:
            self.speedY=-0.5
        if self.y<=60:
            self.speedY=0.5
ah=Arrowhead(140,200,380,60,400,180,111,60,arrowhead,arrowhead1,1)                

class Ground():
    def __init__(self,x,y,x1,y1,width,width1,height,img,aimg,speedX,speedY,state,astate):
        self.x=x
        self.y=y
        self.x1=x1
        self.y1=y1
        self.width=width
        self.width1=width1
        self.height=height
        self.img=img
        self.aimg=aimg
        self.speedX=speedX
        self.speedY=speedY
        self.state=state
        self.astate=astate
    def paint(self):
        canvas.blit(self.img,(self.x,self.y))
        canvas.blit(self.aimg,(self.x1,self.y1))
    def move(self):
            if self.state=="ONE":
                self.x-=self.speedX
                self.x1-=self.speedX
                for i in range(int(len(bX))):
                    bX[i]-=self.speedX
                for i in range(int(len(blX))):
                    blX[i]-=self.speedX
                for i in range(int(len(lblX))):
                    lblX[i]-=self.speedX
                for i in range(int(len(lblXF))):
                    lblXF[i]-=self.speedX
                for i in range(int(len(cX))):
                    cX[i]-=self.speedX
                for i in range(int(len(eX))):
                    eX[i]-=self.speedX
                for i in range(int(len(eXF))):
                    eXF[i]-=self.speedX
                for i in range(int(len(bXF))):
                    bXF[i]-=self.speedX
                for i in range(int(len(blXF))):
                    blXF[i]-=self.speedX
                for i in range(int(len(nX))):
                    nX[i]-=self.speedX
                for i in range(int(len(bXT))):
                    bXT[i]-=self.speedX
                f.x-=self.speedX
                f.x1-=self.speedX
                f.x2-=self.speedX
                for i in range(int(len(rX))):
                    rX[i]-=self.speedX
                rh.x1-=self.speedX
                rh.x2-=self.speedX
                rh.x3-=self.speedX
            if self.state=="TWO":    
                self.x+=self.speedX
                self.x1+=self.speedX
                for i in range(int(len(bX))):
                    bX[i]+=self.speedX
                for i in range(int(len(blX))):
                    blX[i]+=self.speedX
                for i in range(int(len(lblX))):
                    lblX[i]+=self.speedX
                for i in range(int(len(lblXF))):
                    lblXF[i]+=self.speedX
                for i in range(int(len(cX))):
                    cX[i]+=self.speedX
                for i in range(int(len(eX))):
                    eX[i]+=self.speedX
                for i in range(int(len(eXF))):
                    eXF[i]+=self.speedX
                for i in range(int(len(bXF))):
                    bXF[i]+=self.speedX
                for i in range(int(len(blXF))):
                    blXF[i]+=self.speedX
                for i in range(int(len(nX))):
                    nX[i]+=self.speedX
                for i in range(int(len(bXT))):
                    bXT[i]+=self.speedX
                f.x+=self.speedX
                f.x1+=self.speedX
                f.x2+=self.speedX
                for i in range(int(len(rX))):
                    rX[i]+=self.speedX
                rh.x1+=self.speedX
                rh.x2+=self.speedX
                rh.x3+=self.speedX
    def down(self):
        if p.x>self.x1 and p.x+p.width<self.x1+self.width1 and p.y+p.height>=self.y1:
            self.astate="TWO"
        if self.astate=="TWO":
            self.y1+=self.speedY
g=Ground(0,657,2373,657,6676,199,43,ground,ground1,3,5,"NONE","ONE")

class Player():
    def __init__(self,x,y,width,height,img,life,state,astate,jump,speedY,maxjumpdown,keystate,maxUnder):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.img=img
        self.life=life
        self.state=state
        self.astate=astate
        self.jump=jump
        self.speedY=speedY
        self.maxjumpdown=maxjumpdown
        self.keystate=keystate
        self.maxUnder=maxUnder
        self.time=time.time()
    def paint(self):
        canvas.blit(self.img,(self.x,self.y))
        fillText("life X"+str(self.life),(900,10),40)
        if self.state=="ONE":
            self.img=cleaner1
        if self.state=="TWO":    
            self.img=cleaner2
    def moveO(self):
        global state
        if self.jump=="ONE":
            if self.x+self.width>=g.x and self.x<=g.x+g.width and self.y<700:
                self.y-=self.speedY
                self.speedY-=0.1
                self.maxjumpdown=568
                if self.y>self.maxjumpdown:
                    self.y=self.maxjumpdown
                    self.jump="NONE"
                    self.speedY=5
        if self.jump=="NONE":
            self.y+=self.speedY
            if self.y+self.height>=self.maxUnder and self.astate=="ONE":
                self.speedY=5
                self.y=g.y-self.height
            else:
                self.astate="ONE"
                self.maxUnder=568
                self.maxjumpdown=568
            if self.x<=g.x or self.x+self.width>g.x+1092:
                g.state="THREE"
    def move(self):
        global state
        if self.jump=="ONE":
            if self.x+self.width>=g.x and self.x<=g.x+g.width and self.y<700:
                self.y-=self.speedY
                self.speedY-=0.17
                if self.y>self.maxjumpdown:
                    self.y=self.maxjumpdown
                    self.jump="NONE"
                    self.speedY=5
        if self.jump=="NONE":
            self.y+=self.speedY
            if self.y+self.height>=self.maxUnder and self.astate=="ONE":
                self.speedY=5
                self.y=g.y-self.height
            if (self.x>g.x+1092 and self.x+self.width<g.x+1286) or (self.x>g.x+1922 and self.x+self.width<g.x+2094) or (self.x>g.x+2373 and self.x+self.width<g.x+2572):
                self.astate="TWO"
                if self.y>=1000:
                    state="DEAD"
                if self.y>=700:
                    g.speedX=0
            else:
                self.astate="ONE"
                self.maxUnder=568
                self.maxjumpdown=568
    def die(self):
        return self.x+self.width<g.x or g.x+g.width<self.x
    def hitE(self):
        global state
        for i in range(int(len(eX))):
            if self.x+self.width>=eX[i] and eX[i]+e.width>=self.x and self.y+self.height>=eY[i] and eY[i]+e.height>=self.y:
                state="DEAD"
        for i in range(int(len(eXF))):
            if self.x+self.width>=eXF[i] and eXF[i]+e.height>=self.x and self.y+self.height>=eYF[i] and eYF[i]+e.width>=self.y:
                state="DEAD"
    def do(self):
        global state
        self.y-=self.speedY
        self.speedY-=0.2
        self.maxjumpdown=1000
        if self.y>=self.maxjumpdown:
            self.y=self.maxjumpdown
            self.jump="NONE"
            state="RUNNING"
            g.x=0
            g.y=657
            g.x1=2373
            g.y=657
            g.speedX=3
            self.x=100
            self.y=568
            self.life-=1
            self.img=cleaner1
            self.state="ONE"
            self.astate="ONE"
            self.jump="NONE"
            self.speedY=5
            self.maxjumpdown=568
            self.keystate="ONE"
            self.maxUnder=568
            bX.pop()
            bX.pop()
            bX.pop()
            bX.pop()
            bX.append(2280)
            bX.append(2470)
            bX.append(2660)
            bX.append(2960)
            bY.pop()
            bY.pop()
            bY.pop()
            bY.pop()
            bY.append(510)
            bY.append(510)
            bY.append(510)
            bY.append(510)
            bXF.pop()
            bYF.pop()
            bXF.append(1110)
            bYF.append(500)
            bXT.pop()
            bYT.pop()
            bXT.append(2140)
            bYT.append(510)
            eX.pop()
            eX.pop()
            eX.pop()
            eX.append(400)
            eX.append(490)
            eX.append(580)
            eY.append(622)
            eY.append(622)
            eY.append(622)
            eY.pop()
            eY.pop()
            eY.pop()
            eXF.pop()
            eYF.pop()
            eXF.append(850)
            eYF.append(535)
            e.state="NONE"
            blX.pop()
            blX.pop()
            blX.pop()
            blX.pop()
            blX.append(400)
            blX.append(1600)
            blX.append(2960)
            blX.append(3200)
            blY.pop()
            blY.pop()
            blY.pop()
            blY.pop()
            blY.append(510)
            blY.append(300)
            blY.append(500)
            blY.append(470)
            blXF.pop()
            blXF.append(1400)
            blYF.pop()
            blYF.append(450)
            lblX.pop()
            lblX.pop()
            lblX.pop()
            lblY.pop()
            lblY.pop()
            lblY.pop()
            lblX.append(500)
            lblX.append(800)
            lblX.append(2470)
            lblY.append(300)
            lblY.append(510)
            lblY.append(340)
            lblXF.pop()
            lblYF.pop()
            lblXF.append(300)
            lblYF.append(510)
            lblIMG.pop()
            lblIMG.pop()
            lblIMG.pop()
            lblIMG.append(lkbk)
            lblIMG.append(lkbk)
            lblIMG.append(lkbk)
            lblSTATE.pop()
            lblSTATE.pop()
            lblSTATE.pop()
            lblSTATE.append("ONE")
            lblSTATE.append("ONE")
            lblSTATE.append("ONE")
            cX.pop()
            cX.pop()
            cY.pop()
            cY.pop()
            cX.append(840)
            cX.append(2800)
            cY.append(600)
            cY.append(600)
            nX.pop()
            nX.append(1930)
            nY.pop()
            nY.append(-100)
            lkblk.num=0
            f.x=3500
            f.y=368
            f.x1=3512
            f.y1=368
            f.x2=4100
            f.y2=-100
            f.state="ONE"
            f.astate="ONE"
            n.state="ONE"
            g.astate="ONE"
            g.state="NONE"
    def doO(self):
        global state
        g.x=0
        g.y=657
        self.x=100
        self.y=568
        self.img=cleaner1
        self.state="ONE"
        self.astate="ONE"
        self.jump="NONE"
        self.speedY=5
        self.maxjumpdown=568
        self.keystate="ONE"
        self.maxUnder=568
        rX.pop()
        rX.pop()
        rX.pop()
        rY.pop()
        rY.pop()
        rY.pop()
        rX.append(10)
        rX.append(210)
        rX.append(410)
        rY.append(527)
        rY.append(527)
        rY.append(527)
p=Player(100,568,62,89,cleaner1,3,"ONE","ONE","NONE",5,568,"ONE",568)


bX=[2280,2470,2660,2960]
bY=[510,510,510,470]
bXF=[1110]
bYF=[500]
bXT=[2140]
bYT=[510]
class Block():
    def __init__(self,width,height,img,state,astate):
        self.width=width
        self.height=height
        self.img=img
        self.state=state
        self.astate=astate
    def paint(self):
        for i in range(int(len(bX))):
            canvas.blit(self.img,(bX[i],bY[i]))
        for i in range(int(len(bXF))):
           if self.state=="TWO":
                canvas.blit(self.img,(bXF[i],bYF[i]))
        for i in range(int(len(bXT))):
                canvas.blit(self.img,(bXT[i],bYT[i]))
    def hit(self):
        for i in range(int(len(bX))):
            if bX[i]<p.x+p.width<bX[i]+6 and bY[i]-p.height<p.y<bY[i]+self.height:
                g.state="THREE" 
                p.x=bX[i]-p.width
        for i in range(int(len(bXF))):
            if bXF[i]<p.x+p.width<bXF[i]+6 and bYF[i]-p.height<p.y<bYF[i]+self.height and self.state=="TWO":
                g.state="THREE" 
                p.x=bXF[i]-p.width 
        for i in range(int(len(bXT))):
            if bXT[i]<p.x+p.width<bXT[i]+6 and bYT[i]-p.height<p.y<bYT[i]+self.height:
                g.state="THREE" 
                p.x=bXT[i]-p.width
    def hitO(self):
        for i in range(int(len(bX))):
            if bX[i]+self.width-6<p.x<bX[i]+self.width and bY[i]-p.height<p.y<bY[i]+self.height:
                g.state="THREE" 
                p.x=bX[i]+self.width
        for i in range(int(len(bXF))):
            if bXF[i]+self.width-6<p.x<bXF[i]+self.width and bYF[i]-p.height<p.y<bYF[i]+self.height and self.state=="TWO":
                g.state="THREE" 
                p.x=bXF[i]+self.width
        for i in range(int(len(bXT))):
            if bXT[i]+self.width-6<p.x<bXT[i]+self.width and bYT[i]-p.height<p.y<bYT[i]+self.height:
                g.state="THREE" 
                p.x=bXT[i]+self.width        
    def hitT(self):
        for i in range(int(len(bX))):
            if bY[i]<p.y+p.height<bY[i]+self.height and bX[i]-p.width<p.x<bX[i]+self.width:
                p.maxjumpdown=bY[i]
                p.speedY=0
            if p.x>bX[i]+self.width or p.x+p.width<bX[i]:
                p.maxjumpdown=568
        for i in range(int(len(bXF))):
            if bYF[i]<p.y+p.height<bYF[i]+self.height and bXF[i]-p.width<p.x<bXF[i]+self.width and self.state=="TWO":
                p.maxjumpdown=bYF[i]
                p.speedY=0
            if p.x>bXF[i]+self.width or p.x+p.width<bXF[i]:
                p.maxjumpdown=568
        for i in range(int(len(bXT))):
            if bYT[i]<p.y+p.height<bYT[i]+self.height and bXT[i]-p.width<p.x<bXT[i]+self.width:
                bYT[i]=-1000
            if p.x>bXT[i]+self.width or p.x+p.width<bXT[i]:
                    p.maxjumpdown=568
    def hitF(self):
        for i in range(int(len(bX))):
            if bY[i]<p.y<bY[i]+self.height and bX[i]-p.width<p.x<bX[i]+self.width:
                p.speedY*=-1
                p.y=bY[i]+self.height
        for i in range(int(len(bXF))):
            if bYF[i]+21<p.y<bYF[i]+self.height and bXF[i]-p.width<p.x<bXF[i]+self.width:
                p.speedY*=-1
                p.y=bYF[i]+self.height
                self.state="TWO"
        for i in range(int(len(bXT))):
            if bYT[i]<p.y<bYT[i]+self.height and bXT[i]-p.width<p.x<bXT[i]+self.width:
                p.speedY*=-1
                p.y=bYT[i]+self.height
bk=Block(30,30,b,"ONE","ONE")

blX=[400,1600,2960,3200]
blY=[510,300,500,470]  
blXF=[1400]
blYF=[450]  
class LongBlock():
    def __init__(self,width,height,img,speedY,state):
        self.width=width
        self.height=height
        self.img=img
        self.speedY=speedY
        self.state=state
    def paint(self):
        for i in range(int(len(blX))):
            canvas.blit(self.img,(blX[i],blY[i]))
        for i in range(int(len(blXF))):
            canvas.blit(self.img,(blXF[i],blYF[i]))
    def move(self):
        for i in range(int(len(blXF))):
            if self.state=="TWO":
                blYF[i]+=self.speedY
    def hit(self):
        for i in range(int(len(blX))):
            if blX[i]<p.x+p.width<blX[i]+6 and blY[i]-p.height<p.y<blY[i]+self.height:
                g.state="THREE" 
                p.x=blX[i]-p.width
        for i in range(int(len(blXF))):
            if blXF[i]<p.x+p.width<blXF[i]+6 and blYF[i]-p.height<p.y<blYF[i]+self.height:
                g.state="THREE" 
                p.x=blXF[i]-p.width
    def hitO(self):
        for i in range(int(len(blX))):
            if blX[i]+self.width-6<p.x<blX[i]+self.width and blY[i]-p.height<p.y<blY[i]+self.height:
                g.state="THREE" 
                p.x=blX[i]+self.width
        for i in range(int(len(blXF))):
            if blXF[i]+self.width-6<p.x<blXF[i]+self.width and blYF[i]-p.height<p.y<blYF[i]+self.height:
                g.state="THREE" 
                p.x=blXF[i]+self.width
    def hitT(self):
        for i in range(int(len(blX))):
            if blY[i]<p.y+p.height<blY[i]+self.height and blX[i]-p.width<p.x<blX[i]+self.width:
                p.maxjumpdown=blY[i]
                p.speedY=0
            if p.x>blX[i]+self.width or p.x+p.width<blX[i]:
                p.maxjumpdown=568
        for i in range(int(len(blXF))):
            if blYF[i]<p.y+p.height<blYF[i]+self.height and blXF[i]-p.width<p.x<blXF[i]+self.width:
                p.maxjumpdown=blYF[i]
                p.speedY=0
            if p.x>blXF[i]+self.width or p.x+p.width<blXF[i]:
                p.maxjumpdown=568
    def hitF(self):
        global state
        for i in range(int(len(blX))):
            if blY[i]<p.y<blY[i]+self.height and blX[i]-p.width<p.x<blX[i]+self.width:
                p.speedY*=-1
                p.y=blY[i]+self.height
        for i in range(int(len(blXF))):   
            if blXF[i]<p.x+p.width and blXF[i]+self.width>p.x and p.y>blYF[i]+self.height:
                self.state="TWO"
            if self.state=="TWO":
                if p.x+p.width>=blXF[i] and blXF[i]+self.width>p.x and p.y+p.height>blYF[i] and blYF[i]+self.height>p.y:
                    state="DEAD"
lbk=LongBlock(240,30,lb,3,"ONE")    

lblX=[500,800,2470]
lblY=[300,510,340]
lblXF=[300]
lblYF=[510]
lblIMG=[lkbk,lkbk,lkbk]
lblSTATE=["ONE","ONE","ONE"]
class LuckyBlock():
    def __init__(self,width,height,img,state,num):
        self.width=width
        self.height=height
        self.img=img
        self.state=state
        self.num=num
    def paint(self):
        for i in range(int(len(lblX))):
            canvas.blit(lblIMG[i],(lblX[i],lblY[i]))
        for i in range(int(len(lblXF))):
            canvas.blit(self.img,(lblXF[i],lblYF[i]))
    def hit(self):
        for i in range(int(len(lblX))):
            if lblX[i]<p.x+p.width<lblX[i]+6 and lblY[i]-p.height<p.y<lblY[i]+self.height:
                g.state="THREE" 
                p.x=lblX[i]-p.width
        for i in range(int(len(lblXF))):
            if lblXF[i]<p.x+p.width<lblXF[i]+6 and lblYF[i]-p.height<p.y<lblYF[i]+self.height:
                g.state="THREE" 
                p.x=lblXF[i]-p.width
    def hitO(self):
        for i in range(int(len(lblX))):
            if lblX[i]+self.width-6<p.x<lblX[i]+self.width and lblY[i]-p.height<p.y<lblY[i]+self.height:
                g.state="THREE" 
                p.x=lblX[i]+self.width
        for i in range(int(len(lblXF))):
            if lblXF[i]+self.width-6<p.x<lblXF[i]+self.width and lblYF[i]-p.height<p.y<lblYF[i]+self.height:
                g.state="THREE" 
                p.x=lblXF[i]+self.width
    def hitT(self):
        for i in range(int(len(lblX))):
            if lblY[i]<p.y+p.height<lblY[i]+self.height and lblX[i]-p.width<p.x<lblX[i]+self.width:
                p.maxjumpdown=lblY[i]
                p.speedY=0
            if p.x>lblX[i]+self.width or p.x+p.width<lblX[i]:
                p.maxjumpdown=568
        for i in range(int(len(lblXF))):
            if lblYF[i]<p.y+p.height<lblYF[i]+self.height and lblXF[i]-p.width<p.x<lblXF[i]+self.width:
                p.maxjumpdown=lblYF[i]
                p.speedY=0
            if p.x>lblXF[i]+self.width or p.x+p.width<lblXF[i]:
                p.maxjumpdown=568
    def hitF(self):
        for i in range(int(len(lblX))):
            if lblY[i]<p.y<lblY[i]+self.height and lblX[i]-p.width<p.x<lblX[i]+self.width:
                    p.y=lblY[i]+self.height
                    p.speedY*=-1
                    p.y=lblY[i]+self.height 
                    if lblSTATE[i]=="TWO" or lblSTATE[i]=="ONE":
                        lblSTATE[i]="TWO"
            if lblSTATE[i]=="TWO" or lblSTATE[i]=="ONE" or lblSTATE[i]=="THREE":
                        if lblSTATE[i]=="TWO":
                            lblIMG[i]=lkbk1
                            self.num+=1
                            lblSTATE[i]="THREE"
        for i in range(int(len(lblXF))):
            if lblYF[i]<p.y<lblYF[i]+self.height and lblXF[i]-p.width<p.x<lblXF[i]+self.width:
                    lblYF[i]=p.y-self.height
lkblk=LuckyBlock(30,30,lkbk,'ONE',0)

cX=[840,2800]
cY=[600,600]
class Coral():
    def __init__(self,width,height,img,state):
        self.width=width
        self.height=height
        self.img=img
        self.state=state
    def paint(self):
        for i in range(int(len(cX))):
            canvas.blit(self.img,(cX[i],cY[i]))
    def hit(self):
        for i in range(int(len(cX))):
            if cX[i]<p.x+p.width<cX[i]+6 and cY[i]-p.height<p.y<cY[i]+self.height:
                g.state="THREE" 
                p.x=cX[i]-p.width  
            if p.x+p.width>=cX[i]:
                self.state="ONE"
            if self.state=="ONE":
                e.apaint()
                e.amove()
    def hitO(self):
        for i in range(int(len(cX))):
            if cX[i]+self.width-6<p.x<cX[i]+self.width and cY[i]-p.height<p.y<cY[i]+self.height:
                g.state="THREE" 
                p.x=cX[i]+self.width
    def hitT(self):
        for i in range(int(len(cX))):
            if cY[i]<p.y+p.height<cY[i]+self.height and cX[i]-p.width<p.x<cX[i]+self.width:
                p.maxjumpdown=cY[i]
                p.speedY=0
            if p.x>cX[i]+self.width or p.x+p.width<cX[i]:
                p.maxjumpdown=568
c=Coral(66,62,cl,"NONE")

eX=[400,490,580]
eY=[622,622,622]
eXF=[850]
eYF=[535]
class Enemy():
    def __init__(self,width,height,img,aimg,speedX,state):
        self.width=width
        self.height=height
        self.img=img
        self.aimg=aimg
        self.speedX=speedX
        self.state=state
    def paint(self):
        for i in range(int(len(eX))):
            canvas.blit(self.img,(eX[i],eY[i]))
    def apaint(self):
        for i in range(int(len(eXF))):  
            canvas.blit(self.aimg,(eXF[i],eYF[i]))
    def move(self):
        for i in range(int(len(eX))):
            eX[i]-=self.speedX
    def amove(self):
        for i in range(int(len(eYF))):
            eYF[i]-=1
e=Enemy(65,35,enemy1,enemy2,0.5,"NONE")

nX=[1930]
nY=[-100]
class Net():
    def __init__(self,width,height,img,speedY,state):
        self.width=width
        self.height=height
        self.img=img
        self.speedY=speedY
        self.state=state
    def paint(self):
        for i in range(int(len(nX))):
            canvas.blit(self.img,(nX[i],nY[i]))
    def move(self):
        for i in range(int(len(nX))):
            if p.x+p.width>=g.x+1922:
                self.state="TWO"
            if self.state=="TWO":
                nY[i]+=self.speedY 
    def hit(self):
        global state
        for i in range(len(nX)):
            if p.x+p.width>nX[i] and nX[i]+self.width>p.x and p.y+p.height>nY[i] and nY[i]+self.height>p.y:
                state="DEAD"
                
n=Net(109,62,net,15,"ONE")

rX=[10,210,410]
rY=[527,527,527]
rIMG=[rb1,rb2,rb3]
rSTATE=["ONE","TWO","THREE"]
class RubbishBin():
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def paint(self):
        for i in range(int(len(rX))):
            print(1)
            canvas.blit(rIMG[i],(rX[i],rY[i]))
    def hit(self):
        for i in range(int(len(rX))):
            if rX[i]<p.x+p.width<rX[i]+6 and rY[i]-p.height<p.y<rY[i]+self.height:
                g.state="THREE" 
                p.x=rX[i]-p.width  
    def hitO(self):
        for i in range(int(len(rX))):
            if rX[i]+self.width-6<p.x<rX[i]+self.width and rY[i]-p.height<p.y<rY[i]+self.height:
                g.state="THREE" 
                p.x=rX[i]+self.width
    def hitT(self):
        for i in range(int(len(rX))):
            if rY[i]<p.y+p.height<rY[i]+self.height and rX[i]-p.width<p.x<rX[i]+self.width:
                p.maxjumpdown=rY[i]
                p.speedY=0
                if rhList[0]==rSTATE[i]:
                    lkblk.num+=5
                    rhList.pop()
                    rhIMG.pop()
                    rh.state="NONE"
            if p.x>rX[i]+self.width or p.x+p.width<rX[i]:
                p.maxjumpdown=568
rb=RubbishBin(80,130)

rhList=[]
rhIMG=[]
class Rh():
    def __init__(self,x,y,x1,y1,x2,y2,x3,y3):
        self.x=x
        self.y=y
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.x3=x3
        self.y3=y3
        self.state="NONE"
    def paint(self):
        global state
        canvas.blit(rhIMG[0],(self.x,self.y))
        if lkblk.num>=30:
            canvas.blit(lb1,(self.x1,self.y1))
        if lkblk.num>=65:
            canvas.blit(lb1,(self.x2,self.y2))
        if lkblk.num>=100:
            canvas.blit(lb1,(self.x3,self.y3))
            state="WIN"
    def random(self):
        if self.state=="NONE":
            n=random.randint(1,3)
            if n==1:
                rhList.append("ONE")
                rhIMG.append(lj1)
                self.state="HAS"
            if n==2:
                rhList.append("TWO")
                rhIMG.append(lj2)
                self.state="HAS"
            if n==3:
                rhList.append("THREE")
                rhIMG.append(lj3)
                self.state="HAS"
rh=Rh(500,10,900,460,900,260,900,60)

class Flag():
    def __init__(self,x,y,x1,y1,x2,y2,width,height,height1,img,img1,speedY,state,astate):
        self.x=x
        self.y=y
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.width=width
        self.height=height
        self.height1=height1
        self.img=img
        self.img1=img1
        self.speedY=speedY
        self.state=state
        self.astate=astate
    def paint(self):
        canvas.blit(self.img,(self.x,self.y))
        canvas.blit(self.img1,(self.x1,self.y1))
    def move(self):
        global state,astate
        if self.x<p.x+p.width and p.x<self.x+self.width and p.y+p.height>=self.y:
            p.keystate="THREE"
        if p.x+p.width>=self.x:
            canvas.blit(shark,(self.x2,self.y2))
            self.y2+=3
            global state
        if p.x+p.width>self.x2 and self.x2+38>p.x and p.y+p.height>self.y2 and self.y2+75>p.y:
            state="DEAD"
        if p.x+p.width>=self.x+1600:
            state="RUNNINGO"
            p.keystate="ONE"
            p.doO()
        if p.keystate=="THREE":
            p.y+=self.speedY
            g.speedX=0
            self.y1+=self.speedY
            if self.y1+self.height1>=self.y+self.height:
                self.y1=self.y+self.height-self.height1
                self.state="TWO"
            if p.y+p.height>=self.y+self.height:
                p.y=self.y+self.height-p.height
                self.astate="TWO"
            if self.state=="TWO" and self.astate=="TWO":
                p.keystate="FOUR"
        if p.keystate=="FOUR":
            g.state="ONE"
            p.state="ONE"
            g.speedX=3
f=Flag(3500,368,3512,368,4100,-100,12,289,46,flag,flag1,3,"ONE","ONE")

def comPaint():
    if state=="START":
        canvas.blit(start,(0,0))
        canvas.blit(button,(405,500))
    if state=="READDY":
        canvas.blit(worldmap,(0,0))
        ah.paint()
        ah.move()
    if state=="RUNNING" or state=="DEAD":
        canvas.blit(bg,(0,0))
        canvas.blit(gold,(10,10))
        fillText("X"+str(lkblk.num),(30,10),40)
        g.paint()
        p.paint()
        e.paint()
        bk.paint()
        lbk.paint()
        lkblk.paint()
        c.paint()
        n.paint()
        f.paint()
    if state=="RUNNINGO":
        canvas.blit(bg,(0,0))
        canvas.blit(gold,(10,10))
        fillText("X"+str(lkblk.num),(30,10),40)
        g.paint()
        p.paint()
        rh.random()
        rb.paint()
        rh.paint()
    if state=="WIN":
        canvas.blit(win,(0,0))
        fillText("Let us protect oceans",(200,300),70)
def comMove():
    global state,bX
    if state=="RUNNING":
        g.move()
        g.down()
        p.move()
        if p.die():
            state="DEAD"
        e.move()
        lbk.move()
        n.move()
        f.move()
    if state=="RUNNINGO":
        g.move()
        p.moveO()
def checkHit():
    global state
    if state=="RUNNING":
        p.hitE()
        bk.hit()
        bk.hitO()
        bk.hitT()
        bk.hitF()
        lbk.hit()
        lbk.hitO()
        lbk.hitT()
        lbk.hitF()
        lkblk.hit()
        lkblk.hitO()
        lkblk.hitT()
        lkblk.hitF()
        c.hit()
        c.hitO()
        c.hitT()
        p.hitE()
        n.hit()
    if state=="DEAD" or state=="READDY":
        p.do()
    if state=="RUNNINGO":
        rb.hit()
        rb.hitO()
        rb.hitT()
def isActionTime(lastTime, interval):
    if lastTime == 0:
        return True
    currentTime = time.time()
    return currentTime - lastTime >= interval            

def fillText(text,pos,size):
    TextFont=pygame.font.SysFont('微软雅黑', size)
    text=TextFont.render(text,True,(0,255,255))
    canvas.blit(text,pos)

while True:
    print(state)
    comPaint()
    comMove()
    checkHit()
    handleEvent()
    pygame.display.update()
