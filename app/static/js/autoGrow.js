function auto_grow(element) {
    element.style.height = "5px";
    element.style.height = (element.scrollHeight) + "px";
  }
window.onload = function() {
    const textarea = document.getElementById('italic');
    const tittle = document.getElementById('refresh')
    if (textarea) {
        auto_grow(textarea); 
        auto_grow(tittle);
    }
};