# Changelog
All notable changes to the container-template project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Replace CRAN by https://packagemanager.rstudio.com/cran/__linux__/focal/2023-02-16 as package source.
- Added missing system deps ``libpoppler-glib-dev``, ``tcl-dev``
- Install ``R.utils`` enabling reading of .gz files in LAVA
- Rebuilt container ``f9438a80d50831b4b0e244d455d40d43 magma.sif``

## [1.0.0] - 2022-11-30

### Added

- MAGMA v1.09b, LAVA, ldblock (lava-partitioning) tools:
  ``7b488aad6a9e2df36502c65e7367bbee  magma.sif``
- unit-tests
- reference data
- brief documentation

