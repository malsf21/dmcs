<?php
    require("common.php");
    if(!empty($_POST))
    {
        $query = "
            SELECT
                id,
                username,
                password,
                salt,
                email
            FROM users
            WHERE
                email = :email
        ";

        $query_params = array(
            ':email' => $_POST['email']
        );

        try
        {
            $stmt = $db->prepare($query);
            $result = $stmt->execute($query_params);
        }
        catch(PDOException $ex)
        {
            die("Failed to run query: " . $ex->getMessage());
        }

        $login_ok = false;

        $row = $stmt->fetch();
        if($row)
        {

            $check_password = hash('sha256', $_POST['password'] . $row['salt']);
            for($round = 0; $round < 65536; $round++)
            {
                $check_password = hash('sha256', $check_password . $row['salt']);
            }

            if($check_password === $row['password'])
            {
                $login_ok = true;
            }
        }

        if($login_ok)
        {
            unset($row['salt']);
            unset($row['password']);
            $_SESSION['user'] = $row;

            header("Location: home.php");
            die("Redirecting to: home.php");
        }
        else
        {
            print("Login Failed.");
        }
    }

?>
