<?php
if (isset($_GET['file'])) {
    $file = $_GET['file'];

    // ❌ VULNÉRABILITÉ : Pas de vérification des ".."
    $path = "uploads/" . $file; 
    
    if (file_exists($path)) {
        echo "<pre>" . htmlspecialchars(file_get_contents($path)) . "</pre>";
    } else {
        echo "File not found!";
    }
}
?>
