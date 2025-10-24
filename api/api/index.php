<?php
header("Content-Type: application/json");
header("Access-Control-Allow-Origin: *");
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
                    punts INTEGER NOT NULL DEFAULT 0,
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

    $stmt = $db->prepare("SELECT id, username, password, app, punts FROM users WHERE username = :u AND app = :g");
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
                "app" => $user['app'],
                "punts" => $user['punts']
            ]
        ]);
    } else {
        echo json_encode(["status" => "error", "message" => "Invalid credentials"]);
    }
}



// ---------------------------------------------------
// 6️⃣ Action: Update user points
// ---------------------------------------------------
function updatePunts($username, $password, $app, $punts) {
    $db = getDB();

    // Verify user exists and password is correct
    $stmt = $db->prepare("SELECT id, password FROM users WHERE username = :u AND app = :g");
    $stmt->bindValue(':u', $username);
    $stmt->bindValue(':g', $app);
    $stmt->execute();
    $user = $stmt->fetch(PDO::FETCH_ASSOC);

    if (!$user) {
        echo json_encode(["status" => "error", "message" => "User not found"]);
        return;
    }

    if (!password_verify($password, $user['password'])) {
        echo json_encode(["status" => "error", "message" => "Invalid credentials"]);
        return;
    }

    // Update the points
    $stmt = $db->prepare("UPDATE users SET punts = :punts WHERE id = :id");
    $stmt->bindValue(':punts', $punts, PDO::PARAM_INT);
    $stmt->bindValue(':id', $user['id'], PDO::PARAM_INT);
    $stmt->execute();

    echo json_encode(["status" => "success", "message" => "Points updated"]);
}

// ---------------------------------------------------
// 7️⃣ Action: Delete user (requires name + pass + app)
// ---------------------------------------------------
function deleteUser($username, $password, $app) {
    $db = getDB();

    // Find user for that app
    $stmt = $db->prepare("SELECT id, password FROM users WHERE username = :u AND app = :g");
    $stmt->bindValue(':u', $username);
    $stmt->bindValue(':g', $app);
    $stmt->execute();
    $user = $stmt->fetch(PDO::FETCH_ASSOC);

    if (!$user) {
        echo json_encode(["status" => "error", "message" => "User not found"]);
        return;
    }

    // Verify password before deleting
    if (!password_verify($password, $user['password'])) {
        echo json_encode(["status" => "error", "message" => "Invalid credentials"]);
        return;
    }

    // Delete the user
    $stmt = $db->prepare("DELETE FROM users WHERE id = :id");
    $stmt->bindValue(':id', $user['id'], PDO::PARAM_INT);
    $stmt->execute();

    echo json_encode(["status" => "success", "message" => "User deleted"]);
}

// ---------------------------------------------------
// 5️⃣ Router: Decide action based on `a` parameter
// ---------------------------------------------------
$action   = getParam('a');
$username = getParam('name');
$password = getParam('pass');
$punts = getParam('punts');
$app      = getParam('app');

// Basic validation: most actions require name+pass+app, but 'userlist' only needs app
if (empty($action) || empty($app)) {
    echo json_encode(["status" => "error", "message" => "Missing parameters111"]);
    exit();
}

// For register/login ensure name and pass provided
if (in_array($action, ['register', 'login'])) {
    if (empty($username) || empty($password)) {
        echo json_encode(["status" => "error", "message" => "Missing parameters222"]);
        exit();
    }
}

switch ($action) {
    case 'register':
        registerUser($username, $password, $app);
        break;

    case 'login':
        loginUser($username, $password, $app);
        break;

    case 'updatepunts':
        if (empty($username) || empty($password) || !isset($_GET['punts'])) {
            echo json_encode(["status" => "error", "message" => "Missing parameters for updatepunts"]);
            exit();
        }
        updatePunts($username, $password, $app, intval($punts));
        break;


    case 'userlist':
        // Return list of usernames for the given app in the 'msg' field to match client
        //echo "--------".$app;
        $db = getDB();
        $stmt = $db->prepare("SELECT username, password FROM users WHERE app = :g ORDER BY username ASC");
        $stmt->bindValue(':g', $app);
        $stmt->execute();
        $rows = $stmt->fetchAll(PDO::FETCH_COLUMN, 0);
        echo json_encode(["status" => "success", "msg" => $rows]);

        break;

    case 'deleteuser':
        // delete user requires username + password + app
        deleteUser($username, $password, $app);
        break;

    default:
        echo json_encode(["status" => "error", "message" => "Unknown action"]);
        break;
}
?>
