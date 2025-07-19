import requests
from pydantic import BaseModel

class PokemonSchema(BaseModel): # Contrato de dados ou schema de dados ou view da minha API.
    name: str
    type: str

    class Config:
        orm_mode = True

def pegar_pokemon(id: int) -> PokemonSchema:
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")  # select
    data = response.json()
    data_types = data['types'] # Supondo que 'data' e o dicionario com os dados
    types_list = []
    for type_info in data_types:
        types_list.append(type_info['type']['name'])
    types = ', '.join(types_list)
    return PokemonSchema(name=data['name'], type=types)

if __name__ == "__main__":
    print(pegar_pokemon(10))
    print(pegar_pokemon(6))
    print(pegar_pokemon(13))


# geralmente para APIs publicas nao podem fazer essas abaixo:
# requests.post() # create

# requests.put() # update

# requests.delete() # delete
