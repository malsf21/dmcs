<?php
	require("common.php");
	if(empty($_SESSION['user'])){
		header("Location: index.php");
		die("Redirecting to index.php");
	}
  $arr = array_values($_SESSION['user']);
  $user_username = "@".$arr[1];
?>
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
		<meta name="author" content="">
		<title>Home | The Buzz</title>
		<link href="../../../resources/bootstrap-4.0.0-alpha.2/css/bootstrap.min.css" rel="stylesheet" />
    <link href="../../../resources/font-awesome-4.5.0/css/font-awesome.min.css" rel="stylesheet" />
    <style>
			.full-nav > li > .dropdown-menu { min-width: 300px;}
    </style>
	</head>
	<body>
		<?php include_once ('navbar.php'); ?>
    <div class="container" style="padding-top:70px;">
      <div class="row">
        <div class="col-sm-8">
          <h1 class="display-4">Hi <?php echo $user_username; ?>
        </div>
        <div class="col-sm-4">
          <h4>Recent Buzzes</h4>
        </div>
      </div>
    </div>
    <script src="../../../resources/jquery/jquery2.min.js"></script>
		<script src="../../../resources/bootstrap-4.0.0-alpha.2/js/bootstrap.min.js"></script>
  </body>
</html>
