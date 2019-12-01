<?php
  //connect to database
  $path = 'political_figures_database.db';
  $db = new SQLite3($path) or die('Unable to open database');

  //query database
  $query = "SELECT * FROM senate_members
            WHERE first_name = 'Elizabeth' AND last_name = 'Warren'";
  $result = $db -> query($query) or die('Query failed');

  //retrieve first row as array
  $row = $result -> fetchArray();
  //load data as variables
  $first_name = $row['first_name'];
  $last_name = $row['last_name'];
  $date_of_birth = $row['date_of_birth'];
  $gender = $row['gender'];
  $party = $row['party'];
?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <title>Profile</title>
  </head>
  <body>
    <p id = 'first_name'>First Name: <?php echo $first_name ?></p>
    <p id = 'last_name'>Last Name: <?php echo $last_name ?></p>
    <p id = 'date_of_birth'>Date of Birth: <?php echo $date_of_birth ?></p>
    <p id = 'gender'>Gender: <?php echo $gender ?></p>
    <p id = 'party'>Party: <?php echo $party ?></p>
  </body>
</html>
