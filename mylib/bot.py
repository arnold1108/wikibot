import wikipedia


def scrape(name, length=3):
    result = wikipedia.summary(name, sentences=length)
    return result
# scrape("New Zealand national rugby union team", 3)
