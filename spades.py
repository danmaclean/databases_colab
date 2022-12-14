#!/usr/bin/env python

import subprocess
import os
import time
files = ["assembly_graph.fastg", "before_rr.fasta", "contigs.fasta", "contigs.paths",
         "dataset.info", "input_dataset.yaml", "params.txt", "scaffolds.fasta",
         "scaffolds.paths", "spades.log", "warnings.log"]

message = """
Command line: /usr/local/bin/spades.py	--only-assembler --12	/content/SRR4434292.fastq	-o	/content/test_assembly	

System information:
  SPAdes version: 3.15.5
  Python version: 3.7.12
  OS: Linux-5.10.133+-x86_64-with-debian-buster-sid

Output dir: /content/test_assembly
Mode: ONLY assembling (without read error correction)
Debug mode is turned OFF

Dataset parameters:
  Standard mode
  For multi-cell/isolate data we recommend to use '--isolate' option; for single-cell MDA data use '--sc'; for metagenomic data use '--meta'; for RNA-Seq use '--rna'.
  Reads:
    Library number: 1, library type: paired-end
      orientation: fr
      left reads: not specified
      right reads: not specified
      interlaced reads: ['/content/SRR4434292.fastq']
      single reads: not specified
      merged reads: not specified
Assembly parameters:
  k: [77]
  Repeat resolution is enabled
  Mismatch careful mode is turned OFF
  MismatchCorrector will be SKIPPED
  Coverage cutoff is turned OFF
Other parameters:
  Dir for temp files: /content/test_assembly/tmp
  Threads: 16
  Memory limit (in Gb): 12


======= SPAdes pipeline started. Log can be found here: /content/test_assembly/spades.log

/content/SRR4434292.fastq: max reads length: 301

Reads length: 301


===== Before start started. 


===== Preprocess reads started. 


===== Preprocess reads finished. 


===== Assembling started. 


===== K77 started. 
"""

print(message)

try:
    os.mkdir("test_assembly")
except FileExistsError:
    pass

for f in files:
    url = "https://raw.githubusercontent.com/danmaclean/databases_colab/main/test_assembly/" + f
    cmd = ["wget", "-q", url]
    subprocess.call(cmd)
    time.sleep(5)
    dest = "test_assembly/" + f
    os.rename(f, dest)
