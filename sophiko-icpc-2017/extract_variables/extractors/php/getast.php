<?php require 'vendor/autoload.php';
ini_set('xdebug.max_nesting_level', 3000);

use PhpParser\Error;
use PhpParser\ParserFactory;

$code = '<?php  // some code';
$parser = (new ParserFactory)->create(ParserFactory::PREFER_PHP7);


$code = file_get_contents($argv[1], true);

	try {
	    $stmts = $parser->parse($code);
	    echo json_encode($stmts);
//       var_dump($stmts);
	} catch (Error $e) {
	        echo 'Parse Error: ', $e->getMessage();
	}
?>
