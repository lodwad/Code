var xhttp = new XMLHttpRequest();

xhttp.onreadystatechange = function(){
    if(this.readyState == 4 && this.status == 200){
        document.getElementById("demo").innerHTML = xhttp.responseText;
    }
};

xhttp.open("GET", "https://www.cnn.com", true);
xhttp.send();

