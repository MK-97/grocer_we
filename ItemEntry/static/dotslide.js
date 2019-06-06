var steps = $("#stepsbar li"), i = 0;


$(".btn2").click(function(){
  
  if(i < steps.length) {
    console.log("btn2 - "+i); steps.eq(i).removeClass().addClass('done').next().removeClass().addClass('active');
    i++;
  }
});


$(".btn1").click(function(){
  
  if(i <= steps.length && i > 0) {
    
    console.log("btn1 - "+i); steps.eq(i).removeClass().prev().removeClass().addClass('active');
    i--;
    
  }
});

