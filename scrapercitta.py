from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import re
import json
from datetime import datetime



Biblioteche_citta = {
    'Ghetti': 'https://opac.provincia.brescia.it/library/biblioteca-v-ghetti-di-viale-caduti-del-lavoro/timetable/',
    'Ial': 'https://opac.provincia.brescia.it/library/biblioteca-ial-brescia/timetable/',
    'Arnaldo': 'https://opac.provincia.brescia.it/library/ARNALDO-SCOLASTICA-/timetable/', 
    'Abba Ballini': 'https://opac.provincia.brescia.it/library/ABBA-BALLINI-SCOLASTICA-/timetable/',
    'Gambara': 'https://opac.provincia.brescia.it/library/biblioteca-scolastica-isis-veronica-gambara/timetable/',
    'Buffalora': 'https://opac.provincia.brescia.it/library/buffalora/timetable/',
    'Mediateca Queriniana': 'https://opac.provincia.brescia.it/library/mediateca-queriniana/timetable/',
    'Museo di Scienza Naturali': 'https://opac.provincia.brescia.it/library/museo-di-scienze-naturali/timetable/',
    'Largo Torrelunga': 'https://opac.provincia.brescia.it/library/largo-torrelunga/timetable/',
    'Parco Gallo': 'https://opac.provincia.brescia.it/library/parco-gallo/timetable/',
    'Istituto Agazzi': 'https://opac.provincia.brescia.it/library/pasquali-agazzi-istituto/timetable/',
    'Queriniana': 'https://opac.provincia.brescia.it/library/queriniana/timetable/',
    'Prealpino': 'https://opac.provincia.brescia.it/library/prealpino/timetable/',
    'Santa Giulia Scolastica': 'https://opac.provincia.brescia.it/library/SANTAGIULIA-SCOLASTICA-/timetable/',
    'San Polo': 'https://opac.provincia.brescia.it/library/san-polo/timetable/',
    'Tartaglia': 'https://opac.provincia.brescia.it/library/biblioteca-scolastica-tartaglia-olivieri/timetable/',
    'Sala Umberto Eco': 'https://opac.provincia.brescia.it/library/sala-di-lettura-umberto-eco/timetable/',
    'Trebeschi': 'https://opac.provincia.brescia.it/library/fondazione-trebeschi/timetable/',
    'Villaggio Sereno': 'https://opac.provincia.brescia.it/library/sereno/timetable/',
    'Casazza': 'https://opac.provincia.brescia.it/library/casazza/timetable'
    
}

biblio_senza_orario=[]

def run():
    def ottieni_orario(url):
        try:
            html = urlopen(url) # apre url
        except HTTPError as e:
            return e  # eccezione per url vuoto
        try:
            bs = BeautifulSoup(html.read(), 'html.parser')

            
            nomebiblio= bs.find("h2", property="name").get_text() ##Ottiene dalla pagina il nome della biblio 
            
            
            # Preleva orario di oggi
            try:
                for sibling in bs.find('div', id="timetable").td.next_sibling.next_sibling: # preleva il primo orario della giornata
                
                    if ("Chiusa" in sibling):
                        return "chiusa" # ritorna chiusa se la biblioteca è chiusa
                    else:

                        pomeriggio = sibling.next_sibling.next_sibling # prendo l'orario del pomeriggio nel caso ci sia doppio orario

                        return sibling+' \n '+pomeriggio.strip() # restituisco l'orario 
            except AttributeError as e:
                        # Elenca biblio senza tabella e aggiunge a file json.
                        # Utile per avere sott'occhio subito quali biblioteche hanno cancellato l'orario
                        if (str(e)== "'NoneType' object has no attribute 'td'"): 
                            

                            biblio_senza_orario.append(nomebiblio) 
                            return None

                        else:
                            print (e)


            
        except AttributeError as e:
            return e 



    biblio_aperte_dict = {}
    biblio_chiuse_dict = {}
    
    # crea dizionario con orari
    for i in Biblioteche_citta:

        orario = ottieni_orario(Biblioteche_citta[i]) #chiama funzione sopra. Biblioteche_citta[i] è l'url
        try:
            if "chiusa" in orario:
                biblio_chiuse_dict.setdefault('chiuse', []) # inserisce l'elemento radice in file json. Rende più immediato l'inserimento delle biblioteche chiuse

                biblio_chiuse_dict['chiuse'].append(
                    {'nome': i, 'url': Biblioteche_citta[i].split("/timetable/").pop(0)})
                    # ottiene l'url della biblioteca utilizzato per il link cliccabile dall'utente.
                    # pop elimina lo spazio bianco dalla lista
        
            
        
            else:

                biblio_aperte_dict.setdefault('biblio', []) # crea il dizionario che salva solo le biblioteche aperte oggi
                
                biblio_aperte_dict['biblio'].append({'nome': i, 'orario': orario.strip().split("\n"), "url": Biblioteche_citta[i].split("/timetable/").pop(0)}) # core element: inserisce nel dizionario il nome, l'orario e l'url. strip rimuove gi spazi bianchi. split("\n") separa in due campi separati gli orari doppi. 
                    # pop(0) elimina parte inutile in url
                    # split(/"timetable/") serve a rimandare alla pagina principale sul sito opac di ogni biblioteca (invece che alla tabella orari)
            
          
        except TypeError as e:
            print (e)

    biblio_aperte_json = json.dumps(biblio_aperte_dict)  # trasforma dizionario in json
    biblio_chiuse_json = json.dumps(biblio_chiuse_dict)  # trasforma dizionario in json
    runninglog = "\n" + str(datetime.now())  # log di esecuzione


    f1 = open("dati/runninglog.txt", "a") #file di log
    f1.write(runninglog)
    f1.close

    # crea json di biblio aperte
    f2 = open("dati/open.json", "w")
    f2.write(biblio_aperte_json)
    f2.close


    # crea json chiuse
    f3 = open("dati/chiuse.json", "w")
    f3.write(str(biblio_chiuse_json))
    f3.close

    # txt con tutte le biblioteche senza orario sul sito Opac
    f4 = open("dati/biblio_orari_assenti.txt", "w")
    f4.write(str(biblio_senza_orario))
    f4.close

run()
