$(document).ready(function(){
  $(".form").submit(function(){
    var choice = $("input[name="+this.id+"]:checked").val();
    $.ajax({
      url: "/vote/",
      data: {
        'choice': choice
      }
    })
    .done(function(data){
      alert("Thanks for voting!");
    });
  })
})
