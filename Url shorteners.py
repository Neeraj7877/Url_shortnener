import pyshorteners


url = input('Enter the url:')


def shortenurl(url):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))


shortenurl(url)
