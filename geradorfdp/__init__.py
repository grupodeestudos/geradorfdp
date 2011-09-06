#encoding: utf-8
import argparse
from datetime import timedelta

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
    self.inicio = inicio

  """
    Retorna um array com 4 horários:
    [entrada, saida_almoco, retorno_almoco, saida]
  """
  def gerar(self):
    return []


def run_cli():
  args = parser.parse_args()
  print args

