
for file in *
do
	#echo $file
	full_file=$(printf "%06d" "$file")
	new_name=ukbench$full_file.jpg.cnn
	mv "$file" "$new_name" 2> /dev/null
done
