<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the web site, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * Localized language
 * * ABSPATH
 *
 * @link https://wordpress.org/support/article/editing-wp-config-php/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'u962107450_S7Uw0' );

/** Database username */
define( 'DB_USER', 'u962107450_BL6HF' );

/** Database password */
define( 'DB_PASSWORD', '\\iV|e.yT88' );

/** Database hostname */
define( 'DB_HOST', '127.0.0.1' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',          '8FrGDU$#Eb+Zo!R_@kfdoPEux6<SqI&EQj52jDG-y>g(tiR[i$#Rf=U`h*L[qhhE' );
define( 'SECURE_AUTH_KEY',   'OGMK.X}52=>v]ARwas RE?:wkgXGFxm#9k-k<Ab%wdg=$dwyAOdDq>47Fh5`Z%mo' );
define( 'LOGGED_IN_KEY',     '~7nBm,5%bHWl}(9)D^M4W>XYX[Iofi*L kt_HmiDZ9=}U0{J@+BhqCW5/rPk}}Lp' );
define( 'NONCE_KEY',         ')-^klApWYV&!_Tn=Iz>JQO;aXx`gv^yNrclX)9=]# CZ2E`/t!@m?Oo8vpv$f`^v' );
define( 'AUTH_SALT',         '/o9T|AAtB&sl^eg:*uG96|[H`{*I~<ePT*2LSAq}49rg--a(VQ -Y~@sEqBRrnIV' );
define( 'SECURE_AUTH_SALT',  '?H/<FCn=EIv]a{QuY(m0s?I-NHdL1YZ~xIVlj/H2Gu KCe+]vacAJnYV9*u EYNo' );
define( 'LOGGED_IN_SALT',    'pDPf@c05@Zd*I!*EL=o4l{? qKkqQ@d02(n5v}r~iI!93!bNFV9|C8_qgcUR3ew0' );
define( 'NONCE_SALT',        'WkX`ug9G2[^=HH>dJm(_Dfl8ysR4+r,]`Y<T/i]:Bm%=n=vjFv*bg-Wlop.-`,wE' );
define( 'WP_CACHE_KEY_SALT', ' eB!rX:tCVNB5|=`O*yRSaHiAT5r)C#u4Nwq%i&8/o3VZQlA>!u>uwL7s4z:POo,' );


/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 */
$table_prefix = 'wp_';


/* Add any custom values between this line and the "stop editing" line. */



/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://wordpress.org/support/article/debugging-in-wordpress/
 */
if ( ! defined( 'WP_DEBUG' ) ) {
	define( 'WP_DEBUG', false );
}

define( 'FS_METHOD', 'direct' );
define( 'COOKIEHASH', '840e474d77e7b5c6131cb14a23b55c65' );
define( 'WP_AUTO_UPDATE_CORE', 'minor' );
/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';
