#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#3-1-4-2.py
import sys, pygame
import random
import time
import pygame_menu




def drawCheckerBoard(screen):
    screen.blit(bjpic,(0,0)) 
    gameRectWidth=gameRectHeight=mainWidth-INTERSPACE*2
    pygame.draw.rect(screen,'blue1',(INTERSPACE,INTERSPACE,gameRectWidth,gameRectHeight),width=2)
    cellWidth=cellHeight=gameRectWidth/CELLCOUNT
    i=INTERSPACE
    while i<=gameRectHeight:
        i+=cellHeight
        pygame.draw.line(screen,'blue4',(INTERSPACE,i),(gameRectWidth+INTERSPACE,i), 1)
        pygame.draw.line(screen,'blue4',(i,INTERSPACE),(i,gameRectWidth+INTERSPACE), 1)
    pygame.display.update()
    return (cellWidth,cellHeight) 

def initCells(screen):
    cellW,cellH=drawCheckerBoard(screen)
    cellInfo=[[[-1,(cellW*j+INTERSPACE,cellH*i+INTERSPACE)] for i in range(CELLCOUNT)] for j in range(CELLCOUNT)]
    return cellInfo,cellW,cellH

def getPos(x,y,cellW,cellH):
    return int((x-INTERSPACE)/cellW),int((y-INTERSPACE)/cellH)

def drawCell(screen,i,j,piece,cellWidth,cellHeight):
    screen.blit(piece,cellsInfo[i][j][1])
    pygame.display.flip()
    
def downPiece(screen,i,j,piece,cellWidth,cellHeight,nowPieceId):
        drawCell(screen,i,j,piece,cellWidth,cellHeight)
        cellsInfo[i][j][0]=nowPieceId



def getNextScanPos(x,y,scanPos):
    return (x+scanPos[0],y+scanPos[1])

def isWin(i,j):
    nowX=i
    nowY=j
    successPosCount=0
    scanPos=[]
    #X axis
    scanPos.append([(i,0) for i in range(-5,6)])    
    #Y axis
    scanPos.append([(0,i) for i in range(-5,6)])   
    # 左上方到右下方
    scanPos.append([(i,-i) for i in range(-5,6)])  
    #右上方到左下方   
    scanPos.append([(i,i) for i in range(-5,6)])  
    isGameWin=False
    for scanDirection in scanPos:
        for scanXAdd,scanYAdd in scanDirection:
            scanX=nowX+scanXAdd
            scanY=nowY+scanYAdd
            if cellsInfo[scanX][scanY][0]==cellsInfo[nowX][nowY][0]:
                successPosCount+=1
            else:
                successPosCount=0
            if  successPosCount>=5:
                isGameWin=True
                break
        if isGameWin:
            break
    return isGameWin

def showWinMess(screen,pieceId):
    if pieceId==1:
        winPlayer='○'
    else:
        winPlayer='●'
    showMessStr="游戏结束！"+winPlayer+"赢了！"
    winTxtColor=(150,0,100)
    winImg=pygame.font.Font.render(pygame.font.Font(pygame.font.match_font('simsun'), 60),showMessStr,True,winTxtColor)
    screen.blit(winImg,(20,mainHeight/2))
    pygame.display.flip()
    time.sleep(4)        
        
def startGame():
    isGameOver=False
    while not isGameOver:    
        cellsInfo,cellWidth,cellHeight=initCells(screen)
        nowPieceId=0

        while not isGameOver:
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()  
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    i,j=getPos(event.pos[0],event.pos[1],cellWidth,cellHeight)
                    if cellsInfo[i][j][0]<0:            
                        nowPieceId=(nowPieceId+1)%2
                        downPiece(screen,i,j,pieces[nowPieceId],cellWidth,cellHeight,nowPieceId)
                        if isWin(i,j):
                            showWinMess(screen,nowPieceId)
                            isGameOver=True
                            break
            time.sleep(1)       
    



INTERSPACE=20
CELLCOUNT=40
pygame.init()
#sys.path[0]获取当前工作目录
pygame.display.set_caption("五子棋")
logo = pygame.image.load(sys.path[0]+r"\pic\3-1-4\game1.png")
pygame.display.set_icon(logo)
bjpic = pygame.image.load(sys.path[0]+r"\pic\3-1-4\bj.jpg")
bjpicRect = bjpic.get_rect()
minRect=(int(min(bjpicRect.width*0.7,bjpicRect.height*0.7)),int(min(bjpicRect.width*0.7,bjpicRect.height*0.7)))
bjpic=pygame.transform.scale(bjpic,minRect)
size = mainWidth, mainHeight =minRect
screen = pygame.display.set_mode(size)
bjpic=pygame.Surface.convert(bjpic)
piece1 = pygame.image.load(sys.path[0]+r"\pic\3-1-4\game1.png")
piece2=pygame.image.load(sys.path[0]+r"\pic\3-1-4\game2.png")
pieceRect = piece1.get_rect()

piece1=pygame.transform.scale(piece1,(mainHeight/CELLCOUNT,mainWidth/CELLCOUNT))
piece2=pygame.transform.scale(piece2,(mainHeight/CELLCOUNT,mainWidth/CELLCOUNT))
pieceRect = piece1.get_rect()


pieces=[piece1,piece2]
cellsInfo,cellWidth,cellHeight=initCells(screen)
        
menu = pygame_menu.Menu(u'welcome', 400, 300,
                       theme=pygame_menu.themes.THEME_ORANGE)

nameInput=menu.add.text_input(u'名字:', default='张三')
nameInput.set_font(pygame.font.match_font('simsun'), 20,\
                color=pygame.Color('darkorchid'),\
                selected_color=pygame.Color('blue4'),\
                background_color=pygame.Color('goldenrod1'),\
                readonly_color=pygame.Color('green'), readonly_selected_color=pygame.Color('green'))

playBt=menu.add.button('开始游戏', startGame)
playBt.set_font(pygame.font.match_font('simsun'), 20,\
                color=pygame.Color('darkorchid'),\
                selected_color=pygame.Color('blue4'),\
                background_color=pygame.Color('goldenrod1'),\
                readonly_color=pygame.Color('green'), readonly_selected_color=pygame.Color('green'))
exitBt=menu.add.button('退出', pygame_menu.events.EXIT)
exitBt.set_font(pygame.font.match_font('simsun'), 20,\
                color=pygame.Color('darkorchid'),\
                selected_color=pygame.Color('blue4'),\
                background_color=pygame.Color('goldenrod1'),\
                readonly_color=pygame.Color('green'), readonly_selected_color=pygame.Color('green'))

menu.mainloop(screen)

