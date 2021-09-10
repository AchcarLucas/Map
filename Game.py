import pygame
import Map

class Game():
    def __init__(self, screenSize, fps=60, title='Game', icon=None):
        # inicializa as variáveis da classe
        self.gameRunning = True
        self.screenSize = screenSize
        self.title = title
        self.icon = icon
        self.fps = fps

        # inicializa o game
        self.initGame()
        
    def initGame(self):
        self.screen = pygame.display.set_mode(self.screenSize)
        pygame.display.set_caption(self.title)
        if(self.icon != None):
            pygame.display.set_icon(self.icon)

        self.gameClock = pygame.time.Clock()

    # função principal do jogo
    def gameMain(self):
        while self.gameRunning:
            deltaTime = self.gameClock.tick(self.fps)

            for event in pygame.event.get():
                self.gameEvent(event)

            self.gameUpdate(deltaTime)
            self.gameRender(deltaTime)
        
    # função de eventos
    def gameEvent(self, event):
        if(event.type == pygame.QUIT):
            self.gameRunning = False
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_ESCAPE):
                self.gameRunning = False

    # função de atualização
    def gameUpdate(self, deltaTime):
        pass

    # função de renderização
    def gameRender(self, deltaTime):
        pass

game = Game((800, 600), title='Game - Map')
game.gameMain()