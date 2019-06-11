(function($) {

  $(document).ready(function() {

    function setLevelValues(min, max) {
      const $levelDropdown = $('#id_widget-0-level')

      $levelDropdown.val(max)
      $levelDropdown.attr({
        "min": min, 
        "max": max
      })
      $levelDropdown.data('min', min)
      $levelDropdown.data('max', parseInt(max))
    }

    function setDefaultLevelDropdown() {
      const $totalLevelDrowpdown = $('#id_widget-0-total_level')
      const max = $totalLevelDrowpdown.val()

      if ($('body:contains("Añadir Agente")').length > 0) {
        setLevelValues(1, max)
      }
      addLevelHelpermImage(max)

    }

    function addLevelHelpermImage(level) {
      const $widgetContainer = $('#widget-group')
      const $imageHelper = $('<img />').attr("src", '/static/img/' + level + '-widget-complete.png')
      const $imageContainer = $('<div class="level-helper-img-container"></div>').html($imageHelper)
      $('.level-helper-img-container').remove()
      $widgetContainer.after($imageContainer)
    }
  
    function initListeners() {
  
      // Agent form total level selector
      $('body').on('change', '#id_widget-0-total_level', function(e){
        const max = e.target.value
        setLevelValues(1, max)
        addLevelHelpermImage(max)
      })

      // Agent form level number input
      $('body').on('input', '#id_widget-0-level', function(e) {
        const value = e.target.value
        if (value > $(this).data('max')) {
          $(this).val($(this).data('max'))
        }
        
        if (value < 0) {
          $(this).val($(this).data('min'))
        }
      })
    }
  
    function init() {
      initListeners()

      setDefaultLevelDropdown()
    }
  
    init()
  });
  
}(django.jQuery))