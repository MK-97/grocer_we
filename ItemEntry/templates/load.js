//download mask effect
$(document).ready(function() {
	var timeOut = 500;
	var displayOut = function() {
		setTimeout(function() {
			$(".download-overlay").css({ display: "none" });
		}, timeOut);

		//ignore this below used to debug control time
		setTimeout(function() {
			$(".downloading").text("LOADING");
		}, 0);
		setTimeout(function() {
			$(".downloading").text("...");
		}, timeOut);
	};
	displayOut();
	
	//custom style with jQuerry
	setTimeout(function(id) {
		$('[type="checkbox"]').addClass("custom-checkbox");
		$('[type="radio"]').addClass("custom-radio");
		$("input").addClass("initialized");
	}, timeOut);	
});
