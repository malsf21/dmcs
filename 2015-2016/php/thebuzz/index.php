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
			.full-nav > li > .dropdown-menu { min-width: 500px;}
    </style>
	</head>
	<body>
		<nav class="navbar navbar-dark navbar-fixed-top bg-warning">
		  <a class="navbar-brand hidden-sm-down" href="index.php"><span class="fa fa-forumbee"></span> The Buzz</a>
      <ul class="nav navbar-nav">
        <li class="nav-item">
          <a class="nav-link" href="about.php">About</a>
        </li>
        <li class="nav-item dropdown">
			    <a class="nav-link dropdown-toggle" data-toggle="dropdown" href="#" role="button" aria-haspopup="true" aria-expanded="false">Discover</a>
			    <div class="dropdown-menu">
			      <a class="dropdown-item nav-link"><span class="fa fa-fire" style="color:red;"></span> Hot</a>
						<span></span>
            <a class="dropdown-item nav-link"><span class="fa fa-trophy" style="color:gold;"></span> Top</a>
			    </div>
			  </li>
				<div class="full-nav">
	        <li class="nav-item dropdown pull-xs-right">
				    <a class="dropdown-toggle btn btn-secondary" data-toggle="dropdown" href="#" role="button" aria-haspopup="true" aria-expanded="false"><span class="fa fa-users" style="color:yellow;"></span> Login to your Beehive</a>
				    <div class="dropdown-menu">
	            <form action="login.php" method="post">
	              Username: <input type="text" class="form-control" name="username" value="" />
								</br>
								Password: <input type="password" class="form-control" name="password" value="" />
								</br>
								<input class="btn btn-primary-outline" type="submit" value="Login" />
		          </form>
						</div>
				  </li>
				</div>
      </ul>
		</nav>
    <div class="container" style="padding-top:70px;">
      <div class="row">
        <div class="col-sm-7">
					<h1>welcome to</h1>
          <h1 class="display-2"><b>the Buzz.</b></h1>
          <p>a social network designed for coders, designers, bugfixers, and everything in between</p>
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
                Username: <input type="text" class="form-control" name="username" value="" />
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
