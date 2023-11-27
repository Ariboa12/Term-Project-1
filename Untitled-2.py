from cmu_graphics import *

def onAppStart(app):
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
    app.SoldX = 44
    app.SoldY = 40
    app.HeavX = app.SoldX
    app.HeavY = app.SoldY + 40
    app.LightX = app.HeavX 
    app.LightY = app.HeavY + 40
    app.Soldier = []
    app.selectedSoldier = None
    app.SoldierColor = 'red'
    app.enemyColor = 'blue'
    app.SoldierRadius = min(app.boardWidth/app.cols, app.boardHeight/app.cols) / 4
    app.EnemySoldX = -44
    app.EnemySoldY = 40
    app.EnemyHeavX = app.EnemySoldX
    app.EnemyHeavY = app.EnemySoldY + 40
    app.EnemyLightX = app.EnemyHeavX 
    app.EnemyLightY = app.EnemyHeavY + 40
def redrawAll(app):
    drawBoard(app)
    drawBoardBorder(app)
    for rows in app.board:
        for cols in app.board:
            drawCircle(app.SoldX,app.SoldY,15,fill=app.SoldierColor,border='black')
            drawCircle(app.HeavX,app.HeavY,20,fill=app.SoldierColor,border = 'black')
            drawCircle(app.LightX,app.LightY,10,fill = app.SoldierColor,border = 'black')
            drawCircle(app.EnemySoldX,app.EnemySoldY,15,fill=app.enemyColor,border='black')
            drawCircle(app.EnemyHeavX,app.EnemyHeavY,20,fill=app.enemyColor,border = 'black')
            drawCircle(app.EnemyLightX,app.EnemyLightY,10,fill = app.enemyColor,border = 'black')
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

def moveSoldier(app,dx,dy):

    if app.selectedSoldier == 'Soldier':
        app.SoldX += dx
        app.SoldY += dy

    elif app.selectedSoldier == 'Light':
        app.LightX += dx
        app.LightY +=dy 

    elif app.selectedSoldier == 'Heavy':
        app.HeavX += dx 
        app.HeavY += dy
    else:
        print('no soldier')
    app.Soldier.append(dx)
    app.Soldier.append(dy)
    app.newX = app.Soldier[0] + dx
    app.newY  = app.Soldier[1] + dy
def onMousePress(app,mouseX,mouseY):
        if (mouseX - app.SoldX)**2 + (mouseY - app.SoldY)**2 <= app.SoldierRadius**2:
            app.SoldX = mouseX
            app.SoldY = mouseY
            app.selectedSoldier = 'Soldier'
            app.Soldiercolor = 'LightBlue'
        elif (mouseX - app.HeavX)**2 + (mouseY - app.HeavY)**2 <= (2*app.SoldierRadius)**2:
            app.HeavX = mouseX
            app.HeavY = mouseY
            app.selectedSoldier = 'Heavy'
            app.Soldiercolor = 'LightBlue'
            app.LightX = mouseX
            app.LightY = mouseY
        elif (mouseX - app.LightX)**2 + (mouseY - app.LightY)**2 <= app.SoldierRadius**2:
            app.selectedSoldier = 'Light'
            app.Soldiercolor = 'LightBlue'



def isValidMove(app,x,y):
    return 0 <= x < app.cols and 0 <=y < app.rows
    

def CanMoveTo(app,x,y):
    if isValidMove(app,app.newX,app.newY) and CanMoveTo(app,app.newX,app.newY):
        app.board[app.Soldier[1]][app.Soldier[0]] = None
        app.board[app.newX][app.newY] = app.Soldier
        app.Soldier = (app.newX,app.newY)
        return app.board[x][y]
def onKeyPress(app,key):
    
    if key=='up':
        moveSoldier(app,0,-40)
    if key == 'down':
        moveSoldier(app,0,40)
    if key == 'left':
        moveSoldier(app,-40,0)
    if key == 'right':
        print('pressed right')
        moveSoldier(app,40,0)
        
class River:
    def __init__(self, row,col):
        self.row = row
        self.col = row
    def riverSpace(self, row,col):
        if self.row == row and self.col == col:
            fill = 'blue'
        else:
            fill = 'green'
#enemy ai

def main():
    runApp()

main()