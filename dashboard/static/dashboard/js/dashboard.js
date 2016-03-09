
$(document).ready(function(){
	$('[data-toggle="tooltip"]').tooltip(); 

	$('#dashboard_menu').affix({
  		offset: {top: 50}
	});

	$("#folder_contents :checkbox").on("click", function(){
		toggle_button_state();
	});
});

var api_urls = JSON.parse(api_urls);

function checked_items(){
	return $("#folder_contents :checkbox:checked").length + " boxes checked"
}

function toggle_button_state(){

	var num_checked = $("#folder_contents .folder :checkbox:checked").length;

	if(num_checked > 0){
		$("#btn_download").prop('disabled', false);
		if (num_checked == 1){
			$("#btn_edit").prop('disabled', false);
		} else {
			$("#btn_edit").prop('disabled', true);
		}
	} else {
		$("#btn_download").prop('disabled', true);
		$("#btn_edit").prop('disabled', true);
	}

}