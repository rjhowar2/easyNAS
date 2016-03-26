
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

    $("#btn_download").on("click", function(){
        add_selected($("#download_modal .alert-warning ul"));
        $("#download_modal .alert-warning").show();
    });

    $("#btn_edit").on("click", function(){
        //change hidden input val to source
        var val = checked_items().val()
        $("#edit_modal").find("input[name=source]").val(val);
        $("#edit_modal").find("input[name=destination]").val(val);
        //move source to text field
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

    $("#download_modal form").submit(function(event){
        event.preventDefault();
        var $contents_form = $("#folder_contents form");

        $contents_form.attr('action', $(this).attr('action'))

        $contents_form.submit();
        $("#download_modal .close").trigger("click");
        $("#folder_contents :checkbox:checked").trigger("click");

    });

    $("#edit_modal form").submit(function(event){
        event.preventDefault();
        var data = $(this).serialize();
        modal_ajax($("#edit_modal"), data);
        return false;
    });
});

function modal_ajax($modal, form_data){

    var $form = $modal.find("form");
 
    $.ajax({
        url: $form.attr('action'),
        type: 'POST',
        success: completeHandler = function(data) {
            operation_complete(data, $modal);
        },
        error: errorHandler = function(data) {
            operation_failed(data, $modal);
        },
        data: form_data,
    }, 'json');
    return false;
}

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

function operation_failed(data, $modal){
    console.log(data);
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