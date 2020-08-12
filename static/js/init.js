(function ($) {
    $(function () {
        $(".sidenav").sidenav();
        $(".parallax").parallax();
        $("select").formSelect();
        $(".modal").modal();

        /** Make header sticky after scroll y amount */
        $(window).scroll(function() {
            // Track scroll amount
            let yPos = ( $(window).scrollTop() );
            console.log(yPos)
            // Get header height
            let headerHeight = ( $('header').outerHeight() );
            console.log(headerHeight)

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
