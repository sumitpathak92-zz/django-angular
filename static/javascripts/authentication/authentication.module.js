(function () {
  'use strict';

  angular
    .module('thinkster.authentication', [
      'thinkster.authentication.controllers',
      'thinkster.authentication.services'
    ]); //defines modules with its dependencies

  angular
    .module('thinkster.authentication.controllers', []);

  angular
    .module('thinkster.authentication.services', ['ngCookies']);
})();