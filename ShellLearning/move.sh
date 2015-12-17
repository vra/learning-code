for var in *
do

order=${var:7:5}
#echo $order
let "layer=$order/1000"
#there is a error,but I don't know where it is :(
echo $layer

done
