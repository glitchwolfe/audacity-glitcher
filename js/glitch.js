function send_request(url){
	console.log("SEND REQUEST", url)
	$.ajax({
		type: "POST",
		url: url,
		success: function(data) {
		   console.log(data)
		},
		error: function (xhr, ajaxOptions, thrownError) {
		  console.log(xhr.status);
		  console.log(thrownError);
		}
  	});
}

function importRaw(){
	send_request('import');
	Swal.fire({
		title: "Importing File...",
		html: `
		<p>Please check Audacity.</p>
		<table>
			<thead>
				<tr><th colspan=2>Recommended Settings</th></tr>
			</thead>
			<tbody>
				<tr><td>Encoding</td><td>U-Law</td></tr>
				<tr><td>Byte Order</td><td>Big-Endian</td></tr>
				<tr><td>Channels</td><td>1 Channel (Mono)</td></tr>
				<tr><td>Start Offset</td><td>0 Bytes</td></tr>
				<tr><td>Amount to import</td><td>100%</td></tr>
				<tr><td>Sample Rate</td><td>44100 Hz</td></tr>
			</tbody>
		</table>
		`,
		confirmButtonText: "Done",
		footer: "<p>Note: The images that tend to work best are large in size, and in .bmp, .tiff, or .raw format.</p>"
	});
}

function exportRaw(){
	send_request('export');
	Swal.fire({
		title: "Exporting File...",
		html: `
		<p>NOTE: THIS MUST BE DONE MANUALLY</p>
		<p>Press CTRL+SHIFT+E with the Audacity window focused to open the Export File dialog</p>
		<table>
			<thead>
				<tr><th colspan=2>Recommended Settings</th></tr>
			</thead>
			<tbody>
				<tr><td>File Type</td><td>Other uncompressed files</td></tr>
				<tr><td>Byte Order</td><td>RAW (header-less)</td></tr>
				<tr><td>Encoding:</td><td>U-Law</td></tr>
			</tbody>
		</table>
		`,
		confirmButtonText: "Done",
		footer: "Tip: Try naming your files in a way that will help you remember what effects you used!"
	});
}
