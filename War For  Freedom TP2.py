from cmu_graphics import *
import random 
def onAppStart(app):
    #board code
    app.width = 500
    app.height = 500
    app.rows = 10
    app.cols = 10
    app.boardLeft = 4
    app.boardTop = 0
    app.boardWidth = 395
    app.boardHeight = 400
    app.cellBorderWidth = 1
    app.board=[([None]*app.cols) for row in range (app.rows)]
    app.Rivercolor = River(0,0)
    app.GrassColor = 'lightGreen'
    #soldier code
    
    app.SoldX = 44
    app.SoldY = 40
    app.HeavX = app.SoldX
    app.HeavY = app.SoldY + 40
    app.LightX = app.HeavX 
    app.LightY = app.HeavY + 40
    app.Soldier = []
    app.selectedSoldier = None
    app.SoldierColor = 'red'
    app.HeavyColor='red'
    app.LightColor='red'
    app.enemyColorHeav = 'blue'
    app.enemyColorLight = 'blue'
    app.enemyColorMed = 'blue'
    app.SoldierRadius = min(app.boardWidth/app.cols, app.boardHeight/app.cols) / 4
    app.enemySoldX = 344
    app.enemySoldY = 40
    app.enemyHeavX = app.enemySoldX
    app.enemyHeavY = app.enemySoldY + 40
    app.enemyLightX = app.enemyHeavX 
    app.enemyLightY = app.enemyHeavY + 40
    
    #health code
    app.SoldHealth = 100
    app.HeavHealth = 200
    app.LightHealth = 50
    app.enemySoldHealth = app.SoldHealth
    app.enemyHeavHealth =  app.HeavHealth
    app.enemyLightHealth = app.LightHealth
    #line code
   
    app.movement = 0
    app.Playerturn = True


def redrawAll(app):
    drawBoard(app)
    drawBoardBorder(app)
    if app.Playerturn==True:
        drawLabel('turns: Ally',450,250)
    elif app.Playerturn==False:
        drawLabel('turns:Enemy',450,250)
    drawLabel(f'{app.SoldHealth}',450,400)
    drawLabel(f'{app.HeavHealth}',450,450)
    drawLabel(f'{app.LightHealth}',450,500)
    for rows in app.board:
        for cols in app.board:
            if app.SoldHealth != 0:
                drawCircle(app.SoldX,app.SoldY,15,fill=app.SoldierColor,border='black')
            if app.HeavHealth !=0:
                drawCircle(app.HeavX,app.HeavY,20,fill=app.HeavyColor,border = 'black')
            if app.LightHealth != 0:
                drawCircle(app.LightX,app.LightY,10,fill = app.LightColor,border = 'black')
            if app.enemySoldHealth!=0:
                drawCircle(app.enemySoldX,app.enemySoldY,15,fill=app.enemyColorMed,border='black')
            if app.enemyHeavHealth !=0:
                drawCircle(app.enemyHeavX,app.enemyHeavY,20,fill=app.enemyColorHeav,border = 'black')
            if app.enemyLightHealth != 0:
                drawCircle(app.enemyLightX,app.enemyLightY,10,fill = app.enemyColorLight,border = 'black')
    if app.enemySoldHealth == 0 and app.enemyHeavHealth ==0 and app.enemyLightHealth == 0:
        drawLabel('You Win',250,250,size = 40, fill = 'Brown' )

#board code
def drawBoard(app):
    for row in range(app.rows):
        for col in range(app.cols):
            drawCell(app, row, col)


def drawBoardBorder(app):
  drawRect(app.boardLeft, app.boardTop, app.boardWidth, app.boardHeight,
           fill=None, border='black',
           borderWidth=2*app.cellBorderWidth)


def drawCell(app, row, col):
    cellLeft, cellTop = getCellLeftTop(app, row, col)
    cellWidth, cellHeight = getCellSize(app)
    if (row in (4,5 ) and col in (4,5))or (row in (5,5) and col in (5,5)):
        color = 'brown'
    elif col in (4,5):
        color = 'blue'
    else:
        color = 'green'
    
    drawRect(cellLeft, cellTop, cellWidth, cellHeight,
             fill=color,border='black', 
             borderWidth=app.cellBorderWidth)
    

def CenterCell(app,row,col):
    centerRow = app.rows//2
    centerCol = app.cols//2
    return row == centerRow and col == centerCol
             

def getCellLeftTop(app, row, col):
    cellWidth, cellHeight = getCellSize(app)
    cellLeft = app.boardLeft + col * cellWidth
    cellTop = app.boardTop + row * cellHeight
    return (cellLeft, cellTop)

def distance(x1,y1,x2,y2):
    return (((x1-x2)**2) - ((y1-y2)**2)**0.5)

def getCellSize(app):
    cellWidth = app.boardWidth / app.cols
    cellHeight = app.boardHeight / app.rows
    return (cellWidth, cellHeight)

class River:
    def __init__(self, row,col):
        self.row = row
        self.col = row
    def riverSpace(self, row,col):
        if self.row == row and self.col == col:
            fill = 'blue'
        else:
            fill = 'green'
    def moveableRiverSpace(self,row,col):
        if isinstance(self,River):
            app.selectedSoldier
        
#soldier code
def moveSoldier(app,dx,dy):
    if app.selectedSoldier == 'Soldier':
        app.SoldX += dx
        app.SoldY += dy
    elif app.selectedSoldier =='enemySoldier':
        app.enemySoldX+=dx
        app.enemySoldY += dy

    elif app.selectedSoldier == 'Light':
        app.LightX += dx
        app.LightY +=dy 
    elif app.selectedSoldier == 'enemyLight':
        app.enemyLightX+=dx
        app.enemyLightY += dy
    elif app.selectedSoldier == 'Heavy':
        app.HeavX += dx 
        app.HeavY += dy
    elif app.selectedSoldier == 'enemyHeavy':
        app.enemyHeavX+=dx
        app.enemyHeavY+=dy
    app.Soldier.append(dx)
    app.Soldier.append(dy)
    app.newX = app.Soldier[0] + dx
    app.newY  = app.Soldier[1] + dy

