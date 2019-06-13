(function (){

  function getExponents(str) {
    return str.match(/\^\d+/)
  }

  function getExponentString(str) {
    const number = str.split('^')[1]
    return str.replace(/\^\d+/, '<sup>' + number + '</sup>')
  }

  function replaceAllExponents(el, exp) {
    return el.innerHTML.replace(/\^\d+/, exp)
  }

  function renderSup() {
    const $p = document.querySelectorAll('.columns.information .column > p')
    $p.forEach(function(el) {
      const exps = getExponents(el.innerHTML)
      if (exps) {
        exps.forEach(function(e) {
          const exs = getExponentString(e)
          el.innerHTML = replaceAllExponents(el, exs)
        })
      }
    })
  }

  function init() {
    renderSup()
  }

  init()

}())