# Template Matching — Computação Visual

Tutorial teórico e prático da disciplina de **Computação Visual**, da **Universidade Presbiteriana Mackenzie** (Projeto 2 — Opção 2).

O projeto apresenta os fundamentos da técnica de Template Matching e demonstra sua implementação utilizando Python, OpenCV, NumPy, Matplotlib e Jupyter Notebook.

O objetivo é localizar um objeto de referência (*template*) dentro de uma imagem maior, compreender o funcionamento dos métodos de comparação e avaliar suas vantagens e limitações por meio de experimentos práticos.

**Acesse os materiais:**

- [Tutorial teórico e prático](Tutorial_Template_Matching.ipynb)
- [Experimentos e análises — Matheus](Experimentos_Template_Matching_Matheus.ipynb)

---

## 1. Sobre o Template Matching

Template Matching é uma técnica de visão computacional utilizada para localizar uma imagem de referência dentro de uma imagem maior.

O algoritmo percorre a imagem principal utilizando uma janela com as mesmas dimensões do template, calculando uma pontuação de similaridade para cada posição.

O resultado é um mapa de correspondência, no qual é possível identificar a região que apresenta maior semelhança com o objeto procurado.

A seleção da melhor correspondência depende do método utilizado:

- **SQDIFF:** menores pontuações representam melhores correspondências.
- **CCORR e CCOEFF:** maiores pontuações representam melhores correspondências.

O algoritmo identifica padrões visuais, mas não reconhece automaticamente categorias de objetos.

Um limiar de similaridade é utilizado para determinar se a melhor correspondência será considerada uma detecção válida. Essa decisão é heurística e não garante, isoladamente, a presença do objeto.

![Exemplo de resultado](exemplo/resultado.png)

---

## 2. Estrutura do projeto

```text
template_matching/
├── README.md
├── requirements.txt
├── template_matching.py
├── Tutorial_Template_Matching.ipynb
├── Experimentos_Template_Matching_Matheus.ipynb
├── image2.jpg
└── exemplo/
    ├── imagem.png
    ├── template.png
    ├── template_hamster.png
    └── resultado.png
```

### Descrição dos arquivos

| Arquivo | Descrição |
|---|---|
| `Tutorial_Template_Matching.ipynb` | Fundamentação teórica, explicação dos métodos e exemplos executáveis |
| `template_matching.py` | Implementação do algoritmo desenvolvida por João |
| `Experimentos_Template_Matching_Matheus.ipynb` | Experimentos, resultados, análises e conclusão desenvolvidos por Matheus |
| `image2.jpg` | Imagem utilizada nos experimentos |
| `exemplo/template_hamster.png` | Template de referência |
| `requirements.txt` | Bibliotecas necessárias para executar o projeto |
| `README.md` | Documentação e organização do projeto |

---

## 3. Como executar

### 3.1. Preparação do ambiente

É necessário ter Python 3 instalado, com suporte às versões das dependências utilizadas.

Clone o repositório:

```bash
git clone https://github.com/JoaoPioltini/template_matching.git
cd template_matching
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

No Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

No Linux/macOS:

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
python -m pip install jupyterlab ipykernel
```

Abra o Jupyter:

```bash
python -m jupyter lab
```

Selecione `Tutorial_Template_Matching.ipynb` e execute as células na ordem.

Para executar os experimentos, abra `Experimentos_Template_Matching_Matheus.ipynb`.

**Observação:** a primeira célula do notebook experimental foi preparada para o Google Colab. Na execução local, ela deve ser ignorada, pois realiza o clone do repositório e a instalação das dependências.

### 3.2. Execução pelo Google Colab

O projeto também pode ser executado diretamente pelo Google Colab, sem a necessidade de instalar Python no computador.

Acesse:

https://colab.research.google.com/

Abra o notebook desejado e execute suas células.

O notebook de experimentos possui uma célula inicial responsável por clonar o repositório e preparar o ambiente.

### 3.3. Execução pelo terminal

Para executar a implementação principal:

```bash
python template_matching.py exemplo/imagem.png exemplo/template.png
```

Exemplo utilizando a fotografia dos hamsters:

```bash
python template_matching.py image2.jpg exemplo/template_hamster.png
```

Também é possível alterar o método de comparação:

```bash
python template_matching.py exemplo/imagem.png exemplo/template.png --metodo TM_SQDIFF_NORMED --limiar 0.2
```

O programa apresenta a imagem original, o template, o mapa de correspondência e o resultado da localização.

Além disso, informa no terminal a posição encontrada, as dimensões do template, a pontuação de similaridade, a decisão de detecção e o tempo de processamento.

---

## 4. Métodos utilizados

A implementação disponibiliza seis métodos de comparação da biblioteca OpenCV.

