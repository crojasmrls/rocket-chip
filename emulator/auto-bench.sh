#source auto-vvadBench.sh $1=Binary name $2=Number of test $3 = Max ram $4 = binary path
output_dir=OutputTB/$1
rm -rf $output_dir
mkdir -p $output_dir
#counter=0
for (( Ntest = 0; Ntest < $2; Ntest++ )); do
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
		#VCD=$1_$j-$NCores\_test-$Ntest.vcd
		#echo "$VCD"
		PART=$j$NCores
    	CONSTANT=Config
    	CONF=$PART$CONSTANT
    	BPATH=$4$NCores/$1
    	echo "$BPATH"
    	echo "$CONF"
    	echo "./emulator-freechips.rocketchip.system-$CONF $BPATH  > $output_dir/$TXT"  
    	gnome-terminal -x bash -c "./emulator-freechips.rocketchip.system-$CONF $BPATH | tee ./$output_dir/$TXT"
    	AUX=$(echo $(grep  'MemAvailable' /proc/meminfo) |cut -d' ' -f2)
    	echo "aux = $AUX"
    	while [ $AUX -lt $3 ] ; do 
    		sleep 2
    		AUX=$(echo $(grep  'MemAvailable' /proc/meminfo) |cut -d' ' -f2)
    		#echo "aux = $AUX"
    	done
		#./emulator-freechips.rocketchip.system-MESI$NCoresConfig-debug $1 -voutput/$1_MESI-$NCores.vcd > OutputTB/$1/$PROTOCOL$CORES$TEST
		#./emulator-freechips.rocketchip.system-MSI$NCoresConfig-debug $1 -voutput/$1_MSI-$NCores.vcd > OutputTB/$1/$1_MSI-$NCores_test-$Ntest.txt
		#./emulator-freechips.rocketchip.system-MI$NCoresConfig-debug $1 -voutput/$1_MI-$NCores.vcd > OutputTB/$1/$1_MI-$NCores_test-$Ntest.txt
    	done
	done
done


	