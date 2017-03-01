$(document).ready(function() {
	$('#NLU-text').ajaxForm({
		success: function(html, status, xhr, myForm) {

			console.log(html.concepts)
			var concepts = html.concepts;
			var conceptsHTML = '<p><b>Concepts in Notes:</b></p>'

			$.each(concepts, function( index, value ) {
			  conceptsHTML += '<p>' + value.text + ': ' + value.relevance + '</p>'
			});

			$('#concepts').html(conceptsHTML);

		}
	});
});