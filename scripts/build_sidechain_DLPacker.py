#! /usr/bin/env python

from pathlib import Path
from DLPacker.dlpacker import DLPacker
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument('-i','--pdb', type=str, help="Input PDB file")
parser.add_argument('--out', '-o', type=str, default=None, help="Output PDB file")
args = parser.parse_args()

# Output file
outfile = f"{Path(args.pdb).stem}_dlpck.pdb" if args.out is None else args.out

# DLPacker
dlp = DLPacker(args.pdb)
dlp.reconstruct_protein(order='sequence', output_filename=outfile)
