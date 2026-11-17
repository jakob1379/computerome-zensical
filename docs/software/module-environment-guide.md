---
title: "Module Environment Guide"
description: "Software installed on Computerome is managed using modules as described in Environment Modules Project."
tags:
  - HPC
  - Modules
  - Software
  - Anaconda
  - Perl
  - Python
  - R
  - RStudio
  - Linux
  - Commands
---

# Module Environment Guide

![Loading modules in a terminal](../assets/uploads/SS_01_aa72121716.png){ loading=lazy }

Software installed on Computerome is managed using modules as described in the [Environment Modules Project](https://modules.readthedocs.io/en/latest/module.html#module-1). Modules provide a mechanism to set/unset all environment variables related to a given package
in one UNIX shell command. Modules definitions are contained in so-called modulefiles located in several directories. The directory structure is dependent on the system you working on HPC or SPC. Modules are activated by default for users on Computerome.

## Module utilities

To help in finding tools, we have created a module `computerome_utils` with a handful of small utilities.

```console
$ module load tools computerome_utils/2.0
```

```text title="computerome_utils commands"
Module Utils Tools

moduleavail <string>
list available environment modules

moduleapropos [-i] <string>
search for string in module information

modulewhatis <string>
list module information

findintools [-i] <string>
search for string across all applications (modules, perl, anaconda, R)

findinanaconda [-i] <string>
search for string in Anaconda packages

findinperl [-i] <string>
search for string in Perl packages

findinr [-i] <string>
search for string in R packages
```

### `module avail`

To list your currently available modules, type the command below:

```console
$ module avail
```

The command will per default list something similar to this:

??? example "Output of `module avail`"

    ```console
    $ module avail
    -----------------------------------------------------------------------------------
    /cm/local/modulefiles
    -----------------------------------------------------------------------------------
    cluster-tools/8.2 cmd cmsub freeipmi/1.6.2 ipmitool/1.8.18 module-git
    ngs openldap python36 tools cm-cloud-copy/8.2 cmsh dot gcc/8.2.0
    lua/5.3.5 module-info null python2 shared
    ----------------------------------------------------------------------
    /cm/local/.modulefiles_cache/shared/modulefiles
    ----------------------------------------------------------------------
    blacs/openmpi/gcc/64/1.1patch03 cuda10.1/blas/10.1.243
    default-environment hwloc/1.11.11 openblas/dynamic(default)
    blas/gcc/64/3.8.0 cuda10.1/fft/10.1.168
    fftw2/openmpi/gcc/64/double/2.1.5 intel-tbb-oss/ia32/2019_20190410oss
    openblas/dynamic/0.2.20 bonnie++/1.97.3 cuda10.1/fft/10.1.243
    fftw2/openmpi/gcc/64/float/2.1.5 intel-tbb-oss/intel64/2019_20190410oss
    openmpi/gcc/64/1.10.7 cm-pmix3/3.1.4 cuda10.1/nsight/10.1.168
    fftw3/openmpi/gcc/64/3.3.8 iozone/3_482 openmpi/gcc/64/4.0.2
    cuda/toolkit/10.1/10.1.168 cuda10.1/nsight/10.1.243 gdb/8.2
    lapack/gcc/64/3.8.0 scalapack/openmpi/gcc/64/2.0.2
    cuda/toolkit/10.1/10.1.243 cuda10.1/profiler/10.1.168
    globalarrays/openmpi/gcc/64/5.7 mpich/ge/gcc/64/3.3 sge/2011.11p1
    cuda/toolkit/101/10.1.168 cuda10.1/profiler/10.1.243 hdf5/1.10.1
    mvapich2/gcc/64/2.3 slurm/18.08.8 cuda/toolkit/101/10.1.243
    cuda10.1/toolkit/10.1.168 hdf5_18/1.8.20 netcdf/gcc/64/4.6.1
    cuda10.1/blas/10.1.168 cuda10.1/toolkit/10.1.243 hpl/2.2 netperf/2.7.0
    ----------------------------------------------------------------------
    /cm/local/.modulefiles_cache/tools/modulefiles
    -----------------------------------------------------------------------
    454/2.9 depot_tools/20160809 intel/perflibs/2018_update2
    netphorest_human/2.1 samblaster/0.1.24 abawaca/20170520 diamond/0.7.9
    intel/perflibs/2018_update3 netsurfp/1.0b samclip/0.2
    abctoolbox/20090930 diamond/0.8.31 intel/perflibs/2018_update4
    netsurfp/1.0d samstat/1.5.1 abra2/2.20 diamond/0.9.13
    intel/perflibs/2019 nettle/3.5.1 samtools/0.1.18 abricate/0.5
    diamond/0.9.24 intel/perflibs/2019_update2 netturnp/1.0a samtools/0.1.19
    abricate/0.8.7 diginorm/20131102 intel/perflibs/2019_update3
    new_fugue/20100602 samtools/1.2 abyss/2.0.2 disco/1.0
    intel/perflibs/2019_update5 newick-utils/1.6 samtools/1.3.1 abyss/2.1.5
    discovar/52188 intel/redist/2017.2.174 nextflow/0.31.1 samtools/1.4
    activetcl/8.6.8.0 discovar/52488 intel/redist/2017_update4
    nextflow/19.03.0-edge samtools/1.4.1 AdapterRemoval/2.1.3
    discovardenovo/52488 intel/redist/2018 nextflow/19.07.0 samtools/1.5
    adapterremoval/2.1.3 discovarexp/52242 intel/redist/2018_update1
    nextflow/19.09.0-edge samtools/1.6 AdapterRemoval/2.1.7 dissect/1.2
    intel/redist/2018_update3 ngb/2.5.1.374.1 samtools/1.7
    adapterremoval/2.1.7 dlcpar/1.0 intel/redist/2018_update5 ngless/0.7.1
    samtools/1.8 AdapterRemoval/2.2.0 docker-compose/1.21.2
    intel/redist/2019 ngless/0.8.1 samtools/1.9 adapterremoval/2.2.0
    dos2unix/7.3.1 intel/redist/2019_update2 ngless/0.9.1 sas/DEPRECATED/9.4
    AdapterRemoval/2.2.1a dos2unix/7.4.0 interop/1.1.8 ngmlr/0.2.7
    satsuma/3.0 adapterremoval/2.2.1a drop-seq_tools/2.0.0
    interproscan/5.11-51.0 ngsadmix/32 savvy/1.2.0 AdapterRemoval/2.2.2
    dropest/0.8.5 interproscan/5.13-52.0 ngsqctoolkit/2.3.3 sbcl/1.3.17
    adapterremoval/2.2.2 dropest/20190401 interproscan/5.17-56.0
    ngstools/20180814 scaffold/4.9.0 AdapterRemoval/2.2.4 dssp/2.0.4
    interproscan/5.19-58.0 ngstools/20190624 scalpel/0.5.2
    adapterremoval/2.2.4 dssp/2.2.1 interproscan/5.22-61.0 nim/0.16.0
    schmutzi/1.5.5.5 admixture/1.3.0 duphold/0.1.5 interproscan/5.25-64.0
    nim/1.0.0 schmutzi/20161010 admixture/1.23 ea-utils/1.1.2-806
    interproscan/5.32-71.0 ninja/1.8.2 scipion-dev/1.1F adolc/2.5.2
    eager-gui/1.92.37 interproscan/5.36-75.0 ninja/1.9.0 scipion/1.0
    adxv/1.9.10 eagle/2.3.5 ioapi/3.1 nlopt/2.4.2 scipion/1.0.0 adxv/1.9.11
    eclipse-cpp/2018-09 iozone/3.434 nnlinplayer/1.0 scipion/1.0.1
    adxv/1.9.12 eclipse-parallel/2018-09 iperf/2.0.5 nodejs/8.9.1_LTS
    scipion/1.1 agouti/0.3.3.1-gc8bd255 edirect/7.50 iperf/3.0.11
    nodejs/9.2.0 scipion/1.2 albula/3.2.0-2 effectorp/1.0 iperf/3.1
    nodejs/10.1.0 scipion/2.0.0 ale/20130717 effectorp/2.0 ipn/0.581
    nodejs/10.16.0_LTS scratch-1d/1.1 alfred/0.1.17 eggnog-mapper/0.12.7
    iqsub/1.0 nodejs/12.6.0 screen/4.6.2 allelecount/3.2.3
    eggnog-mapper/0.99.3 iqtree/1.5.5 novocaller/20190521 scwrl/4.0
    allelecount/3.3.1 eggnog-mapper/1.0.3 iqtree/1.6.1 novocraft/3.03.02
    searchgui/2.8.5
    ```

Regular users should focus on modules located under `/cm/local/modulefiles`, in particular those highlighted above: `tools, ngs, shared and use.own`. These can be loaded using the using the command:

```console
$ module load <module name>
```

where `<module name>` can be `tools, ngs, shared, use.own` etc. You can limit the number of listed modules, by adding the first letter(s) of the modulename to the `module avail` command

??? example "Output of `module avail f`"

    ```console
    $ module avail f

    -----------------------------------------------------------------------------------
    /cm/local/modulefiles
    -----------------------------------------------------------------------------------
    freeipmi/1.6.2
    ----------------------------------------------------------------------
    /cm/local/.modulefiles_cache/shared/modulefiles
    ----------------------------------------------------------------------
    fftw2/openmpi/gcc/64/double/2.1.5 fftw2/openmpi/gcc/64/float/2.1.5
    fftw3/openmpi/gcc/64/3.3.8
    ----------------------------------------------------------------------
    /cm/local/.modulefiles_cache/tools/modulefiles
    -----------------------------------------------------------------------
    falcon/0.3.0 fastp/0.19.4 fasttree/2.1.8 fftw/3.3.6-pl1
    firebird/CS/2.5.7.27050-0 flye/2.4.2 frogs/2.0.0 falcon/20160621
    fastphylo/1.0.1 fasttree/2.1.9 fftw/3.3.6-pl2 firebird/SS/2.5.7.27050-0
    foldx/4 frustratometer/2.0 falcon_zip/20180716 fastq-tools/0.8
    fasttree/2.1.10 fftw/3.3.7 firefox/67.0 foldx/4_expires20190409
    funannotate/1.1.1 famseq/1.0.3 fastqc/0.11.2 fastuniq/1.1 fftw/3.3.8
    fithic/1.0.1 fpocket/3.1.2 funannotate/1.2.0 fasta/36.3.8e fastqc/0.11.4
    fastx_toolkit/0.0.14(default) fgbio/0.8.1 fix_assembly_errors/20180508
    fpocket/3.1.3 funannotate/1.3.2 fasta/36.3.8g fastqc/0.11.5 fchmm/1.0.0
    fgbio/1.0.0 flash/1.2.11 fraggenescan/1.30 funannotate/1.3.4 fastani/1.1
    fastqc/0.11.7 fdt/0.25 fgwas/0.3.6 flashpca/2.0
    freebayes/1.0.2-33-gdbb6160 funannotate/1.5.1 fastme/2.1.5 fastqc/0.11.8
    fdupes/1.6.1 figtree/1.4.4 fltk/1.3.3 freebayes/1.1.0-50-g61527c5
    funannotate/1.6.0 fastml/3.1 fastqtl/2.184 feh/3.1 filezilla/3.44.2
    fltk/1.3.4-2 freebayes/1.2.0-2-g29c4002 fuseq/1.1.2
    fastNGSadmix/20190716 fastsimcoal/2.6.0.3 ffmpeg/4.1.3
    find-clumpiness/0.2.3.1 fltk/1.3.5 freesasa/1.1 fusionmap/20150331
    fastp/0.12.2 faststructure/20150319 fftw/3.3.4 fineradstructure/20180529
    flye/2.3.7 freetype/2.9.1
    ```

---

### `module whatis`

To get basic information on the modulefiles, you can use `module whatis <modulefile...>`

```console
$ module whatis tools ngs gcc anaconda3/4.4.0

-----------------------------------------------------------------------------------
/cm/local/modulefiles
-----------------------------------------------------------------------------------
tools: Adds cached /services/tools modules
-----------------------------------------------------------------------------------
/cm/local/modulefiles
-----------------------------------------------------------------------------------
ngs: Adds cached NGS modules
-----------------------------------------------------------------------------------
/cm/local/modulefiles
-----------------------------------------------------------------------------------
gcc/8.2.0: adds GNU Cross Compilers to your environment variables
----------------------------------------------------------------------
/cm/local/.modulefiles_cache/tools/modulefiles
-----------------------------------------------------------------------
gcc/4.9.4: GCC 4.9.4 - GNU Compiler Collection gcc/5.4.0: GCC 5.4.0 -
GNU Compiler Collection gcc/6.2.0: GCC 6.2.0 - GNU Compiler Collection
gcc/7.2.0: GCC 7.2.0 - GNU Compiler Collection gcc/8.2.0: GCC 8.2.0 -
GNU Compiler Collection
----------------------------------------------------------------------
/cm/local/.modulefiles_cache/tools/modulefiles
-----------------------------------------------------------------------
anaconda3/4.4.0: Anaconda3 4.4.0 - Python 3 distribution for scientific
computing
```

### `module apropos`

To search for a particular string in the basic information on the modulefiles, you can use `module apropos [string]`. This is the only module sub-command which currently does for case insensitive module parameter evaluation.

??? example "Output of `module apropos genome`"

    ```console
    $ module apropos genome

    ----------------------------------------------------------------------
    /cm/local/.modulefiles_cache/tools/modulefiles
    -----------------------------------------------------------------------
    agouti/0.3.3.1-gc8bd255: AGOUTI 0.3.3.1-gc8bd255 - Annotated Genome
    Optimization Using Transcriptome Information allpathslg/52415:
    ALLPATHS-LG 52415 - short read genome assembler allpathslg/52488:
    ALLPATHS-LG 52488 - short read genome assembler anicalculator/1:
    ANIcalculator 1 - compute gANI,AF values between two genomes arcs/1.0.0:
    ARCS 1.0.0 - Scaffolding genome sequence assemblies using 10X Genomics
    GemCode/Chromium data arcs/1.1.0: ARCS 1.1.0 - Scaffold genome sequence
    assemblies using 10x Genomics data argweaver/20150629: ARGweaver
    20150629 - Sampling and manipulating genome-wide ancestral recombination
    graphs ascatngs/4.2.1: ascatNgs 4.2.1 - Somatic copy number analysis
    using paired end wholegenome sequencing baypass/2.1: BayPass 2.1 -
    Genome-Wide Scan for Adaptive Differentiation and Association Analysis
    with population-specific covariables bedops/2.4.14: BEDOPS 2.4.14 -
    fast, highly scalable and easily-parallelizable genome analysis toolkit
    bedops/2.4.35: BEDOPS 2.4.35 - fast, highly scalable and
    easily-parallelizable genome analysis toolkit bedtools/2.22.1: bedtools
    2.22.1 - powerful toolset for genome arithmetic bedtools/2.26.0:
    bedtools 2.26.0 - powerful toolset for genome arithmetic
    bedtools/2.27.1: bedtools 2.27.1 - powerful toolset for genome
    arithmetic bedtools/2.28.0: bedtools 2.28.0 - powerful toolset for
    genome arithmetic bmagwa/1.0: BMAGWA 1.0 - Bayesian Model Averaging in
    Genome-wide Association Studies bmagwa/2.0-20121210: BMAGWA
    2.0-20121210 - Bayesian Model Averaging in Genome-wide Association
    Studies bpga/1.3: BPGA 1.3 - tool for ultra-fast pan-genome analysis of
    microbes brat_ng/20150505: BRAT NextGen 20150505 - Bayesian analysis of
    recombinations in whole-genome DNA sequence data
    breakdancer/1.1_2011_02_21: BreakDancer 1.1_2011_02_21 - Perl/Cpp
    package that provides genome-wide detection of structural variants from
    next generation paired-end sequencing reads busco/3.0.1_20170529: BUSCO
    3.0.1_20170529 - Assessing genome assembly and annotation completeness
    with Benchmarking Universal Single-Copy Orthologs busco/3.0.2b_20170717:
    BUSCO 3.0.2b_20170717 - Assessing genome assembly and annotation
    completeness with Benchmarking Universal Single-Copy Orthologs
    bwa/0.6.1: BWA 0.6.1 - Burrows-Wheeler Aligner, mapping low-divergent
    sequences against a large reference genome bwa/0.7.6a-r433: BWA
    ExaScience 0.7.6a-r433 - Burrows-Wheeler Aligner (ExaScience fork),
    mapping low-divergent sequences against a large reference genome
    bwa/0.7.10: BWA 0.7.10 - Burrows-Wheeler Aligner, mapping low-divergent
    sequences against a large reference genome bwa/0.7.12: BWA 0.7.12 -
    Burrows-Wheeler Aligner, mapping low-divergent sequences against a large
    reference genome bwa/0.7.15: BWA 0.7.15 - Burrows-Wheeler Aligner,
    mapping low-divergent sequences against a large reference genome
    bwa/0.7.16a: BWA 0.7.16a - Burrows-Wheeler Aligner, mapping
    low-divergent sequences against a large reference genome cbrc_last/861:
    CBRC LAST 861 - Genome-Scale Sequence Comparison cbrc_last/963: CBRC
    LAST 963 - Genome-Scale Sequence Comparison cdsgff2seq/20070813:
    cdsgff2seq 20070813 - read GFF, genome fasta; write CDS sequence, aa
    translation (with check for exon phase). write gene/exon offset
    subranges clonalframeml/20170927: ClonalFrameML 20170927 - Efficient
    Inference of Recombination in Whole Bacterial Genomes codingquarry/2.0:
    CodingQuarry 2.0 - highly accurate hidden Markov model gene prediction
    in fungal genomes using RNA-seq transcripts control-freec/11.5:
    Control-FREEC 11.5 - Copy number and genotype annotation in whole genome
    and whole exome sequencing data cortex_var/1.0.5.21: cortex_var
    1.0.5.21 - genome assembly and variation analysis from sequence data
    das_tool/1.0: DAS_Tool 1.0 - Tool for genome-resolved metagenomics
    das_tool/1.1.1: DAS_Tool 1.1.1 - Tool for genome-resolved metagenomics
    disco/1.0: Disco 1.0 - Multi-threaded Distributed Memory
    Overlap-Layout-Consensus (OLC) Metagenome Assembler discovar/52188:
    DISCOVAR 52188 - assemble genomes and find variants discovar/52488:
    DISCOVAR 52488 - assemble genomes and find variants
    discovardenovo/52488: DISCOVAR de novo 52488 - assemble genomes and find
    variants discovarexp/52242: DISCOVAR de novo - assemble genomes and find
    variants dissect/1.2: DISSECT 1.2 - massive genome analysis tool
    eggnog-mapper/0.12.7: EggNOG-mapper 0.12.7 - Fast genome-wide functional
    annotation through orthology assignment eggnog-mapper/0.99.3:
    EggNOG-mapper 0.99.3 - Fast genome-wide functional annotation through
    orthology assignment eggnog-mapper/1.0.3: EggNOG-mapper 1.0.3 - Fast
    genome-wide functional annotation through orthology assignment
    eggnog-mapper/20170307: EggNOG-mapper 20170307 - Fast genome-wide
    functional annotation through orthology assignment
    estimate_genome_size.pl/0.05: estimate_genome_size.pl 0.05 - Scripts to
    estimate genome size and coverage from kmer distribution generated by
    jellyfish
    ```

Example using `module apropos`

```text
$ module apropos netMHC
----------------------------------------------------------------------
/cm/local/.modulefiles_cache/tools/modulefiles
-----------------------------------------------------------------------
netmhc/3.0c: NetMHC 3.0c - Prediction of peptide-MHC class I binding
using artificial neural networks (ANNs) netmhc/3.4a: NetMHC 3.4a -
Prediction of peptide-MHC class I binding using artificial neural
networks (ANNs) netmhc/4.0a: NetMHC 4.0a - Prediction of peptide-MHC
class I binding using artificial neural networks (ANNs) netmhcii/2.3:
NetMHCII 2.3 - predicts binding of peptides to HLA-DR, HLA-DQ, HLA-DP
and mouse MHC class II alleles netmhciipan/3.1a: NetMHCIIpan 3.1a -
predicts binding of peptides to MHC class II molecules netmhciipan/3.2:
NetMHCIIpan 3.2 - predicts binding of peptides to MHC class II molecules
netmhcpan/2.8a: NetMHCpan 2.8a - Prediction of peptide-MHC class I
binding using artificial neural networks (ANNs) netmhcpan/3.0a:
NetMHCpan 3.0a - Prediction of peptide-MHC class I binding using
artificial neural networks (ANNs) netmhcpan/4.0a: NetMHCpan 4.0a -
Prediction of peptide-MHC class I binding using artificial neural
networks (ANNs) $ module load netmhciipan/3.1a
```

### `module display`

Further information about specific modules is available with `module display [modulefile...]`

This command will also list `conflict` (modules which conflict with this) and `prereq` (modules which must be loaded to use this).

```console
$ module display RepeatMasker/4.0.6

-------------------------------------------------------------------
/cm/local/.modulefiles_cache/tools/modulefiles/RepeatMasker/4.0.6:
module-whatis {RepeatMasker 4.0.6 - screens DNA sequences for
interspersed repeats and low complexity DNA sequences} conflict
RepeatMasker prereq perl prereq trf prereq ncbi-rmblastn hmmer
prepend-path PATH /services/tools/RepeatMasker/4.0.6/util prepend-path
PATH /services/tools/RepeatMasker/4.0.6 prepend-path PERL5LIB
/services/tools/RepeatMasker/4.0.6 setenv REPEATMASKER
/services/tools/RepeatMasker/4.0.6 RepeatMasker is a program that
screens DNA sequences for interspersed repeats and low complexity DNA
sequences. The output of the program is a detailed annotation of the
repeats that are present in the query sequence as well as a modified
version of the query sequence in which all the annotated repeats have
been masked (default: replaced by Ns). Currently over 56% of human
genomic sequence is identified and masked by the program. Sequence
comparisons in RepeatMasker are performed by one of several popular
search engines including nhmmer, cross_match, ABBlast/WUBlast, RMBlast
and Decypher. RepeatMasker makes use of curated libraries of repeats and
currently supports Dfam ( profile HMM library derived from Repbase
sequences ) and Repbase, a service of the Genetic Information Research
Institute.
-------------------------------------------------------------------
```

### `module load`

To add one or more modules, use `module load [modulefile...]`. Modules listed without version information (like tools) reference a new set of modulefiles, so if you for instance load `tools` and `ngs` modules, you will get access to a massive list of extra modulefiles

```console
$ module load tools ngs
$ module avail ...ignoring parts of listing for readability...

---------------------------------------------------
/cm/local/.modulefiles_cache/modulefiles
---------------------------------------------------- anaconda3/2.1.0
hdf5/1.10.0 plink2/1.90beta3 anaconda3/2.2.0 hdf5/1.8.15p1 plumed/2.2.1
anaconda3/4.4.0 hisat2/2.0.1-beta polysolver/1.0 anaconda3/2.1.0
hkl2map/0.3.i-beta poppler/0.45.0 anaconda3/2.2.0 hlaminer/1.3
pplacer/1.1.alpha17 anaconda3/4.4.0 hlareporter/1.0.3 prank/140603
anarci/1.0 hla-vbseq/20150729 preseq/1.0.2 annovar/2015jun17 hmmer/2.3.2
price/1.2 ansys/16.2 hmmer/3.1b2 prinseq-lite/0.20.4 ansys/17.0
htslib/1.2.1 prodigal/2.6.2 ansys/17.1 htslib/1.3.1
progressivecactus/20160427 apache-maven/3.3.3 idba/1.1.1(default)
prokka/1.11 ...long listing left out...
-------------------------------------------------
/cm/local/.modulefiles_cache/ngs/modulefiles
-------------------------------------------------- bcl2fastq/2.17.1.14
ncbi-blast/2.2.26 SPAdes/3.7.0 bedtools/2.22.1(default)
ncbi-blast/2.2.30+ SPAdes/3.8.0 bwa/0.7.10(default) ncbi-blast/2.2.31+
sratoolkit/2.4.5-2 circos/0.64 ncbi-tools/current(default)
sratoolkit/2.5.7 circos/0.67-7(default) netmhciipan/3.1a
srnaworkbench/4.0-alpha circos-tools/0.21 netmhcpan/2.8a
srnaworkbench/4.1-alpha cope/1.2.5 netsurfp/1.0b ssake/3.8.3
cufflinks/2.2.1 ngsqctoolkit/2.3.3 tabix/0.2.6 ensembl-tools/78(default)
PBSuite/15.2.20 tabix/1.2.1(default) express/1.5.1 pear/0.9.6 trf/4.07b
...long listing left out...
```

Modules listed with version information (like gcc/4.8.2) reference a particular version of a tool. Generally, it is recommended to always include the version when loading a tool; if you do not specify version, the (default) will be loaded if any is available - otherwise the command will print an error.

```console
$ module load gcc
$ which gcc /cm/shared/apps/gcc/4.8.2/bin/gcc $ module load
anaconda3/2.1.0 $ which python /services/tools/anaconda-2.1.0/bin/python
```

`modules load` will report any **conflict** and missing **prereq**

```console
$ module load
RepeatMasker/4.0.6 RepeatMasker/4.0.6(37):ERROR:151: Module
'RepeatMasker/4.0.6' depends on one of the module(s) 'perl/5.8.9
perl/5.20.2 perl/5.20.1' RepeatMasker/4.0.6(37):ERROR:102: Tcl command
execution failed: prereq perl
```

If you get such a message, you can use module display command for further information.

```console
$ module display
RepeatMasker/4.0.6
-------------------------------------------------------------------
/services/tools/modulefiles/RepeatMasker/4.0.6: module-whatis
RepeatMasker 4.0.6 - screens DNA sequences for interspersed repeats and
low complexity DNA sequences conflict RepeatMasker prereq perl prereq
trf prereq ncbi-rmblastn prepend-path PATH
/services/tools/RepeatMasker/4.0.6 prepend-path PERL5LIB
/services/tools/RepeatMasker/4.0.6
-------------------------------------------------------------------
```

### `module list`

This command will verify which modules are loaded

```console
$ module list

Currently Loaded Modulefiles:
1) gcc/4.8.2
2) tools
3) ngs
4) anaconda3/2.1.0
```

### `module switch`

To switch loaded `modulefile1` with `modulefile2`, use `switch[modulefile1] modulefile2`. If `modulefile1` is not specified, then it is assumed to be the currently loaded module with the same root name as `modulefile2`

```console
$ module list

Currently Loaded Modulefiles:
1) gcc/4.8.2
2) tools
3) ngs
4) anaconda3/2.1.0

$ module switch
anaconda3/2.1.0 anaconda3/4.4.0

$ module list
Currently Loaded Modulefiles:
1) gcc/4.8.2
2) tools
3) ngs
4) anaconda3/4.4.0
```

### `module unload`

To remove one or more modules, use `module unload [modulefile...]`

```console
$ module list
Currently Loaded Modulefiles: 1) gcc/4.8.2 2) tools 3) ngs 4)
perl/5.20.2
$ module unload perl ngs
$ module list
Currently Loaded Modulefiles: 1) gcc/4.8.2 2) tools
```

### `module purge`

In case all modules need to be unloaded at once use this commmand

```console
$ module purge
$ module list
No Modulefiles Currently Loaded.
```

## Requesting software
To request installation of new software (or other version of existing
software), please send a mail from your department mail to [Computerome
support](mailto:computerome@dtu.dk) - preferably including a descriptive subject line (Software Request), including the tool name, and information on where the requested software can be obtained (homepage, download information, etc.):

## User installed software
Individual users can also install own software in their `Project` (for
sharing inside the project) or `HOME` (for strictly personal use)
directories. This is only recommended for software that is actively being developed or maintained at Computerome. Regular software should preferably be available through the standard modules structure.
