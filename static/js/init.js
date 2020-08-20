(function ($) {
    $(function () {
        $(".sidenav").sidenav();
        $(".parallax").parallax();
        $("select").formSelect();
        $(".modal").modal();
        $(".nav-dropdown-trigger").dropdown({
            coverTrigger: false
        });
        $("textarea#short_description, textarea#ingredients, textarea#method, textarea#nutrition, textarea#chef_notes").characterCounter();
        
        /* Validate Materialize select - script supplied by Code Institute */
        validateMaterializeselect();
        function validateMaterializeselect() {
            let classValid = { "border-bottom": "1px solid #4caf5e", "box-shadow": "0 1px 0 0 #4caf5e" };
            let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
            if ($("select.validate").prop("required")) {
                $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute", "opacity": "0", "left": "65px" });
            }
            $(".select-wrapper input.select-dropdown").on("focusin", function () {
                $(this).parent(".select-wrapper").on("change", function() {
                    if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                        $(this).children("input").css(classValid);
                    }
                });
            }).on("click", function(){
                if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                        $(this).parent(".select-wrapper").children("input").css(classvalid);
                } else {
                    $(".select-wrapper input.select-dropdown").on("focusout", function () {
                        if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                            if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                                $(this).parent(".select-wrapper").children("input").css(classInvalid);
                            }
                        }
                    });
                }
            });
        }

        /** End materialize select */

        /** Make header sticky after scroll y amount */
        $(window).scroll(function() {
            // Track scroll amount
            let yPos = ( $(window).scrollTop() );
            // Get header height
            let headerHeight = ( $('header').outerHeight() );

            //When scroll is greater than header
            if(yPos > (headerHeight + 25) ) { 
                $('header').addClass('sticky');       
            }
            else {
                $('header').removeClass('sticky');
            }
        });

    }); // end of document ready
})(jQuery); // end of jQuery name space
