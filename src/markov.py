import re
import random

class Markov:
    def __init__(self) -> None:
        self.data = []
        self.chain = {}

    def add_data(self, data) -> None:
        if isinstance(data, str):
            self.data.append(data)
        elif isinstance(data, list):
            self.data += data
        else:
            raise TypeError("What are you passing to add_data?")

    def train(self):
        for text in self.data:
            # pat = re.compile(r'[^a-zA-Z ]+')
            # clean_text = re.sub(pat, '', text).lower()
            words = re.findall(r'\w+', text)
            for (i, word) in enumerate(words[:len(words)-1]):
                if word in self.chain:
                    self.chain[word].append(words[i+1])
                else:
                    self.chain[word] = []

    
    def spit_bars(self, n=100):
        default_choices = list(self.chain.keys())
        current = random.choice(default_choices)
        i = 1
        while i <= n:
            if i % 15 == 0:
                print("")
            print(current, end=" ")
            try:
                choices = self.chain[current]
            except KeyError:
                choices = default_choices
            
            if choices:
                current = random.choice(choices)
            else:
                current = random.choice(default_choices)            

            i+=1
        print("")

            
