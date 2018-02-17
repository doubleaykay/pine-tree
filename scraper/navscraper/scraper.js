urls = []

for (key in Object.keys(document.getElementsByClassName("expandable"))) {
	urls.push(document.getElementsByClassName("expandable")[key].nextSibling.href);
}

allurls = document.createElement("div");

for (i in urls) {
    elem = document.createElement("div");
    elem.innerHTML='<object type="text/html" data="'+urls[i]+'?getchildren=1" ></object>';
	allurls.appendChild(elem);
}

document.body.innerHTML = allurls.innerHTML;
console.log(allurls);