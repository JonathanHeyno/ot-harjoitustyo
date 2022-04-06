# Arkkitehtuurikuvaus

## Rakenne
Koodin pakkausrakenne on seuraava

![pakkausrakenne](./kuvat/pakkauskaavio.svg)

Pakkaus **ui** sisältää käyttöliittymästä vastaavan koodin. **Services** sisältää *GameService* luokan joka tarjoaa rajapinnan käyttöliittymälle. *GameService* luokka pyörittää peliä luomalla **entities** pakkauksessa olevat oliot ja välittää niille käskyt. 
**Entities** pakkauksessa luokka
- *Game* ylläpitää tietoa pelin tilasta: missä ruudussa on mikäkin symboli (tai tyhjä ruutu) ja siltä voi kysyä onko peli loppunut, onko joku voittanut pelin ja missä voittava rivi on. Sille myöskin kerrotaan mihin ruutuun laitetaan seuraava symboli.
- *Player* kuvastaa pelaajaa. Siltä kysytään pelaajan seuraavaa siirtoa. Player luokka välittää pyynnön siihen liitettyyn algoritmiin joka palauttaa ko. pelaajan seuraavan siirron. Erikoisalgoritmi *Human* luokka kysyy siis käyttäjältä mikä seuraava siirto pitäisi olla. Muut algoritmit päättävät jollain logiikalla minkä siirron tietokonepelaajan pitäisi tehdä.
- *Algorithms* ylläpitää listaa kaikista eri algoritmeista. Ideana on että ohjelmistoa voi laajentaa luomalla itse erilaisia algoritmeja joiden perusteella tietokone päätää mitä tehdä. Jokaiseen *Player* luokan olioon liitetään siis yksi algoritmi joka vuorollaan päättää minkä siirron ko. pelaajan pitäisi tehdä. Erikoisalgoritmina on *Human* jolla kysytään ihmis-käyttäjältä mitä pitäisi seuraavaksi tehdä.
- *Human* on algoritmi joka kysyy käyttäjältä mikä ruutu pitäisi valita
- *Uniform* luokka on algoritmi joka arpoo tasajakaumalla jonkin vapaana olevan ruudun johon laittaa seuraava merkki.
- *Valuebased* luokka on algoritmi joka laskee vapaina oleville ruuduille arvot niiden pysty-, vaaka- ja diagonaali akseleilla olevien peräkkäisten merkkien määrien perusteella ja valitsee ruudun jolla on korkein arvo.

Pelin logiikasta vastaavien luokkien välistä yhteyttä kuvaa seuraava luokkakaavio

```mermaid
 classDiagram
      GameService "1" --> "1" Game
      GameService -->> Algorithms
      GameService "1" --> "*" Player
      Player "0..1" --> "0..1" Human
      Player "0..1" --> "0..1" Uniform
      Player "0..1" --> "0..1" Valuebased
      Algorithms -->> Human
      Algorithms -->> Uniform
      Algorithms -->> Valuebased
      class GameService{
      }
      class Game{
      }
      class Player{
      }
      class Algorithms{
      }
      class Human{
      }
      class Uniform{
      }
      class Valuebased{
      }
```
