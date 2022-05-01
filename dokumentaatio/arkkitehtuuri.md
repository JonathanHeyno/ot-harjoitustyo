# Arkkitehtuurikuvaus

## Rakenne
Koodin pakkausrakenne on seuraava

![pakkausrakenne](./kuvat/pakkauskaavio.svg)

Pakkaus **ui** sisältää käyttöliittymästä vastaavan koodin. **Services** sisältää ![GameService](../src/services/game_service.py)-luokan joka tarjoaa rajapinnan käyttöliittymälle. ![GameService](../src/services/game_service.py)-luokka pyörittää peliä luomalla **entities** pakkauksessa olevat oliot ja välittämällä niille käskyt. **Algoritms** pakkauksessa on eri algoritmit joiden perusteella pelaajat päättävät mitä siirtoja tehdä. Ideana on että muut voivat laajentaa ohjelmistoa tekemällä omia algoritmeja ja laittamalla ne tähän pakkaukseen. **Repositories** pakkauksessa on luokka ![PlayerScoreRepository](../src/repositories/player_scores_repository.py) jonka kautta luetaan ja kirjoitetaan pelaajien pelitilastoja tietokantaan.

**Entities** pakkauksessa luokka
- ![Game](../src/entities/game.py) ylläpitää tietoa pelin tilasta: missä ruudussa on mikäkin symboli (tai tyhjä ruutu) ja siltä voi kysyä onko peli loppunut, onko joku voittanut pelin ja missä voittava rivi on. Sille myöskin kerrotaan mihin ruutuun laitetaan seuraava symboli.
- ![Player](../src/entities/player.py) kuvastaa pelaajaa. Siltä kysytään pelaajan seuraavaa siirtoa. ![Player](../src/entities/player.py)-luokka välittää pyynnön siihen liitettyyn algoritmiin joka palauttaa ko. pelaajan seuraavan siirron. Erikoisalgoritmi ![Human](../src/entities/algorithms/human.py) kysyy siis käyttäjältä mikä seuraava siirto pitäisi olla. Muut algoritmit päättävät jollain logiikalla minkä siirron tietokonepelaajan pitäisi tehdä.
- ![AlgorithmManager](../src/entities/algorithm_manager.py) ylläpitää listaa kaikista eri algoritmeista. Ideana on että ohjelmistoa voi laajentaa luomalla itse erilaisia algoritmeja joiden perusteella tietokone päätää mitä tehdä. Jokaiseen ![Player](../src/entities/player.py) luokan olioon liitetään siis yksi algoritmi joka vuorollaan päättää minkä siirron ko. pelaajan pitäisi tehdä. Erikoisalgoritmina on ![Human](../src/entities/algorithms/human.py) jolla kysytään ihmis-käyttäjältä mitä pitäisi seuraavaksi tehdä.

**Algorithms** pakkauksessa luokka
- ![Human](../src/entities/algorithms/human.py) on algoritmi joka kysyy käyttäjältä mikä ruutu pitäisi valita
- ![Uniform](../src/entities/algorithms/uniform.py) on algoritmi joka arpoo tasajakaumalla jonkin vapaana olevan ruudun johon laittaa seuraava merkki.
- ![Valuebased](../src/entities/algorithms/valuebased.py) on algoritmi joka laskee vapaina oleville ruuduille arvot niiden pysty-, vaaka- ja diagonaali akseleilla olevien peräkkäisten merkkien määrien perusteella ja valitsee ruudun jolla on korkein arvo.

**Repositories** pakkauksessa luokka
- ![PlayerScoreRepository](../src/repositories/player_scores_repository.py) lukee ja kirjoittaa voitto, tappio ja tasapelitilastoja tietokantaan. Tietokanta johon kirjoitetaan määritellään ![.env](../.env) ja ![.env.test](../.env.test) tiedostoissa erikseen varsinaisia pelejä ja testausta varten.

Pelin logiikasta vastaavien luokkien välistä yhteyttä kuvaa seuraava luokkakaavio

![luokkakaavio](./kuvat/luokkakaavio.svg)

## Käyttöliittymä
Käyttöliittymä sisältää viisi eri näkymää ja **quit** toiminnallisuuden.
- ![GameView](../src/ui/game_view.py)  näyttää itse pelin tilanteen, eli ruudukon ja siinä olevat merkit
- ![NewGameView](../src/ui/newgame_view.py)  näkymässä määritetään pelin parametrit kuten laudan koko ja pelaajat
- ![LoadView](../src/ui/load_view.py) näkymässä valitaan tallennettu tiedosto ja ladataan siitä pelin tilanne
- ![SaveView](../src/ui/save_view.py) kirjoittaa pelin tilanteen tiedostoon
- ![ScoresView](../src/ui/scores_view.py) näyttää tietokannasta pelaajien voittotilastot

