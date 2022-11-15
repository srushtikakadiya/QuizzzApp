//new 
const options = document.getElementsByClassName("option");
const opt = document.getElementsByClassName("opt");
const optA = document.getElementsByClassName("optionA");
const optB = document.getElementsByClassName("optionB");
const optC = document.getElementsByClassName("optionC");
const optD = document.getElementsByClassName("optionD");
const question_id = document.getElementsByClassName("ques_id")[0];
const question_name = document.getElementById("question");
const q_no = document.getElementsByClassName("number")[0];
const form = document.getElementsByTagName("form")[0];
const totalquestion = document.getElementsByClassName("totalquestion")[0];
var id = "";
var n = 0;

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
                        optA.innerHTML=xh.response.optionA
                        optB.innerHTML=xh.response.optionB
                        optC.innerHTML=xh.response.optionC
                        optD.innerHTML=xh.response.optionD
                        optA.value=xh.response.optionA
                        optB.value=xh.response.optionB
                        optC.value=xh.response.optionC
                        optD.value=xh.response.optionD
                        q_no.value=xh.response.number
                }  
        } 

        })