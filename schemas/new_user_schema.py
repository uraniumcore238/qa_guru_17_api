from voluptuous import Schema

new_user = Schema({
    "name": str,
    "job": str,
    "id": str,
    "createdAt": str
})
