# cURL and HTTP Requests

This repository contains Bash scripts for various tasks involving cURL and HTTP requests.

## Task 0: cURL body size

Script: `0-body_size.sh`

This script takes a URL as an argument, sends a request to that URL using cURL, and displays the size of the body of the response in bytes.

Usage:
```bash
./0-body_size.sh 0.0.0.0:5000
```

## Task 1: cURL to the end

Script: `1-body.sh`

This script sends a GET request to a URL provided as an argument using cURL and displays the body of the response for a 200 status code.

Usage:
```bash
./1-body.sh 0.0.0.0:5000/route_1
```

## Task 2: cURL Method

Script: `2-delete.sh`

This script sends a DELETE request to a URL provided as an argument using cURL and displays the body of the response.

Usage:
```bash
./2-delete.sh 0.0.0.0:5000/route_3
```

## Task 3: cURL only methods

Script: `3-methods.sh`

This script takes a URL as an argument and displays all HTTP methods that the server accepts for the given URL using cURL.

Usage:
```bash
./3-methods.sh 0.0.0.0:5000/route_4
```

## Task 4: cURL headers

Script: `4-header.sh`

This script takes a URL as an argument, sends a GET request to the URL with a custom header `X-School-User-Id: 98` using cURL, and displays the body of the response.

Usage:
```bash
./4-header.sh 0.0.0.0:5000/route_5
```

## Task 5: cURL POST parameters

Script: `5-post_params.sh`

This script takes a URL as an argument, sends a POST request to the URL with POST parameters `email` and `subject` using cURL, and displays the body of the response.

Usage:
```bash
./5-post_params.sh 0.0.0.0:5000/route_6
```

---

Make sure to replace the placeholders (`0.0.0.0:5000`, `route_1`, etc.) with the actual URLs and routes provided in your specific environment. These scripts utilize cURL for making HTTP requests and handle various aspects like HTTP methods, headers, and request parameters as specified in the tasks.

---
Made by: Mohammad Omar Siddiq
