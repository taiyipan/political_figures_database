<?php
  //obtain user input
  if (isset($_POST)) {
    $input = sanitizeString($_POST['input']);
    $input = trim($input);
    $area = $_POST['list'];
  }
  //branch into 4 paths
  switch ($area) {
    case 'house_members':
      $tokens = explode(' ', $input, 2); //split string on first space
      $first_name = trim($tokens[0]);
      $last_name = trim($tokens[1]);
      //edge case handling
      if ($input == 'C.A. Dutch Ruppersberger') {
        $first_name = 'C.A. Dutch';
        $last_name = 'Ruppersberger';
      }
      include_once "pages/house_member.php";
      break;

    case 'senate_members':
      $tokens = explode(' ', $input, 2); //split string on first space
      $first_name = trim($tokens[0]);
      $last_name = trim($tokens[1]);
      include_once "pages/senate_member.php";
      break;

    default:
      break;
  }
  function sanitizeString($var) {
    if (get_magic_quotes_gpc())
      $var = stripslashes($var);
    $var = strip_tags($var);
    $var = htmlentities($var);
    return $var;
  }
  function sanitizeMySQL($connection, $var) {
    $var = $connection -> real_escape_string($var);
    $var = sanitizeString($var);
    return $var;
  }
?>
