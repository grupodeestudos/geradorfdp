# encoding: utf-8
from setuptools import setup
import os
import sys

setup(
  name='geradorfdp',
  version='0.1',
  url="https://github.com/daltonmatos/geradorfdp",
  license="GPLv2",
  description='Gerador de horários para Folha de Ponto',
  author="Dalton Barreto",
  author_email="daltonmatos@gmail.com",
  packages=['geradorfdp'],
  scripts=['scripts/fdp-gen'],
  install_requires = ['argparse'],
  classifiers = [
    "License :: OSI Approved :: GNU General Public License (GPL)",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    ])

