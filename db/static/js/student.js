
$(document).ready(function(){
	alert("Student json");
	$('#student').text("waiting for results");
	setInterval(refreshQueue,5000);
});

function refreshQueue(){
	$.getJSON('/allStudents',function(d){
		$('#student').empty();
		$('#debug').text(d);
		for(var i = 0; i <d.length; i++){
			$('<div/>')
				.append($('<span/>',{text:d[i][0] + " " + d[i][1]}))
				.append($('<br/>'))
				.appendTo('#student');
		}
	})
}