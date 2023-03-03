require(devtools)
url <- "https://packagemanager.rstudio.com/cran/__linux__/focal/2023-02-16"
dependencies <- c('Depends', 'Imports', 'LinkingTo')
upgrade <- 'default'
devtools::install_version('BiocManager', version='1.30.19', repos=url, dependencies=dependencies, upgrade=upgrade)
devtools::install_version('BRugs', version='0.9-1', repos=url, dependencies=dependencies, upgrade=upgrade)
devtools::install_version('data.table', version='1.14.6', repos=url, dependencies=dependencies, upgrade=upgrade)
devtools::install_version('matrixsampling', version='2.0.0', repos=url, dependencies=dependencies, upgrade=upgrade)
devtools::install_version('R.utils', version='2.12.2', repos=url, dependencies=dependencies, upgrade=upgrade)