| Método | Princípio | Melhor correspondência |
|---|---|---|
| `TM_SQDIFF` | Soma dos quadrados das diferenças | Menor valor |
| `TM_SQDIFF_NORMED` | Diferença quadrática normalizada | Menor valor |
| `TM_CCORR` | Correlação cruzada | Maior valor |
| `TM_CCORR_NORMED` | Correlação cruzada normalizada | Maior valor |
| `TM_CCOEFF` | Correlação com valores centralizados | Maior valor |
| `TM_CCOEFF_NORMED` | Correlação centralizada normalizada | Maior valor |

O método padrão utilizado é `TM_CCOEFF_NORMED`.

Para os experimentos, foi estabelecido um limiar de similaridade de **0,8**.

As pontuações de diferentes métodos não devem ser comparadas diretamente nem interpretadas como probabilidades.

A implementação trabalha com imagens em escala de cinza e utiliza coordenadas `(x, y)` para representar a posição encontrada.

---

# 5. Experimentos e análise — Matheus Veiga Bacetic Joaquim

**Responsável:** Matheus Veiga Bacetic Joaquim  
**RA:** 10425638  
**Contribuição:** Planejamento e execução dos experimentos, interpretação dos resultados, discussão das limitações, aplicações práticas e conclusão.

**Notebook desenvolvido:** [Experimentos_Template_Matching_Matheus.ipynb](Experimentos_Template_Matching_Matheus.ipynb)

Esta etapa teve como objetivo avaliar o comportamento do algoritmo Template Matching em diferentes condições de processamento de imagens.

Para isso, foram desenvolvidos quatro experimentos utilizando Python, OpenCV, NumPy e Matplotlib, com alterações de iluminação, escala, rotação e ruído.

Os testes utilizaram a imagem `image2.jpg` e o template `exemplo/template_hamster.png`.

O método escolhido foi `TM_CCOEFF_NORMED`, com limiar de detecção de 0,8.

Os experimentos foram executados no Google Colab, com geração de imagens comparativas e registro das pontuações obtidas.

## 5.1. Experimento 1 — Variação de iluminação

O primeiro experimento teve como objetivo verificar se alterações de iluminação prejudicariam a identificação do objeto.

Foram criadas três versões da mesma imagem:

- Imagem original, sem alterações.
- Imagem escurecida.
- Imagem com aumento de brilho.

As modificações foram realizadas utilizando a função `cv2.convertScaleAbs()`.

Em seguida, o algoritmo foi executado nas três versões, utilizando o mesmo template de referência.

### Resultados

| Condição | Similaridade | Posição encontrada | Detecção |
|---|---|---|---|
| Original | 1,0000 | (375, 165) | Sim |
| Escura | 0,9999 | (375, 165) | Sim |
| Clara | 0,9991 | (375, 165) | Sim |

### Análise

O algoritmo conseguiu localizar corretamente o objeto nas três condições.

As pontuações permaneceram próximas de 1,0, demonstrando que o método apresentou baixa sensibilidade às alterações globais de iluminação aplicadas.

Esse comportamento está relacionado à normalização utilizada pelo método `TM_CCOEFF_NORMED`, que reduz a influência de determinadas alterações uniformes de intensidade.

Entretanto, os resultados não garantem o mesmo desempenho em situações com sombras intensas, reflexos ou iluminação não uniforme.

## 5.2. Experimento 2 — Variação de escala

O segundo experimento teve como objetivo avaliar o comportamento do algoritmo quando o tamanho do template é alterado.

Foram utilizadas três escalas:

- 70% do tamanho original.
- 100% do tamanho original.
- 130% do tamanho original.

A imagem de busca permaneceu sem alterações.

O redimensionamento foi realizado utilizando `cv2.resize()`.

### Resultados

| Escala | Similaridade | Detecção |
|---|---|---|
| 70% | 0,6558 | Não |
| 100% | 1,0000 | Sim |
| 130% | 0,6024 | Não |

### Análise

O algoritmo apresentou correspondência máxima quando o template manteve suas dimensões originais.

Entretanto, ao reduzir ou aumentar o tamanho do template, a pontuação de similaridade diminuiu significativamente.

Nas escalas de 70% e 130%, os valores ficaram abaixo do limiar estabelecido.

O experimento demonstrou uma limitação importante do Template Matching tradicional: o algoritmo não realiza automaticamente a adaptação de escala durante a busca.

Uma possível alternativa seria utilizar uma abordagem multiescala, executando comparações com diferentes tamanhos do template.

## 5.3. Experimento 3 — Variação de rotação

O terceiro experimento teve como objetivo verificar se o algoritmo conseguiria localizar o objeto quando o template apresentasse diferentes orientações.

Foram utilizados quatro ângulos:

- 0°
- 15°
- 30°
- 45°

