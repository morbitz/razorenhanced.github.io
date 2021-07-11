
function main(){
    document.addEventListener("DOMContentLoaded", bindActions);
    
    scrollToAnchor();
}

function scrollToAnchor(){
    let url = document.location.href;
    let parts = url.split('#');
    if (parts.length != 2 ) return false;
    let anchor = '#'+parts[1];
    if ( anchor.length > 0 ){
        let anchor_link =  document.getElementById(anchor);
        if (anchor_link != null){
            anchor_link.scrollIntoView();
            //anchor_link.scrollIntoView({ behavior: 'smooth'});
        }
        
    }
    return true;
}

function bindActions(){
    var titles = document.getElementsByClassName("redoc-property-title");
    for (let title_num in titles){
        title = titles[title_num];
        title.onclick = toggleOpenClose;
    }
}

function toggleOpenClose(sender){
    var parent = sender.currentTarget.parentNode;
    while (parent != null && !parent.classList.contains("redoc-collapsable-container") ) {
        parent = parent.parentNode;
    }
    if (!parent){ return false; }
    
    if (parent.classList.contains("open-container")){
        parent.classList.remove("open-container");
        parent.classList.add("closed-container");
    }else if (parent.classList.contains("closed-container")){
        parent.classList.remove("closed-container");
        parent.classList.add("open-container");
    }
    return true;
}



main();