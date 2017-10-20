import glob

from argparse import ArgumentParser

class Options:
    def __init__(self):
        self._init_parser()

    def _init_parser(self):
        usage='bin/background-check'
        self.parser = ArgumentParser(usage=usage)

        self.parser.add_argument('-i'
                                '--input_file',
                                required=True,
                                dest='input_file',
                                help='Input file to read')

        # TODO Add output file argument

    def parse(self, args=None):
        return self.parser.parse_args(args)

    def help(self):
        self.parser.print_help()

