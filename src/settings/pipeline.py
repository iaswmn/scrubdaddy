from ._pipeline import PIPELINE, Slider


PIPELINE['STYLESHEETS'].update({
    'critical': {
        'source_filenames': (
            'scss/grid.scss',
            'scss/layout.scss',
            'scss/buttons.scss',

            'header/scss/header.scss',
            'menu/scss/main_menu.scss',
            'css/preloader.css',
        ),
        'output_filename': 'css_build/critical.css',
    },
    'core': {
        'source_filenames': (
            'css/jquery.datetimepicker.css',
            'scss/forms.scss',
            'scss/preloader.scss',
            'scss/text_styles.scss',
            ) + Slider.css + (
            'scss/popups/popups.scss',
            'scss/popups/preloader.scss',
            'social_networks/scss/social_links.scss',
            'breadcrumbs/scss/breadcrumbs.scss',
            'rating/scss/rating.scss',
            'css/jquery-ui.css',
            
            'contacts/scss/block.scss',
            'contacts/scss/get_in_touch.scss',
            'footer/scss/footer.scss',
        ),
        'output_filename': 'css_build/head_core.css',
    },
    'fonts': {
        'source_filenames': (
            'fonts/kumizfy-italic/stylesheet.css',
            'fonts/museosans500/stylesheet.css',
            'fonts/museosans700/stylesheet.css',
            'fonts/museosans900/stylesheet.css',
        ),
        'output_filename': 'css_build/fonts.css',
        'template_name': 'pipeline/localstorage_css.html',
    },
    'error': {
        'source_filenames': (
            'scss/error_page.scss',
        ),
        'output_filename': 'css_build/error.css',
    },
    'main': {
        'source_filenames': (
            'css/slider_plugin/base.css',
            'css/slider_plugin/pater.css',
            'main/scss/index.scss',
        ),
        'output_filename': 'css_build/main.css',
    },
    'std_page_critical': {
        'source_filenames': (
            'std_page/scss/critical.scss',
        ),
        'output_filename': 'css_build/std_page_critical.css',
    },
    'std_page': {
        'source_filenames': (
            'std_page/scss/index.scss',
        ),
        'output_filename': 'css_build/std_page.css',
    },
    'about': {
        'source_filenames': (
            'css/swiper.css',
            'about/scss/index.scss',
        ),
        'output_filename': 'css_build/about.css',
    },
    'product': {
        'source_filenames': (
            'products/scss/index.scss',
        ),
        'output_filename': 'css_build/product.css',
    },
    'business_account': {
        'source_filenames': (
            'business_account/scss/index.scss',
        ),
        'output_filename': 'css_build/business_account.css',
    },
    'employment_opportunities': {
        'source_filenames': (
            'employment_opportunities/scss/index.scss',
        ),
        'output_filename': 'css_build/employment_opportunities.css',
    },
    'blog': {
        'source_filenames': (
            'blog/scss/index.scss',
            'blog/scss/detail.scss',
            'social_networks/scss/share_buttons.scss',
        ),
        'output_filename': 'css_build/blog.css',
    },
    'media': {
        'source_filenames': (
            'media/scss/index.scss',
        ),
        'output_filename': 'css_build/media.css',
    },
    'support': {
        'source_filenames': (
            'support/scss/index.scss',
        ),
        'output_filename': 'css_build/support.css',
    },
    'where_to_buy': {
        'source_filenames': (
            'where_to_buy/scss/index.scss',
            'flags/sprite.css',
        ),
        'output_filename': 'css_build/where_to_buy.css',
    },
    'contacts': {
        'source_filenames': (
            'google_maps/scss/label.scss',
            'contacts/scss/index.scss',
        ),
        'output_filename': 'css_build/contacts.css',
    },
    'get_in_touch': {
        'source_filenames': (
            'get_in_touch/scss/index.scss',
        ),
        'output_filename': 'css_build/get_in_touch.css',
    },
})

PIPELINE['JAVASCRIPT'].update({
    'core': {
        'source_filenames': (
            'polyfills/modernizr.js',
            'js/jquery-2.2.4.js',
            'js/jquery-ui.js',
            'js/jquery.requestanimationframe.js',

            'common/js/jquery.cookie.js',
            'common/js/jquery.utils.js',
            'common/js/jquery.ajax_csrf.js',

            'js/preloader/three.min.js',
            'js/preloader/fast-simplex-noise.js',
            'js/preloader/index.bundle.js',
            'js/preloader/preloader_init.js',
            'js/prevent_images_download.js',

            ) + Slider.js + (
            'js/plupload/plupload.full.min.js',
            'js/uploader.js',
            'js/datetimepicker.js',
            'js/jquery.datepicker.js',
            'js/popups/jquery.popups.js',
            'js/popups/preloader.js',
            'js/jquery.inspectors.js',
            'js/jquery.scrollTo.js',
            'js/jquery.fitvids.js',
            'js/text_styles.js',

            'attachable_blocks/js/async_blocks.js',
            'placeholder/js/placeholder.js',
            'contacts/js/popups.js',
            'menu/js/main_menu.js',
            'js/back_to_top.js',
            'js/tabs_counter.js',
            'js/jquery.masonry.min.js',
        ),
        'output_filename': 'js_build/core.js',
    },
    'main': {
        'source_filenames': (
            'js/slider/slide_beauty/preloader.js',
            'js/slider/slide_beauty/imagesloaded.pkgd.min.js',
            'js/slider/slide_beauty/anime.min.js',
            'js/slider/slide_beauty/svg_slider.js',
            'main/js/index.js',
        ),
        'output_filename': 'js_build/main.js',
    },
    'std_page': {
        'source_filenames': (
            'std_page/js/index.js',
        ),
        'output_filename': 'js_build/std_page.js',
    },
    'about': {
        'source_filenames': (
            'js/jquery.hints.js',
            'about/js/index.js',
        ),
        'output_filename': 'js_build/about.js',
    },
    'blog': {
        'source_filenames': (
            'blog/js/index.js',
        ),
        'output_filename': 'js_build/blog.js',
    },
    'media': {
        'source_filenames': (
            'media/js/index.js',
        ),
        'output_filename': 'js_build/media.js',
    },
    'product': {
        'source_filenames': (
            'products/js/index.js',
        ),
        'output_filename': 'js_build/product.js',
    },
    'support': {
        'source_filenames': (
            'support/js/list.js',
            'support/js/index.js',
        ),
        'output_filename': 'js_build/support.js',
    },
    'where_to_buy': {
        'source_filenames': (
            'where_to_buy/js/index.js',
            'where_to_buy/js/popups.js',
        ),
        'output_filename': 'js_build/where_to_buy.js',
    },
    'business_account': {
        'source_filenames': (
            'js/jSignature.min.js',
            'js/flashcanvas.js',
            'business_account/js/index.js',
        ),
        'output_filename': 'js_build/business_account.js',
    },
    'employment_opportunities': {
        'source_filenames': (
            'js/jSignature.min.js',
            'js/flashcanvas.js',
            'employment_opportunities/js/index.js',
        ),
        'output_filename': 'js_build/employment_opportunities.js',
    },
    'contacts': {
        'source_filenames': (
            'google_maps/js/core.js',
            'contacts/js/index.js',
        ),
        'output_filename': 'js_build/contacts.js',
    },
    'get_in_touch': {
        'source_filenames': (
            'get_in_touch/js/index.js',
        ),
        'output_filename': 'js_build/get_in_touch.js',
    },
})

