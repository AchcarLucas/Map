import pygame
import numpy as np

class Map:
    '''
        Classe responsável por gerenciar um determinado mapa,
        essa classe pode ser criada várias vezes para vários mapas,
        você deve definir no update principal do jogo qual mapa vai ser desenhado
        utilizando a variável de controle do objeto mapa criado por você
    '''
    def __init__(self,  tile_sheets : pygame.Surface, 
                        dimension_tiles : (int, int),
                        struct_map,
                        offset = (0, 0),
                        map_name = 'None'):
        '''
            Construtor da Classe Map, possui como parâmetro
                tile_sheets             ->  surface (tilesheet) contendo todo o bloco de construção para o mapa
                dimension_tiles         ->  tupla de dois valores inteiros (int, int) correspondente a 
                                            largura e altura da tiles
                struct_map              ->  estrutura array de duas dimensões contendo a estrutura do mapa
                offset                  ->  posição inicial do mapa, por padrão é (0, 0)
                map_name                ->  nome do mapa (opcional)
        '''

        self.dimension_tiles = dimension_tiles
        self.offset = offset

        self.tile_sheets = tile_sheets
        self.struct_map = struct_map

        self.map_name = map_name

        self.map_line = self.struct_map.shape[0]
        self.map_column = self.struct_map.shape[1]

        self.dimension_map = (self.map_column * self.dimension_tiles[0], 
                              self.map_line * self.dimension_tiles[1])

        print(f'Width Map: {self.getMapSize()[0]}')
        print(f'Height Map: {self.getMapSize()[1]}')
        print(f'Tiles Width: {self.dimension_tiles[0]}')
        print(f'Tiles Height: {self.dimension_tiles[1]}')
        print(f'Map Name: {self.map_name}')

    def getStructMap(self):
        '''
            getting da estrutura do mapa
        '''
        return self.struct_map

    def setStructMap(self, struct_map):
        '''
            setting da estrutura do mapa
        '''
        self.struct_map = struct_map
        

    def getOffset(self):
        '''
            getting do offset da posição do mapa
        '''
        return self.offset

    def setOffset(self, offset = (int, int)):
        '''
            setting do offset da posição do mapa
        '''
        self.offset = offset

    def getMapSize(self):
        '''
            getting para informar o tamanho do mapa
        '''
        return (self.map_column * self.dimension_tiles[0], self.map_line * self.dimension_tiles[1])

    def drawMapSurface(self, screen):
        '''
            Função responsável por desenhar o mapa na tela (Respeitando o sistema de offset)
        '''
        screenSize = pygame.display.get_window_size()

        xMaxTiles = np.ceil(screenSize[0] / self.dimension_tiles[0]) + 1
        yMaxTiles = np.ceil(screenSize[1] / self.dimension_tiles[1]) + 1

        # for responsável por desenhar o mapa na tela (desenha apenas a porção que irá aparecer na tela)
        for y in range(0, int(yMaxTiles)):
            # limita o tilesY a valores positivos
            tilesY = np.maximum(0, y + int(self.offset[1] / self.dimension_tiles[1]))

            # verifica se o tilesY é maior que a estrutura, se for sai do for (não tem mais mapa para desenhar)
            if(tilesY >= self.map_line):
                break

            for x in range(0, int(xMaxTiles)):
                # limita o tilesX a valores positivos
                tilesX = np.maximum(0, x - int(self.offset[0] / self.dimension_tiles[0]))

                # verifica se o tilesX é maior que a estrutura, se for sai do for (não tem mais colunas para desenhar)
                if(tilesX >= self.map_column):
                    break

                # pega tiles correspondente ao tilesX e tilesY da posição
                currentTile = self.struct_map[tilesY][tilesX]

                # desenha o tiles na tela usando o sistema de offset
                screen.blit(self.tile_sheets[currentTile], (
                                                    (tilesX * self.dimension_tiles[0] + self.offset[0]), 
                                                    (tilesY * self.dimension_tiles[1] - self.offset[1])
                                                    ))

    def event(self, event):
        '''
            Função responsável por gerenciar os eventos do mapa
            event -> contém a estrutura do evento (veja a documentação do pygame para mais detalhes)
        '''
        pass

    def update(self, deltaTime):
        '''
            Função responsável por atualizar a lógica do mapa
            deltaTime -> váriaveis que guarda o tempo que se passou entre dois frames
        '''
        pass

    def render(self, screen):
        '''
            Função responsável por desenhar o mapa na tela
            screen -> surface principal da tela do jogo
        '''

        self.drawMapSurface(screen)