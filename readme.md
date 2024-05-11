
## Data Solutions AI

O projeto tem como objetivo analisar informações a respeito de tragédias climáticas e gerar sugestões de medidas que podem ser tomadas.

A ideia surgiu devido os acontecimentos recentes no Sul do país.

Informações sobre o que e por que aconteceu são reunidas em um arquivo de texto. O script, por sua vez, recupera o conteúdo desse arquivo e manda uma requisição para a IA pedindo que apresente soluções possíveis para o problema. A resposta é estruturada em uma tabela salva em um arquivo PDF.

## Instalando as Bibliotecas

Para instalar as bibliotecas necessárias para rodar o projeto, execute o seguinte comando:

pip install -r requirements.txt

## Variável de Ambiente

Crie um arquivo .env e coloque nele sua chave de API:

GEMINI_API_KEY=chave_de_api

Você pode gerar sua chave de API [aqui](https://aistudio.google.com/).

## Reunindo informações sobre desastres

Execute o comando python data.py.

O chat irá iniciar e você poderá pesquisar informações sobre as tragédias recentes. Caso o resultado ainda nã oseja o desejado, poderá continuar enviando prompts para o chat. Quando finalmente tiver a resposta que procura, informe a letra n no prompt, e um arquivo de texto será criado contendo a última resposta.

Por ser algo gerado por inteligência artificial, as informações podem conter erros. Certifique-se de verificar a veracidade dos dados.

## Gerando Soluções

Execute o comando python solution.py.

O script irá analisar o arquivo de texto gerado na seção anterior e com base nele irá criar uma tabela com soluções possíveis para o desastre e salvar em um arquivo PDF.

Você também pode inserir manualmente as informações sobre o desastre em um arquivo com o nome "data.txt".