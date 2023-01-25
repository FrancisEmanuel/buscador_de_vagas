# Buscador de Vagas
**Algoritmo feito para buscar vagas em sites de recrutamento.**
*Estou começando pelo site Gupy*

Esse algoritmo foi feito em **Python** e usando **scrapy** como framework Web Crawling.<br>
Para começar, instale o scrapy em sua máquina:<br>

> pip install scrapy

Clone esse repositório e execute os seguintes comandos:

>#### # Para salvar em um arquivo CSV <br>
> scrapy runspider gupy.py -o gupy.csv --nolog

ou

>#### # Para imprimir as vagas na tela <br>
> scrapy runspider gupy.py

<br>

* O arquivo gerado tem quatro colunas com os nomes: 'empresa' ,'cargo' , 'local' e 'descricao' 
* Filtre com as palavras que você queira buscar, como 'Data Science', 'python', 'Lead Tech', 'REMOTO' entre outras.


# Job Seeker
**Algorithm designed to search for vacancies on recruitment sites.**
*I'm starting from the Gupy website*

This algorithm was made in **Python** and using **scrapy** as Web Crawling framework.<br>
To get started, install scrapy on your machine:<br>

> pip install scrapy

Clone that repository and run the following commands:

>>### # To save to a CSV file <br>
> scrapy runspider gupy.py -o gupy.csv --nolog

or

>>### # To print vacancies on screen <br>
> scrapy runspider gupy.py

<br>

* The generated file has four columns with the names: 'company', 'position', 'location' and 'description'
* Filter with the words you want to search for, such as 'Data Science', 'python', 'Lead Tech', 'REMOTO' among others.