def onMousePress(app,mouseX,mouseY):
    if (mouseX - app.SoldX)**2 + (mouseY - app.SoldY)**2 <= app.SoldierRadius**2: 
        app.SoldX = mouseX
        app.SoldY = mouseY
        app.selectedSoldier = 'Soldier'
        if app.selectedSoldier == 'Soldier':
            app.Soldiercolor = 'LightBlue'
        else: 
            app.Soldiercolor = 'Blue'
    elif (mouseX - app.HeavX)**2 + (mouseY - app.HeavY)**2 <= (2*app.SoldierRadius)**2:
        app.selectedSoldier = 'Heavy'
        app.HeavX = mouseX
        app.HeavY = mouseY
        if app.selectedSoldier == 'Heavy':
            app.HeavyColor = 'LightBlue'
        else:
            app.HeavyColor= 'Blue'
    elif (mouseX - app.LightX)**2 + (mouseY - app.LightY)**2 <= app.SoldierRadius**2:
        app.selectedSoldier = 'Light'
        app.LightX = mouseX
        app.LightY = mouseY
        if app.selectedSoldier == 'Light':
            app.LightColor = 'LightBlue'
        else:
            app.SoldierColor = 'Blue'
   
    #for i in app.selectedSoldier:
        #if i != None:
            app.enemy
                
def isValidMove(app,x,y):
    return 0 < x < app.cols and 0 < y < app.rows
    

def CanMoveTo(app,x,y):
    if isValidMove(app,app.newX,app.newY) and CanMoveTo(app,app.newX,app.newY):
        app.board[app.Soldier[1]][app.Soldier[0]] = None
        app.board[app.newX][app.newY] = app.Soldier
        app.Soldier = (app.newX,app.newY)
        return app.board[x][y]
    
def onKeyPress(app,key):
    if app.Playerturn ==True:
        if key=='up':
            moveSoldier(app,0,-40)
            app.movement+=1
        if key == 'down':
            moveSoldier(app,0,40)
            app.movement+=1
        if key == 'left':
            moveSoldier(app,-40,0)
            app.movement+=1
        if key == 'right':
            moveSoldier(app,40,0)
            app.movement+=1
        if key == 'enter':
            app.movement=0
            app.Playerturn=False
            app.SoldierColor = 'Red'
            app.HeavyColor = 'Red'
            app.LightColor = 'Red'
    else: 
        enemyTurn(app)

#turns
def allyTurn(app):
    directions =  ([40,0],[0,40],[-40,0],[0,-40])
    
    if app.Playerturn:
        px,py = random.choice(directions)
        moveSoldier(app,px,py)
        if app.selectedSoldier == 'Light' and app.movement >= 5:
            app.Playerturn==False
            app.movement = 0
        elif app.selectedSoldier == 'Soldier' and app.movement >= 3:
            app.Playerturn==False
            app.movement = 0
        elif app.selectedSoldier == 'Heavy' and app.movement >= 1:
            app.Playerturn==False
            app.movement = 0

        #enemy ai
def moveEnemySoldier(app,dx,dy):
    if app.Playerturn == False:
        if app.selectedSoldier=='enemySoldier':
            app.enemySoldX+=dx
            app.enemySoldY+=dy
def moveEnemyHeavy(app,hx,hy):
     if app.Playerturn == False:
        if app.selectedSoldier=='enemyHeavy':
            app.enemyHeavX+=hx
            app.enemyHEavY+=hy
def moveEnemyLight(app,lx,ly):    
     if app.Playerturn == False:
        if app.selectedSoldier=='enemyLight':
            app.enemySoldX+=lx
            app.enemySoldY+=ly
def enemyTurn(app):
    directions = ([40,0],[0,40],[-40,0],[0,-40])
    EnemyClasses = ['enemySoldier','enemyLight','enemyHeavy']
    if app.Playerturn == False:
        randomEnemyClass = random.choice(EnemyClasses)
        dx,dy = random.choice(directions)
        moveEnemy(app,dx,dy)
        if app.selectedSoldier == 'enemyLight' and app.movement >= 5:
            app.Playerturn == True
            app.movement = 0
        elif app.selectedSoldier == 'enemySoldier' and app.movement >= 3:
            app.Playerturn == True
            app.movement = 0
        elif app.selectedSoldier == 'enemyHeavy' and app.movement >= 1:
            app.Playerturn == True
            app.movement == 0
#kill move
def KillMove(app):
    if app.SoldX == app.EnemySoldX and app.SoldY == app.EnemySoldY:
        app.SoldHealth = 75 
        app.EnemySoldHealth = 75
    elif app.SoldX == app.EnemyHeavX and app.SoldY == app.EnemyHeavY:
        app.SoldHealth = 0   
    elif app.SoldX == app.EnemyLightX and app.LightY == app.EnemyLightY:
        app.EnemyLightHealth = 0
    elif app.LightX == app.EnemyHeavX and app.LightY == app.EnemyHeavY:
        app.enemyHeavHealth==0
    elif app.LightX == app.EnemyLightX and app.LightY == app.EnemyLightY:
        app.enemyLightHealth == 25
        app.LightHealth = 25
    elif app.HeavX == app.enemyHeavX and app.LightY == app.EnemyLightY:
        app.EnemyHeavX == 50
        app.EnemyHeavY == 50

def main():
    runApp()

main()