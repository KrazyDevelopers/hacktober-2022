function fun()
{
  var a = Math.floor(Math.random() * 10);
  var b = Math.floor(Math.random() * 10);
  var c = Math.floor(Math.random() * 10);
  var d = Math.floor(Math.random() * 10);
  let x;
  x = a * 1000 + b * 100 + c * 10 + d ;
  document.getElementById("total").value = x;
  // alert("Your OTP is : "+x);
}


function clip()
{
  var copytext = document.getElementById("total");

  copytext.select();
  copytext.setSelectionRange(0,99999);

  navigator.clipboard.writeText(copytext.value);

  alert("copied text:" +copytext.value);
}
