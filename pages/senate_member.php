<!DOCTYPE html>

<!-- this path may need changed for production--works for testing-->
<?php include_once "php/senate_member_query.php" ?>

<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Senate Member Profile</title>
    <link rel="stylesheet" href="front_end/style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  </head>
  <body>
  <body>
    <div id="grid-container">
      <div id="left_side">
        <div id="card">
          <?php $img_path = "img/senate_members/" . preg_replace('/\s+/', '_', strtolower($first_name)) . "_" . preg_replace('/\s+/', '_', strtolower($last_name)) . ".jpg" ?>
          <img src="<?php echo $img_path ?>" alt="member" style="width:100%">
          <h1><?php echo $first_name . " " . $last_name . " - " . $title ?></h1>
          <p><?php echo $party ?></p>
          <p><?php echo $state ?></p>
          <div style="margin: 24px 0;">
            <a class='logo' href="https://en.wikipedia.org/wiki/<?php echo $first_name . "_" . $last_name ?>"><i class="fa fa-wikipedia-w"></i></a>
            <a class='logo' href="https://www.youtube.com/<?php echo $youtube_account ?>"><i class="fa fa-youtube"></i></a>
            <a class='logo' href="https://www.twitter.com/<?php echo $twitter_account ?>"><i class="fa fa-twitter"></i></a>
            <a class='logo' href="https://www.facebook.com/<?php echo $facebook_account ?>"><i class="fa fa-facebook"></i></a>
          </div>
          <p><button><a class='contact' href="<?php echo $contact_form ?>">Contact</a></button></p>
        </div>

        <div class="back">
            <p><button><a class='contact' href="index.html">More Search</a></button></p>
        </div>

      </div>
      <div id= "right_side">
        <div id="bills">
          <table>
            <tr>
              <th>Vote</th>
              <th class="vote_id">Vote ID</th>
              <th class="date">Date</th>
              <th>Bill Number</th>
              <th>Bill Short Title</th>
              <th>Question</th>
            </tr>
            <?php
              //populate table
              while ($row = $result2 -> fetchArray()) {
                //if bill_short_title is null, replace it with description
                if ($row['bill_short_title'] == null) {
                  $bill_short_title = $row['description'];
                } else {
                  $bill_short_title = $row['bill_short_title'];
                }
                //if bill_number is null, replace it with nomination_id
                if ($row['bill_number'] == null) {
                  $bill_number = $row['nomination_id'];
                } else {
                  $bill_number = $row['bill_number'];
                }
                echo "<tr><td>" . $row["vote"]. "</td><td>" . $row["vote_id"] . "</td><td>" .$row["date"]. "</td><td>" .
                     "<a class='one' href=" . $row["url"] . ">" . $bill_number . "</a></td><td>" .
                     $bill_short_title . "</td><td>" . $row["question"] . "</td></tr>";
              }
            ?>
          </table>
        </div>
      </div>
    </div>
  </body>
</html>
