$(document).ready(function(){
    $(".confirmar-borrado").on("click", function(e){
       e.preventDefault();
       var form = $(this).parents("form");

       Swal.fire({
           title: "Are you sure?",
           text: "You are going to delete the element, you won't be able to revert this!",
           type: "warning",
           showCancelButton: true,
           confirmButtonColor: "#3085d6",
           cancelButtonColor: "#d33",
           confirmButtonText: "Yes, delete it!",
           closeOnConfirm: false
       }).then((result) => {
           if(result.value){
               form.submit();
           }
       });
    });
});