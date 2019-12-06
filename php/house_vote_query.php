<?php
  //connect to database
  $path = 'political_figures_database.db';
  $db = new SQLite3($path) or die('Unable to open database');

  //query database
  $query = "SELECT *
            FROM house_votes
            WHERE id = '$num'";
  $result = $db -> query($query) or die('Query failed');

  //retrieve first entry as array
  $entry = $result -> fetchArray();

  //load data as variables
  $congress = $entry['congress'];
  $session = $entry['session'];
  $chamber = $entry['chamber'];
  $roll_call = $entry['roll_call'];
  $source = $entry['source'];
  $url = $entry['url'];
  $bill_id = $entry['bill_id'];
  $bill_number = $entry['bill_number'];
  $bill_api_uri = $entry['bill_api_uri'];
  $bill_title = $entry['bill_title'];
  $bill_short_title = $entry['bill_short_title'];
  $bill_latest_action = $entry['bill_latest_action'];
  $amendment_number = $entry['amendment_number'];
  $amendment_api_uri = $entry['amendment_api_uri'];
  $amendment_sponsor_id = $entry['amendment_sponsor_id'];
  $amendment_sponsor = $entry['amendment_sponsor'];
  $amendment_sponsor_uri = $entry['amendment_sponsor_uri'];
  $amendment_sponsor_party = $entry['amendment_sponsor_party'];
  $amendment_sponsor_state = $entry['amendment_sponsor_state'];
  $question = $entry['question'];
  $question_text = $entry['question_text'];
  $description = $entry['description'];
  $vote_type = $entry['vote_type'];
  $date = $entry['date'];
  $time = $entry['time'];
  $result = $entry['result'];
  $democratic_yes = $entry['democratic_yes'];
  $democratic_no = $entry['democratic_no'];
  $democratic_present = $entry['democratic_present'];
  $democratic_not_voting = $entry['democratic_not_voting'];
  $democratic_majority_position = $entry['democratic_majority_position'];
  $republican_yes = $entry['republican_yes'];
  $republican_no = $entry['republican_no'];
  $republican_present = $entry['republican_present'];
  $republican_not_voting = $entry['republican_not_voting'];
  $republican_majority_position = $entry['republican_majority_position'];
  $independent_yes = $entry['independent_yes'];
  $independent_no = $entry['independent_no'];
  $independent_present = $entry['independent_present'];
  $independent_not_voting = $entry['independent_not_voting'];
  $total_yes = $entry['total_yes'];
  $total_no = $entry['total_no'];
  $total_present = $entry['total_present'];
  $total_not_voting = $entry['total_not_voting'];
?>
