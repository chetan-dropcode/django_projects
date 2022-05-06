

$(document).ready(function () {

    // Add scrollspy to <body>
    $('body').scrollspy({ target: ".navbar-nav", offset: 67 });

    // product
    $('#product-carousel').owlCarousel({
        loop: true,
        margin: 0,
        dots: false,
        autoplay: true,
        smartSpeed: 1000,
        nav: true,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 2
            },
            1000: {
                items: 4
            }
        }
    })

    $('#product1-carousel').owlCarousel({
        loop: true,
        margin: 0,
        dots: false,
        autoplay: true,
        smartSpeed: 1000,
        nav: true,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 1
            },
            1000: {
                items: 2
            }
        }
    })
});


