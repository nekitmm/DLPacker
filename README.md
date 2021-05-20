<br/>
<h1 align="center">DLPacker</h1>
<br/>

<br/>

This repo contains the code from DLPacker paper [DLPacker: Deep Learning for Prediction of Amino Acid Side Chain Conformations in Proteins](pending).
<br/>
<p align="center">
    <img width="70%" src="https://github.com/nekitmm/DLPacker/blob/main/img5.png" alt="Side chain restroration example">
</p>
<br/>

		from dlpacker import DLPacker
		dlp = DLPacker('my_structure.pdb')
		dlp.reconstruct_protein(order = 'sequence', output_filename = 'my_structure_repacked.pdb')

**Key dependencies:**
* Tensorflow 2.x
* biopython
* pickle5

<center>

|AA Name | SCWRL4 | Rosetta Packer | DLPacker|
|:------:|:------:|:--------------:|:-------:|
|  Arg   |  2.07  |      1.84      |   1.44  |
|  Lys   |  1.54  |      1.40      |   1.21  |
|  Phe   |  0.67  |      0.53      |   0.32  |
|  Tyr   |  0.83  |      0.68      |   0.38  |
|  Trp   |  1.27  |      0.96      |   0.46  |
|  His   |  1.18  |      1.05      |   0.81  |
|  Glu   |  1.34  |      1.26      |   1.02  |
|  Gln   |  1.43  |      1.24      |   1.09  |
|  Met   |  1.08  |      0.91      |   0.76  |
|  Asn   |  0.88  |      0.80      |   0.65  |
|  Asp   |  0.68  |      0.65      |   0.47  |
|  Ser   |  0.59  |      0.52      |   0.36  |
|  Leu   |  0.49  |      0.45      |   0.36  |
|  Thr   |  0.36  |      0.33      |   0.27  |
|  Ile   |  0.40  |      0.36      |   0.31  |
|  Cys   |  0.40  |      0.30      |   0.24  |
|  Val   |  0.24  |      0.23      |   0.19  |
|  Pro   |  0.21  |      0.19      |   0.14  |

</center>