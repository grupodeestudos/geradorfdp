#encoding: utf-8
import argparse
from datetime import timedelta
from random import random
import sys

__all__ = ['Ponto', 'horadiff']

parser = argparse.ArgumentParser()
parser.add_argument('--inicio', dest='inicio', type=int, help="Hora de início")
parser.add_argument('--fim', dest='fim', type=int, help="Hora final")
parser.add_argument('--almoco-rand', dest='almoco_rand', action='store_true', help="Sorteia a hora do almoço entre 12:00-13:00 ou sempre soma 4h à --inicio")


'''
  Redebe dois timedelta e retorna a diferenca como um array
  de duas posicoes: [horas, minutos]
'''
def horadiff(inicio, fim):
  segundos = (fim - inicio).seconds
  horas = segundos / 60 / 60

  novo_inicio = timedelta(hours=horas) + inicio
  minutos = (fim - novo_inicio).seconds / 60
  return [horas, minutos]


class Ponto(object):
  def __init__(self, inicio=8, fim=9, almoco_rand=True):
    
    self.entrada = timedelta(hours=inicio, minutes=self._rand_minute())
    self.saida_almoco = self.entrada + timedelta(hours=4)
    self.volta_almoco = self.saida_almoco + timedelta(hours=1)
    self.saida = self.volta_almoco + timedelta(hours=4)

  def _timedelta_tostr(self, t):
    diff = horadiff(timedelta(hours=0, minutes=0), t)
    return "{0}:{1:02}".format(diff[0], diff[1])


  def __repr__(self):
    return '{0} {1} {2} {3}'.format(
        self._timedelta_tostr(self.entrada), 
        self._timedelta_tostr(self.saida_almoco), 
        self._timedelta_tostr(self.volta_almoco), 
        self._timedelta_tostr(self.saida))

  def _rand_minute(self):
    return int(random() * 100) % 60


def run_cli():
  args = parser.parse_args()
  for d in range(31):
    p = Ponto()
    sys.stdout.write("{0}\n".format(p))

