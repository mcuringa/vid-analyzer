        var numberOfFiles = 1;
		function addUploadItem () {
			numberOfFiles++;
			$('#msgid').append("<label for='file'>Filename:</label><input type='file' name='file" + numberOfFiles + "' id='file" + numberOfFiles + "'><br>");
		}




// function removeLI()
// {
// $(this).closest("li").fadeOut(300);

// }
