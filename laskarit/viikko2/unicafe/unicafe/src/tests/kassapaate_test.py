import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_kassapaatteen_saldo_alussa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_myydyt_lounaat_alussa_nolla(self):
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)

    def test_edullisen_kateisoston_jälkeen_vaihtoraha_ja_saldo_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_edullisen_kateisoston_myyty_maara_kasvanut(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_edullinen_kateisosto_ei_onnistu_jos_raha_ei_riita(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaan_kateisoston_jälkeen_vaihtoraha_ja_saldo_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_maukkaan_kateisoston_myyty_maara_kasvanut(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_maukas_kateisosto_ei_onnistu_jos_raha_ei_riita(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisen_korttiosto_veloitettu_oikein(self):
        kortti = Maksukortti(1000)
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(kortti))
        self.assertEqual(str(kortti), "saldo: 7.6")

    def test_edullisen_korttioston_jalkeen_lounaiden_maara_oikein(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullinen_korttiosto_ei_onnistu_jos_ei_riittavasti_rahaa(self):
        kortti = Maksukortti(10)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(kortti))
        self.assertEqual(str(kortti), "saldo: 0.1")
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaan_korttiosto_veloitettu_oikein(self):
        kortti = Maksukortti(1000)
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(kortti))
        self.assertEqual(str(kortti), "saldo: 6.0")

    def test_maukkaan_korttioston_jalkeen_lounaiden_maara_oikein(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukas_korttiosto_ei_onnistu_jos_ei_riittavasti_rahaa(self):
        kortti = Maksukortti(10)
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(kortti))
        self.assertEqual(str(kortti), "saldo: 0.1")
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kassassa_oleva_rahamaara_ei_muutu_kortilla_ostettaessa(self):
        kortti = Maksukortti(1000)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortin_lataaminen_lisaa_saldoa_ja_kassan_rahaa(self):
        kortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)
        self.assertEqual(str(kortti), "saldo: 20.0")

    def test_negatiivisen_rahamaaran_lataamionen_ei_onnistu(self):
        kortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(kortti, -1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(str(kortti), "saldo: 10.0")
