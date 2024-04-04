
// window.alert("I am here")

function filterTaskTable(e){
    var filterValue = $(this).val();

    if (filterValue === "") {
      // Show all rows
      $(".task-row").show();
    } else if (filterValue === "All") {
      // Show all rows (same as filterValue="")
      $(".task-row").show();
    } else {
      // Show rows with matching status
      $(".task-row").hide();
      $(".task-row[data-status='" + filterValue + "']").show();
    }
}

function onTitleChange(e){
  let title = $(this).val()

  $("#createTaskForm #create-task").addClass('disabled')

  if (title.length > 0){
    $("#createTaskForm #create-task").removeClass('disabled')
  }
}

function searchTaskByTitle(e){
  let filter_title = $(this).val().toLowerCase();

  $(".task-row").each(function() {
    var title = $(this).find(".task-title").text().toLowerCase(); // Target first column by default
    
    if (title.indexOf(filter_title) !== -1) {
      $(this).show();
    } else {
      $(this).hide();
    }
  });
}
