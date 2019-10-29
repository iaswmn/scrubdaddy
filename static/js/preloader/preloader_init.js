document.body.classList.add('render');

document.addEventListener('DOMContentLoaded', function() {

    setTimeout(function() {
        document.body.classList.add('completed');
        var preloader = document.querySelector('.loader-wrapper');
        preloader.remove();
        }, 1500);

});