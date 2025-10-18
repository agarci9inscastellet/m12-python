<?php
header("Content-Type: application/json");
header("Access-Control-Allow-Origin: *");
die("WWWW");
// ---------------------------------------------------
// 1️⃣ Database connection (PDO + SQLite)
// ---------------------------------------------------
function getDB() {
    static $db = null; // reuse the connection
    if ($db === null) {
        try {
            $db = new PDO('sqlite:api.sqlite');
            $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

            // Create table if not exists
            $db->exec("
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL,
                    app TEXT NOT NULL,
                    UNIQUE(username, app)
                );
            ");
        } catch (Exception $e) {
            echo json_encode(["status" => "error", "message" => "Database connection failed"]);
            exit();
        }
    }
    return $db;
}

// ---------------------------------------------------
// 2️⃣ Helper: Get required GET parameters
// ---------------------------------------------------
function getParam($key) {
    return isset($_GET[$key]) ? trim($_GET[$key]) : '';
}

// ---------------------------------------------------
// 3️⃣ Action: Register new user
// ---------------------------------------------------
function registerUser($username, $password, $app) {
    $db = getDB();

    // Check if user already exists for that app
    $stmt = $db->prepare("SELECT id FROM users WHERE username = :u AND app = :g");
    $stmt->bindValue(':u', $username);
    $stmt->bindValue(':g', $app);
    $stmt->execute();

    if ($stmt->fetch()) {
        echo json_encode(["status" => "error", "message" => "User already exists for this app"]);
        return;
    }

    // Insert new user
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
    $stmt = $db->prepare("INSERT INTO users (username, password, app) VALUES (:u, :p, :g)");
    $stmt->bindValue(':u', $username);
    $stmt->bindValue(':p', $hashedPassword);
    $stmt->bindValue(':g', $app);
    $stmt->execute();

    echo json_encode(["status" => "success", "message" => "User registered"]);
}

// ---------------------------------------------------
// 4️⃣ Action: Login user
// ---------------------------------------------------
function loginUser($username, $password, $app) {
    $db = getDB();

    $stmt = $db->prepare("SELECT id, username, password, app FROM users WHERE username = :u AND app = :g");
    $stmt->bindValue(':u', $username);
    $stmt->bindValue(':g', $app);
    $stmt->execute();
    $user = $stmt->fetch(PDO::FETCH_ASSOC);

    if ($user && password_verify($password, $user['password'])) {
        echo json_encode([
            "status" => "success",
            "message" => "Login successful",
            "user" => [
                "id" => $user['id'],
                "username" => $user['username'],
                "app" => $user['app']
            ]
        ]);
    } else {
        echo json_encode(["status" => "error", "message" => "Invalid credentials"]);
    }
}

// ---------------------------------------------------
// 5️⃣ Router: Decide action based on `a` parameter
// ---------------------------------------------------
$action   = getParam('a');
$username = getParam('name');
$password = getParam('pass');
$app     = getParam('app');

if (empty($action) || empty($username) || empty($password) || empty($app)) {
    echo json_encode(["status" => "error", "message" => "Missing parameters"]);
    exit();
}

switch ($action) {
    case 'register':
        registerUser($username, $password, $app);
        break;

    case 'login':
        loginUser($username, $password, $app);
        break;

    default:
        echo json_encode(["status" => "error", "message" => "Unknown action"]);
        break;
}
?>
