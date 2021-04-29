$(document).ready(function() {
	
	$("form").on("submit", function(event) {

	$.ajax({
		// Import dat z formuláře
		data : {
			time : $("#timeInput").val(),
			point_input : $("#pointInput").val(),
			distance : $("#distanceInput").val(),
			style : $("#styleInput").val(),
			course : $("#courseInput").val(),
			gender : $("#genderInput").val()
	},
	// Přesměrování na /process (pomocí POST)
	type : "POST",
	url : "/process"
	})
	
	.done(function(data) {
		
		if (data.error) {
			$("#errorAlert").text(data.error).show(),
			$("#div_points").hide(),
			$("#div_time").hide(),
			$("#div_distance").hide(),
			$("#div_style").hide(),
			$("#div_course").hide(),
			$("#div_gender").hide()
		}
		else {
			$("#errorAlert").hide(),
			$("#div_points").text(data.point).show(),
			$("#div_time").text(data.tim).show(),
			$("#div_distance").text(data.ath_nam).show(),
			$("#div_style").text(data.ath_nat).show(),
			$("#div_course").text(data.wr_t).show(),
			$("#div_gender").text(data.wr_y).show()
		}
	});
	event.preventDefault();
	});
});

