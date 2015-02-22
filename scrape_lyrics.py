import requests
import bs4

root_url = 'http://www.metrolyrics.com/'
url = 'http://www.metrolyrics.com/ride-lyrics-lana-del-rey.html'
song_list_url1 = 'http://www.metrolyrics.com/lana-del-rey-alpage-1.html'
song_list_url2 = 'http://www.metrolyrics.com/lana-del-rey-alpage-2.html'
song_list_url3 = 'http://www.metrolyrics.com/lana-del-rey-alpage-3.html'

#returns a list of all song links
#originally designed for a different lyrics site.
#TODO update to work with metrolyrics
def get_lyrics_page_urls():
	response = requests.get(url)
	soup = bs4.BeautifulSoup(response.text)
	return [a.attrs.get('href') for a in soup.select('#listAlbum a[href^=../lyrics/lanadelrey]')]

def get_song_info(lyrics_page_url):
	song_data = {}
	response = requests.get(lyrics_page_url)
	#response = requests.get(root_url + lyrics_page_url)
	soup = bs4.BeautifulSoup(response.text)
	song_data['title'] = soup.select('h1')[0].get_text().strip()
	song_data['lyrics'] = [p.get_text().strip() for p in soup.select('.verse')] 	
	return song_data

print get_song_info(url)


#lyrics_page_urls = get_lyrics_page_urls()
#for lyrics_page_url in lyrics_page_urls:
#		print get_song_info(lyrics_page_url)


#print(get_lyrics_page_urls())
