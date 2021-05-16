#!/bin/sh
 # Output HTTP header
echo "Content-Type: text/html"
echo

echo "<html><body> The following number of people visited our site!<br>"

 # Read interger from text file count.dat
i=`cat count.dat`

 # i <- i + 1
i=`expr $i + 1`

 # Output i
echo "<h1>"
echo $i
echo "</h1>"

 # Write i to text file
echo $i > count.dat

echo "</body></html>"
