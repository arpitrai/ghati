function highlightCurrentLink() {
    var a = document.getElementsByTagName("a");
    for(var i=0; i<a.length; i++) {
        if(a[i].href.slice(a[i].href.search(".com")+4, a[i].href.length) == document.location.href.slice(document.location.href.search(".com")+4, document.location.href.length-1)) {
            a[i].setAttribute("className", "currentLink");
            a[i].setAttribute("class", "currentLink");
        }
        if(document.location.href.slice(document.location.href.search(".com")+4, document.location.href.length) == '/') {
            temp = document.getElementById("default");
            temp.setAttribute("className", "currentLink");
            temp.setAttribute("class", "currentLink");
        }
    }
}

window.onload=highlightCurrentLink;
