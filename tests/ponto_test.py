#encoding: utf-8
import unittest

from geradorfdp import Ponto, horadiff
from datetime import timedelta

class HoraDiffTest(unittest.TestCase):


  def test_diff_exata_em_horas(self):
    t1 = timedelta(hours=8)
    t2 = timedelta(hours=9)
    self.assertEquals([1, 0], horadiff(t1, t2))

  def test_diff_exata_em_minutos_menos_de_1_hora(self):
    t1 = timedelta(hours=8, minutes=40)
    t2 = timedelta(hours=8, minutes=50)
    self.assertEquals([0, 10], horadiff(t1, t2))

  def test_diff_quebrada(self):
    t1 = timedelta(hours=8, minutes=40)
    t2 = timedelta(hours=9, minutes=50)
    self.assertEquals([1, 10], horadiff(t1, t2))


class ProntoTest(unittest.TestCase):

  '''
    Gera um dia normal, começando entre 8-9
    com o almoço sendo 4h após o inicio
  '''
  def test_geracao_normal(self):
    p = Ponto(almoco_rand=False)
    dia = p.gerar()
    self.assertEquals(4, len(dia))
    self.assertEquals([4, 0], horadiff(dia[0], dia[1]))


