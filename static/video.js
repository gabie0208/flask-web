var myVideoStream = document.getElementById('myVideo')     // make it a global variable
var myStoredInterval = 0

function getVideo(){
navigator.getMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia;
navigator.getMedia({video: true, audio: false},
                   
  function(stream) {
    myVideoStream.srcObject = stream   
    myVideoStream.play();
}, 
                   
 function(error) {
   alert('webcam not working');
});
}

function takeSnapshot() {
 var myCanvasElement = document.getElementById('myCanvas');
 var myCTX = myCanvasElement.getContext('2d');
 myCTX.drawImage(myVideoStream, 0, 0, myCanvasElement.width, myCanvasElement.height);
}

// function takeAuto() {
//   takeSnapshot() // get snapshot right away then wait and repeat
//   clearInterval(myStoredInterval)
//   myStoredInterval = setInterval(function(){                                                                                         
//      takeSnapshot()
//  }, document.getElementById('myInterval').value);        
// }

function getDownload() {
  var myCanvasElement = document.getElementById('Download');
  //var link = myCanvasElement.getContext('2d');
  const link = document.createElement('a');
  link.download = 'download.jpg';
  link.href = myCanvas.toDataURL();
  link.click();
  link.delete;
}

// function sendSnapShot() {
//   var myCanvasElement = document.getElementById('Download');
//   //var link = myCanvasElement.getContext('2d');
//   const link = document.createElement('a');
//   link.download = 'download.jpg';
//   link.href = myCanvas.toDataURL();
//   link.click();
//   link.delete;
// }

// var jqXHR = $.ajax({
//   type: "POST",
//   url: "/reverse_pca.py",
//   async: false,
//   data: { param: input }
// });

// return jqXHR.responseText;
