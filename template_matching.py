"""Localiza um template em uma imagem usando OpenCV."""

import argparse
from time import perf_counter

import cv2
import matplotlib.pyplot as plt
import numpy as np


METODOS = {
    nome: getattr(cv2, nome)
    for nome in (
        "TM_SQDIFF", "TM_SQDIFF_NORMED", "TM_CCORR",
        "TM_CCORR_NORMED", "TM_CCOEFF", "TM_CCOEFF_NORMED",
    )
}


def carregar_imagem(caminho):
    """Carrega uma imagem em BGR; informa quando o arquivo não é legível."""
    imagem = cv2.imread(str(caminho), cv2.IMREAD_COLOR)
    if imagem is None:
        raise ValueError(f"Não foi possível carregar a imagem: {caminho}")
    return imagem


def converter_cinza(imagem):
    """Converte uma imagem BGR para cinza, preservando entradas já em cinza."""
    if imagem.ndim == 2:
        return imagem.copy()
    return cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)


def executar_template_matching(imagem, template, metodo):
    """Retorna o mapa de correspondência em escala de cinza."""
    if metodo not in METODOS.values():
        raise ValueError("Método de template matching inválido.")
    imagem = converter_cinza(imagem)
    template = converter_cinza(template)
    if template.shape[0] > imagem.shape[0] or template.shape[1] > imagem.shape[1]:
        raise ValueError("O template não pode ser maior que a imagem.")
    if metodo == cv2.TM_CCOEFF_NORMED and np.var(template) == 0:
        raise ValueError("TM_CCOEFF_NORMED exige um template com variação de pixels.")
    return cv2.matchTemplate(
        imagem.astype(np.float32), template.astype(np.float32), metodo
    )


def encontrar_melhor_correspondencia(resultado, metodo):
    """Retorna (x, y) do mínimo para SQDIFF ou do máximo nos demais métodos."""
    if metodo not in METODOS.values():
        raise ValueError("Método de template matching inválido.")
    _, _, posicao_minima, posicao_maxima = cv2.minMaxLoc(resultado)
    if metodo in (cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED):
        return posicao_minima
    return posicao_maxima


def destacar_objeto(imagem, posicao, dimensoes):
    """Desenha em uma cópia; dimensoes deve ser (largura, altura)."""
    resultado = imagem.copy()
    x, y = posicao
    largura, altura = dimensoes
    cor = 255 if resultado.ndim == 2 else (0, 255, 0)
    cv2.rectangle(resultado, (x, y), (x + largura - 1, y + altura - 1), cor, 2)
    return resultado


def visualizar_resultados(imagem, template, mapa, resultado):
    """Exibe original, template, mapa de pontuações e imagem destacada."""
    figura, eixos = plt.subplots(2, 2, figsize=(12, 8))
    for eixo, dados, titulo in zip(
        eixos.flat,
        (imagem, template, mapa, resultado),
        ("Imagem original", "Template", "Mapa de correspondência", "Melhor correspondência"),
    ):
        if dados.ndim == 2:
            exibicao = eixo.imshow(dados, cmap="viridis" if dados is mapa else "gray")
        else:
            exibicao = eixo.imshow(cv2.cvtColor(dados, cv2.COLOR_BGR2RGB))
        if dados is mapa:
            figura.colorbar(exibicao, ax=eixo, label="Pontuação")
        eixo.set_title(titulo)
        eixo.axis("off")
    figura.tight_layout()
    plt.show()
    return figura


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("imagem", help="Caminho da imagem de busca")
    parser.add_argument("template", help="Caminho do recorte a localizar")
    parser.add_argument("--metodo", choices=METODOS, default="TM_CCOEFF_NORMED")
    parser.add_argument(
        "--limiar", type=float,
        help="Pontuação mínima (máxima para SQDIFF). Padrão: 0.8 ou 0.2 para SQDIFF_NORMED",
    )
    args = parser.parse_args()
    limiar = args.limiar
    if limiar is None:
        if not args.metodo.endswith("_NORMED"):
            parser.error("Métodos não normalizados exigem --limiar na escala do método.")
        limiar = 0.2 if args.metodo == "TM_SQDIFF_NORMED" else 0.8
    if not np.isfinite(limiar):
        parser.error("--limiar deve ser um número finito.")
    imagem = carregar_imagem(args.imagem)
    template = carregar_imagem(args.template)
    metodo = METODOS[args.metodo]
    inicio = perf_counter()
    mapa = executar_template_matching(imagem, template, metodo)
    posicao = encontrar_melhor_correspondencia(mapa, metodo)
    pontuacao = float(mapa[posicao[1], posicao[0]])
    menor_melhor = metodo in (cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED)
    encontrado = pontuacao <= limiar if menor_melhor else pontuacao >= limiar
    tempo_ms = (perf_counter() - inicio) * 1000
    altura, largura = template.shape[:2]
    resultado = destacar_objeto(imagem, posicao, (largura, altura)) if encontrado else imagem.copy()
    print("\n========================================")
    print("       RESULTADO DA DETECÇÃO")
    print("========================================\n")
    print(f"Método: {args.metodo}\n")
    print(f"Objeto encontrado: {'Sim' if encontrado else 'Não'}")
    print(f"Posição inicial: {posicao if encontrado else '—'}")
    print(f"Dimensões do template: {largura} x {altura}\n")
    print(f"Pontuação: {pontuacao:.4f}")
    print(f"Tempo de processamento: {tempo_ms:.1f} ms")
    print("\n========================================")
    visualizar_resultados(imagem, template, mapa, resultado)


if __name__ == "__main__":
    main()
