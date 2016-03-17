function httpGet(theUrl){
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
  xmlHttp.send( null );
  return xmlHttp.responseText;
}
var data = httpGet("json.php?summonerid=65443758");
var jsonData = JSON.parse(data);
var mattPlaying = false;
if ("status" in jsonData){
  mattPlaying = false;
}
else{
  mattPlaying = true;
  type = jsonData["gameQueueConfigId"];
  if (type === 0){
    var mode = "Custom";
  }
  else if (type == 2){
    var mode = "Blind Pick";
  }
  else if (type == 14){
    var mode = "Normal Draft";
  }
  else if (type == 4){
    var mode = "Ranked Dynamic Queue";
  }
  else if (type == 41){
    var mode = "Ranked 3v3";
  }
  else if (type == 31 || type == 32 || type == 33){
    var mode = "Bot";
  }
  else{
    var mode = "Unidentified";
  }
}
