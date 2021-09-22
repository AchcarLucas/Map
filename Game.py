import pygame
import numpy as np
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
        self.tilesheets = []

        # carrega as sheets
        self.tilesheets.append(self.loadSpriteSheetPacket('./assets', 'hyptosis_tile-art-batch-1.png', (32, 32)))
        self.tilesheets.append(self.loadSpriteSheetPacket('./assets', 'hyptosis_til-art-batch-2.png', (32, 32)))

        ############### Temporário #################
        temp_struct_map = np.arange(22 * 6 * 4).reshape(22, 6 * 4)

        temp_struct_map[0, ] = [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]
        temp_struct_map[1, ] = [6, 7, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]
        temp_struct_map[2, ] = [12, 13, 14, 15, 16, 17, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]
        temp_struct_map[3, ] = [18, 19, 20, 21, 22, 23, 18, 19, 20, 21, 22, 23, 18, 19, 20, 21, 22, 23, 18, 19, 20, 21, 22, 23]
        temp_struct_map[4, ] = [24, 25, 26, 27, 28, 29, 24, 25, 26, 27, 28, 29, 24, 25, 26, 27, 28, 29, 24, 25, 26, 27, 28, 29]
        temp_struct_map[5, ] = [30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35]
        temp_struct_map[6, ] = [30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35]
        temp_struct_map[7, ] = [30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35]
        temp_struct_map[8, ] = [30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35]
        temp_struct_map[9, ] = [30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35]
        temp_struct_map[10, ] = [30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35]
        temp_struct_map[11, ] = [30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35]
        temp_struct_map[12, ] = [30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35]
        temp_struct_map[13, ] = [30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35]
        temp_struct_map[14, ] = [30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35]
        temp_struct_map[15, ] = [30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35]
        temp_struct_map[16, ] = [30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35]
        temp_struct_map[17, ] = [30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35]
        temp_struct_map[18, ] = [30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35]
        temp_struct_map[19, ] = [30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35]
        temp_struct_map[20, ] = [30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35]
        temp_struct_map[21, ] = [30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35, 30, 31, 32, 33, 34, 35]

        self.moveMapX = 0
        self.moveMapY = 0

        ################################

        # lista contendo todos os mapas
        self.maps = []

        # carrega os mapas
        self.maps.append(map.Map(self.tilesheets[1], (32, 32), temp_struct_map, offset = (self.moveMapX, self.moveMapY), map_name='Mapa 1'))
        
    def loadSpriteSheetPacket(self, imagePath, spriteSheetName, dimensionSheet:(int, int), scaleSprite = (1, 1)):
        '''
            Função loadSpriteSheetPacket, cria uma lista de sprites a partir de uma spritesheet
                imagePath       ->  local onde deve ser lido as imagens
                spriteSheetName ->  nome do arquivo a ser carregado
                dimensionSheet  ->  dimensão da sprite (largura e altura)
                scaleSprite     ->  escala das imagens no eixo x e no eixo y
                Ex: loadSpriteSheetPacket('./assets', 'sheet.png', (64, 64), (1, 1))
        '''
        tempSprites = []

        tempSpriteSheet = pygame.image.load(os.path.join(imagePath, spriteSheetName)).convert_alpha()

        for y in range(0, int((tempSpriteSheet.get_height() / dimensionSheet[1]))):
            for x in range(0, int((tempSpriteSheet.get_width() / dimensionSheet[0]))):
                tempImage = pygame.Surface(dimensionSheet)
                tempImage = tempSpriteSheet.subsurface((np.floor(x * dimensionSheet[0]), np.floor(y * dimensionSheet[1]), dimensionSheet[0], dimensionSheet[1]))
                
                tempSprites.append(tempImage)

                print(f'SpriteSheet - [{spriteSheetName}] - Clip SubSurface [{x * dimensionSheet[0], y * dimensionSheet[1], dimensionSheet[0], dimensionSheet[1]}]')

        return tempSprites

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
            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                self.gameEvent(event)

            self.gameUpdate(deltaTime)
            self.gameRender()

            pygame.display.update()

        pygame.quit()
        
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

        keys = pygame.key.get_pressed()

        if(keys[pygame.K_d]):
            self.moveMapX += 1

        if(keys[pygame.K_a]):
            self.moveMapX -= 1

        if(keys[pygame.K_w]):
            self.moveMapY -= 1

        if(keys[pygame.K_s]):
            self.moveMapY += 1


        self.maps[0].setOffset((self.moveMapX, self.moveMapY))

        self.maps[0].update(deltaTime)

    # função de renderização
    def gameRender(self):
        '''
            Função responsável por desenhar na tela do jogo
            deltaTime -> váriaveis que guarda o tempo que se passou entre dois frames
        '''
        self.maps[0].render(self.screen)

game = Game((800, 600), title='Game - Map')
game.gameMain()