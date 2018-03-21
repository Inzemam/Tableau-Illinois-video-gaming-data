#! /usr/bin/env python
import re, sys, os

def main():
    #out_filename="VideoGamingRevenueReport_2012-2018.csv"
    out_filename="foo_2012-2018.csv"
    fd_out = open(out_filename, 'w')
    fd_out.write('"Date",')
    for year in range(2012, 2019):
        for month in range (1, 13):
            if (year== 2012 and month<9):
                continue
            elif (year==2018 and month>1):
                continue
            
            in_filename="VGRevenueReport_%d_%02d.csv" % (year, month)
            print ("in_filename: " + in_filename)
            
            fd_in = open(in_filename, 'r')
            lines = fd_in.readlines()
            fd_in.close()

            if(year==2012 and month==9):
                fd_out.write(lines[3])

            date_parts = lines[1].split()
            print("date_parts: " + str(date_parts))
            #print("fixed: " + date_parts[0] +'","' + date_parts[1]+ ',')
            print("fixed: " + date_parts[0] +',' + date_parts[1]+ ',')
            
            for i in range(4, len(lines)):
                #fd_out.write(date_parts[0] +'","' + date_parts[1]+ ',')
                fd_out.write(date_parts[0] +',' + date_parts[1]+ ',')
                fd_out.write(lines[i])


    fd_out.close()
            
                    

# Execute the main() function
if __name__ == "__main__":
   main()
