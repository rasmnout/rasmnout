<?php

$host = $_SERVER['HTTP_HOST'];

$parts = explode(':', $host);
$hostWithoutPort = $parts[0];

?>
<script>
    window.location.href = "http://<?php echo $hostWithoutPort; ?>";
</script>
