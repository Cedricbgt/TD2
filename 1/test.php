<?php

require_once('../_helpers/strip.php');

// https://depthsecurity.com/blog/exploitation-xml-external-entity-xxe-injection

$xml = isset($_GET['xml']) && strlen($_GET['xml']) > 0 ? $_GET['xml'] : '<root><content>No XML found</content></root>';

$document = new DOMDocument();

// Use LIBXML_NOENT with caution and validate input
libxml_use_internal_errors(true);

if (!$document->loadXML($xml, LIBXML_NOENT | LIBXML_NOERROR | LIBXML_NOWARNING)) {
    echo "Error loading XML";
    foreach (libxml_get_errors() as $error) {
        echo "\n", $error->message;
    }
    libxml_clear_errors();
} else {
    $parsedDocument = simplexml_import_dom($document);
    echo htmlspecialchars($parsedDocument->content, ENT_QUOTES, 'UTF-8'); // Sanitize output to prevent XSS
}