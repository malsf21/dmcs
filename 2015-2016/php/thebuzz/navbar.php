<nav class="navbar navbar-dark navbar-fixed-top bg-warning">
  <div class="container">
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
          <a class="dropdown-toggle btn btn-secondary" data-toggle="dropdown" href="#" role="button" aria-haspopup="true" aria-expanded="false"><span class="fa fa-lock"></span> Login to your Beehive</a>
          <div class="dropdown-menu" style="padding:5px;">
            <form action="login.php" method="post">
              Email: <input type="text" class="form-control" name="email" value="" />
              </br>
              Password: <input type="password" class="form-control" name="password" value="" />
              </br>
              <input class="btn btn-primary-outline" type="submit" value="Login" />
            </form>
          </div>
        </li>
      </div>
    </ul>
  </div>
</nav>
