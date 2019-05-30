output_dir=OutputTB/$1
rm -rf $output_dir
mkdir -p $output_dir
export counter=0
for (( Ntest = 0; Ntest < 10; Ntest++ )); do
	for NCores in 2 4 6; do
	    for j in MESI MSI MI
    	do
    	#statements
		PROTOCOL=$1_$j-
		CORES=$NCores\_test-
		echo "$CORES"
		TEST=$Ntest.txt
		TXT=$PROTOCOL$CORES$TEST
		echo "$TXT"
		VCD=$1_$j-$NCores\_test-$Ntest.vcd
		echo "$VCD"
		PART=$j$NCores
    	CONSTANT=Config
    	CONF=$PART$CONSTANT
    	echo "$CONF"
    	echo "./emulator-freechips.rocketchip.system-$CONF-debug $1 -voutput/$VCD > $output_dir/$TXT"  
    	gnome-terminal -x bash -c "./emulator-freechips.rocketchip.system-$CONF-debug $1 -voutput/$VCD | tee ./$output_dir/$TXT"
    	if [ $counter -eq 22 ]; then
    		sleep 800
    		export counter=0
    		echo "$counter ZERO"cd 
    	else
    		export counter=`expr $counter + 1`
    		echo "$counter"
		fi  
		#./emulator-freechips.rocketchip.system-MESI$NCoresConfig-debug $1 -voutput/$1_MESI-$NCores.vcd > OutputTB/$1/$PROTOCOL$CORES$TEST
		#./emulator-freechips.rocketchip.system-MSI$NCoresConfig-debug $1 -voutput/$1_MSI-$NCores.vcd > OutputTB/$1/$1_MSI-$NCores_test-$Ntest.txt
		#./emulator-freechips.rocketchip.system-MI$NCoresConfig-debug $1 -voutput/$1_MI-$NCores.vcd > OutputTB/$1/$1_MI-$NCores_test-$Ntest.txt
    	done
	done
done


