document.addEventListener("DOMContentLoaded", function() {
  // Анимация для заголовка
  typeAnimation(document.querySelector('.banner h2'), "Добро пожаловать на образовательный портал!", 50);
  
  // Анимация для параграфа
  typeAnimation(document.querySelector('.banner p'), "Начните своё образование с нами", 50);
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
