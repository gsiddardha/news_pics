<?
function getTerms($context) {
  $ch = curl_init();
  $url = "http://search.yahooapis.com/ContentAnalysisService/V1/termExtraction";
  $fields = array(
    'appid' => urlencode('HekkaB6s'),
    'context' => urlencode($context),
    'output' => urlencode('json')
  );
  
  foreach($fields as $key=>$value) {$fields_string .= $key.'='.$value.'&';}
  rtrim($fields_string,'&');
  
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_POST, count($fields));
  curl_setopt($ch, CURLOPT_POSTFIELDS, $fields_string);
  
  $result = curl_exec($ch);
  curl_close($ch);
  
  return $result;
}

?>
