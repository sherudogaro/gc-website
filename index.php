<?php
// Simple router for local clean URL testing
$request = $_SERVER['REQUEST_URI'];
$path = parse_url($request, PHP_URL_PATH);

// Remove leading slash
$path = ltrim($path, '/');

// Map clean URLs to actual files
$routes = [
    '' => 'index.html',
    'strategy' => 'strategy.html',
    'performance' => 'performance.html', 
    'team' => 'team.html',
    'contact' => 'contact.html',
    'fees' => 'fees.html',
    'faq' => 'faq.html',
    'legal/terms' => 'legal/terms.html',
    'legal/privacy' => 'legal/privacy.html',
    'legal/disclaimer' => 'legal/disclaimer.html',
    'thank-you' => 'thank-you.html'
];

// Check if route exists
if (array_key_exists($path, $routes)) {
    $file = $routes[$path];
    if (file_exists($file)) {
        include $file;
        exit;
    }
}

// 404 if not found
http_response_code(404);
echo "<h1>404 Not Found</h1>";
echo "<p>The page you're looking for doesn't exist.</p>";
echo "<p><a href='/'>Return to Homepage</a></p>";
?>