# A manifest file to remedy failed requests

exec {'configure ulimit':
    command => 'sed -i s/15/4096/ /etc/default/nginx && service nginx restart',
    path    => '/usr/bin:/bin'
}
