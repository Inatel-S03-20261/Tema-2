from typing import List
from .dto import TrocasRequestDTO
from .interfaces import InterfaceCartasService, InterfaceDistribuicaoService

class CartasController:
    def __init__(self, service: InterfaceCartasService):
        self.service = service

    def consultarCartas(self, idJogador: int) -> List[int]:
        return self.service.consultarCartas(idJogador)

    def requisicaoTroca(self, dadosTroca: TrocasRequestDTO) -> bool:
        return self.service.requisicaoTroca(dadosTroca)


class DistribuicaoController:
    def __init__(self, service: InterfaceDistribuicaoService):
        self.service = service

    def getJogadorID(self) -> int:
        return 0

    def getPokemonAleatorio(self) -> List[int]:
        return []

    def distribuirCartas(self, idJogador: int, idsPokemon: List[int]) -> None:
        self.service.distribuirCartas(idJogador, idsPokemon)