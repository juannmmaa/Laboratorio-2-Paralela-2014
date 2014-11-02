function clickPaso2(indica) {
	$('#home').fadeOut(500);
	$('#contenido').delay(500).fadeIn(500);
	$('input[name=tipo]').val(indica);
	$('input[name=foto]').css({opacity:0});
	
	$('#red').nstSlider({
		"left_grip_selector": ".leftGrip",
		"value_bar_selector": ".bar",
		"value_changed_callback": function(cause, leftValue, rightValue) {
			var $container = $(this).parent(),
			g = 0,
			r = 0 + leftValue,
			b = 0;
			$container.find('.leftLabelR').text(leftValue);
			$('input[name=tonoR]').val(leftValue);
			$(this).find('.bar').css('background', 'rgb(' + [r, g, b].join(',') + ')');
		}
	});
	$('#green').nstSlider({
		"left_grip_selector": ".leftGrip",
		"value_bar_selector": ".bar",
		"value_changed_callback": function(cause, leftValue, rightValue) {
			var $container = $(this).parent(),
			g = 0 + leftValue,
			r = 0,
			b = 0;
			$container.find('.leftLabelG').text(leftValue);
			$('input[name=tonoG]').val(leftValue);
			$(this).find('.bar').css('background', 'rgb(' + [r, g, b].join(',') + ')');
		}
	});
	$('#blue').nstSlider({
		"left_grip_selector": ".leftGrip",
		"value_bar_selector": ".bar",
		"value_changed_callback": function(cause, leftValue, rightValue) {
			var $container = $(this).parent(),
			g = 0,
			r = 0,
			b = 0 + leftValue;
			$container.find('.leftLabelB').text(leftValue);
			$('input[name=tonoB]').val(leftValue);
			$(this).find('.bar').css('background', 'rgb(' + [r, g, b].join(',') + ')');
		}
	});
	
	if (indica == 'paralelo') {
		$('#proces').show();
		$('#rango-proces').nstSlider({
			"left_grip_selector": ".leftGrip",
			"value_bar_selector": ".bar",
			"value_changed_callback": function(cause, leftValue, rightValue) {
				var $container = $(this).parent(),
				g = 255,
				r = 255,
				b = 255;
				$container.find('.labelProces').text(leftValue);
				$('input[name=proces]').val(leftValue);
				$(this).find('.bar').css('background', 'rgb(' + [r, g, b].join(',') + ')');
			}
		});
		$('#finform').click(function(e){
			if ($('input[name=filtro]').val() == "") {
				e.preventDefault();
				alert('Debes elegir un filtro');
			}
			else if ($('input[name=foto]').val().length < 3) {
				e.preventDefault();
				alert('Debes elegir una foto');
			}
		});
	} else {
		$('#finform').click(function(e){
			if ($('input[name=foto]').val().length < 3) {
				e.preventDefault();
				alert('Debes elegir una foto');
			}
		});
	}
}

var numFiltro = 0;

function clickFiltro(num) {
	if (numFiltro != 0) {
		$('#filtro' + numFiltro).removeClass('over');
	}
	numFiltro = num;
	$('#filtro' + num).addClass('over');
	$('input[name=filtro]').val(num);
}