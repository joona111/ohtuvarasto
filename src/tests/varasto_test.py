import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_saldo(self):
        self.varasto = Varasto(10, -10)
        self.assertEqual(self.varasto.saldo, 0)

        self.varasto = Varasto(10, 5)
        self.assertEqual(self.varasto.saldo, 5)

    def test_konstruktori_luo_tyhjan_varaston(self):

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_uudella_varastolla_oikea_tilavuus2(self):
        self.varasto = Varasto(0)
        self.assertEqual(self.varasto.tilavuus, 0)
        self.varasto = Varasto(-10)
        self.assertEqual(self.varasto.tilavuus, 0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)
        kaikki_mita_voidaan = self.varasto.saldo
        self.assertAlmostEqual(
            self.varasto.ota_varastosta(22), kaikki_mita_voidaan)

        self.assertEqual(self.varasto.lisaa_varastoon(-2), None)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.assertEqual(self.varasto.ota_varastosta(-2), 0)

        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
        self.varasto.lisaa_varastoon(5)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)
