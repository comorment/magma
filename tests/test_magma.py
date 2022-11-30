# encoding: utf-8

"""
Test module for ``magma.sif`` singularity build 
or ``magma`` dockerfile build

In case ``singularity`` is unavailable, the test function(s) should fall 
back to ``docker``.
"""

import os
import socket
import subprocess


# port used by tests
sock = socket.socket()
sock.bind(('', 0))
port = sock.getsockname()[1]


def define_prefixes(cwd):
    # Check that (1) singularity exist, and (2) if not, check for docker. 
    # If neither are found, tests will not run.
    try:
        pth = os.path.join('containers', 'magma.sif')
        out = subprocess.run('singularity')
        PREFIX = f'singularity run {pth}'
        PREFIX_MOUNT = PREFIX_MOUNT = f'singularity run --home={cwd}:/home/ {pth}'
    except FileNotFoundError:    
        try:
            out = subprocess.run('docker')
            PREFIX = f'docker run -p {port}:{port} magma'
            PREFIX_MOUNT = (f'docker run -p {port}:{port} ' + 
                f'--mount type=bind,source={pwd},target={pwd} magma')
        except FileNotFoundError:
            raise FileNotFoundError('Neither `singularity` nor `docker` found in PATH. Can not run tests!')
    return PREFIX, PREFIX_MOUNT


PREFIX, PREFIX_MOUNT = define_prefixes(os.getcwd())


def subprocess_run(call):
    return subprocess.run(filter(None, ' '.join(call.split('\\')).replace('\n', '').split(' ')))


def test_assert():
    """dummy test that should pass"""
    assert True


def test_R():
    """test that the R installation works"""
    call = f'{PREFIX} R --version'
    out = subprocess_run(call)
    assert out.returncode == 0


def test_R_script():
    pwd = os.getcwd() if PREFIX.rfind('docker') >= 0 else '.'
    call = f'''{PREFIX_MOUNT} R {pwd}/tests/extras/hello.R'''
    out = subprocess_run(call)
    assert out.returncode == 0


# py.test tests/test_magma.py  -k test_magma_binary
def test_magma_binary():
    call=f'{PREFIX} magma --version'
    out = subprocess_run(call)
    assert out.returncode == 0


# py.test tests/test_magma.py  -k test_LAVA
def test_LAVA():
    pwd = os.getcwd()
    PREFIX, PREFIX_MOUNT = define_prefixes(os.path.join(os.getcwd(), 'reference/examples/lava'))
    cmd = 'Rscript lava_script.R "vignettes/data/g1000_test" "vignettes/data/test.loci.unittest" "vignettes/data/input.info.txt" "vignettes/data/sample.overlap.txt" "depression;bmi" "depression.bmi"'
    call=f'{PREFIX_MOUNT} {cmd}'
    out = subprocess_run(call)
    assert out.returncode == 0


# py.test tests/test_magma.py  -k test_ldblock
def test_ldblock():
    out_file = f'ldblock.breaks'
    if os.path.exists(out_file): os.remove(out_file)
    call=f'{PREFIX_MOUNT} ldblock reference/examples/lava-partitioning/g1000_test_chr19'
    out = subprocess_run(call)
    assert out.returncode == 0
    assert os.path.exists(out_file)

