<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rasmnout AGENT</title>
    <style>
        body {
            background-color: black;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }

        .white-frame {
            background-color: black;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: center;
            margin-top: 30px;
            max-height: 80vh;
            overflow-y: auto;
        }
        @font-face {
            font-family: 'ProFont';
            src: url('fonttext.ttf') format('truetype');
        }
        #page-title {
            font-family: 'ProFont', sans-serif;
            font-size: 35px;
            font-weight: bold;
            color: white;
            margin-bottom: 20px;
        }

        .folder-button, .file-button {
            font-family: 'ProFont', sans-serif;
            display: block;
            margin: 10px;
            padding: 10px;
            border-radius: 8px;
            text-align: center;
            text-decoration: none;
            cursor: pointer;
            transition: background-color 0.3s, color 0.3s;
        }

        .folder-button {
            color: white;
            background-color: #aaaaaa;
        }

        .file-button {
            color: white;
            background-color: #6e6e6e;
        }

        .folder-button:hover, .file-button:hover {
            background-color: white;
            color: black;
        }
    </style>
</head>
<body>
    <div class="white-frame">
        <div id="page-title">Rasmnout Explorer</div>

        <?php
            $directory = "/rasmnout/bin";
            $contents = array_diff(scandir($directory), array('..', '.'));

            foreach ($contents as $item) {
                $itemPath = $directory . '/' . $item;

                if ($item === 'index.php' || $item === 'index.html' || $item === 'home.php' || $item === '__rasmnoutFile_http_starter.py' || $item === 'fonttext.ttf') {
                    continue;
                }

                if (is_dir($itemPath)) {
                    echo '<a href="http://' . $_SERVER['HTTP_HOST'] . ':8080/' . htmlspecialchars($item) . '" class="folder-button">' . htmlspecialchars($item) . '</a>';
                } else {
                    echo '<a href="http://' . $_SERVER['HTTP_HOST'] . ':8080/' . htmlspecialchars($item) . '" class="folder-button">' . htmlspecialchars($item) . '</a>';
                }
            }
        ?>
        <script>
            function updatePageTitle() {
            var pageTitle = document.getElementById('pageTitle');
                pageTitle.textContent = window.location.hostname;
            }
            updatePageTitle();
        </script>
    </div>
</body>
</html>
