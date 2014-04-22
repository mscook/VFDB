Sequences used in fimH-parC-gyrA typing
=======================================

The following sequences were used to perform the fimH-parC-gyrA typing. We used
mlstBLAST_ to perform the typing.


fimH.fa
-------

The 7 alleles came from::

    Paul et al.
    J Bacteriol. Jan 2013; 195(2): 231–242.
    doi: 10.1128/JB.01524-12

These are a 489-bp segment (referred to as the fimH typing region [fimHTR])

**fimH22:** gb|GQ487041.1|:21-509 Escherichia coli strain HSL030 minor component of type 1 fimbriae (fimH) gene, partial cds
**fimH27:** gb|U00096.2|:4546894-4547382 Escherichia coli str. K-12 substr. MG1655, complete genome
**fimH30:** gb|CP002797.2|:4712714-4713202 Escherichia coli NA114, complete genome
**fimH31:** gb|FJ865843.1|:64-552 Escherichia coli strain TOP1002 type 1 fimbrial adhesin (fimH) gene, partial cds
**fimH35:** gb|CP000802.1|:4553879-4554367 Escherichia coli HS, complete genome
**fimH41:** gi|281177210:4641973-4642461 Escherichia coli SE15 DNA, complete genome
**fimH94:** gb|FJ865709.1|:64-552 Escherichia coli strain TOP578 type 1 fimbrial adhesin (fimH) gene, partial cds


parC.fa
-------

The 10 alleles were described in::

    Johnson et al.
    J Infect Dis. 2013 Mar 15;207(6):919-28. 
    doi: 10.1093/infdis/jis933.

The changes in the parC allele followed::

    parC allele,54,87,94,105,129,238,239,240,251,261,321,348,372,387,391,399,408,411,432,471
    1    ,c,t,c,t,c,a,g,t,a,c,c,g,g,c,c,g,g,g,g,g
    1a   ,-,-,-,-,-,-,-,-,-,-,g,-,-,-,-,-,-,-,-,-
    1b   ,-,-,-,-,-,-,-,-,-,-,t,-,-,-,-,-,-,-,-,-
    1aAB ,-,-,-,-,-,-,t,-,t,-,g,-,-,-,-,-,-,-,-,-
    1aABC,-,-,t,-,-,-,t,-,t,-,g,-,-,-,-,-,-,-,-,-
    1D   ,-,-,-,-,-,c,-,-,-,-,-,-,-,-,-,-,-,-,-,-
    2    ,-,-,-,-,g,-,-,-,-,-,t,-,-,-,-,-,-,-,c,a
    3A   ,-,-,-,-,-,-,t,-,-,-,t,-,t,t,t,a,t,a,-,-
    4A   ,t,c,-,-,-,-,t,c,-,-,-,-,-,-,-,-,-,-,a,a
    5    ,t,c,-,c,-,-,-,-,-,t,-,a,-,-,-,-,-,-,-,-


gyrA.fa
-------

The 7 alleles were described in::

    Johnson et al.
    J Infect Dis. 2013 Mar 15;207(6):919-28. 
    doi: 10.1093/infdis/jis933.

The changes in the gyrA allele followed::

    gyrA allele,248,259,260,516
    1  ,c,g,a,t
    1a ,-,-,-,c
    1A ,t,-,-,-
    1AB,t,a,-,-
    1AC,t,-,g,-
    1B ,-,a,-,-
    1AD,t,t,-,-


Scripts
-------

The script **build_alleles.py** was used to build the multifasta allele
sequences from the tabular formats above.

Example usage::
    
    python build_alleles.py gyrA



.. _mlstBLAST: http://sourceforge.net/projects/srst/files/mlstBLAST

