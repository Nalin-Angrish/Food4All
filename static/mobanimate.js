var interval2, interval3, interval4, interval5, interval6;

function isInViewport(elm) {
    var element = document.getElementById(elm);
    const rect = element.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}


function do2(){
    $('div#2').slideDown("slow", "linear");
    interval3 = setInterval(function(){check3()}, 2000);

}
function do3(){
    $('div#3').slideDown("slow", "linear");
    interval4 = setInterval(function(){check4()}, 2000);
}
function do4(){
    $('div#4').slideDown("slow", "linear");
    interval5 = setInterval(function(){check5()}, 2000);
}
function do5(){
    $('div#5').slideDown("slow", "linear");
    interval6 = setInterval(function(){check6()}, 2000);
}
function do6(){
    $('div#6').slideDown("slow", "linear");
}



function check2(){
    if (isInViewport('end')){
        clearInterval(interval2);
        do2();
    }
}
function check3(){
    if (isInViewport('end')){
        clearInterval(interval3);
        do3();
    }
}
function check4(){
    if (isInViewport('end')){
        clearInterval(interval4);
        do4();
    }
}
function check5(){
    if (isInViewport('end')){
        clearInterval(interval5);
        do5();
    }
}
function check6(){
    if (isInViewport('end')){
        clearInterval(interval6);
        do6();
    }
}



$(document).ready(function(){
    $('div#1').slideDown("slow", "linear");
    interval2 = setInterval(function(){check2()}, 2000);
})