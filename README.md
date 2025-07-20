# youtube-video-downloader

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YouTube Video Downloader</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        h1 {
            text-align: center;
        }
        form {
            max-width: 600px;
            margin: 0 auto;
            background: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        input[type="text"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        input[type="submit"] {
            background: #28a745;
            color: white;
            border: none;
            padding: 10px;
            border-radius: 5px;
            cursor: pointer;
            width: 100%;
        }
        input[type="submit"]:hover {
            background: #218838;
        }
        .error {
            color: red;
            margin-top: 10px;
            text-align: center;
        }
    </style>
</head>
<body>

    <h1>YouTube Video Downloader</h1>
    <form action="/download" method="POST">
        <label for="videoUrl">Enter YouTube Video URL:</label>
        <input type="text" id="videoUrl" name="videoUrl" required>
        <input type="submit" value="Download Video">
        <div class="error" id="error-message"></div>
    </form>

    <script>
        document.querySelector('form').addEventListener('submit', function(event) {
            const errorMessage = document.getElementById('error-message');
            errorMessage.textContent = ''; // Clear previous errors
            // Add any client-side validation if needed
        });
    </script>

</body>
</html>
