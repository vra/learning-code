#!/bin/sh
#
#test the use of md5sum 
#

#will ouput ani.sh's md5 and ani.sh
md5sum ani.sh

md5sum ani.sh > ani.sh.md5

#-c is used to check whether the file contains right md5sum value for the file
md5sum -c ani.sh.md5

