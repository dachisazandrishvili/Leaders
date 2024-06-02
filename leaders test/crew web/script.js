let aboughtMe = document.getElementById("Abm");

let join = document.getElementById("join");

let body = document.getElementById("body")

let header = document.getElementById("header");

let ame = document.getElementById("aboughtMe");

let text = document.getElementById("text");

let img = document.getElementById("imm");

let neme = document.getElementById("name");
let btn = document.getElementById("btn")

aboughtMe.addEventListener("click", function(){
  header.style.display = "none"
  ame.style.display = "flex"
  body.style.display = "flex"
  body.style.justifyContent = "center"
  body.style.alignItems = "center"

})

let countLeft = 0;
let countRight = 0;

function constructor(src, name, text){
  this.src = src;
  this.name = name;
  this.text = text;
}

let me = new constructor("mypic.jpeg", 
"Dachi Sazandrishvili",
"i, my name is Dachi, i live in Tbilisi Georgia, my goal is to become full-stack developer, i have already trained on projects, but still there is a lot to learn, my favourite enjoyment is, watching soccer, reading books, watching movies and of corse coding, well that's all about methanks for reading")
let donald = new constructor("donald.webp",
 "Donald trump", 
 "hi my name is donald and dachi's crew is best")
let chad = new constructor(
  "chad.jpeg",
  "Chad",
  "i am chad, tkank's to dachi")
const sigma = new constructor(
  "sigma.jpeg",
  "Sigma",
  "i am sigma, tkank's to dachi"
)
  






let lst = []
lst.push(me)
lst.push(donald)
lst.push(chad)
lst.push(sigma)

let leftCounter = 0;

let right = document.getElementById("right");
let left = document.getElementById("left");

let ind = 0;
left.addEventListener("click", function(){
  ind--;
  if(ind < 0){
    ind = lst.length - 1
  }
  neme.innerHTML = lst[ind].name;
  img.src = lst[ind].src;
  text.innerHTML = lst[ind].text;
})
right.addEventListener("click", function(){
  ind++;
  if(ind > lst.length){
    ind = 0
  }
  neme.innerHTML = lst[ind].name;
  img.src = lst[ind].src;
  text.innerHTML = lst[ind].text;
  btn.style.marginTop = "10px"
})