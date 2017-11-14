function sendfile(dtform,path_uri=window.location.pathname,callback=function(r){}){
	console.log(dtform,path_uri);
	$.ajax({
		url: path_uri,
		type: 'POST',
		enctype: 'multipart/form-data', 
		data: dtform, 
		processData: false, 
		contentType: false, 
		cache: false,
		success:callback,
	})
	.done(function(data) {
		console.log("File Sended!...");
	})
	.fail(function() {
		console.log("Error Sending File");
	});
}