A rotação foi realizada utilizando as funções `cv2.getRotationMatrix2D()` e `cv2.warpAffine()`.

A imagem original permaneceu fixa, enquanto o template foi rotacionado.

### Resultados

| Rotação | Similaridade | Detecção |
|---|---|---|
| 0° | 1,0000 | Sim |
| 15° | 0,6820 | Não |
| 30° | 0,5740 | Não |
| 45° | 0,5317 | Não |

### Análise

Observou-se que a pontuação de similaridade diminuiu conforme o ângulo de rotação aumentou.

A correspondência caiu de 1,0000 para 0,5317 entre 0° e 45°, representando uma redução aproximada de 46,8%.

Apenas o template sem rotação apresentou pontuação superior ao limiar estabelecido.

Isso demonstra que o Template Matching tradicional apresenta limitações diante de alterações na orientação do objeto.

O procedimento também manteve as dimensões originais do template, podendo provocar cortes e alterações nas bordas durante a rotação.

Uma possível solução seria realizar comparações com múltiplas versões rotacionadas do template.

## 5.4. Experimento 4 — Influência do ruído

O quarto experimento teve como objetivo avaliar a resistência do algoritmo diante da presença de interferências visuais.

Foi aplicado ruído gaussiano à imagem original utilizando NumPy.

Foram considerados quatro níveis de desvio-padrão:

- 0: sem ruído.
- 15: ruído leve.
- 35: ruído moderado.
- 60: ruído intenso.

O template original permaneceu sem alterações.

### Resultados

| Nível de ruído | Similaridade | Posição encontrada | Detecção |
|---|---|---|---|
| 0 | 1,0000 | (375, 165) | Sim |
| 15 | 0,9781 | (375, 165) | Sim |
| 35 | 0,8986 | (375, 165) | Sim |
| 60 | 0,7647 | (375, 165) | Não |

### Análise

Os resultados demonstraram uma redução gradual na pontuação de similaridade conforme a intensidade do ruído aumentou.

Nos níveis 0, 15 e 35, o algoritmo apresentou pontuações superiores ao limiar de detecção.

No nível 60, embora a melhor posição encontrada permanecesse correta, a pontuação caiu para 0,7647, ficando abaixo do limiar.

Esse resultado evidencia uma diferença importante entre encontrar a melhor posição e confirmar uma detecção.

O algoritmo apresentou resistência ao ruído leve e moderado, mas o ruído intenso prejudicou a pontuação de similaridade.

## 5.5. Comparação geral dos experimentos

A tabela apresenta uma síntese dos resultados obtidos.

| Experimento | Condição avaliada | Principal resultado |
|---|---|---|
| Iluminação | Alterações globais de brilho | Similaridade permaneceu próxima de 1,0 |
| Escala | Redução e ampliação de 30% | Similaridade caiu abaixo de 0,8 |
| Rotação | Ângulos de até 45° | Redução progressiva da similaridade |
| Ruído | Ruído gaussiano de até 60 | Redução gradual da pontuação |

### Discussão geral

Os experimentos permitiram identificar vantagens e limitações do Template Matching.

O método apresentou bons resultados quando as características visuais do objeto permaneceram relativamente constantes.

As alterações globais de iluminação produziram pequenas variações nas pontuações, enquanto o ruído leve e moderado não impediu a detecção.

Por outro lado, alterações de escala e rotação provocaram reduções significativas na similaridade.

Entre as principais vantagens da técnica estão:

- Simplicidade de implementação.
- Facilidade de interpretação dos resultados.
- Integração com a biblioteca OpenCV.
- Aplicabilidade em ambientes com condições visuais controladas.
- Possibilidade de utilizar diferentes métodos de comparação.

As principais limitações observadas ou conhecidas incluem:

- Sensibilidade às alterações de escala.
- Sensibilidade às rotações.
- Possíveis dificuldades diante de mudanças de perspectiva.
- Influência de oclusões e interferências visuais.
- Dependência da escolha do limiar de detecção.

Os resultados também demonstraram que a melhor posição calculada pelo algoritmo não representa necessariamente uma detecção aceita pelo limiar.

Os experimentos foram realizados com uma imagem de referência específica. Portanto, os resultados descrevem o comportamento observado nesse cenário e não devem ser generalizados para todas as imagens.

## 5.6. Aplicações práticas

O Template Matching pode ser utilizado em diferentes aplicações de visão computacional, especialmente quando os objetos apresentam aparência, dimensões e orientação conhecidas.

### Automação industrial

Pode auxiliar na localização de peças, componentes e padrões visuais durante processos de produção e inspeção.

### Inspeção visual

Pode ser utilizado para comparar regiões de imagens e identificar padrões conhecidos em ambientes controlados.

### Automação de interfaces

