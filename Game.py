import pygame
import os
import Map as map

class Game():
    '''
        Classe responsável por gerenciar o jogo
    '''
    def __init__(self, screenSize : (int, int), fps=60, title='Game', icon=None):
        '''
            Construtor da Classe Game, possui como parâmetro
                screenSize  ->  tupla contendo de dois valores inteiros (int, int) 
                                que corresponde a largura e altura, ex (800, 600)
                fps         ->  contendo da taxa de atualização da tela
                title       ->  contendo o titulo do jogo
                icon        ->  contendo uma surface (imagem) com o icone a ser exibido na tela
        '''
        # inicializa as variáveis da classe
        self.gameRunning = True
        self.screenSize = screenSize

        self.title = title
        self.icon = icon
        self.fps = fps

        # inicializa o game
        self.initGame()

        # lista contendo todas as sheets
        self.sheets = []

        # carrega as sheets
        self.sheets.append(pygame.image.load(os.path.join('assets', 'hyptosis_tile-art-batch-1.png')).convert())
        self.sheets.append(pygame.image.load(os.path.join('assets', 'hyptosis_til-art-batch-2.png')).convert())

        tempMap = [[1, 1, 1, 2, 2, 2],
                   [1, 1, 1, 2, 2, 2]]

        # lista contendo todos os mapas
        self.maps = []

        # carrega os mapas
        self.maps.append(map.Map(self.sheets[0], (32, 32), tempMap))
        
    def initGame(self):
        '''
            Função responsável por inicializar e configurar a tela do jogo,
            essa função não possui parâmetros
        '''
        self.screen = pygame.display.set_mode(self.screenSize)
        pygame.display.set_caption(self.title)

        if(self.icon != None):
            pygame.display.set_icon(self.icon)

        self.gameClock = pygame.time.Clock()

    # função principal do jogo
    def gameMain(self):
        '''
            Loop principal do jogo, essa função não possui parâmetros
        '''
        while self.gameRunning:
            deltaTime = self.gameClock.tick(self.fps)

            for event in pygame.event.get():
                self.gameEvent(event)

            self.gameUpdate(deltaTime)
            self.gameRender(deltaTime)
        
    # função de eventos
    def gameEvent(self, event):
        '''
            Função responsável por gerenciar os eventos do display
            event -> contém a estrutura do evento (veja a documentação do pygame para mais detalhes)
        '''
        if(event.type == pygame.QUIT):
            self.gameRunning = False
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_ESCAPE):
                self.gameRunning = False

    # função de atualização
    def gameUpdate(self, deltaTime):
        '''
            Função responsável por atualizar a lógica do jogo
            deltaTime -> váriaveis que guarda o tempo que se passou entre dois frames
        '''
        pass

    # função de renderização
    def gameRender(self, deltaTime):
        '''
            Função responsável por desenhar na tela do jogo
            deltaTime -> váriaveis que guarda o tempo que se passou entre dois frames
        '''
        pass

game = Game((800, 600), title='Game - Map')
game.gameMain()