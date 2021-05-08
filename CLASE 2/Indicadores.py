from urllib.request import Request, urlopen
from pyquery import PyQuery

class Indicadores():

    def indicadoresEconomicos(self):
        req = Request('https://www.dane.gov.co/index.php/indicadores-economicos',None,{'User-agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'})
        content = urlopen(req).read()

        pq = PyQuery(content)
        trm = str([i.text() for i in pq('table').eq(1)('h1').items()][0]).replace('$','').replace('.','').replace(',','.')
        return trm
