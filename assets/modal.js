var modal = document.getElementsByClassName("modal-summary")[0];
var aboutmodal = document.getElementsByClassName("modal-about")[0];
var contactmodal = document.getElementsByClassName("modal-contact")[0];
var projectsmodal = document.getElementsByClassName("modal-projects")[0];

// Get the buttons and links that opens the modals
var btn = document.getElementById("myBtn");
var about_navlink = document.getElementById("nav-link-about");
var contact_navlink = document.getElementById("nav-link-contact");
var projects_navlink = document.getElementById("nav-link-projects");

// Get the <button> elements that closes the modal
var closebutton = document.getElementsByClassName("btn-close")[0];
var closebutton2 = document.getElementsByClassName("btn btn-secondary")[0];

// When the user clicks the button or links, open the corresponding modal 
btn.onclick = function() {
  modal.style.display = "block";
}
// about me modal
about_navlink.onclick = function() {
  aboutmodal.style.display = "block";
}
// contact modal
contact_navlink.onclick = function() {
  contactmodal.style.display = "block";
}
// projects modal
projects_navlink.onclick = function() {
  projectsmodal.style.display = "block";
}


// When the user clicks on <button> (x), close the modal
closebutton.onclick = function() {
  modal.style.display = "none";
}

// when user clicks on <button> (close) close the modal
closebutton2.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
  if (event.target == aboutmodal) {
    aboutmodal.style.display = "none";
  }

  if (event.target == contactmodal) {
    contactmodal.style.display = "none";
  }

  if (event.target == projectsmodal) {
    projectsmodal.style.display = "none";
  }
}