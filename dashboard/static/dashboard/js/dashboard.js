
$(document).ready(function(){
	$('[data-toggle="tooltip"]').tooltip(); 

	$('#dashboard_menu').affix({
  		offset: {top: 50}
	});

	$("#folder_contents :checkbox").on("click", function(){
		toggle_button_state();
	});

	$(".modal-footer button").on("click", function(){
		$modal = $(this).parents(".modal");
		reset_modal($modal);
	})

	$("#upload_form").submit(function(event){
		event.preventDefault();
		var $form = $(this);
		var form_data = new FormData($form[0]);

		$.ajax({
            url: $form.attr('action'),
            type: 'POST',
            success: completeHandler = function(data) {
            	var $modal_alert = $("#upload_modal .alert");
            	var message = data["action"] + ": " + data["path"];
            	$modal_alert.text(message);

            	$modal_alert.attr("class", "alert alert-success");
            	$modal_alert.show();
            	update_folder_contents();
            },
            error: errorHandler = function(data) {
            	console.log(data);
            },
            data: form_data,
            cache: false,
            contentType: false,
            processData: false
        }, 'json');
      	return false;
   	});
});

function update_folder_contents(){
	$("#folder_contents_container").load(folder_contents_url)
}

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

function reset_modal($modal){
	$modal.find("input").not("input[type=hidden]").not("input[type=submit]").val("");
	$modal.find(".alert").hide();

}