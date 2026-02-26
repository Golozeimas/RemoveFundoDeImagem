from rembg import remove

# fornece ao interpretador recursos de edição de imagens
from PIL import Image

entrada = input("Digite o nome do arquivo com seu formato (ex: foto.png): ")
img_entrada = f"entrada_de_imagens/{entrada}"

saida = input("Digite o nome da foto que deseja junto com o tipo (ex: foto_saida.png): ")
img_saida = f"{saida}"

INPUT = Image.open(img_entrada)

OUTPUT = remove(INPUT)

# salva isso na imagem de saida
OUTPUT.save(f"saida_de_imagens/{saida}")