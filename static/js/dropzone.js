

document.addEventListener("DOMContentLoaded", () => {
    const dropzone = document.getElementById("dropzone");
    const input = document.getElementById("imageInput");
    const preview = document.getElementById("preview");

    if (!dropzone || !input || !preview) return;

    dropzone.addEventListener("click", () => input.click());

    dropzone.addEventListener("dragover", (e) => {
        e.preventDefault();
        dropzone.classList.add("dragover");
    });

    dropzone.addEventListener("dragleave", () => {
        dropzone.classList.remove("dragover");
    });

    dropzone.addEventListener("drop", (e) => {
        e.preventDefault();
        dropzone.classList.remove("dragover");
        input.files = e.dataTransfer.files;
        showPreview(input.files[0]);
    });

    input.addEventListener("change", () => {
        if (input.files.length > 0) {
            showPreview(input.files[0]);
        }
    });

    function showPreview(file) {
        if (!file.type.startsWith("image/")) return;

        const reader = new FileReader();
        reader.onload = (e) => {
            preview.innerHTML = `<img src="${e.target.result}" alt="Podgląd">`;
        };
        reader.readAsDataURL(file);
    }
});
