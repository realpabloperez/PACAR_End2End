db.createUser(
    {
        user: "root",
        pwd: "example",
        roles: [
            {
                role: "admin",
                db: "valenbisi"
            }
        ]
    }
);