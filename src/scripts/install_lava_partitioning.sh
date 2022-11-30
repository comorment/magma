# the original software is https://github.com/cadeleeuw/lava-partitioning
# ofrei fork is a minor change in the makefile 
git clone https://github.com/ofrei/lava-partitioning.git && cd lava-partitioning && git reset --hard baa96da73b2ce3e58bbb02c13fc645245a712f88
make
cp ldblock /bin

