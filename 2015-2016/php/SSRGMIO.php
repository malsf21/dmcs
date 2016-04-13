<html>
<?php

// S__equential
echo "Hello <br>";
echo "World <br>";

// Variable
$i = 7;

// S__elect a path or branch using an if statement
if ($i < 4) {
	echo "too low <br>";
} else if ($i > 4) {
	echo "too high <br>";
} else {
	echo "4! <br>";
}

// R__epitition using while and for loops
// there is also for each loop to loop through arrays, figure that out yourself
while ($i > 0) {
	echo $i;
	$i--;
}

echo "<br>";

for ($i = 10; $i > 0; $i--) {
	echo $i;
}

echo "<br>";

// G__raphics can be accomplished using HTML
echo "<img src='https://pbs.twimg.com/profile_images/422907300286709760/laD3977r.png'><br>";

// M__odularization - if you want to do some lines of code a few times, put it in a function
writeMsgTimes("I am the best coder", 5);

function writeMsgTimes($myMsg,$num) {
	while ($num > 0) {
		echo $myMsg;
		$num--;
		echo "<br>";
	}
}

// file IO can be accomplished in PHP
$filename = "deleteme.txt";
$file = fopen( $filename, "w" );
if( $file == false )
{
   echo ( "Error in opening new file" );
   exit();
}
fwrite( $file, "This is  a simple test\n" );
echo $filename . " written to disk";
fclose( $file );


?>

<br>

<?php

if (file_exists($filename)) {
   $filesize = filesize( $filename );
   $msg = "File  created with name $filename ";
   $msg .= "containing " . $filesize . " bytes";
   echo ($msg );
} else {
   echo ("File " . $filename . " does not exist" );
}

?>
</html>
