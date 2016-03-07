
$(document).ready(function(){
	$('[data-toggle="tooltip"]').tooltip(); 

	$('#dashboard_menu').affix({
  		offset: {top: 50}
	});
});

var api_urls = JSON.parse(api_urls);