![UI](../src/ui/ui.py)-luokka vastaa näkymien näyttämisestä. ![GameService](../src/services/game_service.py)-luokan olio välitetään aina kulloinkin aktiivisena olevalle näkymälle joka joko kysyy tältä pelin statukseen liittyviä tietoja tai välittää sille tehtävät muutokset, kuten uuden merkin lisäämistä valittuun ruutuun.

## Sovelluslogiikka
![GameService](../src/services/game_service.py)-luokka tarjoaa siis rajapinnan käyttöliittymälle pelin pelaamiseksi. Metodi
- `new_game` alustaa uuden pelin annetun kokoisella laudalla ja tiedolla montako tarvitaan peräkkäin voittoon
- `add_player` lisää uuden pelaajan annetulla pelisymbolilla, algoritmilla ja mahdollisella nimellä. Metodi lisää pelaajan myös voittotilastokantaan jos se on ihmispelaaja kutsumalla ![GameService](../src/services/game_service.py)-luokkaan liitettyä ![PlayerScoreRepository](../src/repositories/player_scores_repository.py) oliota.
- `add_move_and_get_updates` tarkistaa ![Game](../src/entities/game.py)-luokan oliolta onko siirto sallittu, sitten käskee tätä lisäämään siirron jonka jälkeen tarkistetaan loppuiko peli ko. siirtoon. Tämän jälkeen kutsutaan metodia `make_computer_moves_and_get_updates` jolla käydään läpi tietokonepelaajien siirtoja niin kauan kunnes peli loppuu tai tulee ihmispelaajan vuoro tehdä siirto. Metodi palauttaa kaikki nämä siirrot käyttöliittymälle joka tietää korostaa ko. ruudut kun renderöi päivitetyn pelinäkymän

## Tietojen pysyväistallennus
Ohjelma tallentaa pysyväistietoja kahteen paikkaan: pelaajien voittotilastoja tietokantaan, sekä tallennettuja pelejä käyttäjän nimeämiin tekstitiedostoihin. Voittotilastojen suhteen noudatetaan repository-suunnittelumallia jossa luokka ![PlayerScoreRepository](../src/repositories/player_scores_repository.py) vastaa tietojen lukemisesta ja kirjoittamisesta ![.env](../.env)-tiedostossa määritettyyn tietokantaan PlayerScores tauluun. Testien tapauksessa tietokanta on määritetty ![.env.test](../.env.test)-tiedostossa.

Pelin tallennuksessa käyttäjä määrittelee ![SaveView](../src/ui/save_view.py)-näkymässä tiedoston nimen johon pelin tilanne tallennetaan, joka sitten kutsuu ![GameService](../src/services/game_service.py) luokan metodia `save` annetulla tiedostonimellä. Tämä kirjoittaa kaikki pelin tilannetiedot (pelaajien tiedot, ruuduissa olevat pelimerkit) ulkoiseen tekstitiedostoon jossa tiedot ovat eritettynä "§" merkillä. Pelin lataaminen tapahtuu vastaavasti ![LoadView](../src/ui/load_view.py)-näkymässä lukemalla käyttjän määrittelemä tiedosto sisään ja asettamalla siinä oleva pelitilanne voimaan.

## Päätoiminnallisuudet
Alla on kuvattu sekvenssikaavioilla muutama keskeinen toiminnallisuus: uuden pelin alustaminen ja ihmiskäyttäjän tekemä häviävä siirto tietokonepelaajaa vstaan

### Uusi peli
Alla on kuvattu sekvenssikaaviolla uuden pelin käynnistämisen tapahtumakulku kahdelle pelaajalle

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant GameService
  participant Game
  participant AlgorithmManager
  participant Player
  participant PlayerScoresRepository
  User->>UI: click "Start" button
  UI->>GameService: new_game(size, how_many_to_win)
  GameService->>Game: Game(size, how_many_to_win)
  Game-->>GameService: game
  UI->>GameService: add_player(name, symbol, str_algorithm, difficulty, is_human)
  GameService->>AlgorithmManager: AlgorithmManager()
  AlgorithmManager-->>GameService: algorithm
  GameService->>Player: Player(name, symbol, algorithm, is_human)
  Player-->>GameService: player
  GameService->>PlayerScoresRepository: add_player(name)
  UI->>GameService: add_player(name, symbol, str_algorithm, difficulty, is_human)
  GameService->>AlgorithmManager: AlgorithmManager()
  AlgorithmManager-->>GameService: algorithm
  GameService->>Player: Player(name, symbol, algorithm, is_human)
  Player-->>GameService: player
  GameService->>PlayerScoresRepository: add_player(name)
  UI->UI: _show_game_view()
