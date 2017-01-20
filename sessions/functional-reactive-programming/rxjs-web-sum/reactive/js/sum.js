(function($) {

  function currentTextOf($input) {
    // Creates Stream
    const sKeyPresses = Rx.Observable.fromEvent($input, 'keyup');
    // Creates Cell from Stream events
    const text = new Rx.BehaviorSubject($input.val());
    sKeyPresses.map(function (e) { return $input.val(); }).subscribe(text);
    return text;
  }

  function toInt(text) {
    return parseInt(text);
  }

  $(function() {
    const $a = $('#a');
    const $b = $('#b');
    const $r = $('#r');

    // Creates Cells of ints from a Cell of strings modified on each keyup
    const a = currentTextOf($a).map(toInt);
    const b = currentTextOf($b).map(toInt);

    // merges into a single Cell
    var c = a.combineLatest(b, function(aa, bb) { return aa + bb; });

    // Subscribes to update UI
    c.subscribe(function(r) { $r.text(r); });
  });

})(jQuery);
