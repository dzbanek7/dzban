<?php if(!defined('IN_GS')){ die('you cannot load this page directly.'); } ?>
	<?php
	  $bc = return_i18n_breadcrumbs(return_page_slug());
	  $slug = $bc[0]['url'];
	  $pages = return_i18n_pages();
	  //print_r($pages);
	  if (@$pages[$slug]['children']) {
	    echo '<h3>'.$bc[0]['menu'].'</h3>';
	    echo '<ul>';
	    get_i18n_navigation(return_page_slug(),1,99);
	    echo '</ul>';
	  }
	?>
	<h3>Zobacz również</h3>
	<?php get_component('linki');  ?>