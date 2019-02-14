function createSlick(){

	$(".center").not('.slick-initialized').slick({
      centerMode: true,
	  centerPadding: '5px',
	  slidesToShow: 3,
	  autoplay: true,
	  autoplaySpeed: 2000,
	  responsive: [
	    {
	      breakpoint: 768,
	      settings: {
	        arrows: false,
	        centerMode: true,
	        centerPadding: '30px',
	        slidesToShow: 3
	      }
	    },
	    {
	      breakpoint: 480,
	      settings: {
	        arrows: false,
	        centerMode: true,
	        centerPadding: '30px',
	        slidesToShow: 1
	      }
	    }
	  ]
});

}

$(".polojenie" ).on( "click", function() {
	$('#myModal').modal()
});




createSlick();

$(window).on( 'resize', createSlick );