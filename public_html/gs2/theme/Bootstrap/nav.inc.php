<?php if(!defined('IN_GS')){ die('you cannot load this page directly.'); } ?>
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <a class="navbar-brand" href="#">Nasza klasa</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#nawigacja" aria-controls="nawigacja" aria-expanded="false" aria-label="Toggle navigation">
         <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="nawigacja">
         <ul class="navbar-nav m-auto">
          <?php get_i18n_navigation(return_page_slug(), 0, 0, I18N_SHOW_NORMAL, $component='bs_menu'); ?>
         </ul>
         <form class="form-inline my-2 my-lg-0">
            <input class="form-control mr-sm-2" type="search" placeholder="Szukaj" aria-label="Szukaj">
            <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Szukaj</button>
         </form>
      </div>
   </nav>