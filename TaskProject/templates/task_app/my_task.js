
// window.alert("I am here")

// const app = Vue.createApp({
//     template:""
// });

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