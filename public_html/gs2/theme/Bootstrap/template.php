<?php if(!defined('IN_GS')){ die('you cannot load this page directly.'); }
   include('header.inc.php');
   include('nav.inc.php');

?>


   <div class="container">
      <div class="row">
         <div class="col-md-8">
            <section class="my-4">
               <h2><?php get_page_title(); ?></h2>
               <?php get_page_content(); ?>
            </section>
         </div>
         <div class="col-md-4">
            <aside class="rounded p-2 text-md-right my-1 my-md-4">
               <?php include('sidebar.php'); ?>
            </aside>
         </div>
      </div>
   </div>

<?php include('footer.php'); ?>

</body>
</html>
