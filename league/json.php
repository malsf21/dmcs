<?php
  $apikey = "";
  $summonerid = $_GET["summonerid"];
  $url = "https://na.api.pvp.net/observer-mode/rest/consumer/getSpectatorGameInfo/NA1/".$summonerid."?api_key=".$apikey;
  $ch = curl_init($url);
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
  $data = curl_exec($ch);
  $info = curl_getinfo($ch);
  http_response_code($info["http_code"]);
  header("Access-Control-Allow-Origin: http://matthewwang.me");
  print($data);
?>
