# config that will fix Apache2 server error using puppet
exec {'fix apache server error':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path    => '/bin/:/usr/bin/',
    }
