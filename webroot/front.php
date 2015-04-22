
<html>
        <head>
                <style>
                body { font-family: sans-serif; font-size: 18pt; background: black; 
                        color: #ddd;}
                td { text-align: center; border: 1px solid #ddd;}
                a { 
                        background: lightgray;
                        width: 30px;
                        height: 30px;
                        line-height: 30px;
                        text-decoration: none;
                        color: black;
                        font-weight: bold;
                        display: inline-block; 
                        border-radius: 5px;
                }
                .active {
                        background: red;
                        color: white;
                }
                </style>
        </head>
        <body>
                

                <div style="position: relative; margin: 0 auto; width: 640px;" id="front-picture">
                </div>



                <div style="width: 500px; margin: 0 auto;" id="front-selector">
                </div>


                <script src="jquery-2.1.3.min.js"></script>

                <script>

                        function antennaRequest(radio, type, antenna) {
                                $.ajax({
                                  url: "setant.php?radio="+radio+"&ant="+antenna+"&type="+type+"",
                                }).done(function(data) {
                                  console.log(data);
                                });


                                
                        }

                        function loadFrontPicture() {
                                $.ajax({
                                  url: "front-picture.php",
                                }).done(function(data) {
                                  $("#front-picture").html(data);
                                  setTimeout("loadFrontPicture()",250);
                                });
                        }

                        function loadFrontSelector() {
                                $.ajax({
                                  url: "front-selector.php",
                                }).done(function(data) {
                                  $("#front-selector").html(data);
                                  setTimeout("loadFrontSelector()",1000);
                                });
                        }

                        loadFrontPicture();
                        loadFrontSelector();


                </script>

        </body>
</html>