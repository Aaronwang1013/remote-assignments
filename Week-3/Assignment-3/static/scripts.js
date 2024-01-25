
//This is the Jquery version of code 
// function getSum() {
//     const number = $('#number').val()
//     $.get('/data' , { number: number})
//     .done(function(result) {
//         $('#Result').text('Result: ' + result);
//     })
// }

//This is the JS verison
function getSum() {
    // get the value from number dom
    const number = document.getElementById('number').value;
    // create a new AJAX object
    var xhr = new XMLHttpRequest();
    // check staus
    xhr.onreadystatechange = function (){
        if (xhr.readyState == 4 && xhr.status == 200){
            document.getElementById('Result').innerText = 'Result: ' + xhr.responseText;
        }
    };
    //open the requested file and transmit the data
    xhr.open('GET', '/data?number=' + number, true);
    xhr.send();
}