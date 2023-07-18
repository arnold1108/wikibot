import wikipedia


def scrape(name, length):
    result = wikipedia.summary(name, sentences=length)
    print(result)
scrape("New Zealand national rugby union team", 3)
