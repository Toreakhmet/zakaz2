document.addEventListener("DOMContentLoaded", function() {
    const addMoreFieldsButton = document.getElementById("addMoreFields");
    const extraFieldsContainer = document.getElementById("extraFieldsContainer");
    let fieldCount = 1; // Счетчик полей

    addMoreFieldsButton.addEventListener("click", function() {
        // Создаем новый input элемент
        const newInput = document.createElement("input");
        
        // Устанавливаем нужные атрибуты для input
        newInput.type = "file";
        newInput.name = `file${fieldCount + 20}`; // Допустим, что изначальные поля называются file1, file2, ..., file20
        newInput.id = `file${fieldCount + 20}`;
        
        // Добавляем новый input элемент в контейнер
        extraFieldsContainer.appendChild(newInput);

        // Обновляем счетчик полей
        fieldCount++;
    });
});
    