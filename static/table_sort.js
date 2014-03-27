$(document).ready(function() {
  $(".table_header").on( "click", function() {
    $.ajax({
      type: "GET",
      url: "/sorted/" + this.id,
      success: function(response) {
        $("#victims_list").html(response);
      }
    });
    return false;
  });
});