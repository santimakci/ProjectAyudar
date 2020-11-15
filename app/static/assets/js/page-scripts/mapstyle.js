$($(window).resize(
    function () {
        var $winH = $(this).height();
        var $winW = $(this).width();

        if (1000 < $winW) {
            $('.mapboxgl-canvas').width("650px");
            $('.mapboxgl-canvas').height("470px");
            $('#mapid').width("650px");
            $('#mapid').height("470px");
        } else if (768 < $winW) {
            $('.mapboxgl-canvas').width("450px");
            $('.mapboxgl-canvas').height("470px");
            $('#mapid').width("450px");
            $('#mapid').height("470px");
            $('.botones').css("padding-top", "");
        } else {
            $('.botones').css("padding-top", "120px");
            $('#mapid').width($winW - 150);
            $('#mapid').height($winH - 100);
            $('.mapboxgl-canvas').width($winW - 150);
            $('.mapboxgl-canvas').height($winH - 100);
        }
    }
))