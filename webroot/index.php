

<style>
.box {
	display:inline-block;
	width:20px;
	height:20px;
	background: #eee;
	margin-top: 2px;
}
.active {
	background: forestGreen;
	color: white;
}
.tx {
	background: red;
	color: white;
}
.verticaldiv {
	width: 30px;
	display: inline-block;
	height: 160px;
	float: left;
}
html {
	font-family: verdana;
}
td {
	border: 1px solid #ddd;
}
.pin {
	width: 25px;
}
</style>

Stato attuale:
<br/>
<div id="status">lettura in corso...</div>

<script src="jquery-2.1.3.min.js"></script>

<script>

setTimeout(function() {

	$.ajax({
		url: "/state.php",
	}).done(function(data) {
		$('#status').html(data);
	})

}, 300);

</script>