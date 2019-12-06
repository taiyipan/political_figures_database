<!DOCTYPE html>

<?php include_once "php/senate_member_query.php" ?>

<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>US Senate Member Profile</title>
  </head>

  <body>
    <header>

    </header>

    <main>
      <h1>Senator Profile</h1>
      <nav>
        <ul>
          <li>id <?php echo $id ?></li>
          <li>title <?php echo $title ?></li>
          <li>short_title <?php echo $short_title ?></li>
          <li>api_uri <?php echo $api_uri ?></li>
          <li>first_name <?php echo $first_name ?></li>
          <li>middle_name <?php echo $middle_name ?></li>
          <li>last_name <?php echo $last_name ?></li>
          <li>suffix <?php echo $suffix ?></li>
          <li>date_of_birth <?php echo $date_of_birth ?></li>
          <li>gender <?php echo $gender ?></li>
          <li>party <?php echo $party ?></li>
          <li>leadership_role <?php echo $leadership_role ?></li>
          <li>twitter_account <?php echo $twitter_account ?></li>
          <li>facebook_account <?php echo $facebook_account ?></li>
          <li>youtube_account <?php echo $youtube_account ?></li>
          <li>govtrack_id <?php echo $govtrack_id ?></li>
          <li>cspan_id <?php echo $cspan_id ?></li>
          <li>votesmart_id <?php echo $votesmart_id ?></li>
          <li>icpsr_id <?php echo $icpsr_id ?></li>
          <li>crp_id <?php echo $crp_id ?></li>
          <li>google_entity_id <?php echo $google_entity_id ?></li>
          <li>fec_candidate_id <?php echo $fec_candidate_id ?></li>
          <li>url <?php echo $url ?></li>
          <li>rss_url <?php echo $rss_url ?></li>
          <li>contact_form <?php echo $contact_form ?></li>
          <li>in_office <?php echo $in_office ?></li>
          <li>cook_pvi <?php echo $cook_pvi ?></li>
          <li>dw_nominate <?php echo $dw_nominate ?></li>
          <li>ideal_point <?php echo $ideal_point ?></li>
          <li>seniority <?php echo $seniority ?></li>
          <li>next_election <?php echo $next_election ?></li>
          <li>total_votes <?php echo $total_votes ?></li>
          <li>missed_votes <?php echo $missed_votes ?></li>
          <li>total_present <?php echo $total_present ?></li>
          <li>last_updated <?php echo $last_updated ?></li>
          <li>ocd_id <?php echo $ocd_id ?></li>
          <li>office <?php echo $office ?></li>
          <li>phone <?php echo $phone ?></li>
          <li>fax <?php echo $fax ?></li>
          <li>state <?php echo $state ?></li>
          <li>senate_class <?php echo $senate_class ?></li>
          <li>state_rank <?php echo $state_rank ?></li>
          <li>lis_id <?php echo $lis_id ?></li>
          <li>missed_votes_pct <?php echo $missed_votes_pct ?></li>
          <li>votes_with_party_pct <?php echo $votes_with_party_pct ?></li>
          <li>votes_against_party_pct <?php echo $votes_against_party_pct ?></li>
        </ul>
      </nav>

    </main>

    <footer>
      <p><a href="index.html">Go back</a></p>
    </footer>
  </body>
</html>
