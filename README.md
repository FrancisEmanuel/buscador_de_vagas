# Buscador de Vagas
**Algoritmo feito para buscar vagas em sites de recrutamento.**
*Estou começando pelo site Gupy*

Esse algoritmo foi feito em **Python** e usando **scrapy** como framework Web Crawling.<br>
Para começar, instale o scrapy em sua máquina:<br>

> pip install scrapy

Clone esse repositório e execute os seguintes comando:

>#### # Para salvar em um arquivo CSV <br>
> scrapy runspider gupy.py -o gupy.csv --nolog

ou

>#### # Para imprimir as vagas na tela <br>
> scrapy runspider gupy.py

<br>

* O arquivo gerado tem quatro colunas com os nomes: 'empresa' ,'cargo' , 'local' e 'descricao' 
* Filtre com as palavras que você queira buscar, como 'Data Science', 'python', 'Lead Tech', 'REMOTO' e outras.
