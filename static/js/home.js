document.addEventListener("DOMContentLoaded", function() {
  // Анимация для заголовка
  typeAnimation(document.querySelector('.banner h2'), "Welcome to the Educational Portal", 50);
  
  // Анимация для параграфа
  typeAnimation(document.querySelector('.banner p'), "Your gateway to world-class online learning", 50);
});

function typeAnimation(element, text, speed) {
  let i = 0;
  
  function type() {
    if (i < text.length) {
      element.innerHTML += text.charAt(i);
      i++;
      setTimeout(type, speed);
    }
  }
  
  type();
}
