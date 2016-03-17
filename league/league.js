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
}
