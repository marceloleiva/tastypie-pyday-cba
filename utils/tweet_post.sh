curl --dump-header - -H "Content-Type: application/json" -X POST --data '{"tweet": "Hello     World.", "user": "/api/v1/user/1/"}' http://127.0.0.1:8000/api/v1/tweet/
