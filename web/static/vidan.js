        var numberOfFiles = 1;
		function addUploadItem () {
            alert ("xxx");
			numberOfFiles++;
			$('#msgid').append("<label for='file'>Filename:</label><input type='file' name='file" + numberOfFiles + "' id='file" + numberOfFiles + "'><br>");
		}