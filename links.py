from timeit import repeat
import requests, json
import time
import webbrowser

apikey = "563492ad6f917000010000018c00c19ff1f24c18aae857f06fe738eb"
Bash = "https://api.pexels.com/videos/popular"

#enviando autorização no cabeçalho 'headers'
def url():
    r = requests.get(Bash, headers={'Authorization': apikey})
    filmes = json.loads(r.text)
    
    #loop que mostra quantas url´s a api possui
    repete = 0
    for i in filmes['videos']: 
        repete+=1
        
    #loop que cria uma lista com as url´s
    urls = []
    for i in range(repete):
        link = (filmes['videos'][i]['video_files'][0]['link'])
        urls.append(link)       
    return urls

for i in url():
    webbrowser.open(i,0)
    time.sleep(5)

