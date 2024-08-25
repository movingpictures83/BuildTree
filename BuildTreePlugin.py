import ete3
from ete3 import NCBITaxa

class BuildTreePlugin:
    def input(self, inputfile):
       self.ncbi = NCBITaxa()
       self.listofids = []
       infile = open(inputfile, 'r')
       for line in infile:
           self.listofids.append(int(line.strip()))

    def run(self):
       self.tree = self.ncbi.get_topology(self.listofids)

    def output(self, outputfile):
       unrooted = self.tree.write(format=1)
       rooted = '(' + unrooted[:len(unrooted)-1] + ');'
       outfile = open(outputfile, 'w')
       outfile.write(rooted)


