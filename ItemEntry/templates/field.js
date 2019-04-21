/**
 * On: focus blur => Floating label
 * Based on http://jsfiddle.net/RyanWalters/z9ymd852/
 */
$('.is-floating-label input, .is-floating-label textarea').on('focus blur', function (e) {
  $(this).parents('.is-floating-label').toggleClass('is-focused', (e.type === 'focus' || this.value.length > 0));
}).trigger('blur');