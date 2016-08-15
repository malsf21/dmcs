var github_repo = "";
var github_time = "";
function githubFetch(username){
  var github_data = JSON.parse(httpGet("https://api.github.com/users/"+username+"/events/public?jsoncallback=?"));
  var found = false;
  var counter = 0;
  while (found == false){
    if (github_data[counter]["type"] == "PushEvent"){
      found = true;
      break;
    }
    else{
      counter += 1;
    }
  }
  github_repo = github_data[counter]["repo"]["name"].substring(github_data[counter]["repo"]["name"].lastIndexOf('/')+1,github_data[counter]["repo"]["name"].length);
  var github_unix_time = new Date(Date.parse(github_data[counter]["created_at"]));
  github_time = "at " + String(github_unix_time).substring(16,21) + " " + github_unix_time.toDateString();
  githubInfo();
}
