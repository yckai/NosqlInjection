<?php
$db_connection = pg_connect("host=localhost dbname=profiles user=profiles password=profiles");
$result = pg_query($db_connection, "SELECT * FROM profiles");
while ($row = pg_fetch_row($result)) {
  echo "ligne1: $row[0]  ligne2: $row[1] ligne3: $row[2]";
  echo "<br />\n";
}
?>