Pode auxiliar na localização de botões, ícones e outros elementos gráficos em capturas de tela.

### Dispositivos móveis

Pode ser utilizado em aplicações que analisam imagens capturadas pela câmera de smartphones, desde que as condições visuais sejam adequadas.

Nesses ambientes, alterações de iluminação, distância e orientação podem exigir estratégias adicionais de processamento.

## 5.7. Conclusão dos experimentos

Os experimentos demonstraram que o Template Matching é uma técnica simples e eficiente para localizar padrões visuais quando as características do objeto permanecem relativamente constantes.

A implementação com Python e OpenCV permitiu avaliar o comportamento do algoritmo diante de diferentes condições de iluminação, escala, rotação e ruído.

Os resultados indicaram maior resistência às alterações globais de iluminação e ao ruído moderado.

Em contrapartida, as mudanças de escala e rotação provocaram reduções significativas nas pontuações de similaridade.

Conclui-se que o Template Matching é adequado para aplicações com condições visuais controladas. Em cenários com grandes variações na aparência dos objetos, podem ser necessárias abordagens mais robustas, como correspondência multiescala, detecção de características locais ou métodos baseados em aprendizado de máquina.

**Toda a implementação dos experimentos, as imagens comparativas e os resultados estão disponíveis no notebook desenvolvido por Matheus:**

[Experimentos_Template_Matching_Matheus.ipynb](Experimentos_Template_Matching_Matheus.ipynb)

---

## 6. Organização e contribuições do grupo

O projeto foi dividido em três etapas, desenvolvidas pelos integrantes.

### Alexandre Eiji Tomimura Carvalho — Fundamentação teórica

Responsável pela apresentação dos conceitos fundamentais de Template Matching, incluindo:

- Definição e funcionamento da técnica.
- Explicação do deslocamento da janela de comparação.
- Representação matemática dos métodos.
- Explicação dos mapas de correspondência.
- Interpretação das pontuações e seleção da melhor correspondência.
- Exemplos visuais para compreensão do algoritmo.

### João Pedro Pioltini de Oliveira — Implementação prática

Responsável pelo desenvolvimento do código principal, incluindo:

- Carregamento das imagens.
- Conversão para escala de cinza.
- Implementação de `cv2.matchTemplate()`.
- Seleção da melhor correspondência com `cv2.minMaxLoc()`.
- Destaque visual do objeto encontrado.
- Exibição das imagens e dos resultados.
- Informações de posição, dimensões, pontuação e tempo de processamento.

### Matheus Veiga Bacetic Joaquim — Experimentos e análise

Responsável pela avaliação experimental do algoritmo, incluindo:

- Preparação do ambiente de experimentação no Google Colab.
- Seleção da imagem e do template utilizados nos testes.
- Implementação dos experimentos de iluminação, escala, rotação e ruído.
- Geração das imagens comparativas.
- Coleta e organização das pontuações de similaridade.
- Análise dos acertos e das falhas.
- Avaliação das vantagens e limitações da técnica.
- Discussão de aplicações práticas em visão computacional.
- Elaboração da conclusão da etapa experimental.

Os experimentos foram organizados em um notebook independente, permitindo sua reprodução e posterior integração ao tutorial desenvolvido pelo grupo.

---

## 7. Integrantes

| Integrante | RA | Responsabilidade |
|---|---|---|
| Alexandre Eiji Tomimura Carvalho | 10371680 | Fundamentação teórica |
| João Pedro Pioltini de Oliveira | 10425643 | Implementação prática |
| Matheus Veiga Bacetic Joaquim | 10425638 | Experimentos, análise e conclusão |

---

## 8. Referências bibliográficas

- **OpenCV.** Template Matching — teoria e métodos. Disponível em: https://docs.opencv.org/4.x/de/da9/tutorial_template_matching.html

- **OpenCV.** TemplateMatchModes e documentação de `matchTemplate()`. Disponível em: https://docs.opencv.org/4.x/df/dfb/group__imgproc__object.html

- **OpenCV.** Template Matching — Tutorial Python. Disponível em: https://docs.opencv.org/4.x/d4/dc6/tutorial_py_template_matching.html

Acesso em: 25 de outubro de 2026.

---

## 9. Observações finais

O projeto foi desenvolvido com finalidade acadêmica, como parte da disciplina de Computação Visual da Universidade Presbiteriana Mackenzie.

A implementação e os experimentos permitem compreender tanto o funcionamento do Template Matching quanto suas limitações em diferentes condições de processamento de imagens.

O material está organizado para permitir que outros estudantes reproduzam os exemplos, comparem os resultados e explorem diferentes métodos de correspondência.

**Pendência:** confirmar a procedência e as condições de licença das imagens utilizadas, caso sejam redistribuídas.
