(function($) {

  function updateSum(a, b) {
    const $r = $('#r');
    $r.text(a + b);
  }

  $(function() {
    const $a = $('#a');
    const $b = $('#b');

    var a, b = undefined;

    //listen for changes
    $a.keyup(function(){
      a = parseInt($(this).val());
      updateSum(a, b);
    });

    $b.keyup(function(){
      b = parseInt($(this).val());
      updateSum(a, b);
    });

  });

})(jQuery);
