function Comment(){
  var comment = $("#comments").val();
  var userComments = $("#UserComments");
  if (comment != ""){
    userComments.text(comment);
  } else {
    alert("Please enter in a comment before clicking the OK button.")
  }
}

function SetUp(){
  $("#comments_button").click(Comment);
}

$(document).ready(SetUp);
