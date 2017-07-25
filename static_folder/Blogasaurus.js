function Comment(){
  var comment = $("#comments").val();
  var userComments = $("#UserComments");
  var newClick = 0
  var newLine = $("p");
  var newerLine = $("h5")
  if (comment != ""){
    for (newClick; newClick < 1; newClick++){
      userComments.append(newLine)
      userComments.append(comment)
    }
  } else {
    alert("Please enter in a comment before clicking the OK button.")
  }
}

function SetUp(){
  $("#comments_button").click(Comment);
}

$(document).ready(SetUp);
