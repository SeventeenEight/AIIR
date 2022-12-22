<html>
    <head>
        <title>KR_Gorokhov</title>
    </head>
    <body>
        <h2>Remove punctuation marks</h2>
        <h3>String without punctuation marks</h3>
        <?php
            if (isset($_POST['s'])){
                $myCurl = curl_init();
                curl_setopt_array(
                    $myCurl,
                    array(
                        CURLOPT_URL => 'http://nginxserver/api/'.$_POST['s'],
                        CURLOPT_RETURNTRANSFER => true,
                        CURLOPT_HEADER => false,
                    )
                );
                $response = curl_exec($myCurl);
                curl_close($myCurl);
                var_dump($response);
//                 $include_code = response['include'];
//                 echo $include_code
//                 $fp = fopen(s, "w+");// открытие файла на запись[30]
//                 fwrite($fp, include_decode($include_code)); //запись в файл декодированных байтов[31]
//                 fclose($fp);// закрытие файла
//                 echo "Result: ".$include_code;
            }
        ?>
        <form action="index.php" method="post">
            <label for="s">Enter symbol: </label>
            <input placeholder="your symbol" type="text" name="s" id="s" required>
            <input type="submit" value="go!">
        </form>
    </body>
</html>
