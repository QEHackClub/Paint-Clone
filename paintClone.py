#paint clone
import pygame
import time
running = True
WIDTH = 380
pygame.font.init()
pygame.init()
rows=10
screen = pygame.display.set_mode((WIDTH,500))
screen.fill((60,25,60))
Lines=[]
for y in range(0,rows):
    Lines.append([])
    for x in range(0,10):
        Lines[y].append("")
        Lines[y][x]="0"
        pygame.draw.rect(screen,(255,25,60),pygame.Rect(0+(x*WIDTH/10),y*WIDTH/10,WIDTH/10,WIDTH/10),width=1)

class button:
    def __init__(self,command,inp,text,dimensions,colour1,colour2,output):
        self.command=command
        self.text=text
        self.dimensions=dimensions
        self.colour1=colour1
        self.colour2=colour2
        self.inp=inp
        self.output=output
        self.active=True
    def create(self):
        self.active=True
        pygame.draw.rect(screen,self.colour1,pygame.Rect(self.dimensions))
        text_to_screen(screen,self.text,self.dimensions[0]+5,self.dimensions[1])
            
    def listen(self):
        if pygame.mouse.get_pressed()[0]==True:
            mx = pygame.mouse.get_pos()[0]
            my = pygame.mouse.get_pos()[1]
            if mx > self.dimensions[0] and mx < (self.dimensions[0]+self.dimensions[2]) and my > self.dimensions[1] and my<self.dimensions[3]+self.dimensions[1]:
                self.output=eval(self.command+"("+str(self.inp)+")")

    def destroy(self):
        pygame.draw.rect(surface=screen,color=(60,25,60),rect=self.dimensions)
        self.active=False
    def setText(self,newText,size=30):
        pygame.draw.rect(surface=screen,color=self.colour1,rect=self.dimensions)
        text_to_screen(screen,newText,self.dimensions[0]+5,self.dimensions[1],size=size)
        
def text_to_screen(screen, text, x, y, size = 30,
            color = (200, 000, 000)):
    try:

        text = str(text)
        font = pygame.font.SysFont(None, 50)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))

    except:
        print('Font Error :(')
tog="output"
foo=""
Stog=""
Range=100
thickness = 8
x = 350
y=680

def paste(inp):
    global running
    running=False
    pygame.quit()
    print("input taken")
    return Lines

def toggle(inp):
    tog=inp[0]
    Range=inp[1]
    thickness=inp[2]
    x=inp[3]
    y=inp[4]
    Lines=inp[5]
    if tog=="input":
        tog="output"
        Switch.setText("paint",size=rows)
        toggle.filler=-1
        
    else:
        tog="input"
        Switch.setText("erase")
        toggle.filler=1
    time.sleep(1)
    return tog
toggle.filler=-1
Switch=button("toggle",[tog,Range,thickness,x,y,Lines],"paint",(100,400,100,50),(40,40,160),(0,0,0),Stog)
Switch.create()
Switch.output=tog
output=button("paste",[Lines],   "print",(200,400,100,50), (0,100,0),(0,0,100),False)
output.create()

#mainloop
while running:
    Switch.listen()
    output.listen()
    if running == True:       
        tog=Switch.output
        Switch.inp=[tog,Range,thickness,x,y,Lines]
        pygame.init()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
        if pygame.mouse.get_pressed()[0]==True:
            for y in range(0,rows):
                if y*WIDTH/10 < pygame.mouse.get_pos()[1] and (y+1)*WIDTH/10 > pygame.mouse.get_pos()[1]:
                    for x in range(0,31):
                        if 0+(x*WIDTH/10)<pygame.mouse.get_pos()[0] and 0+((x+1)*WIDTH/10) > pygame.mouse.get_pos()[0]:
                            if toggle.filler==-1:
                                pygame.draw.rect(screen,(255,25,60),pygame.Rect(0+(x*WIDTH/10),y*WIDTH/10,WIDTH/10,WIDTH/10))
                                Lines[y][x]="1"
                            else:
                                pygame.draw.rect(screen,(60,25,60),pygame.Rect(0+(x*WIDTH/10),y*WIDTH/10,WIDTH/10,WIDTH/10))
                                pygame.draw.rect(screen,(255,25,60),pygame.Rect(0+(x*WIDTH/10),y*WIDTH/10,WIDTH/10,WIDTH/10),width=1)
                                Lines[y][x]="0" 
pygame.quit()
