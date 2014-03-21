VFDB
====

This repository provides the sequences relating to virulence factors and 
regions of interest used in the publication "Global dissemination of a 
multidrug resistant Escherichia coli clone"::

    PETTY NK*, BEN ZAKOUR NL*, STANTON-COOK M, SKIPPINGTON E, TOTSIKA M, FORDE BM,
    PHAN MD, MORIEL D, PETERS KM, DAVIES MR, ROGERS BA, DOUGAN G, RODRIGUEZ-BAÑO J,
    PASCUAL A, PITOUT JDD, UPTON M, PATERSON DL, WALSH TR, SCHEMBRI MA^, BEATSON
    SA^. Global dissemination of a multidrug resistant Escherichia coli clone. 
    Proc Natl Acad Sci USA (in press). 
    
    ^CORRESPONDING AUTHORS *AUTHORS CONTRIBUTED EQUALLY

In addition, please see the repository providing draft assemblies for 
`99 Escherichia coli strain of sequence type 131`_.

These sequences, the assemblies and the tool `SeqFindR`_ were used to generate 
Figures 3, S4 and S6 in the publication above. The sequences here are formatted 
in the `SeqFindR`_ database format.


Databases used in Global dissemination of a multidrug resistant Escherichia coli clone
--------------------------------------------------------------------------------------

The following explains how the databases map to the figures:

=========== =========================
Figure      SeqFindR Database
=========== =========================
Figure 3    Islands_200bp_chunks.fa
Figure S4   plasmid_replicons.fa
Figure S6   Schembri_VFDB.fa  
=========== =========================


Islands_200bp_chunks.fa
~~~~~~~~~~~~~~~~~~~~~~~

The sequences are from `Dataset S1 of Totsika et al`_, Insights into a 
Multidrug Resistant Escherichia coli Pathogen of the Globally Disseminated 
ST131 Lineage: Genome Analysis and Virulence Mechanisms, 
DOI:10.1371/journal.pone.0026578. We chunked each element into 200 bp 
subsequences to maintain scale and also to consider our draft Illumina 
assemblies. 

plasmid_replicons.fa
~~~~~~~~~~~~~~~~~~~~

Sequences of 19 plasmid replicon types.

Schembri_VFDB.fa
~~~~~~~~~~~~~~~~

Is a concatenation of the following sub_databases: Autotransporters.fa (42), 
CU_fimbriae.fa (38), Iron_uptake.fa (15), Other_virulence_genes.fa (30), 
Toxins.fa (4) and UPEC_specific_genes.fa (125).

A CSV formatted file providing detailed information for each sequence is 
`available here`_.


Additional databases
--------------------

**Colicins_and_microcins.fa:** Sequences for 21 representative Colicins and 
Microcins.

**ST131_publishedPlasmids.fa and ST131_publishedPlasmids_500bp_chunked.fa:**
7 published plasmids found associated with ST131 genomes. These were 
chunked into 500 bp subsequences.

**ST131_AllPlasmids.fa and ST131_AllPlasmids_500bp_chunked.fa:** As above but
includes pEC958.

**fimB.fa:** Wild type *fimB* and *fimB* insertion. 

**CTX-M.fa** 122 CTX-M-* genes extracted from on `Lahey Hospital and Medical
Centre database`_ on the 07/08/2013.

**Antibiotics.fa and Antibiotics_EC958_CTX-M-15.fa:** 30 short 70'mers to 
screen antibiotic profiles. In Antibiotics_EC958_CTX-M-15.fa we have switched 
out 70-ctx143, bla-CTX-M-1 for EC958_CTX-M-15.


Scripts
-------

We provide chunk_mfa.py which was used to chunk Island elements into 200 bp
subsequences.

chunk_mfa.py is used like this::

    $ python chunk_mfa.py input.fa 200 > outname.fa
    # 
    # where:
    #   * input.fa is 1 or more fasta formatted sequences  
    #   * 200 can be any integer. This will be your sub sequence length
    #   * outname.fa is the name you want your final output to be.


.. _`99 Escherichia coli strain of sequence type 131`: https://github.com/BeatsonLab-MicrobialGenomics/ST131_99
.. _`SeqFindR`: https://github.com/mscook/SeqFindR
.. _`Dataset S1 of Totsika et al`: http://www.plosone.org/article/fetchSingleRepresentation.action?uri=info:doi/10.1371/journal.pone.0026578.s002
.. _`available here`: https://github.com/mscook/VFDB/blob/master/VFDB_info.csv
.. _`Lahey Hospital and Medical Centre database`: http://www.lahey.org/Studies 

