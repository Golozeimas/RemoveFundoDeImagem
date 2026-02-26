# 🖼️ Removedor de Background

Script Python simples para remover o fundo de imagens automaticamente, utilizando as bibliotecas `rembg` e `Pillow`.

---

## 📋 Pré-requisitos

Certifique-se de ter o Python instalado e as seguintes bibliotecas:

```bash
pip install rembg Pillow
```

---

## 📁 Estrutura de Pastas

Antes de executar o script, crie as seguintes pastas no mesmo diretório:

```
projeto/
├── background.py
├── entrada_de_imagens/   ← coloque aqui as imagens de entrada
└── saida_de_imagens/     ← as imagens processadas serão salvas aqui
```

---

## 🚀 Como Usar

1. Coloque a imagem desejada na pasta `entrada_de_imagens/`
2. Execute o script:

```bash
python background.py
```

3. Informe o nome do arquivo de entrada quando solicitado:

```
Digite o nome do arquivo com seu formato (ex: foto.png): foto.png
```

4. Informe o nome do arquivo de saída:

```
Digite o nome da foto que deseja junto com o tipo (ex: foto_saida.png): foto_saida.png
```

5. A imagem com o fundo removido será salva em `saida_de_imagens/`.

---

## ⚠️ Observações

- O arquivo de saída deve ser salvo no formato `.png` para suportar transparência.
- Formatos suportados de entrada: `.png`, `.jpg`, `.jpeg`, `.webp`, entre outros.
- O processamento pode demorar alguns segundos dependendo do tamanho da imagem e do hardware disponível.

---

## 🛠️ Tecnologias Utilizadas

- [rembg](https://github.com/danielgatis/rembg) — remoção automática de fundo com IA
- [Pillow](https://python-pillow.org/) — manipulação de imagens em Python
