
[![.github/workflows/main.yml](https://github.com/arnold1108/wikibot/actions/workflows/main.yml/badge.svg)](https://github.com/arnold1108/wikibot/actions/workflows/main.yml)
# Wikibot
# Wikipedia Scraper
This project is a simple program that allows you to scrape the first few sentences of a Wikipedia page using Python. It utilizes the `wikipedia` library and provides a command-line interface for easy interaction.

## Features
* Retrieve the contents of a Wikipedia page by providing a topic and desired number of sentences.
* Utilize the `wikipedia` library to fetch data from Wikipedia
* Customize the number of sentences to retrieve through command-line options 

## Getting started 
clone the repository:

`git clone https://github.com/arnold1108/wikibot.git`

Install dependencies:

Before installing, I would recommend that you activate the virtual environment:

`source .env/bin/activate`

Then use the `Makefile` to install:

`make install`

Alternatively, you can use the `requirements.txt` file to install the dependencies:

`pip install -r requirements.txt`

## Usage
To run the Wikipedia Scraper, use the following command:

`python wikibot.py --topic "Topic name" --sentences 3`

You can get an info by running the following command:

`python wikibot.py --help`

Example:

`python wikibot.py --topic "Microsoft" --sentences
 2`

The output would look like:

`Microsoft Corporation is an American multinational technology corporation headquartered in Redmond, Wa
shington. Microsoft's best-known software products are the Windows line of operating systems, the Micr
osoft 365 suite of productivity applications, and the Internet Explorer and Edge web browsers.
`
