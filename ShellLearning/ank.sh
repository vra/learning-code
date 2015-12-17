#!/bin/sh

del_file()
{
	echo "*** CTRL-C Traps Occurs (delete temporary files)***"
	rm -f /tmp/input0.$$
	exit 1
}

Take_input1()
{
	recno=0
	clear
	echo "Appointment Note keeper Application for Linux"
	echo -n "Please input your database file name:"
	read filename

	if [ ! -f $filename ];then
		echo "Sorry, $filename does not exist.Creating $filename database"
		echo "Appointment Note keeper Application database " > $filename

	fi	

	echo "Data entry start date: `date`" > /tmp/input0.$$

	while :
	do 
		echo -n "Appointment Title:"		
		read na

		echo -n "Time:"
		read ti

		echo -n "Any Remark:"
		read remark

		echo -n "Is data okay (y/n)? "
		read ans

		if [ $ans = y -o $ans = Y ];then
			recno=`expr $recno + 1`
			echo "$recno. $na $ti $remark" >> /tmp/input0.$$
		fi
		
		echo -n "Add next Appointment (y/n)? "
		read isnext
		
		if [ $isnext = n -o $isnext = N ];then
			cat /tmp/input0.$$ >> $filename
			rm -f /tmp/input0.$$
			return 
		fi

	done #end while loop
}


trap del_file 2
Take_input1
