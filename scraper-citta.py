from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import re
import json
from datetime import datetime

Diz_Biblioteche= {
    'Ghetti':'https://opac.provincia.brescia.it/library/biblioteca-v-ghetti-di-viale-caduti-del-lavoro/timetable/',
    'Ial': 'https://opac.provincia.brescia.it/library/biblioteca-ial-brescia/timetable/',
    'Arnaldo': 'https://opac.provincia.brescia.it/library/ARNALDO-SCOLASTICA-/timetable/',
    'Abba Ballini':'https://opac.provincia.brescia.it/library/ABBA-BALLINI-SCOLASTICA-/timetable/',
    'Gambara':'https://opac.provincia.brescia.it/library/biblioteca-scolastica-isis-veronica-gambara/timetable/',
    'Buffalora':'https://opac.provincia.brescia.it/library/buffalora/timetable/',
    'Mediateca Queriniana':'https://opac.provincia.brescia.it/library/mediateca-queriniana/timetable/',
    'Museo di Scienza Naturali':'https://opac.provincia.brescia.it/library/museo-di-scienze-naturali/timetable/',
    'Largo Torrelunga':'https://opac.provincia.brescia.it/library/largo-torrelunga/timetable/',
    'Parco Gallo':'https://opac.provincia.brescia.it/library/parco-gallo/timetable/',
    'Istituto Agazzi':'https://opac.provincia.brescia.it/library/pasquali-agazzi-istituto/timetable/',
    'Queriniana':'https://opac.provincia.brescia.it/library/queriniana/timetable/',
    'Prealpino':'https://opac.provincia.brescia.it/library/prealpino/timetable/',
    'Santa Giulia Scolastica':'https://opac.provincia.brescia.it/library/SANTAGIULIA-SCOLASTICA-/timetable/',
    'San Polo':'https://opac.provincia.brescia.it/library/san-polo/timetable/',
    'Tartaglia':'https://opac.provincia.brescia.it/library/biblioteca-scolastica-tartaglia-olivieri/timetable/',
    'Sala Umberto Eco':'https://opac.provincia.brescia.it/library/sala-di-lettura-umberto-eco/timetable/',
    'Trebeschi':'https://opac.provincia.brescia.it/library/fondazione-trebeschi/timetable/',
    'Villaggio Sereno':'https://opac.provincia.brescia.it/library/sereno/timetable/'
    }


def getElement(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None #eccezione per url vuoto
    try: 
        bs= BeautifulSoup(html.read(), 'html.parser')
        elem= bs.title #ottengo elemento che mi serve

        for sibling in bs.find('div', id="timetable").td.next_sibling.next_sibling: #prelevo orario di oggi
            
            if ("Chiusa" in sibling):
                return "chiusa"
            else:
                return sibling

            
     
    except AttributeError as e:
        return None
    return elem

biblio_aperte_dict= {}
biblio_chiuse= []
biblio_aperte_prejson = {}
biblio_chiuse_dict= {}

for i in Diz_Biblioteche:
   

    orario= getElement(Diz_Biblioteche[i])
    if "chiusa" in orario:
        biblio_chiuse_dict.setdefault('chiuse',[])
        biblio_chiuse_dict['chiuse'].append({'nome':i, 'url': Diz_Biblioteche[i].split("/timetable/").pop(0)}) #ottengo url della biblioteca e non della sua tabella orario. pop elimina spazio bianco da lista
        
      
    else:
        
        
        #  #creo un dizionario che salva solo le biblioteche aperte oggi 
        biblio_aperte_dict.setdefault('biblio',[])
        biblio_aperte_dict['biblio'].append({'nome': i, 'orario': orario.strip(), "url": Diz_Biblioteche[i].split("/timetable/").pop(0)})

        #implemento: URL IN nome biblioteca
        #elimino /timetable da Diz_Biblioteche[i]




biblio_aperte_json = json.dumps(biblio_aperte_dict) #trasformo dict in json
biblio_chiuse_json = json.dumps(biblio_chiuse_dict) #trasformo dict in json
runninglog = "\n" + str(datetime.now()) #log di esecuzione



f1= open("runninglog.txt","a")
f1.write(runninglog)
f1.close

#creo json aperte
f2= open("open.json", "w") 
f2.write(biblio_aperte_json)
f2.close


#creo json chiuse
f4= open("chiuse.json", "w")
f4.write(str(biblio_chiuse_json))
f4.close
