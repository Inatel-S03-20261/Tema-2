from typing import List
from .dto import TrocasRequestDTO
from .interfaces import (
    InterfaceCartasService, 
    InterfaceDistribuicaoService,
    InterfaceCartasRepository
)
from .clients import PokeApiClient

class CartasService(InterfaceCartasService):
    def __init__(self, repository: InterfaceCartasRepository):
        self.repository = repository

    def consultarCartas(self, idJogador: int) -> List[int]:
        return self.repository.consultarCartas(idJogador)

    def requisicaoTroca(self, dadosTroca: TrocasRequestDTO) -> bool:
        return True

class DistribuicaoService(InterfaceDistribuicaoService):
    def __init__(self, repository: InterfaceCartasRepository, pokeapi_client: PokeApiClient):
        self.repository = repository
        self.pokeapi_client = pokeapi_client

    def distribuirCartas(self, idJogador: int, idsPokemon: List[int]) -> None:
        pass

    def gerar_cartas_aleatorias(self, quantidade: int = 5) -> List[int]:
        pass