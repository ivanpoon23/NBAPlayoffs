from bs4 import BeautifulSoup
import pandas as pd
import requests
def main():
    url = "https://www.basketball-reference.com/playoffs/NBA_2023_advanced.html"

# Send an HTTP GET request to the website
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    tables = soup.find_all('table')
table = soup.find('table', class_ = 'sortable')

playoffs_advanced23 = pd.DataFrame(columns=['Player','Pos',	'Age','Tm', 'G', 'MP','PER', 'TS%','3PAr','FTr','ORB%','DRB%', 'TRB%','AST%','STL%','BLK%',	'TOV%',	'USG%','OWS', 'DWS','WS','WS/48','OBPM','DBPM','BPM','VORP'])

i = 0
for row in table.tbody.find_all('tr'):
    columns = row.find_all('td')
    if columns != []:
        Player = str(columns[0].text.strip())
        Pos = str(columns[1].text.strip())
        Age = int(columns[2].text.strip())
        Tm = str(columns[3].text.strip())
        G = int(columns[4].text.strip())
        MP =  columns[5].text.strip()
        PER =  columns[6].text.strip()
        ts =  columns[7].text.strip()
        PAr =  columns[8].text.strip()
        ft =  columns[9].text.strip()
        orb =  columns[10].text.strip()
        drb =  columns[11].text.strip() 
        trb =  columns[12].text.strip() 
        ast =  columns[13].text.strip() 
        stl =  columns[14].text.strip() 
        blk =  columns[15].text.strip() 
        tov =  columns[16].text.strip() 
        usg =  columns[17].text.strip() 
        ows =  columns[19].text.strip() 
        dws =  columns[20].text.strip()
        ws =  columns[21].text.strip()
        wsper =  columns[22].text.strip()
        obpm =  columns[24].text.strip()
        dbpm =  columns[25].text.strip() 
        bpm =  columns[26].text.strip()
        vrop =  columns[27].text.strip()

        playoffs_advanced23.loc[i] = [Player, Pos,Age,Tm, G, MP,PER, ts,PAr, ft, orb,drb,trb, ast,stl,blk, tov,usg,ows, dws,ws,wsper,obpm,dbpm,bpm,vrop]
        i+= 1
        print(playoffs_advanced23)


if main() == '__main__':
    main()