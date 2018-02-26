#! /usr/bin/env python
import re, sys, os

def main():
    file_num=4
    for year in range(2013, 2019):
        for month in range (1, 13):
            #src_file="VGRevenueReport_%d_%02d.cvs" % (year, month)
            src_file="VGRevenueReport\ \(%d\).cvs" % (file_num)
            dest_file="VGRevenueReport_%d_%02d.csv" % (year, month)
            mv_cmd="mv %s %s" % (src_file, dest_file)
            print (mv_cmd)
            #os.system(mv_cmd)
            file_num += 1
            if(file_num>64):
                break

# Execute the main() function
if __name__ == "__main__":
   main()
