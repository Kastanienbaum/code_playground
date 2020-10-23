#!/bin/sh

# my 1st shell script 

# PJM-4stelligeNummer
constraint="^PJM-[0-9]\{4}"

echo Hello World
echo "Hello World $constraint"

if [ 1 == 2 ]; then
	echo one is one
else 
	echo not one
fi

# EOF 