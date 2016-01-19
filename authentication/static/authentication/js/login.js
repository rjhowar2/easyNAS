$(document).ready(function(){
	$("#loginSubmit").on("click", function(e){

		e.preventDefault();

		var email = $("#inputEmail").val();
		var password = $("#inputPassword").val();

		if(email != '' && password != '') {

			$.ajax({
       			url : login_url,
       			type : "POST",
       			data : {email: email, password: password},
 				success : function() {
 					window.location.href = dashboard_url;
 				},
 				error : function(xhr,errmsg,err) {
 					$(".form-signin .alert").show();
 				}
 			});
		}
	});
});