# Container `magma.sif`

This container includes [MAGMA](https://ctg.cncr.nl/software/magma) and [LAVA](https://ctg.cncr.nl/software/lava) software packages.

For LAVA, the example data is  (``https://github.com/josefin-werme/LAVA/tree/main/vignettes``) is availabel within ``$COMORMENT/magma/reference/example/lava`` folder. The folder also has a README file explaining how to trigger this analysis.
The ``ldblock`` tool (https://github.com/cadeleeuw/lava-partitioning) is also included in ``magma.sif`` container.

## Getting Started

* Download ``magma.sif`` from [here](https://github.com/comorment/magma/tree/main/containers)
* Import these files to your secure HPC environment
* Run ``singularity exec --no-home magma.sif R --help``, to validate that you can run singularity. This command is expected to produce the standard R help message, starting like this:

```
Usage: R [options] [< infile] [> outfile]
   or: R CMD command [arguments]

Start R, a system for statistical computation and graphics, with the  
specified options, or invoke an R tool via the 'R CMD' interface.
...
```

