

for (( Ntest = 0; Ntest < 10; Ntest++ )); do
	
for NCores in 2 4 6; do
#statements

./emulator-freechips.rocketchip.system-MESI$(NCores)Config-debug $1 -voutput/$1_MESI-$(NCores).vcd > OutputTB/$1/$1_MESI-$(NCores)_test-$(Ntest).txt
./emulator-freechips.rocketchip.system-MSI$(NCores)Config-debug $1 -voutput/$1_MSI-$(NCores).vcd > OutputTB/$1/$1_MSI-$(NCores)_test-$(Ntest).txt
./emulator-freechips.rocketchip.system-MI$(NCores)Config-debug $1 -voutput/$1_MI-$(NCores).vcd > OutputTB/$1/$1_MI-$(NCores)_test-$(Ntest).txt

done


done


