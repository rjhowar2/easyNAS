
$(document).ready(function(){
	$('[data-toggle="tooltip"]').tooltip(); 

	$('#dashboard_menu').affix({
  		offset: {top: 50}
	});

	$("#dashboard_menu .btn").on("click", function(){
		$(".modal input[type=submit]").attr("disabled", false);
	})

	$("#folder_contents").on("click", ":checkbox", function(){
		toggle_button_state();
	});

	$(".modal-footer button").on("click", function(){
		$modal = $(this).parents(".modal");
		reset_modal($modal);
		toggle_button_state();
	})

	$("#btn_delete").on("click", function(){
		add_selected($("#delete_modal .alert-warning ul"));
		$("#delete_modal .alert-warning").show();
	});

	//----------  Modal form handlers --------------------

	$("#upload_modal form").submit(function(event){
		event.preventDefault();
		var $form = $(this);
		var form_data = new FormData($form[0]);

		$.ajax({
            url: $form.attr('action'),
            type: 'POST',
            success: completeHandler = function(data) {
            	operation_complete(data, $("#upload_modal"));
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

   	$("#delete_modal form").submit(function(event){
   		event.preventDefault();
   		var $form = $(this);

   		var form_data = $("#folder_contents form").serialize();

   		$.ajax({
            url: $form.attr('action'),
            type: 'POST',
            success: completeHandler = function(data) {
            	operation_complete(data, $("#delete_modal"))
            },
            error: errorHandler = function(data) {
            	console.log(data);
            },
            data: form_data
        }, 'json');
   	});

   	$("#new_folder_modal form").submit(function(event){
   		event.preventDefault();
   		var $form = $(this);

   		$.ajax({
            url: $form.attr('action'),
            type: 'POST',
            success: completeHandler = function(data) {
            	operation_complete(data, $("#new_folder_modal"))
            },
            error: errorHandler = function(data) {
            	console.log(data);
            },
            data: $form.serialize()
        }, 'json');
   	});
});

function operation_complete(data, $modal){
	$modal.find("input[type=submit]").attr("disabled", true);
	var $modal_alert = $modal.find(".alert-success");
    var message = data["action"] + ": " + data["path"];
	$modal_alert.text(message);

	//hide other alerts
	$modal.find(".alert").hide();
	//show success modal only
	$modal_alert.show();
	//load the folder contents
	update_folder_contents();
}

function update_folder_contents(){
	$("#folder_contents").load(folder_contents_url)
}

function checked_items(){
	return $("#folder_contents :checkbox:checked")
}

function toggle_button_state(){

	var num_checked = checked_items().length;

	if(num_checked > 0){
		$("#btn_download").prop('disabled', false);
		$("#btn_delete").prop('disabled', false);
		if (num_checked == 1){
			$("#btn_edit").prop('disabled', false);
		} else {
			$("#btn_edit").prop('disabled', true);
		}
	} else {
		$("#btn_download").prop('disabled', true);
		$("#btn_edit").prop('disabled', true);
		$("#btn_delete").prop('disabled', true);
	}

}

function reset_modal($modal){
	$modal.find("input").not("input[type=hidden]").not("input[type=submit]").val("");
	$modal.find(".alert").hide();
}

function add_selected($list){
	var items = checked_items();

	$list.html("");

	$.each(items, function(index, value){
		$list.append("<li>" + $(value).val() + "</li>")
	})

}