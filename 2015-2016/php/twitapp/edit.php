<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
		<meta name="author" content="">
		<title>Country - Animal Database</title>
		<link href="../../../resources/bootstrap-4.0.0-alpha.2/css/bootstrap.min.css" rel="stylesheet" />
	</head>
	<body>
	<div class="container" style="padding-top:30px;">
	<?php

	    // pass in some info;
		require("common.php");

		if(empty($_SESSION['user'])) {

			// If they are not, we redirect them to the login page.
			$location = "http://" . $_SERVER['HTTP_HOST'] . "/login.php";
			echo '<META HTTP-EQUIV="refresh" CONTENT="0;URL='.$location.'">';
			//exit;

        	// Remember that this die statement is absolutely critical.  Without it,
        	// people can view your members-only content without logging in.
        	die("Redirecting to login.php");
    	}

		// To access $_SESSION['user'] values put in an array, show user his username
		$arr = array_values($_SESSION['user']);
		echo "<h1 class='display-1'> Welcome " . $arr[2] . "</h1>";

		// open connection
		$connection = mysql_connect($host, $username, $password) or die ("Unable to connect!");

		// select database
		mysql_select_db($dbname) or die ("Unable to select database!");

		// create query
		$query = "SELECT * FROM symbols";

		// execute query
		$result = mysql_query($query) or die ("Error in query: $query. ".mysql_error());

		// see if any rows were returned
		if (mysql_num_rows($result) > 0) {

    		// print them one after another
				echo "<table class='table table-striped table-bordered table-hover' style='text-align:center;'>";
				echo "<tbody>";
				while($row = mysql_fetch_row($result)) {
						echo "<tr>";
				echo "<td>".$row[0]."</td>";
						echo "<td>" . $row[1]."</td>";
						//echo "<td>".$row[2]."</td>";
				echo "<td><a class='btn btn-danger-outline' href=".$_SERVER['PHP_SELF']."?id=".$row[2].">Delete</a></td>";
						echo "</tr>";
				}
				echo "</tbody>";
				echo "</table>";

				echo "<div class='alert alert-success' role='alert'><strong>Congrats!</strong> The table has been correctly been loaded.</div>";

		} else {

    		// print status message
	    	echo "<div class='alert alert-danger' role='alert'><strong>Oh snap!</strong> No rows were found.</div>";
		}

		// free result set memory
		mysql_free_result($result);

		// set variable values to HTML form inputs
		$country = mysql_escape_string($_POST['country']);
    	$animal = mysql_escape_string($_POST['animal']);

		// check to see if user has entered anything
		if ($animal != "") {
	 		// build SQL query
			$query = "INSERT INTO symbols (country, animal) VALUES ('$country', '$animal')";
			// run the query
     		$result = mysql_query($query) or die ("Error in query: $query. ".mysql_error());
			// refresh the page to show new update
	 		echo "<meta http-equiv='refresh' content='0'>";
		}

		// if DELETE pressed, set an id, if id is set then delete it from DB
		if (isset($_GET['id'])) {

			// create query to delete record
			echo $_SERVER['PHP_SELF'];
    		$query = "DELETE FROM symbols WHERE id = ".$_GET['id'];

			// run the query
     		$result = mysql_query($query) or die ("Error in query: $query. ".mysql_error());

			// reset the url to remove id $_GET variable
			$location = "http://" . $_SERVER['HTTP_HOST'] . $_SERVER['PHP_SELF'];
			echo '<META HTTP-EQUIV="refresh" CONTENT="0;URL='.$location.'">';
			exit;

		}

		// close connection
		mysql_close($connection);

	?>

    <!-- This is the HTML form that appears in the browser -->
			<div style="padding:20px;">
		   	<form action="<?=$_SERVER['PHP_SELF']?>" method="post">
					<div class="row" style="text-align:center;">
						<div class="col-md-4">
							<div class="row">
								<div class="col-md-4">
						    	Country:
								</div>
								<div class="col-md-8">
									<input class="form-control" type="text" name="country">
								</div>
							</div>
						</div>
						<div class="col-md-4">
							<div class="row">
								<div class="col-md-4">
						    	Animal
								</div>
								<div class="col-md-8">
									<input class="form-control" type="text" name="animal">
								</div>
							</div>
						</div>
						<div class="col-md-4">
							<input class="btn btn-primary-outline" type="submit" name="submit"></input>
						</div>
					</div>
		    </form>
			</div>
		</div>
    <form action="logout.php" method="post"><button>Log out</button></form>
	<script src="https://code.jquery.com/jquery-2.2.3.min.js"></script>
	<script src="../../../resources/bootstrap-4.0.0-alpha.2/js/bootstrap.min.js"></script>
	</body>
</html>
