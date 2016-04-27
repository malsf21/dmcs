<?php
	require("functions/common.php");
	if(!(empty($_SESSION['user']))){
		header("Location: home.php");
		die("Redirecting to home.php");
	}
?>
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
		<meta name="author" content="">
		<title>The Buzz</title>
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
        <div class="col-sm-7">
					<h1>welcome to:</h1>
          <h1 class="display-1"><b>The Buzz.</b></h1>
          <h4>a social network designed for coders, designers, bugfixers, and everything in between</h4>
					<div class="row">
						<div class="col-sm-8">
							<div class="card">
								<div class="card-block">
									<h4 class="card-title">Matthew Wang <span class="text-muted">@malsf21</span></h4>
							    <p class="card-text">@hedgeriot I'm loving the functionality of @GitHub and @Atom combined together, you should try it #coding #compsci #webdesign</p>
								</div>
							</div>
						</div>
						<div class="col-sm-4">
							<blockquote class="blockquote">
								Talk about things to people simply and quickly
							</blockquote>
						</div>
					</div>
					<div class="row">
						<div class="col-sm-4">
							<blockquote class="blockquote blockquote-reverse">
								Connect with other coders around the world
							</blockquote>
						</div>
						<div class="col-sm-8">
							<div class="card">
								<div class="card-block">
									<h4 class="card-title">John Mace <span class="text-muted">@hedgeriot</span></h4>
							    <p class="card-text">Anybody seen the new @Bootstrap toolkit? #awesome</p>
								</div>
							</div>
							<div class="card">
								<div class="card-block">
									<p class="card-text text-muted"><span class="fa fa-reply"></span> in response to @hedgeriot</p>
									<h4 class="card-title">Matthew Wang <span class="text-muted">@malsf21</span></h4>
							    <p class="card-text">Yeah man, it looks amazing! Props to @Bootstrap ! I'll probably use it in some of my #webdesign projects soon!</p>
								</div>
							</div>
						</div>
					</div>
        </div>
        <div class="col-sm-5">
          <h2><span class="fa fa-user-plus"></span> Register</h2>
          <form action="register.php" method="post">
            Username: <input class="form-control" type="text" name="username" value="" />
						</br>
            Email: <input class="form-control" type="text" name="email" value="" />
						</br>
            Password: <input class="form-control" type="password" name="password" value="" />
						</br>
            <input class="btn btn-primary-outline" type="submit" value="Register" />
          </form>
					<h4 style="text-align:center;">or,</h4>
          <h2><span class="fa fa-key"></span> Login</h2>
          <form action="login.php" method="post">
            <div class="row">
              <div class="col-sm-6">
                Email: <input type="text" class="form-control" name="email" value="" />
              </div>
              <div class="col-sm-6">
                Password: <input type="password" class="form-control" name="password" value="" />
              </div>
            </div>
						</br>
						<input class="btn btn-primary-outline" type="submit" value="Login" />
          </form>
        </div>
      </div>
    </div>
		<script src="../../../resources/jquery/jquery2.min.js"></script>
		<script src="../../../resources/bootstrap-4.0.0-alpha.2/js/bootstrap.min.js"></script>
  </body>
</html>
