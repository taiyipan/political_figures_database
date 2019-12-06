<?php
  //connect to database
  $path = 'political_figures_database.db';
  $db = new SQLite3($path) or die('Unable to open database');

  //query database
  $query = "SELECT *
            FROM senate_members
            WHERE first_name = '$first_name' AND last_name = '$last_name'";
  $result = $db -> query($query) or die('Query failed');

  //retrieve first entry as array
  $entry = $result -> fetchArray();

  //load data as variables
  $id = $entry['id'];
  $title = $entry['title'];
  $short_title = $entry['short_title'];
  $api_uri = $entry['api_uri'];
  $first_name = $entry['first_name'];
  $middle_name = $entry['middle_name'];
  $last_name = $entry['last_name'];
  $suffix = $entry['suffix'];
  $date_of_birth = $entry['date_of_birth'];
  $gender = $entry['gender'];
  $party = $entry['party'];
  $leadership_role = $entry['leadership_role'];
  $twitter_account = $entry['twitter_account'];
  $facebook_account = $entry['facebook_account'];
  $youtube_account = $entry['youtube_account'];
  $govtrack_id = $entry['govtrack_id'];
  $cspan_id = $entry['cspan_id'];
  $votesmart_id = $entry['votesmart_id'];
  $icpsr_id = $entry['icpsr_id'];
  $crp_id = $entry['crp_id'];
  $google_entity_id = $entry['google_entity_id'];
  $fec_candidate_id = $entry['fec_candidate_id'];
  $url = $entry['url'];
  $rss_url = $entry['rss_url'];
  $contact_form = $entry['contact_form'];
  $in_office = $entry['in_office'];
  $cook_pvi = $entry['cook_pvi'];
  $dw_nominate = $entry['dw_nominate'];
  $ideal_point = $entry['ideal_point'];
  $seniority = $entry['seniority'];
  $next_election = $entry['next_election'];
  $total_votes = $entry['total_votes'];
  $missed_votes = $entry['missed_votes'];
  $total_present = $entry['total_present'];
  $last_updated = $entry['last_updated'];
  $ocd_id = $entry['ocd_id'];
  $office = $entry['office'];
  $phone = $entry['phone'];
  $fax = $entry['fax'];
  $state = $entry['state'];
  $senate_class = $entry['senate_class'];
  $state_rank = $entry['state_rank'];
  $lis_id = $entry['lis_id'];
  $missed_votes_pct = $entry['missed_votes_pct'];
  $votes_with_party_pct = $entry['votes_with_party_pct'];
  $votes_against_party_pct = $entry['votes_against_party_pct'];
?>
