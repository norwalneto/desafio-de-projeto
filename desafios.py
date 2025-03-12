import pytesseract
from PIL import Image
import cv2
import os
from transformers import pipeline

def configurar_tesseract():
    print("Configurando o Tesseract...")
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def carregar_imagem(imagem_path):
    print(f"Carregando a imagem de: {imagem_path}")
    if not os.path.exists(imagem_path):
        print(f"Erro: A imagem '{imagem_path}' não foi encontrada.")
        return None
    return cv2.imread(imagem_path)

def processar_imagem(imagem):
    print("Processando a imagem...")
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    return cv2.threshold(imagem_cinza, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def salvar_imagem(imagem, output_img_path):
    os.makedirs(os.path.dirname(output_img_path), exist_ok=True)
    cv2.imwrite(output_img_path, imagem)
    print(f"Imagem processada salva com sucesso em: {output_img_path}")

def extrair_texto(imagem_tratada, lang='por'):
    print("Extraindo texto da imagem...")
    imagem_pil = Image.fromarray(imagem_tratada)
    return pytesseract.image_to_string(imagem_pil, lang=lang)

def salvar_texto(texto, output_txt_path):
    os.makedirs(os.path.dirname(output_txt_path), exist_ok=True)
    with open(output_txt_path, 'w', encoding='utf-8') as arquivo:
        arquivo.write(texto)
    print(f"Arquivo TXT salvo com sucesso em: {output_txt_path}")

def analisar_sentimento(texto):
    print("Analisando o sentimento do texto...")
    sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
    return sentiment_pipeline(texto)

def main():
    print("Diretório atual:", os.getcwd())
    configurar_tesseract()

    # Caminhos absolutos para facilitar a depuração
    imagem_path = os.path.abspath(r'desafio-deprojeto-2\inputs\images.png')
    output_img_path = os.path.abspath("output/imagem_processada.png")
    output_txt_texto_path = os.path.abspath("output/imagem.txt")
    output_txt_sentenca_path = os.path.abspath("output/sentenca.txt")

    print("Caminho absoluto da imagem:", imagem_path)
    
    imagem = carregar_imagem(imagem_path)
    if imagem is None:
        return

    imagem_tratada = processar_imagem(imagem)
    salvar_imagem(imagem_tratada, output_img_path)

    texto_extraido = extrair_texto(imagem_tratada, lang='por')
    print("\nTexto extraído:")
    print(texto_extraido)
    salvar_texto(texto_extraido, output_txt_texto_path)

    if texto_extraido.strip():
        try:
            analise = analisar_sentimento(texto_extraido)
            sentimento = analise[0]['label']
            pontuacao = analise[0]['score']
            sentenca_resultado = f"A sentença apresenta um sentimento '{sentimento}' com uma confiança de {pontuacao:.2f}."
            print("\nAnálise de sentimento:")
            print(sentenca_resultado)
            salvar_texto(sentenca_resultado, output_txt_sentenca_path)
            print("Arquivo de sentença gerado com sucesso!")
        except Exception as e:
            print("Ocorreu um erro durante a análise de sentimento:", e)
    else:
        print("Nenhum texto foi extraído para análise de sentimento.")

if __name__ == "__main__":
    main()
