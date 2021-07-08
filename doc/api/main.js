
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
    
}





main();