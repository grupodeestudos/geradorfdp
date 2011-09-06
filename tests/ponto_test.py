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

  def test_diff_quebrada(self):
    t1 = timedelta(hours=0, minutes=0)
    t2 = timedelta(hours=9, minutes=50)
    self.assertEquals([9, 50], horadiff(t1, t2))


class ProntoTest(unittest.TestCase):

  '''
    Gera um dia normal, começando entre 8-9
    com o almoço sendo 4h após o inicio
  '''
  def test_geracao_normal(self):
    p = Ponto(almoco_rand=False)

    self.assertEquals([4, 0], horadiff(p.entrada, p.saida_almoco))

    self.assertEquals([1, 0], horadiff(p.saida_almoco, p.volta_almoco))
    self.assertEquals([4, 0], horadiff(p.volta_almoco, p.saida))

  def test_repr(self):
    p = Ponto()
    p.entrada = timedelta(hours=8)
    p.saida_almoco = timedelta(hours=12)
    p.volta_almoco = timedelta(hours=13)
    p.saida = timedelta(hours=17)
    self.assertEquals("8:00 12:00 13:00 17:00", p.__repr__())

  def test_timedelta_tostr(self):
    t = timedelta(hours=8, minutes=0)
    self.assertEquals("8:00", Ponto()._timedelta_tostr(t))

