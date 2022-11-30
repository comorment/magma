# R container
FROM rocker/verse:4.0.5

ENV TZ=Europe
ENV DEBIAN_FRONTEND noninteractive

# Essential tools
WORKDIR /tmp
COPY /scripts/apt_get_essential.sh .
RUN bash apt_get_essential.sh && \
    rm apt_get_essential.sh

# deps for R packages
RUN apt-get update -y && apt-get install -y --no-install-recommends \
    libperl-dev=5.30.0-9ubuntu0.3 \
    libgslcblas0=2.5+dfsg-6build1 \
    lmodern=2.004.5-6 \
    texlive-latex-extra=2019.202000218-1 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# lava_partitioning
WORKDIR /tools/
COPY /scripts/install_lava_partitioning.sh /tmp
RUN chmod +x /tmp/install_lava_partitioning.sh
RUN bash /tmp/install_lava_partitioning.sh

# magma
WORKDIR /tools/magma
COPY /scripts/install_magma.sh /tmp
RUN chmod +x /tmp/install_magma.sh
RUN bash /tmp/install_magma.sh

# R packages.
# CRAN packages
WORKDIR /tmp/
RUN R -e "install.packages('devtools', version='2.4.5', repos='https://cloud.r-project.org', dependencies=TRUE)"
COPY /scripts/R/cran.R .
RUN Rscript cran.R

# Misc. packages
COPY /scripts/R/misc.R .
RUN Rscript misc.R

# GitHub distributed packages:
COPY /scripts/R/github.R .
RUN Rscript github.R


WORKDIR /tools
