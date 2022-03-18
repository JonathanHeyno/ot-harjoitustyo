```mermaid
 classDiagram
      Pelilauta "1" -- "*" Ruutu
	  Ruutu "1" -- "*" Pelinappula
	  Pelaaja "1" -- "1" Pelinappula
	  Pelilauta "1" -- "*" Pelaaja
	  Ruutu "" -- "1" Ruutu
      class Pelilauta{

      }
      class Ruutu{

      }
	  class Pelinappula{

      }
	  class Pelaaja{

      }
```