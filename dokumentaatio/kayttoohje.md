# Käyttöohje

Lataa ohjelman viimeisin [release](https://github.com/JonathanHeyno/ot-harjoitustyo/releases/tag/loppupalautus)

## Konfigurointi
Voittotilastot tallentuvat [.env](../.env)-tiedostossa määriteltyyn tietokantaan \data\ nimiseen kansioon. Pelien tallennus tapahtuu \saves\ nimiseen kansioon. Nämä polut määrietetään [config.py](../src/config.py)-tiedostossa.

## Ohjelman asennus ja käynnistäminen

Mene ohjelman kansioon ja asenna riippuvuudet komennolla
```
poetry install
```

Kun riippuvuudet on kertaalleen asennettu, ohjelman voi käynnistää komentoriviltä komennolla
```
poetry run invoke start
```

Ohjelma luo itse tarvittavan tietokannan

## Pelin aloittaminen
Peli käynnistyy voittotilastonäkymään. Siirry **New Game** näkymään. Aseta ruudukon koko sekä tieto montako pitää saada peräkkäin voittoon. Lisää pelaajat peliin. Ihmis pelaajille voi antaa nimen jolloin järjestelmä pitää kirjaa tämän voitoista, tappioista ja tasapeleistä. Merkitse pelaajan pelisymboli, esim "X" vastaavaan symbolikenttään. Paina lopuksi **add** nappia jolloin pelaaja tulee lisätyksi. Voit sitten lisätä muite pelaajia jotta ei tarvitse pelata yksin. Algorithms alasvetovalikosta voi valita tietokonevastustajien käyttämää algoritmia, ja difficulty mittarista niiden vaikeustason jos ko. algoritmi sellaista tukee. Nämä lisätään myös **add** nappulasta. Pelaajat voidaan poistaa pelistä **remove** nappulasta. Kun pelaajat ja pelilaudan koko on asetettu, peli voidaan käynnistää **start** nappulasta.

![](./kuvat/new_game.jpg)

## Pelin pelaaminen
Peliä pelataan painamalla haluttuua ruutua. Peli näyttää korostetulla vimmeisimmät tietokonepelaajien tekemät siirrot sekä pelin loputtua voittavan rivin.

![](./kuvat/game.jpg)

## Pelin tallentaminen
Peli voidaan tallentaa siirtymällä **save** näkymään ja antamalla talletettavalle pelille nimi tai vaihtoehtoisesti tallentamalla aiemmin talletetun pelin päälle. Annettuasi nimi pelille, paina **Save** nappia.

![](./kuvat/save.jpg)

## Pelin lataaminen
Tallennetun pelin voi ladata **Load** näkymästä. Valitse tallennettu peli alasvetovalikosta tai kirjoita se, ja paina sitten **Load**-nappia.

![](./kuvat/load.jpg)

## Pelitulosten tarkasteleminen
Siirry **Scores** näkymään tarkastelemaan pelaajien voittotilastoja.

## Ohjelman lopettaminen
Ohjelman voi lopettaa **Quit** painikkeesta.

## Ohjelman laajentaminen omatekoisilla algoritmeilla
Tietokonepelaajat pelaavat niille määrättyjen algoritmien mukaisesti. Peliä voi laajentaa luomalla itse niille algoritmeja seuraavasti:
- Luo algoritmille luokka. Luokalla pitää olla property ja setteri nimeltä `difficulty` (vaikka se ei vaikeustason perusteella osaisikaan muuttaa käyttäytymistään) ja metodi `next_move(game, symbol)` joka palauttaa tuplena seuraavan siirron x ja y koordinaatit **(x, y)**. Metodille annetaan siis peli-olio ja vuorossa olevan pelaajan symboli. Peli-oliolta voidaan kysellä mm. pelilaudan tilannetta ja pelaajien lukumäärää.
- Kyseinen luokka laitetaan kansioon \src\entities\algoritms\
- Luokka ja sen nimitys lisätään **AlgorithmManager** luokan konstruktorissa olevaan dictiin jotta sen voi valita käyttöliittymässä
