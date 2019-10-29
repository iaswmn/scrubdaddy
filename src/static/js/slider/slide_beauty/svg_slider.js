'use strict';

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

/**
 * demo2.js
 * http://www.codrops.com
 *
 * Licensed under the MIT license.
 * http://www.opensource.org/licenses/mit-license.php
 *
 * Copyright 2017, Codrops
 * http://www.codrops.com
 */
{
    // From https://davidwalsh.name/javascript-debounce-function.
    var debounce = function debounce(func, wait, immediate) {
        var timeout;
        return function () {
            var context = this,
                args = arguments;
            var later = function later() {
                timeout = null;
                if (!immediate) func.apply(context, args);
            };
            var callNow = immediate && !timeout;
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
            if (callNow) func.apply(context, args);
        };
    };



    var Slideshow = function () {
        function Slideshow(el) {
            _classCallCheck(this, Slideshow);

            this.DOM = {};
            this.DOM.el = el;
            this.settings = {
                animation: {
                    slides: {
                        duration: 600,
                        easing: 'easeOutQuint'
                    },
                    shape: {
                        duration: 300,
                        easing: { in: 'easeOutQuad', out: 'easeOutQuad' }
                    }
                },
                frameFill: 'url(#gradient1)'
            };
            this.init();
        }

        _createClass(Slideshow, [{
            key: 'init',
            value: function init() {
                this.DOM.slides = Array.from(this.DOM.el.querySelectorAll('.slides > .slide'));
                this.slidesTotal = this.DOM.slides.length;
                this.DOM.nav = this.DOM.el.querySelector('.slidenav');
                this.DOM.nextCtrl = this.DOM.nav.querySelector('.slidenav__item--next');
                this.DOM.prevCtrl = this.DOM.nav.querySelector('.slidenav__item--prev');
                this.current = 0;
                this.slideHeight = 0;
                this.onGoingTouches = [];
                this.DOM.navBtns = [];
                this.timer = null;

                this.slideHeight = this.DOM.slides[this.current].getBoundingClientRect().height;

                this.DOM.el.setAttribute("style", "height:" + ( this.DOM.slides[this.current].querySelector('img').getBoundingClientRect().height ) + "px");

                this.createNavigation();
                this.createFrame();
                this.initEvents();
                this.updateHeight();
                this.createAutoScroll();

                var currentSlide = this.DOM.slides[this.current];


                if ( $.winWidth() <= 900 ) {


                    var slideImg = currentSlide.querySelector('img'),
                        slideImgMargin = parseInt(getComputedStyle(slideImg).marginTop),
                        imgHeight = slideImg.getBoundingClientRect().height,
                        textContent = currentSlide.querySelector('.grid').getBoundingClientRect().height,
                        navHeight = this.DOM.nav.getBoundingClientRect().height,
                        slideContentHeight = imgHeight + textContent + navHeight + slideImgMargin;




                    this.DOM.svg.setAttribute('viewbox', '0 0 ' + this.rect.width + ' ' + slideContentHeight );

                    this.rect.height = slideContentHeight;

                    this.DOM.el.setAttribute("style", "height:" + slideContentHeight + "px");

                } else if ( currentSlide.classList.contains('small-slide') ) {


                    var slideHeight = currentSlide.getBoundingClientRect().height,
                        headerHeight = document.querySelector('header').height,
                        slideContentHeight = slideHeight + headerHeight;

                    this.DOM.svg.setAttribute('viewbox', '0 0 ' + this.rect.width + ' ' + slideContentHeight );

                    this.rect.height = slideContentHeight;

                    this.DOM.el.setAttribute("style", "height:" + slideContentHeight + "px");
                }

            }
        },
            {
                key: 'createNavigation',
                value: function createNavigation() {
                    var _this = this;

                    if ( !this.slidesTotal || this.slidesTotal < 2) return false;

                    this.DOM.slides.forEach(function(slide, index){

                        var slideBtn = document.createElement("btn");

                        slideBtn.classList.add("navigation-btn");
                        slideBtn.setAttribute("data-index", index);

                        if ( _this.current === index ) slideBtn.classList.add("active");

                        _this.DOM.navBtns.push(slideBtn);
                        _this.DOM.nav.appendChild(slideBtn);

                    });

                }
            },
            {
                key: 'updateNavigation',
                value: function updateNavigation() {

                    var allBtns = this.DOM.nav.querySelectorAll(".navigation-btn"),
                        currentSlideBtn = this.DOM.nav.querySelector(".navigation-btn[data-index='" + this.current + "']");

                    allBtns.forEach(function(btn) {
                        btn.classList.remove("active");
                    });

                    currentSlideBtn.classList.add('active');
                }
            },
            {
                key: 'slideTo',
                value: function slideTo(slideIndex) {
                    var _this2 = this;


                    if ( this.current === slideIndex || this.isAnimating ) return false;

                    this.isAnimating = true;

                    if ( this.timer !== null ) {
                        clearInterval(this.timer);
                    }


                    var animateShapeInTimeline = anime.timeline({
                        duration: this.settings.animation.shape.duration,
                        easing: this.settings.animation.shape.easing.in
                    });
                    animateShapeInTimeline.add({
                        targets: this.DOM.shape,
                        d: this.paths.final.step1
                    }).add({
                        targets: this.DOM.shape,
                        d: this.paths.final.step2,
                        offset: '-=' + this.settings.animation.shape.duration * .5
                    }).add({
                        targets: this.DOM.shape,
                        d: this.paths.final.step3,
                        offset: '-=' + this.settings.animation.shape.duration * .5
                    }).add({
                        targets: this.DOM.shape,
                        d: this.paths.final.step4,
                        offset: '-=' + this.settings.animation.shape.duration * .5
                    });

                    var animateSlides = function animateSlides() {
                        return new Promise(function (resolve, reject) {
                            var currentSlide = _this2.DOM.slides[_this2.current];
                            anime({
                                targets: currentSlide,
                                duration: _this2.settings.animation.slides.duration,
                                easing: _this2.settings.animation.slides.easing,

                                translateX: _this2.current > slideIndex ?
                                    -1 * _this2.rect.width : _this2.rect.width,

                                complete: function complete() {
                                    currentSlide.classList.remove('slide--current');
                                    resolve();
                                }
                            });

                            _this2.current = slideIndex;

                            var newSlide = _this2.DOM.slides[slideIndex];
                            newSlide.classList.add('slide--current');
                            anime({
                                targets: newSlide,
                                duration: _this2.settings.animation.slides.duration,
                                easing: _this2.settings.animation.slides.easing,
                                translateX: [ _this2.current > slideIndex ? _this2.rect.width : -1 * _this2.rect.width, 0]
                            });

                            var newSlideImg = newSlide.querySelector('.slide__img');

                            anime.remove(newSlideImg);

                            anime({
                                targets: newSlideImg,
                                duration: _this2.settings.animation.slides.duration * 4,
                                easing: _this2.settings.animation.slides.easing,
                                translateX: [ _this2.current > slideIndex ? 200 : -200, 0]
                            });

                            var animateTargets = [];

                            var slideTitle = newSlide.querySelector('.title-h1');
                            var slideDescription = newSlide.querySelector('.description');
                            var slideBtn = newSlide.querySelector('.btn');

                            if ( slideTitle ) animateTargets.push(slideTitle);

                            if ( slideDescription ) animateTargets.push(slideDescription);

                            if ( slideBtn ) animateTargets.push(slideBtn);

                            if ( animateTargets.length ) {

                                anime({
                                    targets: animateTargets,
                                    duration: _this2.settings.animation.slides.duration * 2,
                                    easing: _this2.settings.animation.slides.easing,
                                    delay: function delay(t, i) {
                                        return i * 100 + 100;
                                    },
                                    translateX: [ _this2.current > slideIndex ? 300 : -300, 0],
                                    opacity: [0, 1]
                                });

                            }

                        });
                    };

                    var animateShapeOut = function animateShapeOut() {
                        var animateShapeOutTimeline = anime.timeline({
                            duration: _this2.settings.animation.shape.duration,
                            easing: _this2.settings.animation.shape.easing.out
                        });
                        animateShapeOutTimeline.add({
                            targets: _this2.DOM.shape,
                            d: _this2.paths.final.step3
                        }).add({
                            targets: _this2.DOM.shape,
                            d: _this2.paths.final.step2,
                            offset: '-=' + _this2.settings.animation.shape.duration * .5
                        }).add({
                            targets: _this2.DOM.shape,
                            d: _this2.paths.final.step1,
                            offset: '-=' + _this2.settings.animation.shape.duration * .5
                        }).add({
                            targets: _this2.DOM.shape,
                            d: _this2.paths.initial,
                            offset: '-=' + _this2.settings.animation.shape.duration * .5,
                            complete: function complete() {
                                _this2.updateHeight();
                                _this2.isAnimating = false;

                                return _this2.createAutoScroll();
                            }
                        });
                    };

                    animateShapeInTimeline.finished.then(animateSlides).then(animateShapeOut);
                }
            },
            {
                key: 'createFrame',
                value: function createFrame() {
                    this.rect = this.DOM.el.getBoundingClientRect();
                    this.frameSize = this.rect.width / 12;
                    this.paths = {
                        initial: this.calculatePath('initial'),
                        final: this.calculatePath('final')
                    };
                    this.DOM.svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
                    this.DOM.svg.setAttribute('class', 'shape');
                    this.DOM.svg.setAttribute('width', '100%');
                    this.DOM.svg.setAttribute('height', '100%');




                    this.DOM.svg.setAttribute('viewbox', '0 0 ' + this.rect.width + ' ' + this.rect.height);


                    if ( $.winWidth() <= 1280 && parseInt(this.slideHeight) > $.winHeight() ) {

                        this.DOM.svg.setAttribute('viewbox', '0 0 ' + this.rect.width + ' ' + (this.slideHeight + 30));

                        this.rect.height = ( this.slideHeight + 30 );

                        this.paths = {
                            initial: this.calculatePath("initial"),
                            final: this.calculatePath("final")
                        }

                    } else if ( $.winWidth() <= 900 ) {

                        var currentSlide = this.DOM.slides[this.current],
                            slideImg = currentSlide.querySelector('img'),
                            imgHeight = slideImg.getBoundingClientRect().height,
                            slideImgMargin = parseInt(getComputedStyle(slideImg).marginTop),
                            textContent = currentSlide.querySelector('.grid').getBoundingClientRect().height,
                            navHeight = this.DOM.nav.getBoundingClientRect().height,
                            slideContentHeight = imgHeight + textContent + navHeight + slideImgMargin;


                        this.DOM.svg.setAttribute('viewbox', '0 0 ' + this.rect.width + ' ' + slideContentHeight );

                        this.rect.height = slideContentHeight;


                        this.DOM.el.setAttribute("style", "height:" + slideContentHeight + "px");


                        this.paths = {
                            initial: this.calculatePath("initial"),
                            final: this.calculatePath("final"),
                        };

                    } else {

                        this.paths.initial = this.calculatePath('initial');
                        this.paths.final = this.calculatePath('final');
                    }

                    this.DOM.svg.innerHTML = '\n                ' +
                        '<defs>\n                ' +
                        '<radialGradient id="gradient1" x1="0%" y1="0%" x2="0%" y2="100%">\n                    ' +
                        '<stop offset="29%" stop-color="#3789ff">\n                        ' +
                        '<!--animate attributeName="stop-color" values="#ED4264; #FFEDBC; #ED4264" dur="3s" repeatCount="indefinite"></animate-->\n                    ' +
                        '</stop>\n                    <stop offset="49%" stop-color="#0042b7">\n                        ' +
                        '<!--animate attributeName="stop-color" values="#FFEDBC; #ED4264; #FFEDBC" dur="3s" repeatCount="indefinite"></animate-->\n                    ' +
                        '</stop>\n                ' +
                        '</radialGradient>\n                </defs>\n                <path fill="' + this.settings.frameFill + '" d="' + this.paths.initial + '"/>\n            ';
                    this.DOM.el.insertBefore(this.DOM.svg, this.DOM.nav);
                    this.DOM.shape = this.DOM.svg.querySelector('path');
                }
            },
            {
                key: 'updateHeight',
                value: function updateHeight() {

                    var _this = this,
                        currentSlide = this.DOM.slides[this.current],
                        isSmallSlide = currentSlide.classList.contains('small-slide');

                    if ( $.winWidth() < 900 ) {


                        if ( !isSmallSlide ) {
                            var slideImg = currentSlide.querySelector('img'),
                                slideImgMargin = parseInt(getComputedStyle(slideImg).marginTop),
                                imgHeight = slideImg.getBoundingClientRect().height,
                                textContent = currentSlide.querySelector('.grid').getBoundingClientRect().height,
                                navHeight = this.DOM.nav.getBoundingClientRect().height,
                                slideContentHeight = imgHeight + textContent + navHeight + slideImgMargin;
                        }

                        this.rect.height = slideContentHeight;

                    }

                    _this.updateFrame();
                }
            },
            {
                key: 'updateFrame',
                value: function updateFrame() {

                    var slideHeight;

                    var _this = this,
                        currentSlide = this.DOM.slides[this.current],
                        isSmallSlide = currentSlide.classList.contains('small-slide'),
                        slideImg = currentSlide.querySelector('img');

                    if ( $.winWidth() <= 900 ) {

                        var slideImgMargin = parseInt(getComputedStyle(slideImg).marginTop),
                            imgHeight = slideImg.getBoundingClientRect().height,
                            textContent = currentSlide.querySelector('.grid').getBoundingClientRect().height,
                            navHeight = this.DOM.nav.getBoundingClientRect().height,
                            slideContentHeight = imgHeight + textContent + navHeight + slideImgMargin;

                        if ( isSmallSlide ) {

                            slideHeight = textContent + navHeight + slideImgMargin;

                        } else {

                            slideHeight = slideContentHeight;

                        }



                        this.rect.height = slideHeight;

                        anime({
                            targets: _this.DOM.rect,
                            height: slideHeight,
                            duration: _this.settings.animation.slides.duration,
                            easing: _this.settings.animation.slides.easing
                        });

                        anime({
                            targets: _this.DOM.el,
                            height: slideHeight,
                            duration: _this.settings.animation.slides.duration,
                            easing: _this.settings.animation.slides.easing
                        });


                        this.paths = {
                            initial: this.calculatePath("initial"),
                            final: this.calculatePath("final")
                        }

                    } else {




                        if ( isSmallSlide || slideImg.getBoundingClientRect().height > $.winHeight() ) {

                            slideHeight = $.winHeight();

                        } else {

                            slideHeight = slideImg.getBoundingClientRect().height;

                        }


                        this.rect.height = slideHeight;


                        anime({
                            targets: _this.DOM.el,
                            height: slideHeight,
                            duration: _this.settings.animation.slides.duration,
                            easing: _this.settings.animation.slides.easing
                        });


                        this.paths = {
                            initial: this.calculatePath("initial"),
                            final: this.calculatePath("final")
                        }

                    }

                    this.updateNavigation();

                    this.DOM.shape.setAttribute('d', this.paths.initial);
                }
            },
            {
                key: 'calculatePath',
                value: function calculatePath() {
                    var path = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : 'initial';


                    if (path === 'initial') {
                        return 'M 0,0 0,' + this.rect.height + ' ' + this.rect.width + ',' + this.rect.height + ' ' + this.rect.width + ',0 0,0 Z M 0,0 ' + this.rect.width + ',0 ' + this.rect.width + ',' + this.rect.height + ' 0,' + this.rect.height + ' Z';
                    } else {
                        return {
                            step1: 'M 0,0 0,' + this.rect.height + ' ' + this.rect.width + ',' + this.rect.height + ' ' + this.rect.width + ',0 0,0 Z M ' + this.frameSize + ',' + this.frameSize + ' ' + this.rect.width + ',0 ' + this.rect.width + ',' + this.rect.height + ' 0,' + this.rect.height + ' Z',
                            step2: 'M 0,0 0,' + this.rect.height + ' ' + this.rect.width + ',' + this.rect.height + ' ' + this.rect.width + ',0 0,0 Z M ' + this.frameSize + ',' + this.frameSize + ' ' + (this.rect.width - this.frameSize) + ',' + this.frameSize + ' ' + this.rect.width + ',' + this.rect.height + ' 0,' + this.rect.height + ' Z',
                            step3: 'M 0,0 0,' + this.rect.height + ' ' + this.rect.width + ',' + this.rect.height + ' ' + this.rect.width + ',0 0,0 Z M ' + this.frameSize + ',' + this.frameSize + ' ' + (this.rect.width - this.frameSize) + ',' + this.frameSize + ' ' + (this.rect.width - this.frameSize) + ',' + (this.rect.height - this.frameSize) + ' 0,' + this.rect.height + ' Z',
                            step4: 'M 0,0 0,' + this.rect.height + ' ' + this.rect.width + ',' + this.rect.height + ' ' + this.rect.width + ',0 0,0 Z M ' + this.frameSize + ',' + this.frameSize + ' ' + (this.rect.width - this.frameSize) + ',' + this.frameSize + ' ' + (this.rect.width - this.frameSize) + ',' + (this.rect.height - this.frameSize) + ' ' + this.frameSize + ',' + (this.rect.height - this.frameSize) + ' Z'
                        };
                    }
                }
            },
            {
                key: 'initEvents',
                value: function initEvents() {
                    var _this = this;

                    this.DOM.nextCtrl.addEventListener('click', function () {
                        return _this.navigate('next');
                    });
                    this.DOM.prevCtrl.addEventListener('click', function () {
                        return _this.navigate('prev');
                    });

                    window.addEventListener('resize', debounce(function () {
                        _this.rect = _this.DOM.el.getBoundingClientRect();
                        _this.updateHeight();
                    }, 20));

                    document.addEventListener('keydown', function (ev) {
                        var keyCode = ev.keyCode || ev.which;

                        if ( _this.timer !== null ) {
                            clearInterval(_this.timer);
                        }

                        if (keyCode === 37) {

                            _this.navigate('prev');

                        } else if (keyCode === 39) {

                            _this.navigate('next');

                        }
                    });

                    this.DOM.el.addEventListener('touchstart', function (evt) {

                        _this.onGoingTouches.push(evt.changedTouches[0]);
                    });

                    this.DOM.el.addEventListener("touchend", function(evt) {

                        if ( _this.timer !== null ) {
                            clearInterval(_this.timer);
                        }

                        _this.onGoingTouches.push(evt.changedTouches[0]);


                        var deltaX = _this.onGoingTouches[0].clientX - _this.onGoingTouches[1].clientX;


                        if ( deltaX > 30 ) {

                            _this.navigate('next');

                        } else if ( deltaX < -30 ) {

                            _this.navigate('prev');
                        }

                        _this.onGoingTouches = [];

                    });

                    if ( this.DOM.navBtns.length ) {

                        this.DOM.navBtns.forEach(function(btn) {
                            btn.addEventListener("click", function () {

                                if ( _this.timer !== null ) {
                                    clearInterval(_this.timer);
                                }
                                _this.slideTo(+this.getAttribute('data-index'));
                            });
                        });

                    }
                }
            },
            {
                key: 'navigate',
                value: function navigate() {
                    var _this2 = this;

                    var dir = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : 'next';

                    if (this.isAnimating ) return false;

                    if ( this.timer !== null ) {
                        clearInterval(this.timer);
                    }

                    this.isAnimating = true;


                    var animateShapeInTimeline = anime.timeline({
                        duration: this.settings.animation.shape.duration,
                        easing: this.settings.animation.shape.easing.in
                    });
                    animateShapeInTimeline.add({
                        targets: this.DOM.shape,
                        d: this.paths.final.step1
                    }).add({
                        targets: this.DOM.shape,
                        d: this.paths.final.step2,
                        offset: '-=' + this.settings.animation.shape.duration * .5
                    }).add({
                        targets: this.DOM.shape,
                        d: this.paths.final.step3,
                        offset: '-=' + this.settings.animation.shape.duration * .5
                    }).add({
                        targets: this.DOM.shape,
                        d: this.paths.final.step4,
                        offset: '-=' + this.settings.animation.shape.duration * .5
                    });

                    var animateSlides = function animateSlides() {
                        return new Promise(function (resolve, reject) {
                            var currentSlide = _this2.DOM.slides[_this2.current];
                            anime({
                                targets: currentSlide,
                                duration: _this2.settings.animation.slides.duration,
                                easing: _this2.settings.animation.slides.easing,
                                translateX: dir === 'next' ? -1 * _this2.rect.width : _this2.rect.width,
                                complete: function complete() {
                                    currentSlide.classList.remove('slide--current');
                                    resolve();
                                }
                            });

                            _this2.current = dir === 'next' ?
                                _this2.current < _this2.slidesTotal - 1 ?
                                    _this2.current + 1 :
                                    0 :
                                _this2.current > 0 ?
                                    _this2.current - 1 :
                                    _this2.slidesTotal - 1;

                            var newSlide = _this2.DOM.slides[_this2.current];
                            newSlide.classList.add('slide--current');
                            anime({
                                targets: newSlide,
                                duration: _this2.settings.animation.slides.duration,
                                easing: _this2.settings.animation.slides.easing,
                                translateX: [dir === 'next' ? _this2.rect.width : -1 * _this2.rect.width, 0]
                            });

                            var newSlideImg = newSlide.querySelector('.slide__img');
                            anime.remove(newSlideImg);
                            anime({
                                targets: newSlideImg,
                                duration: _this2.settings.animation.slides.duration * 4,
                                easing: _this2.settings.animation.slides.easing,
                                translateX: [dir === 'next' ? 200 : -200, 0]
                            });

                            var animateTargets = [];

                            var slideTitle = newSlide.querySelector('.title-h1');
                            var slideDescription = newSlide.querySelector('.description');
                            var slideBtn = newSlide.querySelector('.btn');

                            if ( slideTitle ) animateTargets.push(slideTitle);

                            if ( slideDescription ) animateTargets.push(slideDescription);

                            if ( slideBtn ) animateTargets.push(slideBtn);

                            if ( animateTargets.length ) {

                                anime({
                                    targets: animateTargets,
                                    duration: _this2.settings.animation.slides.duration * 2,
                                    easing: _this2.settings.animation.slides.easing,
                                    delay: function delay(t, i) {
                                        return i * 100 + 100;
                                    },
                                    translateX: [dir === 'next' ? 300 : -300, 0],
                                    opacity: [0, 1]
                                });

                            }

                        });
                    };

                    var animateShapeOut = function animateShapeOut() {
                        var animateShapeOutTimeline = anime.timeline({
                            duration: _this2.settings.animation.shape.duration,
                            easing: _this2.settings.animation.shape.easing.out
                        });
                        animateShapeOutTimeline.add({
                            targets: _this2.DOM.shape,
                            d: _this2.paths.final.step3
                        }).add({
                            targets: _this2.DOM.shape,
                            d: _this2.paths.final.step2,
                            offset: '-=' + _this2.settings.animation.shape.duration * .5
                        }).add({
                            targets: _this2.DOM.shape,
                            d: _this2.paths.final.step1,
                            offset: '-=' + _this2.settings.animation.shape.duration * .5
                        }).add({
                            targets: _this2.DOM.shape,
                            d: _this2.paths.initial,
                            offset: '-=' + _this2.settings.animation.shape.duration * .5,
                            complete: function complete() {
                                _this2.updateHeight();
                                _this2.isAnimating = false;

                                return _this2.createAutoScroll();
                            }
                        });
                    };

                    animateShapeInTimeline.finished.then(animateSlides).then(animateShapeOut);

                }
            },
            {
                key: 'createAutoScroll',
                value: function createAutoScroll() {
                    if ( this.isAnimating ) {
                        clearInterval(this.timer);
                        return false;
                    }

                    var _this = this;

                    this.timer = setInterval(function() {

                        _this.navigate('next');

                    }, 8000);

                }
            }
        ]);

        return Slideshow;
    }();

    imagesLoaded('.slide__img', { background: true }, function () {
        new Slideshow(document.querySelector('.slideshow'));
        return document.body.classList.remove('loading');
    });
}