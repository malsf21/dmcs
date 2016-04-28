<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
		<meta name="author" content="">
		<title>Everything Feed | The Buzz</title>
		<link href="../../../resources/bootstrap-4.0.0-alpha.2/css/bootstrap.min.css" rel="stylesheet" />
    <link href="../../../resources/font-awesome-4.5.0/css/font-awesome.min.css" rel="stylesheet" />
    <style>
			.full-nav > li > .dropdown-menu { min-width: 300px;}
    </style>
	</head>
	<body>
		<?php include_once ('navbar.php'); ?>
    <div class="container" style="padding-top:70px;">
			<h1 class="display-2">Everything.</h1>
			<h4>That's right, <b>everything.</b></h4>
			<div class="card">
				<div class="card-block">
					<div id="feed-container">

					</div>
				</div>
			</div>
    </div>
    <script src="../../../resources/jquery/jquery2.min.js"></script>
    <script src="../../../resources/bootstrap-4.0.0-alpha.2/js/bootstrap.min.js"></script>
		<script>
			function httpGet(theUrl){
				var xmlHttp = new XMLHttpRequest();
				xmlHttp.open( "GET", theUrl, false );
				xmlHttp.send( null );
				return xmlHttp.responseText;
			}
			var feedData = JSON.parse(httpGet("feed.php"));
			console.log(feedData);
		</script>
  </body>
</html>
