import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
        
    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "saldo: 10.1")

    def test_rahan_ottaminen_vahentaa_oikean_maaran(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.05")

    def test_rahan_ottaminen_ei_vahenna_saldoa_jos_saldo_ei_riita(self):
        self.maksukortti.ota_rahaa(50)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_ottaminen_palauttaa_true_jos_saldo_riittaa(self):
        self.assertTrue(self.maksukortti.ota_rahaa(5))
        
    def test_rahan_ottaminen_palauttaa_false_jos_saldo_ei_riita(self):
        self.assertFalse(self.maksukortti.ota_rahaa(50))