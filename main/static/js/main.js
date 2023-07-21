$(document).ready(function () {
    $("#phone").mask("+7 (999) 99-99-999");
    $(".banner__enrollInput").mask("+7 (999) 99-99-999");
    $('#slider').owlCarousel({
        loop: true,
        margin: 10,
        nav: true,
        dot: false,
        responsive: {
            0: {
                items: 1
            },
            700: {
                items: 2
            },
            1000: {
                items: 2
            }
        }
    });
    $('#aboutSlider').owlCarousel({
        loop: true,
        margin: 55,
        nav: true,
        dot: false,
        items: 1,
    });
    Fancybox.bind('[data-fancybox="gallery"]', {
        buttons: [
            'slideShow',
            'share',
            'zoom',
            'fullScreen',
            'close'
        ],
        thumbs: {
            autoStart: true
        }
    });
    $('.open').click(function () {
        $('#enrollWindow').fadeIn(300);
        $('body').css('overflow', 'hidden');
        let phone = $('.banner__enrollInput').val();
        if (phone != '')
            $('#phone').val(phone);
    });
    $('.enrollWindow__close').click(function () {
        $('#enrollWindow').fadeOut(300);
        $('body').css('overflow', 'auto');
    });
    $(document).mouseup(function (e) {
        let div = $(".enrollWindow__form");
        if (!div.is(e.target)
            && div.has(e.target).length === 0) {
            $('#enrollWindow').fadeOut(300);
            $('body').css('overflow', 'auto');
        }
    });

    function emailCheck(mail) {
        let reg = /^[a-z0-9_-]+@[a-z0-9-]+\.([a-z]{1,6}\.)?[a-z]{2,6}$/i;
        if (mail.search(reg) == 0)
            return 1;
        else
            return 0;
    }
    $("#sendpost").click(function () {
        let email = $(this).parent().find('input[type="email"]').val();
        let phone = $(this).parent().find('input[type="text"]').val();
        if (email != '' && emailCheck(email) && phone != '') {
            $.ajax({
                data: $(this).parent().serialize(),
                url: '/sendpost',
                success: function (response) {
                    $('#enrollWindow').fadeOut(0);
                    $('#sucsses').fadeIn(0);
                    setTimeout(function () {
                        $('.error_text').fadeOut(0);
                        $('#sucsses').fadeOut(300);
                        $('body').css('overflow', 'auto');
                    }, 3500);
                },
                // если ошибка, то
                error: function (response) {
                    // предупредим об ошибке
                    console.log(response.responseJSON.errors)
                }
            });
        }
        else
            $('.error_text').fadeIn(0);
    });
});