```

Käyttäjä painaa ![NewGameView](../src/ui/newgame_view.py) näkymässä "Start" painiketta jolloin kenttiin kirjoitetut tiedot luetaan ja välitetään ![GameService](../src/services/game_service.py) oliolle. Tämä siis alustaa pelin ja lisää pelaajat peliin ja voittotietokantaan jos ne puutuvat sieltä, jonka jälkeen laitetaan pelinäkymä ![GameView](../src/ui/game_view.py) näkyville.

### Ihminen tekee häviävän siirron tietokonepelaajaa vastaan
Alla on kuvattu tapahtumankulkua kun ihmispelaaja tekee siirron jonka jälkeen ![Valuebased](../src/entities/algorithms/valuebased.py)-algoritmilla toimiva tieotkonepelaaja tekee voittavan siirron.

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant GameService
  participant Game
  participant Player
  participant Valuebased
  participant PlayerScoresRepository
  User->>UI: _handle_button_click("button_number")
  UI->>GameService: add_move_and_get_updates("button_number")
  GameService->>Game: move_is_allowed(x-coord, y-coord)
  Game-->>GameService: True
  GameService->>Game: add_move(x-coord, y-coord, symbol)
  GameService->>Game: is_over()
  Game-->>GameService: False
  GameService->>Player: is_human()
  Player-->>GameService: False
  GameService->>Game: is_over()
  Game-->>GameService: False
  GameService->>Player: next_move(game)
  Player->>Valuebased: next_move(game)
  Valuebased-->>Player: (x-coord, y-coord)
  Player-->>GameService: (x-coord, y-coord, symbol)
  GameService->>Game: is_over()
  Game-->>GameService: True
  GameService->>Game: is_won()
  Game-->>GameService: True
  GameService->>Player: is_human()
  Player-->>GameService: True
  GameService->>PlayerScoreRepository: update_score("Player_name", 0, 1, 0)
  GameService->>Player: is_human()
  Player-->>GameService: False
  GameService-->>UI: [(x-coord, y-coord, symbol)]
  UI->>GameService: turn_symbol()
  UI-->>GameService: "turn_symbol"
  UI->>GameService: game_is_over()
  GameService-->>UI: True
  UI->>GameService: game_is_won()
  GameService-->>UI: True
  UI->>GameService: winner_symbol()
  GameService-->>UI: "winner_symbol"
  UI->>GameService: get_winning_row()
  GameService-->>UI: [winning_row]
```

Kun käyttäjä on painanun jonkin ruudun nappia, painetun ruudun numero välitetään ![GameService](../src/services/game_service.py) oliolle joka kysyy ensiksi ![Game](../src/entities/game.py)-oliolta onko siirto sallittu jonka jälkeen se käskee tätä päivittämään siirron peliin. Tämän jälkeen tartkistetaan onko peli ohi, ja kun se ei ole, kysytään seuraavalta pelaajalta onko se ihmispelaaja. Koska tämä ei ole, niin kutsutaan tämän pelaajan metodia `next_move` joka puolestaan kysyy siihen liitetyltä algoritmilta mikä ruutu valitaan seuraavaksi ja palauttaa tämän tiedon. Jälleen katsotaan onko peli ohi. Koska tietokoneen tekemä siirto oli voittava, niin se on. Tällöin lähdetään käymään läpi kaikkia pelissä olevia pelaajia ja päivittämään niiden voitto tai tappiotiedot tietokantaan jos ko. pelaajat ovat ihmisiä. Tietokantapäivitykset tapatuvat ![PlayerScoreRepository](../src/repositories/player_scores_repository.py)-olion välityksellä. Käyttäjän tekemä siirto ja kaikkien tietokonepelaajien tekemät siirrot sen jälkeen palautetaan käyttöliittymälle. Käyttöliittymä kysyy ![GameService](../src/services/game_service.py) oliolta seuraavaksi vuorossa olevan pelaajan symbolia onko peli ohi
