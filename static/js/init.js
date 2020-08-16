(function ($) {
    $(function () {
        $(".sidenav").sidenav();
        $(".parallax").parallax();
        $("select").formSelect();
        $(".modal").modal();
        $(".dropdown-trigger").dropdown();

        /** Make header sticky after scroll y amount */
        $(window).scroll(function() {
            // Track scroll amount
            let yPos = ( $(window).scrollTop() );
            // Get header height
            let headerHeight = ( $('header').outerHeight() );

            //When scroll is greater than header
            if(yPos > headerHeight ) { 
                $('header').addClass('sticky');       
            }
            else {
                $('header').removeClass('sticky');
            }
        });

    }); // end of document ready
})(jQuery); // end of jQuery name space
