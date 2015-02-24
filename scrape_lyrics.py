import requests
import bs4

root_url = 'http://lyrics.wikia.com'
artist_url = '/Lana_Del_Rey'


#returns a list of all song links
def get_lyrics_page_urls(artist_url):
	response = requests.get(root_url + artist_url)
	soup = bs4.BeautifulSoup(response.text)
	return [a.attrs.get('href') for a in soup.select('ol a')]

def get_song_info(lyrics_page_url):
	song_data = {}
	response = requests.get(root_url + lyrics_page_url)
	soup = bs4.BeautifulSoup(response.text)
	[s.extract() for s in soup('script')] #removes scripts surrounding lyrics
	song_data = [p.get_text().strip() for p in soup.select('.lyricbox')] 	
	return song_data

lyrics_page_urls = get_lyrics_page_urls(artist_url)
for lyrics_page_url in lyrics_page_urls:
		print get_song_info(lyrics_page_url)


