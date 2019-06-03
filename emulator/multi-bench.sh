#source auto-vvadBench.sh $1=Binary name $2=Number of test $3 = Max ram $4 = binary path
for i in 0 1 2 3 4; do
	BINARY=$1$i.riscv
	echo "BINARY"
	source auto-bench.sh $BINARY $2 $3 $4
done