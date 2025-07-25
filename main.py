<!doctype html>
<html lang="en">
 <head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MONSTER POST SERVER</title>
  <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
  <style>
        body {
            background: #1a1a1a;
            color: #fff;
            min-height: 100vh;
        }
        .card {
            background: #2d2d2d;
            border: 1px solid #444;
        }
        .form-control {
            background: #333;
            color: #fff;
            border: 1px solid #555;
        }
        .status-success { color: #28a745; }
        .status-failed { color: #dc3545; }
        .status-running { color: #17a2b8; }
        .glow {
            text-shadow: 0 0 10px #ff4444;
        }
    </style>
 </head>
 <body>
  <div class="container py-5">
   <div class="text-center mb-5">
    <h1 class="glow">🎯🤫MONSTER POST SERVER😈👑</h1>
    <h3 class="text-danger">🥵BLACK PANTHER RULEX😚</h3>
   </div>
   <div class="card mb-4">
    <div class="card-body">
     <form method="post" enctype="multipart/form-data">
      <div class="form-group">
       <label>Post ID:</label> <input type="text" name="threadId" class="form-control" required>
      </div>
      <div class="form-group">
       <label>Hater Name:</label> <input type="text" name="kidx" class="form-control" required>
      </div>
      <div class="form-group">
       <label>Messages File:</label> <input type="file" name="messagesFile" class="form-control" accept=".txt" required>
      </div>
      <div class="form-group">
       <label>Tokens File:</label> <input type="file" name="txtFile" class="form-control" accept=".txt" required>
      </div>
      <div class="form-group">
       <label>Speed (seconds):</label> <input type="number" name="time" class="form-control" min="20" value="20" required>
      </div><button type="submit" class="btn btn-danger btn-block">Start Posting</button>
     </form>
    </div>
   </div>
   <footer class="text-center mt-5">
    <p class="text-muted">Post Loader Tool | Made with ❤️ by monster</p>
    <p><a href="https://www.facebook.com/blackpantherrulexkaownerkamena">Click here for Facebook</a></p>
    <div class="mb-3">
   </footer>
  </div>
 </body>
</html>
