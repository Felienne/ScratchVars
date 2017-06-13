$top_number = 100;
$x = 1;
$total = 0;
while ( $x <= $top_number ) {
	$total = $total + $x;	# short form: $total += $x;
	$x += 1;		# do you follow this short form?
}

print "The total from 1 to $top_number is $total\n";