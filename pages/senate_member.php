<!DOCTYPE html>

<!-- this path may need changed for production--works for testing-->
<?php include_once "../php/senate_member_query.php" ?>

<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>US Senate Member Profile</title>
      <link rel="stylesheet" href="../front_end/style.css">
  </head>

  <body>
  <body>
  <div class="grid-container">
      <div class="member_info">
          <img src="../img/senate_members/elizabeth_warren.jpg" alt="member" width="480" height="600">
          <p id = 'name'><?php echo $first_name . " " . $last_name . " - " . $title ?></p>
          <p id = 'party'>Party: <?php echo $party ?></p>
          <p id = 'date_of_birth'>Date of Birth: <?php echo $date_of_birth ?></p>
          <p id = 'gender'>Gender: <?php echo $gender ?></p>
      </div>

      <div class="voting_record">
          <?php
          /*
          //print voting record
          foreach($voting_record as $value) {
              echo $value['vote_id'];
              echo "  ";
              echo $value['vote'];
              echo "<br>";
          }
          */
          ?>
      </div>

      <div class="bills">
          <table>
              <tr>
                  <th>Vote</th>
                  <th>Vote ID</th>
                  <th>Datesssssssss</th>
                  <th>Bill Number</th>
                  <th>Bill Short Title</th>
              </tr>
              <?php
              //print bills
              foreach($bills as $value2)
              {
                  if(isset($value2['bill_short_title']))
                  {
                      echo "<tr><td>" . $value2["vote"]. "</td><td>" . $value2["vote_id"] . "</td><td>" .$value2["date"]. "</td><td>" . $value2["bill_number"] . "</td><td>"
                          . $value2["bill_short_title"]. "</td></tr>";
                      /*
                      echo $value2['date'];
                      echo "  ";
                      echo $value2['bill_number'];
                      echo "  ";
                      echo $value2['bill_short_title'];
                      echo "  ";
                      echo "<br>";
                      */

                  }
              }
              echo "</table>";
              ?>
      </div>
  </div>
  </body>
</html>
