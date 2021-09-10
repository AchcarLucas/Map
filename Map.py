import pygame

class Map:
    '''
        Classe responsável por gerenciar um determinado mapa,
        essa classe pode ser criada várias vezes para vários mapas,
        você deve definir no update principal do jogo qual mapa vai ser desenhado
        utilizando a variável de controle do objeto mapa criado por você
    '''
    def __init__(self,  sheet : pygame.Surface, 
                        tilesDimension : (int, int),
                        struct_map : []):
        '''
            Construtor da Classe Map, possui como parâmetro
                sheet           ->  surface (sheet) contendo todo o bloco de construção para o mapa
                tilesDimension  ->  tupla de dois valores inteiros (int, int) correspondente a 
                                    largura e altura da tiles
                struct_map      ->  estrutura array de duas dimensões contendo a estrutura do mapa
        '''
        self.sheet = sheet
        self.tilesDimension = tilesDimension
        self.struct_map = struct_map

    def event(self, event):
        pass

    def update(self, deltaTime):
        pass

    def render(self, deltaTime):
        pass