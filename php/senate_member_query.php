<?php
  //connect to database
  $path = 'political_figures_database.db';
  $db = new SQLite3($path) or die('Unable to open database');

  //query database
  $query = "SELECT *
            FROM senate_members
            WHERE first_name = '$first_name' AND last_name = '$last_name'"; //this is hard-coded for testing
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

//query database for voting record
//we want vote_id[1] and vote[4]
$query2 = "SELECT * FROM senate_voting_records
         WHERE member_id = (
              SELECT id
              FROM senate_members
              WHERE first_name = '$first_name'
              AND last_name = '$last_name')";
$result2 = $db -> query($query2) or die('Query failed');

//iterate thru voting record and store in array
$bills = array();
$i = 0;
while($res = $result2 -> fetchArray(SQLITE3_ASSOC))
{
  if(!isset($res['vote_id'])) continue;
  $bills[$i]['vote_id'] = $res['vote_id'];
  $bills[$i]['vote'] = $res['vote'];
  $i++;
}

//query vote info
$query3 = "SELECT * FROM senate_votes";
$result3 = $db -> query($query3) or die('Query failed');

//iterate thru bills and store in array
$j = 0;

while($res2 = $result3 -> fetchArray(SQLITE3_ASSOC))
{
  if(!isset($res2['date'])) continue;
  $bills[$j]['date'] = $res2['date'];
  $bills[$j]['url'] = $res2['url'];
  $bills[$j]['bill_id'] = $res2['bill_id'];
  $bills[$j]['bill_number'] = $res2['bill_number'];
  $bills[$i]['bill_title'] = $res['bill_title'];
  $bills[$j]['bill_short_title'] = $res2['bill_short_title'];
  $bills[$j]['amendment_number'] = $res2['amendment_number'];
  $bills[$i]['congress'] = $res2['congress'];
  $bills[$i]['session'] = $res2['session'];
  $bills[$i]['chamber'] = $res2['chamber'];
  $bills[$i]['url'] = $res2['url'];
  $bills[$i]['bill_latest_action'] = $res2['bill_latest_action'];
  $bills[$i]['amendment_number'] = $res2['amendment_number'];
  $bills[$i]['question'] = $res2['question'];
  $bills[$i]['question_text'] = $res2['question_text'];
  $bills[$i]['description'] = $res2['description'];
  $bills[$i]['vote_type'] = $res2['vote_type'];
  $bills[$i]['date'] = $res2['date'];
  $bills[$i]['result'] = $res2['result'];
  $bills[$i]['democratic_yes'] = $res2['democratic_yes'];
  $bills[$i]['democratic_no'] = $res2['democratic_no'];
  $bills[$i]['democratic_present'] = $res2['democratic_present'];
  $bills[$i]['democratic_not_voting'] = $res2['democratic_not_voting'];
  $bills[$i]['democratic_majority_position'] = $res2['democratic_majority_position'];
  $bills[$i]['republican_yes'] = $res2['republican_yes'];
  $bills[$i]['republican_no'] = $res2['republican_no'];
  $bills[$i]['republican_present'] = $res2['republican_present'];
  $bills[$i]['republican_not_voting'] = $res2['republican_not_voting'];
  $bills[$i]['republican_majority_position'] = $res2['republican_majority_position'];
  $bills[$i]['independent_yes'] = $res2['independent_yes'];
  $bills[$i]['independent_no'] = $res2['independent_no'];
  $bills[$i]['independent_present'] = $res2['independent_present'];
  $bills[$i]['independent_not_voting'] = $res2['independent_not_voting'];
  $bills[$i]['total_yes'] = $res2['total_yes'];
  $bills[$i]['total_no'] = $res2['total_no'];
  $bills[$i]['total_present'] = $res2['total_present'];
  $bills[$i]['total_not_voting'] = $res2['total_not_voting'];
  $j++;
}

  if($party == 'D')
  {
    $party = 'Democrat';
  }
  else if($party == 'R')
  {
    $party = 'Republican';
  }
  else if($party == 'ID')
  {
    $party = 'Independent';
  }
?>
