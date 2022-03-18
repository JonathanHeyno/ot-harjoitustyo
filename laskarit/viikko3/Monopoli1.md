```mermaid
 classDiagram
      Pelilauta "1" -- "40" Ruutu
	  Ruutu "1" -- "0..8" Pelinappula
	  Pelaaja "0..1" -- "1" Pelinappula
	  Pelilauta "1" -- "2..8" Pelaaja
	  Ruutu "" -- "1" Ruutu: seuraava ruutu
      class Pelilauta{

      }
      class Ruutu{

      }
	  class Pelinappula{

      }
	  class Pelaaja{

      }
```
