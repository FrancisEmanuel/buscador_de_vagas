import scrapy

class VagaItem(scrapy.Item):
  empresa = scrapy.Field()
  cargo = scrapy.Field()
  local = scrapy.Field()
  descricao = scrapy.Field()