# Ai-minem
A lyrics generator using markov chain.


### Searching for lyrics
Uses requests and beautifulsoup to get lyrics from genius.com
```python
lyric = ""
res = requests.get(url)
page = BeautifulSoup(res.content, "html.parser")
for div in page.find_all(attrs={"class": "Lyrics__Container-sc-1ynbvzw-6"}):
    for link in div.find_all("a"):
        lyric += link.text.strip()
        lyric += "\n"
```



### training the markov model
converts the strings into list of words and creates a chain that that later is used to generate
lyrics
```python
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
```

### generating lyrics
```python
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
```


### A sample of generated lyrics
    eye dropsPain meds cyclops Yeah That s pop radio shock brat Gun addresses on 
    other None never let it must ve gotTo On posters youIt fool add hit me 
    from the tires stationThe sublim blueprint jug tongue after occurLike Spider 2004 Risperdal wall goddamn 
    blow the front to feel it you better lose yourself like the arm MAC ha 
    Loch Weinstein students balls deck da dom dah You say is my wallIt reminds me 
    know what If you But what you I m a show I still hungry I 
    m devastating want him I spray and I ma feed you just like a maxi 
    pad pulled most tableOver Machine point Member Crew olderSponge arsenal futile even got a Rap 
    GodAll my Pharoahe adrenaline flack ear team bad Verse 3 Eminem Dear Mr Rappers figure 
    outHow to blowThis opportunity comes once in the secret Brain dead eye dropsPain meds cyclops 
    Yeah That type of the track cornrows Kid pants Brain dead eye dropsPain meds cyclops 
    Yeah That s nada like Rock Steady eye dropsPain meds cyclops Yeah But next schmoe 
    bathrobe MatthewThat track palms spazzin H A normal life for a feature Maybach Yup Trainwrecks 
    sidewalksPayless high tops Uh K Fed iHopPlaytex icebox Yeah When the back of shit out 
    Chorus Dido My girlfriend screamin scratch threatening olderSponge Crew His soul and drove omnipotent my 
    windowAnd I spray and the trailer s pop totterCaught can do not alike there to 
    skunk ball pay Truckers I m devastating drive bein didn t batter Well gotta dance 
    long as indecent her Bonnie occurLike bleedsIt virgins readyTo AA Godzilla fire spitter monster Blood 
    on my nine stop wellSo getting guess Keith clouds up blow eighty or just to 
    do a killin ago depressed lumma you run with your brother I fell Now I 
    cannot knowsHis Ice Road Truckers I m depressed students bodies Ayy And if I m 
    devastating patientAnd so mad but it Sincerely ass Risperdal long as rude anyways are not 
    so loudHe hear it It s to the trailer park in my seed her up 
    my life is gaping Machine Fans than I ma sleep and tell me from drownin 
    I m talkin to own daughter My tea s nada like this mic when they 
    didn t have in your wrists students These hoes don t see you man you 
    suckOtherwise Minute sure as honestBut Aftermath dollars you re on Just DJ provide area theSame 
    shock batteryBitch since Pew And I m not taking make elevator shitty day but still 
    ain t mistake f nice 3 Eminem Cause e fan easy no fatherHe jarred years 
    niggas AK 47 W herFace Bitch like Ice Road Truckers I just a human index 
    bite hella go capture this is boring blond intentionally nine Bonnie vomit read from ColumbinePut 
    cell figure outHow to chat Ja Stay front to think you can t like a 
    tape rock King levitating years nutsack some bitch she suffocates cable Prince money pupil t 
    call rageTear masterfully rough C Breezy