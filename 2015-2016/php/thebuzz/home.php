<?php
	require("common.php");
	if(empty($_SESSION['user'])){
		header("Location: index.php");
		die("Redirecting to index.php");
	}
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
          <div class="alert alert-success alert-dismissable fade in" role="alert">
            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
              <span class="fa fa-close"></span>
             </button>
            Welcome back <strong><?php echo $_SESSION['user']['username']; ?></strong>! Here's your latest honeycombs.
          </div>
          <div class="card card-inverse bg-warning">
            <form action="post.php" method="post">
              <div class="card-block">
                <div class="row">
                  <div class="col-sm-9">
                    <textarea class="form-control" id="submitTextarea" name="content" rows="3" placeholder="Give us your two cents!"></textarea>
                  </div>
                  <div class="col-sm-3">
                    <input class="btn btn-block btn-primary" type="submit" value="Buzz" />
                    <button class="btn btn-block btn-danger">Clear</button>
                  </div>
                </div>
              </div>
            </form>
          </div>
          <div class="card">
            <div class="card-block">
              <h4 class="card-title">Matthew Wang <span class="text-muted">@malsf21</span></h4>
              <p class="card-text">@hedgeriot I'm loving the functionality of @GitHub and @Atom combined together, you should try it #coding #compsci #webdesign</p>
            </div>
          </div>
          <div class="card">
            <div class="card-block">
              <h4 class="card-title">Matthew Wang <span class="text-muted">@malsf21</span></h4>
              <p class="card-text">@hedgeriot I'm loving the functionality of @GitHub and @Atom combined together, you should try it #coding #compsci #webdesign</p>
            </div>
          </div>
          <div class="card">
            <div class="card-block">
              <h4 class="card-title">Matthew Wang <span class="text-muted">@malsf21</span></h4>
              <p class="card-text">@hedgeriot I'm loving the functionality of @GitHub and @Atom combined together, you should try it #coding #compsci #webdesign</p>
            </div>
          </div>
        </div>
        <div class="col-sm-4">
          <div class="card">
            <div class="card-block">
              <h2 class="card-title">Recent Buzzes</h2>
              <p class="card-text">
                <ul class="list-unstyled">
                  <li><a href="#">#Bootstrap</a><li>
                  <li><a href="#">#TheBuzz</a><li>
                  <li><a href="#">#GitHub</a><li>
                  <li><a href="#">#Atom</a><li>
                </ul>
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <script src="../../../resources/jquery/jquery2.min.js"></script>
		<script src="../../../resources/bootstrap-4.0.0-alpha.2/js/bootstrap.min.js"></script>
  </body>
</html>
