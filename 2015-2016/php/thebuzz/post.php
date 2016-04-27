<?php
  require("common.php");

  if(!empty($_POST))
  {
    if (isset($_GET['reply'])){
      $reply = $_GET['reply'];
    }
    else{
      $reply = "false";
    }
    $current_time = time();
    $query_params = array(
        ':author' => $_SESSION['user']['username'],
        ':content' => $_POST['content'],
        ':timestamp' => $current_time,
        ':reply' => $reply
    );

    $query = "
        INSERT INTO posts (
            author,
            content,
            timestamp,
            reply
        ) VALUES (
            :author,
            :content,
            :timestamp,
            :reply
        )
    ";

    try
    {
        $stmt = $db->prepare($query);
        $result = $stmt->execute($query_params);
    }
    catch(PDOException $ex)
    {
        die("Failed to run query: " . $ex->getMessage());
    }

    header("Location: home.php");
    die("Redirecting to home.php");
  }

?>
