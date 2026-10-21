# Template Matching — Computação Visual

Trabalho em grupo da disciplina de Computação Visual, desenvolvido em Python com OpenCV, NumPy e Matplotlib. O programa localiza um recorte de referência (template) dentro de uma imagem por comparação visual.

## Integrante e contribuição

**João Pedro Pioltini de Oliveira — RA: 10425643**

Nesta etapa, implementei o carregamento das imagens, a conversão para escala de cinza, a execução do template matching e a seleção da melhor correspondência. Também desenvolvi o destaque do objeto, a visualização dos resultados e a saída no terminal com posição, dimensões, pontuação e tempo de processamento.

Os demais integrantes complementarão o projeto e registrarão suas contribuições posteriormente.

## Como executar

Crie um ambiente virtual e instale as dependências:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Execute com a imagem completa primeiro e o template depois:

```bash
python template_matching.py exemplo/imagem.png exemplo/template.png
```

Exemplo com uma fotografia:

```bash
python template_matching.py image2.jpg exemplo/template_hamster.png
```

O programa exibe a imagem original, o template, o mapa de correspondência e o resultado. O terminal informa se a pontuação atende ao limiar de detecção.

Para alterar o método ou o limiar:

```bash
python template_matching.py exemplo/imagem.png exemplo/template.png --metodo TM_SQDIFF_NORMED --limiar 0.2
```

## Funcionamento e limitações

O template é um recorte do objeto que se deseja localizar, e não pode ser maior que a imagem de busca. O algoritmo procura semelhança visual; não reconhece categorias de objetos automaticamente e não exige fundo branco. Nesta implementação, mudanças de escala, rotação, perspectiva ou oclusão podem prejudicar a correspondência.

As posições usam `(x, y)` e as dimensões usam `(largura, altura)`. Para os métodos `TM_SQDIFF`, menor pontuação significa melhor correspondência; nos demais, maior é melhor. O limiar padrão é 0.8 para correlação normalizada e 0.2 para `TM_SQDIFF_NORMED`. Métodos não normalizados exigem `--limiar` explícito na escala do método. A decisão pelo limiar é uma heurística, não uma garantia de presença do objeto.

O tempo informado inclui a conversão para cinza, o matching e a seleção da correspondência, sem incluir leitura de arquivos ou visualização.
