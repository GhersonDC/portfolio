fetch('json/repos.json')
  .then((res) => res.json())
  .then((data) => {
    let output = '';
    data.forEach(function (repo) {
      output += `<!--repo card started--><div class="col-sm-4 mb-40" id="repo-size"><div class="mdl-card mdl-shadow--2dp pa-0 repo-card"><div class="mdl-card__title pa-0"><img class="blog-img"loading="lazy"src="${
        repo.banner
      }"></div><div class="mdl-card__supporting-text relative"><span class="blog-cat" style="${
        repo.lang ? '' : 'display: none'
      };"><span class="lang"style="background-color: ${
        repo.color
      };"></span><span>${repo.lang}</span></span><a href="${
        repo.url
      }" target="_blank" rel="noopener noreferrer"><h4 class="mt-15 mb-20">${repo.name}</h4></a><p>${
        repo.description
      }</p><a href="${
        repo.url
      }" target="_blank" rel="noopener noreferrer" class="mdl-button mdl-js-button mdl-button--fab mdl-js-ripple-effect bg-blue mdl-shadow--8dp"data-upgraded="MaterialButton,MaterialRipple"><i class="zmdi zmdi-cloud-download"></i><span class="mdl-button__ripple-container"><span class="mdl-ripple"></span></span></a></div><div class="mdl-card__actions mdl-card--border">
      </span></div></div></div></div><!--repo card ended-->`;
    });
    document.getElementById('repo-card').innerHTML = output;
  });
