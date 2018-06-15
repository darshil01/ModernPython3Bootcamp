import requests
from bs4 import BeautifulSoup
import pdb
from random import choice

results = {}
hints = {}

def build_base():
    url = "http://quotes.toscrape.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    objects = soup.find_all("div", {"class": "quote"})

    for x in range(len(objects)):
        q = objects[x].find("span", {"class": "text"}).text
        a = objects[x].find("small", {"class": "author"}).text
        url = "http://quotes.toscrape.com" + str(objects[x].find("a")['href'])
        results[x] = [q, a, url]

def build_hints():
    quote = choice(results)
    author_reponse = requests.get(quote[2])
    author_soup = BeautifulSoup(author_reponse.text, "html.parser")
    hints["birth_date"] = author_soup.find("span", {"class": "author-born-date"}).text
    hints["birth_locale"] = author_soup.find("span", {"class": "author-born-location"}).text
    hints["first_initial"] = quote[1][0]
    hints["last_initial"] = quote[1].split(" ")[-1][0]
    return quote    

def get_hint(num):
    if num == 4:
        return f"They were born on {hints['birth_date']}"
    if num == 3:
        return f"They were born in {hints['birth_locale']}"
    if num == 2:
        return f"Their first initial is {hints['first_initial']}"
    if num == 1:
        return f"Their last initial is {hints['last_initial']}"

def play_game(q):
    guesses = 5
    quote = q
    guess = input(f"{quote[0]} was said by: ")
    while guesses != 1:
        # print(f"answer {quote[1]} entered {guess} equal: {guess == quote[1]}")
        if guess == "quit":
            break
        if guess == quote[1]:
            print("You win")
            break
        else:
            guesses -= 1
            print(get_hint(guesses))
            guess = input(f"Guesses remaining {guesses}: ")
    if guesses == 1:
        print(quote)
        print("LOOOSSSEERRRR")

build_base()

while True:
    qu = build_hints()
    play_game(qu)
    play_again = input("Play again yes / no ")
    if "y" not in play_again.lower():
        break



