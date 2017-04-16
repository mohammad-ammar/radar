import serial
import pygame
import math
import sys
from pygame.locals import *

pygame.init()
width,height=700,700
disp=pygame.display.set_mode((width,height))
ser=serial.Serial()
ser.timeout=1
ser.port='com6' # port name where the arduino 
ser.open()
green=(0,255,0)
point_list=[]

##convert functions
def to_window(x,y): # coordinate to window
    x,y=int(x),int(y)
    n_x=x+width//2
    n_y=height//2 -y
    return([n_x,n_y])

def to_radian(angle):
    x=(angle*3.14)/180
    return(x)
##

##draw function
def add_to_list(angle,distance):
    global point_list
    distance*=10
    angle=to_radian(angle)
    x,y=math.cos(angle)*distance,math.sin(angle)*distance
    pos=to_window(x,y)
    point_list.append(pos)
    
def draw_point(list_point,disp=disp):
    for point in list_point:
        pygame.draw.circle(disp,green,point,2)

def draw_circles(disp=disp):
    raduis=50
    for x in range(1,width//2):
        n_raduis=((x//raduis)+1)*raduis
        pygame.draw.circle(disp,green,(width//2,height//2),n_raduis,2)
def draw_line(angle,disp=disp):
    a=math.tan(to_radian(angle))
    y=height//2
    if a==0:
        y=0
        if angle==0:x=width/2
        elif angle==180:x=-width/2
    else:x=y//a
    pos=to_window(x,y)
    pygame.draw.line(disp,green,(width/2,height/2),pos,2)

def angle_distance(ser):
    #ser.reset_input_buffer()
    read_input=ser.readline()
    read_input=read_input.decode()
    read_input=read_input[:len(read_input)-2]
    read_input=read_input.split(";")
    if len(read_input)!=2 or ("" in read_input):
        return(False)
    return(read_input)

def draw_text(disp,text,t_size):
        fontObj = pygame.font.Font('freesansbold.ttf',t_size)
        textSurface=fontObj.render(text, True,(255,255,255))
        disp.blit(textSurface,(0,0))
        
##main##
while True:
    disp.fill((0,0,0))
    angle_dist=angle_distance(ser)
    if angle_dist==False:continue
    angle,dist=float(angle_dist[0]),float(angle_dist[1])
    if (angle==0 or angle==180):point_list=[]
    draw_circles(disp)
    draw_line(angle)
    add_to_list(angle,dist)
    draw_point(point_list)
    draw_text(disp,"angle = "+str(angle)+", distance = "+str(dist),15)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    
