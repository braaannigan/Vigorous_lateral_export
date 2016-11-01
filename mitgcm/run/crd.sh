#!/bin/bash

echo Input first job
read first_job
echo Input last job
read last_job

cp data dataTemplate
sed -i 's/^ nIter0.*/ nIter0=XXX,'/ dataTemplate
sed -i 's/^ nTimeSteps.*/ nTimeSteps=YYY,'/ dataTemplate
sed -i 's/^ deltaT.*/ deltaT=dTT,'/ dataTemplate
sed -i 's/^ pChkptFreq.*/ pChkptFreq=ZZZ,'/ dataTemplate

if (($last_job<$first_job)); then
 echo last_job less than first_job
 exit 1
fi
for ((i=$first_job; i<=$last_job;i++));       do
   if (($i % 10==0))
    then
    echo $i
     fi
cp dataTemplate $(printf "data%03d" $i)
YYY=43200
XXX=$(($i*$YYY))
dTT=1
ZZZ=$(($dTT*YYY))
perl -p  -i -e "s/XXX/$XXX/g" $(printf "data%03d" $i)
perl -p  -i -e "s/YYY/$YYY/g" $(printf "data%03d" $i)
perl -p  -i -e "s/dTT/$dTT/g" $(printf "data%03d" $i)
perl -p  -i -e "s/ZZZ/$ZZZ/g" $(printf "data%03d" $i)
done

exit
for k in {0..90}
 do 
cp dataTemplate $(printf "data%03d" $k)
YYY=51840
XXX=$(($k*$YYY))
dT=50
ZZZ=$(($dT*YYY))
perl -p  -i -e "s/XXX/$XXX/g" $(printf "data%03d" $k)
perl -p  -i -e "s/YYY/$YYY/g" $(printf "data%03d" $k)
perl -p  -i -e "s/ZZZ/$ZZZ/g" $(printf "data%03d" $k)
done

