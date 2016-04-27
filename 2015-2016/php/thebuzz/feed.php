<?php
	function pull_posts(){
		include_once("common.php");

		$query = "SELECT * FROM posts;";

		// execute query
		$result = mysql_query($query) or die ("Error in query: $query. ".mysql_error());

		$data = [];
		while($row = mysql_fetch_row($result)) {
			array_push($data, $row);
		}

		return(json_encode($data));
		mysql_free_result($result);
		mysql_close($connection);
	}
	echo pull_posts();
?>
