from scrap import GeniusScraper
from utils import write_list, read_list
from markov import Markov

def main():
    # urls = [
    #     "https://genius.com/Eminem-godzilla-lyrics",
    #     "https://genius.com/Eminem-rap-god-lyrics",
    #     "https://genius.com/Eminem-lose-yourself-lyrics",
    #     "https://genius.com/Eminem-stan-lyrics",
    #     "https://genius.com/Eminem-not-alike-lyrics"
    # ]
    # scraper = GeniusScraper()
    # scraper.add_url(urls)
    # lyrics = scraper.scrap()
    # write_list(lyrics, "res/lyrics")
    lyrics = read_list("res/lyrics")
    markov = Markov()
    markov.add_data(lyrics)
    markov.train()
    markov.spit_bars(500)



if __name__ == "__main__":
    main()