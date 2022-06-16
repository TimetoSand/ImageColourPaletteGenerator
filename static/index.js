function clip_text(a_string){
    var input = document.createElement('input');
    input.id="__copyText__";
    input.value = a_string; // OOPS! document.getElementById(divId).innerText;
    //document.body.appendChild(input);
    input.select();

    input.setSelectionRange(0, 999);
    navigator.clipboard.writeText(input.value);
  //copyText.select();
  //copyText.setSelectionRange(0, 99999);
  //navigator.clipboard.writeText(copyText.value);

  //  document.execCommand("copy");
  //  var txt = input.value
  //  input.remove()
}
function clip_div(divId){
   let table = document.querySelector(".table");
   table.addEventListener('click', function(event) {
    	// event.target = '<td>', so we pick it's parent
    	const row = event.target.parentNode.parentNode;
    	const raf = row.innerText.split(' ');
    	const leo = raf[0].substring(2, 10);
        //console.log(leo)
    	// row = '<tr>'
    	return clip_text(leo);
    });

}
const buttons = document.querySelectorAll(".copy");
buttons.forEach((btn) => {
  btn.addEventListener('click', function(e){
    if(btn.innerText = "Copy"){
        btn.innerText = "Done";
    }else{
    btn.innerText="Copy";
    }


  })
});