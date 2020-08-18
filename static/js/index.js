
function htmlToElement(html) {
    var template = document.createElement('template');
    html = html.trim(); 
    template.innerHTML = html;
    return template.content.firstChild;
}

arr=['Hello.mp3','whois.mp3','tata.mp3']
var i=0
var cards="";
fetch('http://127.0.0.1:5000/product').then(res => res.json()).then(res=>{
    res.forEach(data => {
        var card=`
<div class="p-4 md:w-3/3">
<div class="h-full border-2 border-gray-200 rounded-lg overflow-hidden">
  <img class="lg:h-48 md:h-36 w-full object-cover object-center" src="https://dummyimage.com/720x400" alt="blog">
  <audio controls>
  <source src="../static/music/${arr[i++]}" type="audio/mpeg">
  </audio>
  <div class="p-6">
    <h2 class="tracking-widest text-xs title-font font-medium text-gray-500 mb-1">NAME</h2>
    <h1 class="title-font text-lg font-medium text-gray-900 mb-3">${data.name}</h1>
    <p class="leading-relaxed mb-3">${data.description}</p>
    <div class="flex items-center flex-wrap ">
      <a class="text-orange-500 inline-flex items-center md:mb-2 lg:mb-0">Learn More
        <svg class="w-4 h-4 ml-2" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
          <path d="M5 12h14"></path>
          <path d="M12 5l7 7-7 7"></path>
        </svg>
      </a>
      <span class="text-gray-600 mr-3 inline-flex items-center lg:ml-auto md:ml-0 ml-auto leading-none text-sm pr-3 py-1 border-r-2 border-gray-300">
        <svg class="w-4 h-4 mr-1" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24">
          <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
          <circle cx="12" cy="12" r="3"></circle>
        </svg>1.2L
      </span>
      <span class="text-gray-600 inline-flex items-center leading-none text-sm">
        <svg class="w-4 h-4 mr-1" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24">
          <path d="M21 11.5a8.38 8.38 0 01-.9 3.8 8.5 8.5 0 01-7.6 4.7 8.38 8.38 0 01-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 01-.9-3.8 8.5 8.5 0 014.7-7.6 8.38 8.38 0 013.8-.9h.5a8.48 8.48 0 018 8v.5z"></path>
        </svg>6
      </span>
    </div>
  </div>
</div>
</div>`
cards=cards+card;
});

var parsedCard=htmlToElement('<div>'+cards+'</div>')
document.getElementById("02").appendChild(parsedCard)
}) 



