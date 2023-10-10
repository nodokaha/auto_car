<html>
<head>
<meta charset="UTF-8">
<title>auto car</title>
</head>
<body>
<?php
echo '<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">';
echo "<h1>Hello, world!</h1>\n";
echo "<h2> This is Auto Car Remote Control Site!!</h2>\n";

if (isset($_POST["led"]))
{
	$rec = htmlspecialchars($_POST["led"], ENT_QUOTES, "UTF-8");
}
if(isset($_POST["mortor"]))
{
	$status = htmlspecialchars($_POST["mortor"], ENT_QUOTES, "UTF-8");
}
if(isset($_POST["speed"]) && $_POST["speed"] != '')
{
	$speed = htmlspecialchars($_POST["speed"], ENT_QUOTES, "UTF-8");
}
echo $rec;
shell_exec('gpio -g mode 27 out');
shell_exec('gpio -g mode 2 out');
shell_exec('gpio -g mode 3 out');
shell_exec('gpio -g mode 23 out');
shell_exec('gpio -g mode 24 out');
shell_exec('gpio -g mode 18 pwm');
for($x=0; $x<$rec; $x++)
{
	sleep(1);
	shell_exec('gpio -g write 27 1');
	sleep(1);
	shell_exec('gpio -g write 27 0');
}
switch ($status)
{
	case "stop":
		shell_exec('gpio -g write 2 0');
		shell_exec('gpio -g write 3 0');
		shell_exec('gpio -g write 23 0');
		shell_exec('gpio -g write 24 0');
		echo "<h5>STOP!!</h5>";
		break;
	case "roll":
		shell_exec('gpio -g write 2 1');
		shell_exec('gpio -g write 3 0');
		shell_exec('gpio -g write 23 1');
		shell_exec('gpio -g write 24 0');
		echo "<h5>ROLL!!</h5>";
		break;
	case "back_roll":
		shell_exec('gpio -g write 2 0');
		shell_exec('gpio -g write 3 1');
		shell_exec('gpio -g write 23 0');
		shell_exec('gpio -g write 24 1');
		echo "<h5>BACK_ROLL!!</h5>";
		break;

	case "turn_right":
		shell_exec('gpio -g write 2 1');
		shell_exec('gpio -g write 3 0');
		shell_exec('gpio -g write 23 0');
		shell_exec('gpio -g write 24 0');
		echo "<h5>TURN_RIGHT</h5>";
		break;

	case "turn_left":
		shell_exec('gpio -g write 2 0');
		shell_exec('gpio -g write 3 0');
		shell_exec('gpio -g write 23 1');
		shell_exec('gpio -g write 24 0');
		echo "<h5>TURN_LEFT</h5>";
		break;

	case "brake":
		shell_exec('gpio -g write 2 1');
		shell_exec('gpio -g write 3 1');
		shell_exec('gpio -g write 23 1');
		shell_exec('gpio -g write 24 1');
		echo "<h5>BREAKE</h5>";
		break;
	case "set":
		shell_exec('gpio -g pwm 18 ' . $speed);
	default: break;
}
shell_exec('gpio -g pwm 18 ' . $speed);
echo "Mortor Control!!\n";
echo '<p>Speed is ' . (isset($speed) ? $speed : 900) . "<p>\n";
echo "<form method=\"POST\" action=\"\">\n";
echo "<input type=\"range\" min=500 max=1023 step=1 value=" . (isset($speed) ? $speed : 900) . " name=\"speed\">\n";
echo "<input type=\"submit\" value=\"set\" name=\"mortor\" />\n";
echo "<input type=\"submit\" value=\"stop\" name=\"mortor\" />";
echo "<input type=\"submit\" value=\"roll\" name=\"mortor\" />";
echo "<input type=\"submit\" value=\"turn_right\" name=\"mortor\" />";
echo "<input type=\"submit\" value=\"turn_left\" name=\"mortor\" />";
echo "<input type=\"submit\" value=\"back_roll\" name=\"mortor\" />";
echo "<input type=\"submit\" value=\"brake\" name=\"mortor\" />";
echo "</form>\n";
?>
<form method="POST" action="">
<input type="submit" value=1 name="led" />
<input type="submit" value=2 name="led" />
<input type="submit" value=3 name="led" />
<input type="submit" value=4 name="led" />
<input type="submit" value=5 name="led" />
</form>
</body>
</html>
