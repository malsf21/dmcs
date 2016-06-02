function httpGet(theUrl){
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open( "GET", theUrl, false );
  xmlHttp.send( null );
  return xmlHttp.responseText;
}
function getCommitteeData(){
  var committeeData = JSON.parse(httpGet("http://matthewwang.me/omun/api/committees.json"));
  for (var key in committeeData){
    if (key != "structure"){
      $("#committees").append('<li class="table-view-cell media"><a class="navigate-right"><img class="media-object pull-left" src="' + committeeData[key]["image"] + '" height="42" width="42"><div class="media-body">' + committeeData[key]["name"] + '</div></a></li>');
      /*
      <li class="table-view-cell media">
        <a class="navigate-right">
          <img class="media-object pull-left" src="' + committeeData[key]["image"] + '" height="42" width="42">
          <div class="media-body">
            ' + committeeData[key]["name"] + '
          </div>
        </a>
      </li>
      */
    }
  }
}

var initializers = {
    'Committees': function() {
        getCommitteeData();
    }
};

function initializePage(title) {
    var func = initializers[title];
    if(func) { func(); }
}

jQuery(document).ready(function($) {
    window.addEventListener('push', function(e) {
        initializePage(e.detail.state.title);
    });
    initializePage('{{ page.title }}');
});
