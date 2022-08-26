

$(function(){

    $("#captureBtn").on("click", function(){

        html2canvas(document.querySelector("#layout")).then(canvas =>{

                    saveAs(canvas.toDataURL("image/png"),"capture-test.png");


        });
        
    });
    function saveAs(uri, filename){

        var link =document.createElement('a');
        if(typeof link.download === 'string'){

            link.href= uri;
            link.download = filename;
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);

        }else {

            window.open(uri);
        }
    }




})

