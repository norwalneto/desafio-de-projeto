# desafio-de-projeto

# Análise de Sentimentos com Language Studio no Azure AI

Este projeto tem como objetivo realizar a extração de texto a partir de uma imagem e, em seguida, aplicar uma análise de sentimentos sobre o conteúdo extraído. Como alternativa ao Azure AI Language Studio, utilizamos a biblioteca **pytesseract** para OCR (Reconhecimento Óptico de Caracteres) e o modelo **Hugging Face Transformers** para análise de sentimentos.

## 📂 Estrutura do Projeto
```
📁 desafio-de-projeto-2
│── 📂 inputs
│   ├── sentenca.txt  # Resultado da análise de sentimentos
│── README.md  # Documentação do projeto
```

## 📊 Resultados e Insights
### 🔍 Texto Extraído
```
JOÃO RECEBEU UM TEXTO DE
INSTRUÇÃO PARA MONTAR UM
BRINQUEDO: BRACELETE DE SUPER
HERÓI, MAS, A PESSOA QUE ESCREVEU,
ESQUECEU DE FAZER LISTA DOS
MATERIAIS, VOCÊ CONSEGUE AJUDÁ-LO
A FAZER A LISTA DOS MATERIAIS QUE
PRECISAM SER SEPARADOS PARA
MONTAR ESSE BRINQUEDO?
```

### 📈 Análise de Sentimento
**Resultado:** Neutro com leve urgência para colaboração.

O modelo de análise de sentimentos identificou o tom do texto como **neutro**, com uma leve sensação de urgência devido à falta de informações essenciais. Não há emoções extremas presentes no conteúdo.

## 🚀 Possibilidades de Melhoria
- Implementação de uma API para processar imagens e realizar a análise de sentimento automaticamente.
- Adaptação do modelo para melhor suporte à língua portuguesa.
- Uso de modelos específicos de análise de sentimentos em português, como o **bertimbau**.

---
📌 **Autor:** _norwalneto_  
📌 **Repositório:** [GitHub](https://github.com/seu-usuario/desafio-de-projeto-2)

