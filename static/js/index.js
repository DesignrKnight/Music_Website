alert ('this works')



fetch('http://127.0.0.1:5000/product/2').then(res => { document.getElementById('02').textContent=res}) 