

<style>
.box {
	display:inline-block;
	width:20px;
	height:20px;
	background: #eee;
}
.active {
	background: forestGreen;
}
</style>

Stato attuale:
<br/>
<div id="status">lettura in corso...</div>

<script src="jquery-2.1.3.min.js"></script>

<script>

setTimeout("500",function() {

	$.ajax({
		url: "/state.php",
	}).done(function(data) {
		$('#status').html(data);
	})

});

</script>