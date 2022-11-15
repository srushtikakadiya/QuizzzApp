//new 
const options = document.getElementsByClassName("option");
const opt = document.getElementsByClassName("opt");
const question_id = document.getElementsByClassName("ques_id")[0];
const question_name = document.getElementById("question");
const q_no = document.getElementsByClassName("number")[0];
const form = document.getElementsByTagName("form")[0];
const totalquestion = document.getElementsByClassName("totalquestion")[0];

const h1_date = document.getElementById("startdate_demo");
var input_time = document.getElementById("startdate").value;
var ending_time = 00;
var id = "";
var n = 0;

let time = input_time * 60;
h1_date.innerHTML =  `${input_time} : ${ending_time}`


const url = window.location.href;

var interval = setInterval(function(){
        const minutes = Math.floor(time / 60);
        let seconds = time % 60;
        seconds =  seconds < 10 ? '0' + seconds : seconds;
        h1_date.innerHTML =`${minutes} : ${seconds}`;
        time--;
        if (seconds == 0 & minutes== 0) {
          clearInterval(interval);
          window.location.replace("/displayresult");
        }
      }, 1000);
 

//to display all the question
form.addEventListener("submit",(e) => {
        if (totalquestion.value != q_no.value) {
                e.preventDefault();
                let url = window.location.href;
                console.log(url);        
                var formd = new FormData(form);
                let xh = new XMLHttpRequest();
                xh.open('POST', url);
                xh.responseType="json"
                xh.send(formd);
                xh.onload = () => {
                        console.log(xh);        
                        question_id.value=xh.response.ques_id
                        question_name.innerHTML=xh.response.number+" . "+xh.response.questions
                        opt[0].innerHTML=xh.response.optionA
                        opt[1].innerHTML=xh.response.optionB
                        opt[2].innerHTML=xh.response.optionC
                        opt[3].innerHTML=xh.response.optionD
                        options[0].value=xh.response.optionA
                        options[1].value=xh.response.optionB
                        options[2].value=xh.response.optionC
                        options[3].value=xh.response.optionD
                        q_no.value=xh.response.number
                } 
                options[0].checked = false; 
                options[1].checked = false; 
                options[2].checked = false; 
                options[3].checked = false;               
        } 
        })