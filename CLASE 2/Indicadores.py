from urllib.request import Request, urlopen
from pyquery import PyQuery

class Indicadores():

    def indicadoresEconomicos(self):
        req = Request('https://www.dane.gov.co/index.php/indicadores-economicos',None,{'User-agent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13ua['google chrome']"})
        content = urlopen(req).read()

        pq = PyQuery(content)
        trm = str([i.text() for i in pq('table').eq(1)('h1').items()][0]).replace('$','').replace('.','').replace(',','.')
        return trm
