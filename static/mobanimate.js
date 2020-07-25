var interval2, interval3, interval4, interval5, interval6;      // Initialize some variables (These will be used to differentiate animation of different slides)

function isInViewport(elm) {                    //Function to check whether an element is visible or not
    var element = document.getElementById(elm);
    const rect = element.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}


function do2(){                 // Animate 2nd Slide
    $('div#2').slideDown("slow", "linear");
    interval3 = setInterval(function(){check3()}, 2000);    //Start next animation

}
function do3(){                 // Animate 33d Slide
    $('div#3').slideDown("slow", "linear");
    interval4 = setInterval(function(){check4()}, 2000);    //Start next animation
}
function do4(){                 // Animate 4th Slide
    $('div#4').slideDown("slow", "linear");
    interval5 = setInterval(function(){check5()}, 2000);    //Start next animation
}
function do5(){                 // Animate 5th Slide
    $('div#5').slideDown("slow", "linear");
    interval6 = setInterval(function(){check6()}, 2000);    //Start next animation
}
function do6(){                 // Animate 6th Slide
    $('div#6').slideDown("slow", "linear");
}



function check2(){              // Constantly check whether or not to animate 2nd Slide
    if (isInViewport('end')){
        clearInterval(interval2);       //Stop checking for this slide
        do2();
    }
}
function check3(){              // Constantly check whether or not to animate 3rd Slide
    if (isInViewport('end')){
        clearInterval(interval3);       //Stop checking for this slide
        do3();
    }
}
function check4(){              // Constantly check whether or not to animate 4th Slide
    if (isInViewport('end')){
        clearInterval(interval4);       //Stop checking for this slide
        do4();
    }
}
function check5(){              // Constantly check whether or not to animate 5th Slide
    if (isInViewport('end')){
        clearInterval(interval5);       //Stop checking for this slide
        do5();
    }
}
function check6(){              // Constantly check whether or not to animate 6th Slide
    if (isInViewport('end')){
        clearInterval(interval6);       //Stop checking for this slide
        do6();
    }
}



$(document).ready(function(){           // Initiate the animations
    $('div#1').slideDown("slow", "linear");
    interval2 = setInterval(function(){check2()}, 2000);
})