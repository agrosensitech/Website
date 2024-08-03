let featuedImg = document.getElementById('featured-image');
let smallImgs = document.getElementsByClassName('small-Img');
let references = document.getElementsByClassName('references')[0];


let text = references.innerHTML
    // Regular expression to find URLs in text
    var urlRegex = /(https?:\/\/[^\s]+)/g;
  
    // Replace URLs with anchor tags
    var newText = text.replace(urlRegex, function(url) {
      return '<a href="' + url + '" target="_blank">' + url + '</a>';
    });
  
  // Example usage
  references.innerHTML = newText;
  