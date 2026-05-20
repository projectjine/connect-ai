<?php
/**
 * Theme functions for SocialLogicLab child theme.
 * Enqueues Google fonts, global CSS, and global JS.
 * Adds body class for premium‑content blur guard.
 */

// Exit if accessed directly.
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

/**
 * Enqueue Google Fonts – Playfair Display & Arimo.
 */
function stitch_load_google_fonts() {
    wp_enqueue_style(
        'stitch-google-fonts',
        'https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Arimo:wght@400;700&display=swap',
        [],
        null
    );
}
add_action( 'wp_enqueue_scripts', 'stitch_load_google_fonts' );

/**
 * Enqueue the global Stitch CSS & JS created by Antigravity.
 */
function stitch_enqueue_global_assets() {
    $theme_dir = get_stylesheet_directory_uri();
    // Global CSS
    wp_enqueue_style( 'stitch-global-css', $theme_dir . '/stitch-global.css', [], null );
    // Global JS – load in footer for better performance
    wp_enqueue_script( 'stitch-global-js', $theme_dir . '/stitch-global.js', [], null, true );
}
add_action( 'wp_enqueue_scripts', 'stitch_enqueue_global_assets' );

/**
 * Add a body class when the visitor does NOT have access to premium content.
 * Adjust capability check to match your membership plugin.
 */
function stitch_body_class_for_guard( $classes ) {
    // Example: using WordPress default capability; replace with your own logic.
    if ( ! current_user_can( 'read_private_posts' ) ) {
        $classes[] = 'stitch-blur-guard';
    }
    return $classes;
}
add_filter( 'body_class', 'stitch_body_class_for_guard' );
?>
