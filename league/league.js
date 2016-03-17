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

  var champ_data = httpGet("champ.php");
  var champ_jsonData = JSON.parse(champ_data);

  mattPlaying = true;
  var mode = "Custom/Unidentified";
  type = jsonData["gameQueueConfigId"];
  if (type == 2){
    mode = "Blind Pick";
  }
  else if (type == 14){
    mode = "Normal Draft";
  }
  else if (type == 4){
    mode = "Ranked";
  }
  else if (type == 41){
    mode = "Ranked 3v3";
  }
  else if (type == 65){
    mode = "ARAM";
  }
  else if (type == 31 || type == 32 || type == 33){
    mode = "Bot";
  }
  for (i = 0; i < jsonData["participants"].length; i++){
    if (jsonData['participants'][i]["summonerId"] == 65443758){
      var champid = jsonData['participants'][i]['championId'];
    }
  }
  var champ = champ_jsonData["data"][String(champid)]["name"];
  console.log(champ);
}
