(function () {
  'use strict';

  angular
    .module('authentication', [
      'authentication.controllers',
      'authentication.services'
    ]); //defines modules with its dependencies

  angular
    .module('authentication.controllers', []);

  angular
    .module('authentication.services', ['ngCookies']);
})();