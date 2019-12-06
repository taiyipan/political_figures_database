<!DOCTYPE html>

<?php include_once "php/senate_vote_query.php" ?>

<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>US Senate Rollcall Vote</title>
  </head>

  <body>
    <header>

    </header>

    <main>
      <h1>US Senate Rollcall Vote <?php echo $roll_call ?></h1>
      <nav>
        <ul>
          <li>congress <?php echo $congress ?></li>
          <li>session <?php echo $session ?></li>
          <li>chamber <?php echo $chamber ?></li>
          <li>roll_call <?php echo $roll_call ?></li>
          <li>source <?php echo $source ?></li>
          <li>url <?php echo $url ?></li>
          <li>bill_id <?php echo $bill_id ?></li>
          <li>bill_number <?php echo $bill_number ?></li>
          <li>bill_api_uri <?php echo $bill_api_uri ?></li>
          <li>bill_title <?php echo $bill_title ?></li>
          <li>bill_short_title <?php echo $bill_short_title ?></li>
          <li>bill_latest_action <?php echo $bill_latest_action ?></li>
          <li>amendment_number <?php echo $amendment_number ?></li>
          <li>amendment_api_uri <?php echo $amendment_api_uri ?></li>
          <li>amendment_sponsor_id <?php echo $amendment_sponsor_id ?></li>
          <li>amendment_sponsor <?php echo $amendment_sponsor ?></li>
          <li>amendment_sponsor_uri <?php echo $amendment_sponsor_uri ?></li>
          <li>amendment_sponsor_party <?php echo $amendment_sponsor_party ?></li>
          <li>amendment_sponsor_state <?php echo $amendment_sponsor_state ?></li>
          <li>question <?php echo $question ?></li>
          <li>question_text <?php echo $question_text ?></li>
          <li>description <?php echo $description ?></li>
          <li>vote_type <?php echo $vote_type ?></li>
          <li>date <?php echo $date ?></li>
          <li>time <?php echo $time ?></li>
          <li>result <?php echo $result ?></li>
          <li>tie_breaker <?php echo $tie_breaker ?></li>
          <li>tie_breaker_vote <?php echo $tie_breaker_vote ?></li>
          <li>document_number <?php echo $document_number ?></li>
          <li>document_title <?php echo $document_title ?></li>
          <li>democratic_yes <?php echo $democratic_yes ?></li>
          <li>democratic_no <?php echo $democratic_no ?></li>
          <li>democratic_present <?php echo $democratic_present ?></li>
          <li>democratic_not_voting <?php echo $democratic_not_voting ?></li>
          <li>democratic_majority_position <?php echo $democratic_majority_position ?></li>
          <li>republican_yes <?php echo $republican_yes ?></li>
          <li>republican_no <?php echo $republican_no ?></li>
          <li>republican_present <?php echo $republican_present ?></li>
          <li>republican_not_voting <?php echo $republican_not_voting ?></li>
          <li>republican_majority_position <?php echo $republican_majority_position ?></li>
          <li>independent_yes <?php echo $independent_yes ?></li>
          <li>independent_no <?php echo $independent_no ?></li>
          <li>independent_present <?php echo $independent_present ?></li>
          <li>independent_not_voting <?php echo $independent_not_voting ?></li>
          <li>total_yes <?php echo $total_yes ?></li>
          <li>total_no <?php echo $total_no ?></li>
          <li>total_present <?php echo $total_present ?></li>
          <li>total_not_voting <?php echo $total_not_voting ?></li>
        </ul>
      </nav>

    </main>

    <footer>
      <p><a href="index.html">Go back</a></p>
    </footer>
  </body>
</html>
