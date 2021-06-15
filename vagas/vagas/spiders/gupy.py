import scrapy
from vagas.items import VagaItem
from scrapy.selector import Selector
import pdb


class GupySpider(scrapy.Spider):
    name = 'gupy'
    allowed_domains = ['gupy.io']
    start_urls = ['http://gupy.io/']

    def start_requests(self):
         yield scrapy.Request('https://gupy.io/login', self.parse)
            
    def parse(self, response):
        body_sel = Selector(response)
        empresas =  body_sel.xpath("//tbody/tr/td/text()").extract()
        urls_empresas = body_sel.xpath("//tbody/tr/td/a/@href").extract() #--- https://4all.gupy.io/
        
        
        #------- Filtro de urls, tira os que tem /candidates
        test=''
        nova_urls_empresas=[]
        for nue in urls_empresas:
            if nue.count('candidates'):
                test='ok'
            else:
                nova_urls_empresas.append(nue)
         
        
        #------- passando urls e nomes das empresas
        i=0          
        for url in nova_urls_empresas :
            request = scrapy.Request(url, self.parse_vagas)
            request.cb_kwargs['url_empresa'] = url
            empresa = empresas[i]
            request.cb_kwargs['empresa'] = empresa
            i+=1
            yield request
            
            
    def parse_vagas(self, response, url_empresa, empresa):
        
        body_sel = Selector(response)
        urls_vagas = body_sel.xpath("//td/a/@href").extract()             #--- url da vaga
        
        for url_vaga in urls_vagas:
            nova_url = url_empresa+url_vaga[1:]                           #--- [1:] tira /
            request = scrapy.Request(nova_url, self.parse_cargo)          #--- url completa
            request.cb_kwargs['empresa'] = empresa
            yield request
    
            
    def parse_cargo(self, response, empresa):
        body_sel = Selector(response)
        
        cargo = self.to_str(body_sel.xpath("//title/text()"))
        
        local = body_sel.xpath("//div[@class='header__content']/div/ul/li/text()").extract()
        local = local[1][23:]

        descricao = body_sel.xpath("//div[@class='description']/p/text()").extract()
        vagas_ativas = VagaItem(empresa=empresa, cargo=cargo, local=local, descricao=descricao)

        #self.print_item(vagas_ativas) #--- imprimir na tela
        yield vagas_ativas             #--- gravar 
        
        
        
    def to_str(self, element):
        return element.extract()[0]

    def print_item(self, vagas_ativas):
        for k, v in vagas_ativas.items():
            print(f"{k}: {v}")
        print("--------------------")
