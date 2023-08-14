import os, sys
import argparse
import configparser
from photoshopy import Photoshopy
from compilado_feed import CompiladoFeed
from compilado_formatter import CompiladoFormatter
import logging

class CompiladoCLI:
    CLI_VERSION = "Compilado CLI 1.0.0"
    INI_FILE = "compilado.ini"

    def __load_ini_file(self. filename)
        config = configparser.ConfigParser()
        config.read(filename)
        return config
    