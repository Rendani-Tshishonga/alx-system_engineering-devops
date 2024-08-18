# A puppet script to automate the replacing of a word

exec {'Replace text':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path    => '/usr/bin:/bin',
}
