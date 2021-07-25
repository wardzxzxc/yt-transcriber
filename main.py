import requests
import re
from bs4 import BeautifulSoup

if __name__ == '__main__':
    video_id = input("Enter YouTube Video Id:")
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 '
                      'Safari/537.36',
        'Content-Type': 'text/html',
    }
    r = requests.get("https://www.youtube.com/watch?" + video_id, headers=headers)
    yt_page_html = r.text
    yt_regex = re.compile('playerCaptionsTracklistRenderer.*?(youtube.com\/api\/timedtext.*?)"')
    url_transcript = yt_regex.search(yt_page_html).group(1)
    decoded_url_transcript = url_transcript.encode('utf-8').decode('unicode-escape')
    r = requests.get("https://www." + decoded_url_transcript)
    text = BeautifulSoup(r.text, 'html.parser').get_text(separator=' ')

    # To decode the HTML characters
    transcript = BeautifulSoup(text, features="lxml").get_text()

    with open('transcript.txt', 'w+') as fh:
        fh.write(transcript)

    print("Transcribing done!")

