# DIAMOnD

DIAMOnD.py runs the DIAMOnD algorithm as described in
 
 A DIseAse MOdule Detection (DIAMOnD) Algorithm derived from a
 systematic analysis of connectivity patterns of disease proteins in
 the Human Interactome. PlOS Comp Bio (in press), 2015.

by Susan Dina Ghiassian, Joerg Menche & Albert-Laszlo Barabasi

The DIAMOnD website can be found at: 

Installation as a package:
<em><pre>pip install git+https://github.com/REPO4EU/DIAMOnD.git</pre></em>
This provides the command <em>diamond-module</em>, which takes the same arguments as DIAMOnD.py, and lets you <em>import DIAMOnD</em> in Python.

Instruction to use the source code:
1. Download the code.
2. Make sure you are in the main directory where the code is.
3. Run the following.</br>
 <em><pre>python3 DIAMOnD.py  network_file seed_file  n  alpha(optional)  outfile_name(optional)</pre></em>

# -------------------

Directory Example

contains two input files:
1. seed_genes.txt (list of genes associated with a phenotype of interest) 
2. PPI.txt (Protein-protein interaction network. note that gene IDs should be consistent in the two input files)</br>
The following command will generate the first 100 DIAMOnD nodes and save them in a file) </br>
<em><pre>python3  DIAMOnD.py  Example/PPI.txt  Example/seed_genes.txt  100</pre></em>


