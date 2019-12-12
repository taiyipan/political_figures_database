<?php
  //connect to database
  $path = 'congress.db';
  $db = new SQLite3($path) or die('Unable to open database');

  //query database for member bio
  $query = "SELECT *
            FROM senate_members
            WHERE first_name = '$first_name' AND last_name = '$last_name'";
  $result = $db -> query($query) or die('Query failed');

  //retrieve first entry as array
  $entry = $result -> fetchArray();

  //load data as variables
  $title = $entry['title'];
  $first_name = $entry['first_name'];
  $last_name = $entry['last_name'];
  $suffix = $entry['suffix'];
  $party = $entry['party'];
  $twitter_account = $entry['twitter_account'];
  $facebook_account = $entry['facebook_account'];
  $youtube_account = $entry['youtube_account'];
  $contact_form = $entry['contact_form'];
  $state = $entry['state'];

  //query database for member voting record
  $query2 = "SELECT *
             FROM senate_voting_records
             LEFT JOIN senate_votes
               ON senate_voting_records.vote_id = senate_votes.id
             WHERE member_id = (
               SELECT id
               FROM senate_members
               WHERE first_name = '$first_name'
               AND last_name = '$last_name'
             )";
  $result2 = $db -> query($query2) or die('Query failed');

  //expand on party
  if($party == 'D') {
    $party = 'Democrat';
  } else if($party == 'R') {
    $party = 'Republican';
  } else if($party == 'ID') {
    $party = 'Independent';
  }
?>
