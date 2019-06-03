for i in 2 4 6
do
    for j in MESI MSI MI
    do 
    	PART=$j$i
    	CONSTANT=Config
    	CONF=$PART$CONSTANT
    	echo "$CONF"
    	make CONFIG=$CONF
    done
done