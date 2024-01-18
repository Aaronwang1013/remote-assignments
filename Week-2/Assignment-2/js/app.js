//get the welcome element and listen to it
const welcomebtn = document.querySelector('.welcome');

welcomebtn.addEventListener('click' , () => {
    welcomebtn.textContent = "Have a Good Time!";
    });




// get the call-action and container2 element
const action = document.querySelector('.call-action');
const container1 = document.querySelectorAll('.container2')[0];
const container2 = document.querySelectorAll('.container2')[1];
container1.style.display = 'none';
container2.style.display = 'none';

action.addEventListener('click' , () => {
    container1.style.display = 'flex';
    container2.style.display = 'flex';
})

